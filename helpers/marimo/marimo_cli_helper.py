"""
Marimo CLI Helper

Helper functions for working with marimo from Claude Code.
Provides wrappers around common marimo CLI operations.
"""

import subprocess
import os
from typing import Optional, List, Dict
from pathlib import Path


class MarimoCliHelper:
    """Helper class for marimo CLI operations."""

    @staticmethod
    def create_notebook(filename: str, template: Optional[str] = None) -> Dict[str, any]:
        """
        Create a new marimo notebook.

        Args:
            filename: Path to the notebook file (.py)
            template: Optional template name (basic, data_analysis, dashboard)

        Returns:
            dict with success status and message
        """
        try:
            if not filename.endswith('.py'):
                filename += '.py'

            # Check if file exists
            if os.path.exists(filename):
                return {
                    "success": False,
                    "message": f"File {filename} already exists"
                }

            # Create basic template
            if template:
                from marimo_generator import (
                    create_basic_notebook,
                    create_data_analysis_notebook,
                    create_dashboard_notebook
                )

                templates = {
                    "basic": create_basic_notebook,
                    "data_analysis": create_data_analysis_notebook,
                    "dashboard": create_dashboard_notebook
                }

                if template in templates:
                    content = templates[template](
                        title=Path(filename).stem.replace('_', ' ').title()
                    )
                    with open(filename, 'w') as f:
                        f.write(content)
                    return {
                        "success": True,
                        "message": f"Created {filename} from {template} template",
                        "file": filename
                    }

            # Create empty notebook
            result = subprocess.run(
                ["marimo", "create", filename],
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                return {
                    "success": True,
                    "message": f"Created {filename}",
                    "file": filename
                }
            else:
                return {
                    "success": False,
                    "message": f"Error: {result.stderr}"
                }

        except Exception as e:
            return {
                "success": False,
                "message": f"Error creating notebook: {str(e)}"
            }

    @staticmethod
    def edit_notebook(filename: str, headless: bool = False, port: Optional[int] = None) -> Dict[str, any]:
        """
        Open a marimo notebook in edit mode.

        Args:
            filename: Path to the notebook file
            headless: Run without opening browser
            port: Port number for the server

        Returns:
            dict with command and instructions
        """
        if not os.path.exists(filename):
            return {
                "success": False,
                "message": f"File {filename} not found"
            }

        cmd = ["marimo", "edit", filename]

        if headless:
            cmd.append("--headless")

        if port:
            cmd.extend(["--port", str(port)])

        return {
            "success": True,
            "command": " ".join(cmd),
            "message": f"Run this command to edit {filename}:\n{' '.join(cmd)}",
            "instructions": "The editor will open in your browser. Use Ctrl+C to stop the server."
        }

    @staticmethod
    def run_notebook(filename: str, headless: bool = False, port: Optional[int] = None) -> Dict[str, any]:
        """
        Run a marimo notebook as an app.

        Args:
            filename: Path to the notebook file
            headless: Run without opening browser
            port: Port number for the server

        Returns:
            dict with command and instructions
        """
        if not os.path.exists(filename):
            return {
                "success": False,
                "message": f"File {filename} not found"
            }

        cmd = ["marimo", "run", filename]

        if headless:
            cmd.append("--headless")

        if port:
            cmd.extend(["--port", str(port)])

        return {
            "success": True,
            "command": " ".join(cmd),
            "message": f"Run this command to run {filename} as an app:\n{' '.join(cmd)}",
            "instructions": "The app will run in read-only mode. Use Ctrl+C to stop."
        }

    @staticmethod
    def export_notebook(filename: str, output_format: str = "html",
                       output_file: Optional[str] = None) -> Dict[str, any]:
        """
        Export a marimo notebook to various formats.

        Args:
            filename: Path to the notebook file
            output_format: Export format (html, html-wasm, md, script, ipynb)
            output_file: Output filename (optional)

        Returns:
            dict with command and result
        """
        if not os.path.exists(filename):
            return {
                "success": False,
                "message": f"File {filename} not found"
            }

        valid_formats = ["html", "html-wasm", "md", "script", "ipynb"]
        if output_format not in valid_formats:
            return {
                "success": False,
                "message": f"Invalid format. Choose from: {', '.join(valid_formats)}"
            }

        cmd = ["marimo", "export", output_format, filename]

        if output_file:
            cmd.extend(["--output", output_file])

        try:
            result = subprocess.run(cmd, capture_output=True, text=True)

            if result.returncode == 0:
                return {
                    "success": True,
                    "message": f"Exported {filename} to {output_format} format",
                    "output": output_file or f"{Path(filename).stem}.{output_format}"
                }
            else:
                return {
                    "success": False,
                    "message": f"Export failed: {result.stderr}"
                }

        except Exception as e:
            return {
                "success": False,
                "message": f"Error during export: {str(e)}"
            }

    @staticmethod
    def run_tutorial(tutorial_name: str = "intro") -> Dict[str, any]:
        """
        Run a marimo tutorial.

        Args:
            tutorial_name: Tutorial name (intro, dataflow, ui, layout, etc.)

        Returns:
            dict with command and instructions
        """
        cmd = ["marimo", "tutorial", tutorial_name]

        return {
            "success": True,
            "command": " ".join(cmd),
            "message": f"Run this command to start the {tutorial_name} tutorial:\n{' '.join(cmd)}",
            "instructions": "The tutorial will open in your browser."
        }

    @staticmethod
    def check_installation() -> Dict[str, any]:
        """
        Check if marimo is installed and get version.

        Returns:
            dict with installation status and version
        """
        try:
            result = subprocess.run(
                ["marimo", "--version"],
                capture_output=True,
                text=True
            )

            if result.returncode == 0:
                version = result.stdout.strip()
                return {
                    "success": True,
                    "installed": True,
                    "version": version,
                    "message": f"marimo is installed: {version}"
                }
            else:
                return {
                    "success": False,
                    "installed": False,
                    "message": "marimo is not installed"
                }

        except FileNotFoundError:
            return {
                "success": False,
                "installed": False,
                "message": "marimo is not installed. Install with: pip install marimo"
            }

    @staticmethod
    def validate_notebook(filename: str) -> Dict[str, any]:
        """
        Validate a marimo notebook for common issues.

        Args:
            filename: Path to the notebook file

        Returns:
            dict with validation results
        """
        if not os.path.exists(filename):
            return {
                "success": False,
                "message": f"File {filename} not found"
            }

        issues = []

        try:
            with open(filename, 'r') as f:
                content = f.read()

            # Check for basic structure
            if 'import marimo' not in content:
                issues.append("Missing 'import marimo'")

            if '__generated_with' not in content and 'app = marimo.App()' not in content:
                issues.append("Missing marimo.App() initialization")

            if '@app.cell' not in content:
                issues.append("No cells found (missing @app.cell decorators)")

            # Check for common mistakes
            if 'from marimo import' in content:
                issues.append("Use 'import marimo as mo' instead of 'from marimo import'")

            # Count cells
            cell_count = content.count('@app.cell')

            # Check for return statements
            if cell_count > 0:
                return_count = content.count('return ')
                if return_count == 0:
                    issues.append("No return statements found in cells")

            return {
                "success": True,
                "valid": len(issues) == 0,
                "issues": issues,
                "cell_count": cell_count,
                "message": "Notebook is valid" if not issues else f"Found {len(issues)} issue(s)"
            }

        except Exception as e:
            return {
                "success": False,
                "message": f"Error validating notebook: {str(e)}"
            }


# ============================================================================
# QUICK COMMANDS
# ============================================================================

def quick_create(name: str, template: str = "basic") -> str:
    """Quick create a notebook and return the filename."""
    helper = MarimoCliHelper()
    result = helper.create_notebook(name, template)
    if result["success"]:
        return result["file"]
    else:
        raise ValueError(result["message"])


def quick_edit(filename: str) -> str:
    """Quick edit command for a notebook."""
    helper = MarimoCliHelper()
    result = helper.edit_notebook(filename)
    if result["success"]:
        return result["command"]
    else:
        raise ValueError(result["message"])


def quick_export_html(filename: str) -> str:
    """Quick export to HTML."""
    helper = MarimoCliHelper()
    result = helper.export_notebook(filename, "html")
    if result["success"]:
        return result["output"]
    else:
        raise ValueError(result["message"])


# ============================================================================
# USAGE GUIDE
# ============================================================================

USAGE_GUIDE = """
MARIMO CLI HELPER USAGE GUIDE
==============================

## Installation Check

```python
from marimo_cli_helper import MarimoCliHelper

helper = MarimoCliHelper()
status = helper.check_installation()
print(status)
```

## Creating Notebooks

```python
# Create from template
result = helper.create_notebook("analysis.py", template="data_analysis")

# Create basic notebook
result = helper.create_notebook("notebook.py")

# Quick create
from marimo_cli_helper import quick_create
filename = quick_create("test", template="dashboard")
```

## Editing Notebooks

```python
# Get edit command
result = helper.edit_notebook("notebook.py")
print(result["command"])  # Run this command

# With custom port
result = helper.edit_notebook("notebook.py", port=8080)

# Headless mode (for remote servers)
result = helper.edit_notebook("notebook.py", headless=True)
```

## Running as Apps

```python
# Get run command
result = helper.run_notebook("notebook.py")
print(result["command"])
```

## Exporting

```python
# Export to HTML
helper.export_notebook("notebook.py", "html", "output.html")

# Export to WASM (runs in browser without Python)
helper.export_notebook("notebook.py", "html-wasm", "standalone.html")

# Export to Markdown
helper.export_notebook("notebook.py", "md", "README.md")

# Export as Python script
helper.export_notebook("notebook.py", "script", "script.py")
```

## Validation

```python
# Validate a notebook
result = helper.validate_notebook("notebook.py")
if not result["valid"]:
    print("Issues found:")
    for issue in result["issues"]:
        print(f"  - {issue}")
```

## Tutorials

```python
# Run intro tutorial
result = helper.run_tutorial("intro")

# Other tutorials
helper.run_tutorial("dataflow")
helper.run_tutorial("ui")
helper.run_tutorial("layout")
```
"""


if __name__ == "__main__":
    print(USAGE_GUIDE)
