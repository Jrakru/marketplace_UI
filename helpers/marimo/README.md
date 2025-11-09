# Marimo Helpers for Claude Code

Helper scripts to integrate marimo reactive notebooks with Claude Code.

## Overview

This directory contains helper scripts that make it easier for AI agents to:
- Generate marimo notebooks programmatically
- Work with marimo CLI commands
- Create common notebook patterns
- Validate and debug marimo notebooks

## Files

### `marimo_generator.py`

Programmatic notebook generation.

**Key Features:**
- `MarimoNotebookGenerator`: Build notebooks cell-by-cell
- Template generators for common use cases
- Pattern library for reactive components

**Usage:**
```python
from marimo_generator import MarimoNotebookGenerator

gen = MarimoNotebookGenerator()
gen.add_imports_cell(["import marimo as mo", "import pandas as pd"])
gen.add_markdown_cell("# My Analysis")
gen.add_widget_cell("slider", "slider", start=0, stop=100, value=50)

# Generate and save
code = gen.generate()
gen.save("analysis.py")
```

**Templates:**
```python
from marimo_generator import (
    create_basic_notebook,
    create_data_analysis_notebook,
    create_dashboard_notebook
)

# Create a basic notebook
notebook_code = create_basic_notebook("My Project")

# Create data analysis template
analysis_code = create_data_analysis_notebook("sales_data")

# Create dashboard
dashboard_code = create_dashboard_notebook("Sales Dashboard")
```

### `marimo_cli_helper.py`

Wrapper around marimo CLI for easier programmatic use.

**Key Features:**
- `MarimoCliHelper`: Helper class for CLI operations
- Quick commands for common operations
- Validation and error checking

**Usage:**
```python
from marimo_cli_helper import MarimoCliHelper

helper = MarimoCliHelper()

# Check installation
status = helper.check_installation()

# Create notebook
result = helper.create_notebook("test.py", template="data_analysis")

# Get edit command
cmd = helper.edit_notebook("test.py")
print(cmd["command"])  # marimo edit test.py

# Export to HTML
helper.export_notebook("test.py", "html", "output.html")

# Validate
validation = helper.validate_notebook("test.py")
```

## Common Patterns

### Pattern 1: Generate and Edit

```python
from marimo_generator import create_dashboard_notebook
from marimo_cli_helper import MarimoCliHelper

# Generate
code = create_dashboard_notebook("My Dashboard")

# Save
with open("dashboard.py", "w") as f:
    f.write(code)

# Get edit command
helper = MarimoCliHelper()
result = helper.edit_notebook("dashboard.py")
print(f"Run: {result['command']}")
```

### Pattern 2: Custom Notebook Builder

```python
from marimo_generator import MarimoNotebookGenerator

gen = MarimoNotebookGenerator()

# Imports
gen.add_imports_cell([
    "import marimo as mo",
    "import pandas as pd",
    "import plotly.express as px"
])

# Title
gen.add_markdown_cell("# Sales Analysis Dashboard")

# File upload
gen.add_widget_cell(
    "file_input",
    "file",
    filetypes=[".csv"],
    label="Upload sales data"
)

# Data processing
gen.add_cell(
    "df = pd.read_csv(file_input.contents()) if file_input.value else None",
    dependencies=["pd", "file_input"],
    returns=["df"]
)

# Visualization
gen.add_cell(
    "fig = px.bar(df, x='product', y='sales') if df is not None else None\nfig",
    dependencies=["px", "df"],
    returns=["fig"]
)

# Save
gen.save("sales_dashboard.py")
```

### Pattern 3: Quick Workflow

```python
from marimo_cli_helper import quick_create, quick_edit, quick_export_html

# Create notebook
filename = quick_create("analysis", template="data_analysis")

# Edit it (returns command to run)
edit_cmd = quick_edit(filename)

# Export to HTML
html_file = quick_export_html(filename)
print(f"Exported to {html_file}")
```

## Integration with Claude Code

### Recommended Workflow

1. **Use helpers to generate notebooks:**
   ```python
   from marimo_generator import create_data_analysis_notebook
   code = create_data_analysis_notebook("my_data")
   ```

2. **Save to file:**
   ```python
   with open("analysis.py", "w") as f:
       f.write(code)
   ```

3. **Get command to run:**
   ```python
   from marimo_cli_helper import MarimoCliHelper
   helper = MarimoCliHelper()
   result = helper.edit_notebook("analysis.py")
   ```

4. **Tell user to run:**
   ```
   Run this command to open the notebook:
   marimo edit analysis.py
   ```

### Best Practices

1. **Always validate notebooks before running:**
   ```python
   validation = helper.validate_notebook("notebook.py")
   if not validation["valid"]:
       print("Issues:", validation["issues"])
   ```

2. **Use templates for common patterns:**
   - data_analysis: For data exploration
   - dashboard: For interactive dashboards
   - basic: For general-purpose notebooks

3. **Export for sharing:**
   - HTML: Interactive, requires Python backend
   - HTML-WASM: Standalone, runs in browser
   - Markdown: For documentation

4. **Check marimo installation:**
   ```python
   status = helper.check_installation()
   if not status["installed"]:
       print("Install marimo: pip install marimo")
   ```

## Error Handling

All helper methods return dictionaries with `success` and `message` keys:

```python
result = helper.create_notebook("test.py")
if result["success"]:
    print(result["message"])
    # Use result["file"] or other data
else:
    print(f"Error: {result['message']}")
```

## Examples

See the `skills/marimo/` directory for comprehensive examples of:
- Getting started with marimo
- Using UI widgets
- Creating layouts
- Building interactive dashboards

## Resources

- **Marimo Docs**: https://docs.marimo.io
- **GitHub**: https://github.com/marimo-team/marimo
- **Tutorials**: Run `marimo tutorial intro`
