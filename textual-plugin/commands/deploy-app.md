# /deploy-app

Deploy Textual applications to various platforms using multiple deployment strategies.

## Usage

```
/deploy-app [options] <source_path>
```

## Parameters

### Required
- `source_path`: Path to the Textual application to deploy

### Optional Flags

- `--target <platform>` - Target platform: static, docker, pyinstaller, pypi, or pip
- `--output <path>` - Output directory for deployment artifacts
- `--config <file>` - Custom deployment configuration file
- `--env <env_name>` - Environment: development, staging, or production
- `--optimize` - Enable optimizations for production
- `--with-dependencies` - Include all dependencies in deployment
- `--compress` - Compress deployment artifacts

## Deployment Targets

### Static Distribution

Package application as standalone distributable files.

```bash
# Create static distribution
/deploy-app --target static --output dist/ my_app

# Create optimized static distribution
/deploy-app --target static --optimize --compress my_app
```

**Output Structure:**
```
dist/
├── static/
│   ├── app.py              # Main application entry point
│   ├── requirements.txt    # Python dependencies
│   ├── run.sh             # Launch script
│   ├── app.desktop        # Desktop entry (Linux)
│   └── README.txt         # Installation instructions
```

**Platform-specific Instructions:**

#### Linux
```bash
# Make executable
chmod +x dist/static/run.sh

# Create desktop shortcut
cp dist/static/app.desktop ~/.local/share/applications/

# Run application
./dist/static/run.sh
```

#### macOS
```bash
# Create .app bundle
cd dist/static
python create_app_bundle.py

# The .app bundle is created in dist/static/MyApp.app
open MyApp.app
```

#### Windows
```batch
# Run via batch file
dist\static\run.bat

# Or create .exe with PyInstaller (see PyInstaller section)
```

### Docker Deployment

Containerize application using Docker.

```bash
# Build Docker image
/deploy-app --target docker my_app

# Build with custom tag
/deploy-app --target docker --output myapp:latest my_app

# Multi-platform build
/deploy-app --target docker --platform linux/amd64,linux/arm64 my_app
```

**Generated Dockerfile:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/ ./src/
COPY static/ ./static/

# Set environment variables
ENV TEXTUAL_THEME=dark
ENV PYTHONUNBUFFERED=1

# Create non-root user
RUN useradd --create-home --shell /bin/bash app \
    && chown -R app:app /app
USER app

# Run application
CMD ["python", "-m", "my_app"]
```

**Docker Compose Example:**
```yaml
# docker-compose.yml
version: '3.8'

services:
  textual-app:
    build: .
    container_name: my-textual-app
    environment:
      - TEXTUAL_THEME=dark
      - TERM=xterm-256color
    stdin_open: true
    tty: true
    volumes:
      - ./data:/app/data
      - ./config:/app/config

  # Optional: Add reverse proxy
  nginx:
    image: nginx:alpine
    ports:
      - "8080:80"
    depends_on:
      - textual-app
```

**Docker Commands:**
```bash
# Build image
docker build -t my-app:latest .

# Run container
docker run -it --rm my-app:latest

# Run with volume mounts
docker run -it --rm \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/config:/app/config \
  my-app:latest

# Run in detached mode
docker run -d --name my-app my-app:latest

# View logs
docker logs -f my-app

# Stop container
docker stop my-app
```

### PyInstaller Deployment

Create standalone executables using PyInstaller.

```bash
# Create standalone executable
/deploy-app --target pyinstaller my_app

# Create optimized executable
/deploy-app --target pyinstaller --optimize --onefile my_app

# Cross-platform build (experimental)
/deploy-app --target pyinstaller --cross-platform my_app
```

**Generated PyInstaller Spec:**
```python
# my_app.spec
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['src/my_app/__main__.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('static', 'static'),
        ('assets', 'assets'),
    ],
    hiddenimports=[
        'textual',
        'textual.app',
        'textual.widgets',
    ],
    hookspath=[],
    hooksconfig={},
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
    name='my_app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
```

**PyInstaller Commands:**
```bash
# Build executable
pyinstaller my_app.spec

# Build with options
pyinstaller --onefile --windowed --icon=icon.ico my_app.spec

# Build for specific platform
pyinstaller --target-arch x86_64 my_app.spec

# Create App Bundle (macOS)
pyinstaller --windowed --osx-bundle-identifier com.myapp.myapp my_app.spec

# Create MSI installer (Windows)
pyinstaller --onefile --windowed my_app.spec
pythoninstaller my_app.spec
```

**Output:**
```
dist/
├── my_app.exe           # Windows executable
├── my_app.app           # macOS app bundle
├── my_app               # Linux binary
└── _internal/          # All dependencies (if not onefile)
```

### PyPI Distribution

Publish application to Python Package Index.

```bash
# Build distribution packages
/deploy-app --target pypi --env production my_app

# Build and upload to Test PyPI
/deploy-app --target pypi --repository testpypi my_app

