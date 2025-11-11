#!/usr/bin/env python3
"""
Textual Deployment Utilities

This script provides comprehensive deployment and distribution tools for
Textual TUI applications. It supports static export (HTML), Docker
containerization, PyInstaller packaging, and distribution helpers.

Features:
- Static export to HTML
- Docker containerization
- PyInstaller packaging
- Distribution helpers
- Version management
- Build optimization

Usage:
    python textual-deploy.py --export-html app.py
    python textual-deploy.py --docker app.py
    python textual-deploy.py --package app.py
    python textual-deploy.py --all app.py
"""

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import re


# ============================================================================
# DEPLOYMENT CONSTANTS
# ============================================================================

DOCKERFILE_TEMPLATE = '''FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \\
    build-essential \\
    libgtk-3-0 \\
    libgbm1 \\
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY {app_name}.py .

# Set environment variables
ENV TEXTUAL_DEVICES=1
ENV TERM=xterm-256color

# Run application
CMD ["python", "{app_name}.py"]
'''

DOCKERIGNORE_TEMPLATE = '''__pycache__
*.pyc
*.pyo
*.pyd
.pytest_cache
.coverage
.venv
venv
.env
.git
.gitignore
README.md
*.md
'''

PYINSTALLER_SPEC_TEMPLATE = '''# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['{app_name}.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'textual',
        'textual.app',
        'textual.widgets',
        'textual.containers',
    ],
    hookspath=[],
    hooksconfig={{}},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='{app_name}',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
'''

REQUIREMENTS_TEMPLATE = '''textual>=0.40.0
'''

README_TEMPLATE = '''# {app_name}

A Textual TUI application.

## Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```bash
python {app_name}.py
```

## Docker

Build and run with Docker:
```bash
docker build -t {app_name} .
docker run -it {app_name}
```

## Packaging

Create a standalone executable:
```bash
pip install pyinstaller
pyinstaller {app_name}.spec
```

The executable will be in the `dist/` directory.

## Features

{features}

## License

MIT
'''

GITHUB_WORKFLOW_TEMPLATE = '''name: Build and Deploy

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install textual pyinstaller

    - name: Build with PyInstaller
      run: |
        pyinstaller {app_name}.spec

    - name: Upload artifact
      uses: actions/upload-artifact@v3
      with:
        name: {app_name}-executable
        path: dist/{app_name}
'''


# ============================================================================
# DEPLOYMENT CLASS
# ============================================================================

class TextualDeployer:
    """Deploys Textual applications."""

    def __init__(self, app_file: str, output_dir: str = "dist"):
        """Initialize deployer.

        Args:
            app_file: Path to the application file
            output_dir: Output directory for builds
        """
        self.app_file = Path(app_file)
        self.output_dir = Path(output_dir)
        self.app_name = self.app_file.stem

        if not self.app_file.exists():
            raise FileNotFoundError(f"App file not found: {app_file}")

        self.output_dir.mkdir(parents=True, exist_ok=True)

    def export_html(self) -> None:
        """Export application to HTML."""
        print("📦 Exporting to HTML...")

        try:
            from textual.web import render_app
        except ImportError:
            print("⚠️  Warning: textual.web not available. HTML export may not work.")
            print("   Install with: pip install 'textual[web]'")

        temp_dir = tempfile.mkdtemp()

        try:
            html_file = self.output_dir / f"{self.app_name}.html"

            export_script = f'''
import sys
sys.path.insert(0, "{self.app_file.parent}")

from textual.web import render_app
from {self.app_name} import {self.app_name.title().replace('_', '')} as App

import asyncio
async def main():
    app = App()
    html = await render_app(app, title="{self.app_name}")
    with open("{html_file}", "w") as f:
        f.write(html)

asyncio.run(main())
'''

            subprocess.run([sys.executable, '-c', export_script],
                         check=True, capture_output=True)

            print(f"  ✓ HTML exported to: {html_file}")

            if html_file.exists():
                with open(html_file, 'r') as f:
                    content = f.read()

                if '<!-- TEXTUAL APP -->' in content:
                    print(f"  ✓ HTML file size: {len(content)} bytes")

        except Exception as e:
            print(f"  ✗ Error exporting HTML: {e}")

    def create_docker_image(self) -> None:
        """Create Docker image."""
        print("🐳 Creating Docker image...")

        docker_dir = self.output_dir / "docker"
        docker_dir.mkdir(exist_ok=True)

        dockerfile = docker_dir / "Dockerfile"
        dockerignore = docker_dir / ".dockerignore"
        requirements = docker_dir / "requirements.txt"

        with open(dockerfile, 'w') as f:
            f.write(DOCKERFILE_TEMPLATE.format(app_name=self.app_name))

        with open(dockerignore, 'w') as f:
            f.write(DOCKERIGNORE_TEMPLATE)

        with open(requirements, 'w') as f:
            f.write(REQUIREMENTS_TEMPLATE)

        app_copy = docker_dir / f"{self.app_name}.py"
        shutil.copy2(self.app_file, app_copy)

        print(f"  ✓ Dockerfile created in: {docker_dir}")
        print(f"  → Build with: cd {docker_dir} && docker build -t {self.app_name} .")
        print(f"  → Run with:   docker run -it {self.app_name}")

    def package_with_pyinstaller(self) -> None:
        """Create standalone executable with PyInstaller."""
        print("📦 Packaging with PyInstaller...")

        pyinstaller_dir = self.output_dir / "pyinstaller"
        pyinstaller_dir.mkdir(exist_ok=True)

        spec_file = pyinstaller_dir / f"{self.app_name}.spec"
        with open(spec_file, 'w') as f:
            f.write(PYINSTALLER_SPEC_TEMPLATE.format(app_name=self.app_name))

        app_copy = pyinstaller_dir / f"{self.app_name}.py"
        shutil.copy2(self.app_file, app_copy)

        build_script = f'''
cd "{pyinstaller_dir}"
pyinstaller --clean {self.app_name}.spec
'''

        try:
            result = subprocess.run(
                [sys.executable, '-c', f'''
import subprocess
import sys

subprocess.run([
    sys.executable, "-m", "PyInstaller",
    "--clean",
    "--noconfirm",
    "{spec_file}"
], cwd="{pyinstaller_dir}")
'''],
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                dist_dir = pyinstaller_dir / "dist"
                executable = dist_dir / self.app_name

                if executable.exists():
                    print(f"  ✓ Executable created: {executable}")
                    print(f"  → Size: {executable.stat().st_size / 1024 / 1024:.2f} MB")
                else:
                    print("  ✗ Executable not found")
            else:
                print(f"  ✗ PyInstaller failed: {result.stderr}")

        except FileNotFoundError:
            print("  ✗ PyInstaller not found. Install with: pip install pyinstaller")
        except Exception as e:
            print(f"  ✗ Error packaging: {e}")

    def create_distribution_package(self) -> None:
        """Create distribution package (zip file)."""
        print("📦 Creating distribution package...")

        package_dir = self.output_dir / f"{self.app_name}-package"
        package_dir.mkdir(exist_ok=True)

        app_copy = package_dir / f"{self.app_name}.py"
        shutil.copy2(self.app_file, app_copy)

        readme = package_dir / "README.md"
        features = self._extract_features()
        with open(readme, 'w') as f:
            f.write(README_TEMPLATE.format(
                app_name=self.app_name,
                features=features
            ))

        requirements = package_dir / "requirements.txt"
        with open(requirements, 'w') as f:
            f.write(REQUIREMENTS_TEMPLATE)

        docker_dir = package_dir / "docker"
        docker_dir.mkdir(exist_ok=True)

        with open(docker_dir / "Dockerfile", 'w') as f:
            f.write(DOCKERFILE_TEMPLATE.format(app_name=self.app_name))

        with open(docker_dir / "requirements.txt", 'w') as f:
            f.write(REQUIREMENTS_TEMPLATE)

        github_dir = package_dir / ".github" / "workflows"
        github_dir.mkdir(parents=True, exist_ok=True)

        with open(github_dir / "build.yml", 'w') as f:
            f.write(GITHUB_WORKFLOW_TEMPLATE.format(app_name=self.app_name))

        zip_file = self.output_dir / f"{self.app_name}-package.zip"

        with zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED) as zf:
            for root, dirs, files in os.walk(package_dir):
                for file in files:
                    file_path = Path(root) / file
                    arc_name = file_path.relative_to(package_dir.parent)
                    zf.write(file_path, arc_name)

        shutil.rmtree(package_dir)

        print(f"  ✓ Package created: {zip_file}")
        print(f"  → Size: {zip_file.stat().st_size / 1024 / 1024:.2f} MB")

    def create_launcher_script(self) -> None:
        """Create launcher script."""
        print("📦 Creating launcher script...")

        script_dir = self.output_dir
        script_file = script_dir / f"{self.app_name}.sh"

        script_content = f'''#!/bin/bash

# {self.app_name} launcher script

SCRIPT_DIR="$( cd "$( dirname "{{{{0}}}}" )" && pwd )"
APP_FILE="${{SCRIPT_DIR}}/{self.app_name}.py"

if [ ! -f "$APP_FILE" ]; then
    echo "Error: {self.app_name}.py not found"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -q textual

# Run application
python "$APP_FILE"
'''

        with open(script_file, 'w') as f:
            f.write(script_content)

        os.chmod(script_file, 0o755)

        print(f"  ✓ Launcher script created: {script_file}")

    def generate_version_info(self) -> None:
        """Generate version information."""
        print("📦 Generating version info...")

        version_info = {
            "app_name": self.app_name,
            "version": "1.0.0",
            "python_version": f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}",
            "textual_version": self._get_textual_version(),
            "build_date": "TODO",
            "build_hash": "TODO",
        }

        version_file = self.output_dir / "version.json"
        with open(version_file, 'w') as f:
            json.dump(version_info, f, indent=2)

        print(f"  ✓ Version info saved to: {version_file}")

    def _extract_features(self) -> str:
        """Extract features from the app file."""
        try:
            with open(self.app_file, 'r') as f:
                content = f.read()

            features = []

            if 'Button' in content:
                features.append("- Interactive buttons")
            if 'Input' in content:
                features.append("- Text input")
            if 'Table' in content or 'DataTable' in content:
                features.append("- Data tables")
            if 'Tabs' in content:
                features.append("- Tab navigation")
            if 'CSS' in content:
                features.append("- Custom styling")
            if 'BINDINGS' in content:
                features.append("- Keyboard shortcuts")

            if not features:
                features.append("- Basic TUI interface")

            return "\n".join(features)

        except Exception:
            return "- Custom Textual application"

    def _get_textual_version(self) -> str:
        """Get installed Textual version."""
        try:
            import textual
            return textual.__version__
        except ImportError:
            return "Not installed"

    def deploy_all(self) -> None:
        """Run all deployment steps."""
        print(f"\n🚀 Deploying {self.app_name}...")
        print("=" * 70)

        self.export_html()
        print()
        self.create_docker_image()
        print()
        self.package_with_pyinstaller()
        print()
        self.create_distribution_package()
        print()
        self.create_launcher_script()
        print()
        self.generate_version_info()

        print("\n" + "=" * 70)
        print("✅ Deployment complete!")
        print(f"📁 Output directory: {self.output_dir.absolute()}")
        print("=" * 70 + "\n")


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def get_app_info(app_file: str) -> Dict[str, str]:
    """Get information about the app."""
    app_path = Path(app_file)

    info = {
        "name": app_path.stem,
        "path": str(app_path.absolute()),
        "size": f"{app_path.stat().st_size} bytes",
    }

    try:
        with open(app_path, 'r') as f:
            content = f.read()

        info["lines"] = str(content.count('\n') + 1)
        info["widgets"] = str(len(re.findall(r'\b(Button|Label|Input|Table)\b', content)))

    except Exception as e:
        info["error"] = str(e)

    return info