# Build with specific version
/deploy-app --target pypi --version 1.0.0 my_app
```

**Generated Files:**
```
dist/
├── pypi/
│   ├── my_app-1.0.0-py3-none-any.whl
│   ├── my_app-1.0.0.tar.gz
│   ├── SOURCE_DATE_EPOCH
│   └── MANIFEST.in
```

**PyPI Deployment Process:**
```bash
# Install build tools
pip install build twine

# Build packages
python -m build

# Test upload to Test PyPI
twine upload --repository testpypi dist/pypi/*

# Upload to production PyPI
twine upload dist/pypi/*
```

### pip Install

Create installable pip package.

```bash
# Create pip-installable package
/deploy-app --target pip my_app

# Create wheel distribution
/deploy-app --target pip --output wheel my_app

# Create with all dependencies
/deploy-app --target pip --with-dependencies my_app
```

**Installation:**
```bash
# Install from local package
pip install dist/pip/my_app-1.0.0-py3-none-any.whl

# Install from wheel
pip install dist/wheel/my_app-1.0.0-py3-none-any.whl

# Install in development mode
pip install -e .

# Install with extras
pip install my_app[dev,test]
```

## Platform-Specific Deployment

### Linux

#### AppImage (Portable)
```bash
# Create AppImage
/deploy-app --target appimage my_app

# Output: dist/MyApp-1.0.0-x86_64.AppImage
```

#### Snap Package
```yaml
# snapcraft.yaml
name: my-textual-app
version: '1.0.0'
summary: A Textual TUI application
description: |
  A powerful terminal user interface application built with Textual

grade: stable
confinement: strict

apps:
  my-app:
    command: python -m my_app
    plugs:
      - desktop
      - desktop-legacy

parts:
  app:
    plugin: python
    source: .
    python-packages:
      - textual
```

#### DEB Package
```bash
# Build DEB package
/deploy-app --target deb my_app

# Output: dist/my-app_1.0.0_amd64.deb
```

### Windows

#### MSI Installer
```xml
<!-- installer.xml -->
<?xml version="1.0"?>
<Wix xmlns="http://schemas.microsoft.com/wix/2006/wi">
  <Product Id="*" Name="MyApp" Language="1033" Version="1.0.0.0">
    <Package InstallerVersion="200" Compressed="yes" />
    <Directory Id="TARGETDIR" Name="SourceDir">
      <Directory Id="ProgramFilesFolder">
        <Directory Id="INSTALLFOLDER" Name="MyApp" />
      </Directory>
    </Directory>
    <ComponentGroup Id="ProductComponents" Directory="INSTALLFOLDER">
      <Component Id="MainExecutable">
        <File Id="MyAppExe" Source="dist/my_app.exe" />
      </Component>
    </ComponentGroup>
    <Feature Id="ProductFeature" Title="MyApp" Level="1">
      <ComponentGroupRef Id="ProductComponents" />
    </Feature>
  </Product>
</Wix>
```

#### NSIS Installer
```nsis
; installer.nsi
!include "MUI2.nsh"

Name "MyApp 1.0.0"
OutFile "dist\my-app-installer.exe"
InstallDir "$PROGRAMFILES\MyApp"
RequestExecutionLevel admin

Page directory
Page instfiles

Section
  SetOutPath $INSTDIR
  File "dist\my_app.exe"
  WriteUninstaller "$INSTDIR\Uninstall.exe"
SectionEnd
```

### macOS

#### DMG Installer
```bash
# Create DMG package
/deploy-app --target dmg my_app

# Output: dist/MyApp-1.0.0.dmg
```

#### Homebrew Formula
```ruby
# my-app.rb (Formula)
class MyApp < Formula
  desc "A Textual TUI application"
  homepage "https://github.com/user/my-app"
  version "1.0.0"

  if OS.mac?
    url "https://github.com/user/my-app/archive/v1.0.0.tar.gz"
    sha256 "..."
  end

  depends_on "python@3.11"

  def install
    virtualenv = with_env(PYTHONPATH: nil) { `which python3`.strip }
    system "#{virtualenv}", "-m", "pip", "install", "."
  end

  test do
    assert_match "MyApp", shell_output("#{bin}/my_app --version")
  end
end
```

## Configuration

### Deployment Config File (deploy.toml)

```toml
# deploy.toml
[deployment]
app_name = "my_app"
version = "1.0.0"
python_version = "3.11"
description = "A Textual TUI application"
author = "Your Name"
license = "MIT"

[targets.static]
include_assets = true
compress = true
optimize = true

[targets.docker]
base_image = "python:3.11-slim"
tag = "my-app:latest"
build_args = {}
registry = "ghcr.io"

[targets.pyinstaller]
onefile = true
windowed = true
icon = "assets/icon.ico"
include_data = ["static/*", "assets/*"]

[targets.pypi]
repository = "pypi"
username = "__token__"
skip_existing = true

[metadata]
long_description = "file://README.md"
long_description_content_type = "text/markdown"
classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
]
```

### Environment Variables

```bash
# Environment-specific settings
export TEXTUAL_THEME=dark
export APP_CONFIG_PATH=/etc/my_app
export APP_LOG_LEVEL=INFO

# Docker-specific
export DOCKER_REGISTRY=ghcr.io
export DOCKER_TAG=latest

# PyPI-specific
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=$PYPI_TOKEN
```

## Optimization Options

### Performance Optimization

```bash
# Enable all optimizations
/deploy-app --target static --optimize my_app

# What optimizations are applied:
# - Minify CSS
# - Compress assets
# - Optimize Python bytecode
# - Remove debug symbols
# - Enable PGO (Profile-Guided Optimization)
```

### Size Optimization

```bash
# Minimize package size
/deploy-app --target pyinstaller --compress --onefile my_app

# Removes:
# - Unused dependencies
# - Debug information
# - Test files
# - Documentation
```

## Distribution and Sharing

### GitHub Releases

```bash
# Create GitHub release with deployment artifacts
/deploy-app --target github-release --token $GITHUB_TOKEN my_app

# Automatically creates:
# - Release notes
# - Asset uploads
# - Tag creation
```

### GitHub Container Registry

```bash
# Push to GitHub Container Registry
/deploy-app --target docker \
  --registry ghcr.io \
  --username $GITHUB_USERNAME \
  --token $GITHUB_TOKEN \
  my_app
```

### Self-Hosted Repository

```bash
# Deploy to private PyPI server
/deploy-app --target pypi \
  --repository https://pypi.company.com/simple/ \
  --username $PYPI_USERNAME \
  --password $PYPI_PASSWORD \
  my_app
```

## Examples

### Complete CI/CD Pipeline

```yaml
# .github/workflows/deploy.yml
name: Deploy Textual App

on:
  push:
    tags:
      - 'v*'

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        target: [static, docker, pyinstaller, pypi]

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'

    - name: Install dependencies
      run: |
        pip install textual-dev
        pip install -e .

    - name: Run tests
      run: pytest

    - name: Validate structure
      run: textual-validate --strict .

    - name: Deploy
      run: |
        /deploy-app --target ${{ matrix.target }} \
          --env production \
          --optimize \
          my_app

    - name: Upload artifacts
      uses: actions/upload-artifact@v3
      with:
        name: dist-${{ matrix.target }}
        path: dist/
```

### Multi-Platform Deployment Script

```bash
#!/bin/bash
# deploy.sh

APP_NAME="my_app"
VERSION=$(python -c "import my_app; print(my_app.__version__)")

# Deploy to all targets
echo "Deploying $APP_NAME v$VERSION"

# Static distribution
/deploy-app --target static --output dist/static/ $APP_NAME

# Docker images for multiple architectures
for arch in amd64 arm64; do
  /deploy-app --target docker \
    --output ${APP_NAME}:${VERSION}-${arch} \
    --platform linux/${arch} \
    $APP_NAME
done

# PyInstaller executables
for platform in linux macos windows; do
  /deploy-app --target pyinstaller \
    --output dist/${platform}/ \
    --cross-platform \
    $APP_NAME
done

# PyPI
if [ "$1" = "--publish" ]; then
  /deploy-app --target pypi --version $VERSION $APP_NAME
fi

echo "Deployment complete!"
```

## Troubleshooting

### Common Issues

**PyInstaller: Module not found**
```
Error: ModuleNotFoundError: No module named 'textual.widgets'
```
```
Solution: Add hidden imports to .spec file:
hiddenimports=['textual.widgets', 'textual.app']
```

**Docker: Permission denied**
```
Error: PermissionError: [Errno 13] Permission denied
```
```
Solution: Run container with --user $(id -u):$(id -g)
or set USER in Dockerfile
```

**PyPI: Package already exists**
```
Error: File already exists on PyPI
```
```
Solution: Increment version number or use --skip-existing
```

**Static: Runtime error**
```
Error: Module not found at runtime
```
```
Solution: Ensure all dependencies are in requirements.txt
or use --with-dependencies flag
```

### Debugging

**Enable verbose output**
```bash
# All deployment targets support --verbose
/deploy-app --target docker --verbose my_app
```

**Dry run**
```bash
# Preview deployment without executing
/deploy-app --target pypi --dry-run my_app
```

**Check generated files**
```bash
# Inspect deployment artifacts before publishing
ls -la dist/
```

## Security Considerations

### Code Signing

**Windows:**
```bash
# Sign executable
signtool sign /f certificate.p12 /p password dist/my_app.exe
```

**macOS:**
```bash
# Sign app bundle
codesign --sign "Developer ID Application: Your Name" dist/MyApp.app
```

**Linux:**
```bash
# Create GPG signature
gpg --detach-sign --armor dist/my_app
```

### Container Security

```dockerfile
# Use non-root user
RUN useradd --create-home --shell /bin/bash app
USER app

# Scan for vulnerabilities
RUN pip install safety safety-textual
safety check

# Use specific versions for security
RUN pip install textual==0.40.0
```

## See Also

- `/create-app` - Create new Textual applications
- `/validate-structure` - Validate Textual application structure
- Textual Deployment Guide: https://textual.textualize.io/guide/
- PyInstaller Documentation: https://pyinstaller.org/
- Docker Best Practices: https://docs.docker.com/develop/dev-best-practices/