def optimize_app(app_file: str, output_file: str) -> None:
    """Optimize app for production."""
    print("🔧 Optimizing app for production...")

    with open(app_file, 'r') as f:
        content = f.read()

    optimizations = [
        (r'Textual\n', 'Textual'),
        (r'def on_mount\(self\) -> None:\n    """Mount the application\."""\n', ''),
        (r'print\(', 'pass  # print('),
    ]

    for pattern, replacement in optimizations:
        content = re.sub(pattern, replacement, content)

    with open(output_file, 'w') as f:
        f.write(content)

    print(f"  ✓ Optimized version saved to: {output_file}")


def check_dependencies(app_file: str) -> List[str]:
    """Check if dependencies are installed."""
    dependencies = ['textual', 'pyinstaller']

    missing = []
    for dep in dependencies:
        try:
            __import__(dep)
        except ImportError:
            missing.append(dep)

    return missing


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Deploy Textual TUI applications",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --export-html app.py
  %(prog)s --docker app.py
  %(prog)s --package app.py
  %(prog)s --all app.py
  %(prog)s --info app.py
  %(prog)s --optimize app.py --output optimized.py
        """
    )

    parser.add_argument(
        'app_file',
        nargs='?',
        help='Path to Textual application file'
    )

    parser.add_argument(
        '--export-html',
        action='store_true',
        help='Export to HTML'
    )

    parser.add_argument(
        '--docker',
        action='store_true',
        help='Create Docker image'
    )

    parser.add_argument(
        '--package',
        action='store_true',
        help='Package with PyInstaller'
    )

    parser.add_argument(
        '--dist',
        action='store_true',
        help='Create distribution package'
    )

    parser.add_argument(
        '--script',
        action='store_true',
        help='Create launcher script'
    )

    parser.add_argument(
        '--all',
        action='store_true',
        help='Run all deployment steps'
    )

    parser.add_argument(
        '--output',
        default='dist',
        help='Output directory (default: dist)'
    )

    parser.add_argument(
        '--optimize',
        action='store_true',
        help='Optimize app for production'
    )

    parser.add_argument(
        '--optimized-output',
        default='optimized.py',
        help='Output file for optimized version'
    )

    parser.add_argument(
        '--info',
        action='store_true',
        help='Show app information'
    )

    parser.add_argument(
        '--check-deps',
        action='store_true',
        help='Check dependencies'
    )

    args = parser.parse_args()

    if not args.app_file:
        parser.print_help()
        sys.exit(1)

    app_path = Path(args.app_file)
    if not app_path.exists():
        print(f"❌ Error: File not found: {app_path}")
        sys.exit(1)

    if args.info:
        print("\n📊 App Information")
        print("=" * 70)
        info = get_app_info(args.app_file)
        for key, value in info.items():
            print(f"{key.capitalize():15} : {value}")
        print("=" * 70 + "\n")

    if args.check_deps:
        missing = check_dependencies(args.app_file)
        if missing:
            print("⚠️  Missing dependencies:")
            for dep in missing:
                print(f"  - {dep}")
            print("\nInstall with: pip install " + " ".join(missing))
        else:
            print("✅ All dependencies are installed")
        print()

    if args.optimize:
        optimize_app(args.app_file, args.optimized_output)

    if any([args.export_html, args.docker, args.package, args.dist, args.script, args.all]):
        try:
            deployer = TextualDeployer(args.app_file, args.output)

            if args.all:
                deployer.deploy_all()
            else:
                if args.export_html:
                    deployer.export_html()

                if args.docker:
                    deployer.create_docker_image()

                if args.package:
                    deployer.package_with_pyinstaller()

                if args.dist:
                    deployer.create_distribution_package()

                if args.script:
                    deployer.create_launcher_script()

            print("\n✅ Deployment completed successfully!")

        except Exception as e:
            print(f"\n❌ Error: {e}")
            import traceback
            traceback.print_exc()
            sys.exit(1)


if __name__ == '__main__':
    main()
