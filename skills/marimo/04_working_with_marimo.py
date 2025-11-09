"""
Skill: Working with Marimo in Claude Code

This skill shows how to effectively use marimo with Claude Code,
including using helper scripts, CLI commands, and best practices.
Follows Anthropic's agent skill guidelines for practical, executable code.
"""

# ============================================================================
# INSTALLATION AND SETUP
# ============================================================================

INSTALLATION_GUIDE = """
MARIMO INSTALLATION AND SETUP
==============================

## Installation

```bash
# Install marimo
pip install marimo

# Verify installation
marimo --version

# Optional: Install with plotting support
pip install marimo plotly matplotlib altair
```

## First Steps

```bash
# Run interactive tutorial
marimo tutorial intro

# Create a new notebook
marimo edit my_notebook.py

# Run existing notebook as app
marimo run my_notebook.py
```

## Directory Structure

Recommended structure for marimo projects:

```
my_project/
├── notebooks/           # Marimo notebooks (.py files)
│   ├── analysis.py
│   ├── dashboard.py
│   └── exploration.py
├── data/               # Data files
├── outputs/            # Exported HTML, images
└── requirements.txt    # Dependencies
```
"""

# ============================================================================
# USING HELPER SCRIPTS
# ============================================================================

def demonstrate_helpers():
    """
    Demonstrate using marimo helper scripts.

    This shows the recommended workflow for Claude Code agents
    working with marimo notebooks.
    """

    # Example 1: Generate a notebook programmatically
    example_generate = """
    # Import the generator
    import sys
    sys.path.append('helpers/marimo')
    from marimo_generator import MarimoNotebookGenerator

    # Create a new notebook
    gen = MarimoNotebookGenerator()

    # Add imports
    gen.add_imports_cell([
        "import marimo as mo",
        "import pandas as pd",
        "import plotly.express as px"
    ])

    # Add title
    gen.add_markdown_cell("# My Data Analysis")

    # Add file upload widget
    gen.add_widget_cell(
        "file_upload",
        "file",
        filetypes=[".csv"],
        label="Upload CSV file"
    )

    # Add data processing cell
    gen.add_cell(
        "df = pd.read_csv(file_upload.contents()) if file_upload.value else None",
        dependencies=["pd", "file_upload"],
        returns=["df"]
    )

    # Add visualization
    gen.add_cell(
        "fig = px.scatter(df, x='x', y='y') if df is not None else None\\nfig",
        dependencies=["px", "df"],
        returns=["fig"]
    )

    # Save the notebook
    gen.save("analysis.py")
    print("Created analysis.py")
    """

    # Example 2: Use CLI helper
    example_cli = """
    import sys
    sys.path.append('helpers/marimo')
    from marimo_cli_helper import MarimoCliHelper

    helper = MarimoCliHelper()

    # Check if marimo is installed
    status = helper.check_installation()
    if not status["installed"]:
        print("Please install marimo: pip install marimo")
        return

    # Create a new notebook from template
    result = helper.create_notebook(
        "dashboard.py",
        template="dashboard"
    )

    if result["success"]:
        print(f"Created {result['file']}")

        # Get the edit command
        edit_cmd = helper.edit_notebook(result['file'])
        print(f"\\nTo edit: {edit_cmd['command']}")
    """

    # Example 3: Validate a notebook
    example_validate = """
    import sys
    sys.path.append('helpers/marimo')
    from marimo_cli_helper import MarimoCliHelper

    helper = MarimoCliHelper()

    # Validate notebook structure
    result = helper.validate_notebook("my_notebook.py")

    if result["valid"]:
        print(f"✓ Notebook is valid ({result['cell_count']} cells)")
    else:
        print("Issues found:")
        for issue in result["issues"]:
            print(f"  - {issue}")
    """

    return {
        "generate": example_generate,
        "cli": example_cli,
        "validate": example_validate
    }

# ============================================================================
# CLI COMMANDS REFERENCE
# ============================================================================

CLI_COMMANDS = """
MARIMO CLI COMMANDS
===================

## Creating and Editing

```bash
# Create new notebook (opens editor)
marimo edit new_notebook.py

# Edit existing notebook
marimo edit notebook.py

# Edit with custom port
marimo edit notebook.py --port 8080

# Edit in headless mode (for remote servers)
marimo edit notebook.py --headless
```

## Running Notebooks

```bash
# Run as interactive app
marimo run notebook.py

# Run on custom port
marimo run notebook.py --port 3000

# Run in headless mode
marimo run notebook.py --headless
```

## Exporting

```bash
# Export to static HTML (requires Python backend)
marimo export html notebook.py --output output.html

# Export to WASM HTML (runs standalone in browser)
marimo export html-wasm notebook.py --output standalone.html

# Export to Markdown
marimo export md notebook.py --output README.md

# Export as Python script
marimo export script notebook.py --output script.py

# Export to Jupyter notebook
marimo export ipynb notebook.py --output notebook.ipynb
```

## Tutorials

```bash
# Interactive tutorials
marimo tutorial intro      # Introduction to marimo
marimo tutorial dataflow   # Understanding dataflow
marimo tutorial ui         # UI elements
marimo tutorial layout     # Layouts and organization
marimo tutorial plots      # Plotting and visualization
marimo tutorial sql        # SQL integration
```

## Configuration

```bash
# Show configuration
marimo config show

# Set configuration
marimo config set key value
```
"""

# ============================================================================
# BEST PRACTICES FOR CLAUDE CODE
# ============================================================================

BEST_PRACTICES = """
BEST PRACTICES: MARIMO + CLAUDE CODE
====================================

## 1. Use Helper Scripts

DON'T manually write notebook code:
```python
# Bad: Error-prone
with open("notebook.py", "w") as f:
    f.write('import marimo\\n')
    f.write('app = marimo.App()\\n')
    # ... manual string building
```

DO use the generator:
```python
# Good: Reliable and type-safe
from marimo_generator import MarimoNotebookGenerator

gen = MarimoNotebookGenerator()
gen.add_imports_cell(["import marimo as mo"])
gen.add_markdown_cell("# Title")
gen.save("notebook.py")
```

## 2. Validate Before Running

Always validate notebooks before suggesting users run them:

```python
from marimo_cli_helper import MarimoCliHelper

helper = MarimoCliHelper()
result = helper.validate_notebook("notebook.py")

if not result["valid"]:
    print("Fix these issues first:")
    for issue in result["issues"]:
        print(f"  - {issue}")
```

## 3. Provide Clear Instructions

When creating notebooks, tell users exactly what to do:

```python
# After creating a notebook
print(f\"\"\"
Notebook created: {filename}

To edit:
  marimo edit {filename}

To run as app:
  marimo run {filename}

To export to HTML:
  marimo export html {filename} --output output.html
\"\"\")
```

## 4. Use Templates

For common patterns, use templates:

```python
from marimo_generator import (
    create_data_analysis_notebook,
    create_dashboard_notebook
)

# For data analysis tasks
code = create_data_analysis_notebook("sales_data")

# For dashboards
code = create_dashboard_notebook("Sales Dashboard")
```

## 5. Handle Errors Gracefully

Check for marimo installation:

```python
from marimo_cli_helper import MarimoCliHelper

helper = MarimoCliHelper()
status = helper.check_installation()

if not status["installed"]:
    print(\"\"\"
    Marimo is not installed.

    Install with:
      pip install marimo

    Or with plotting support:
      pip install marimo plotly matplotlib
    \"\"\")
    return
```

## 6. Structure Notebooks Properly

Follow this cell order:
1. Imports (always first)
2. Title/description markdown
3. Configuration/parameters
4. Data loading
5. Processing/analysis
6. Visualization
7. Output/export

Example:
```python
gen = MarimoNotebookGenerator()

# 1. Imports
gen.add_imports_cell(["import marimo as mo", "import pandas as pd"])

# 2. Title
gen.add_markdown_cell("# Data Analysis")

# 3. Config
gen.add_widget_cell("data_file", "file", filetypes=[".csv"])

# 4. Load data
gen.add_cell("df = pd.read_csv(data_file.contents())", ...)

# 5. Process
gen.add_cell("summary = df.describe()", ...)

# 6. Visualize
gen.add_cell("fig = px.bar(df, ...)", ...)
```

## 7. Return Values Correctly

ALWAYS return values as tuples:

```python
# Correct
gen.add_cell(
    "x = 10",
    returns=["x"]  # Returns as tuple
)

# This generates:
# return x,  # Note the comma!
```

## 8. Manage Dependencies

Specify cell dependencies correctly:

```python
gen.add_cell(
    "result = process(data, config)",
    dependencies=["data", "config", "process"],
    returns=["result"]
)
```

## 9. Export for Sharing

When users want to share:
- **HTML**: For interactive viewing (requires Python)
- **HTML-WASM**: Standalone (runs in browser, no Python)
- **Markdown**: For documentation
- **Script**: For running in CI/CD

```python
# WASM is best for sharing
helper.export_notebook("dashboard.py", "html-wasm", "share.html")
print("Share share.html - it runs entirely in the browser!")
```

## 10. Test Notebooks

Create a test workflow:

```python
# 1. Generate
gen.save("test.py")

# 2. Validate
result = helper.validate_notebook("test.py")
assert result["valid"], f"Validation failed: {result['issues']}"

# 3. Export to verify it works
helper.export_notebook("test.py", "html", "test.html")
```
"""

# ============================================================================
# COMMON WORKFLOWS
# ============================================================================

def workflow_create_data_dashboard():
    """
    Complete workflow: Create a data dashboard.

    This demonstrates the full process of creating a marimo
    dashboard using helper scripts.
    """
    workflow = """
# WORKFLOW: Create Data Dashboard
# ================================

import sys
sys.path.append('helpers/marimo')
from marimo_generator import MarimoNotebookGenerator
from marimo_cli_helper import MarimoCliHelper

# Step 1: Create generator
gen = MarimoNotebookGenerator()

# Step 2: Add imports
gen.add_imports_cell([
    "import marimo as mo",
    "import pandas as pd",
    "import plotly.express as px"
])

# Step 3: Add title
gen.add_markdown_cell("# Sales Dashboard\\n\\nInteractive sales data visualization")

# Step 4: Add file upload
gen.add_widget_cell(
    "file_input",
    "file",
    filetypes=[".csv"],
    label="Upload sales data (CSV)"
)

# Step 5: Load data
gen.add_cell(
    '''if file_input.value:
    df = pd.read_csv(file_input.contents())
else:
    df = None''',
    dependencies=["file_input", "pd"],
    returns=["df"]
)

# Step 6: Add filters
gen.add_widget_cell(
    "category_filter",
    "multiselect",
    options=["Electronics", "Clothing", "Food"],
    label="Filter by category"
)

# Step 7: Filter data
gen.add_cell(
    '''if df is not None and category_filter.value:
    filtered_df = df[df['category'].isin(category_filter.value)]
else:
    filtered_df = df''',
    dependencies=["df", "category_filter"],
    returns=["filtered_df"]
)

# Step 8: Create visualization
gen.add_cell(
    '''if filtered_df is not None:
    fig = px.bar(filtered_df, x='product', y='sales', color='category')
    fig.update_layout(title='Sales by Product')
else:
    fig = None

mo.plotly(fig) if fig else mo.md("Upload data to see visualization")''',
    dependencies=["filtered_df", "px", "mo"],
    returns=["fig"]
)

# Step 9: Add summary statistics
gen.add_cell(
    '''if filtered_df is not None:
    total_sales = filtered_df['sales'].sum()
    avg_sales = filtered_df['sales'].mean()

    mo.md(f\"\"\"
    ### Summary Statistics
    - **Total Sales:** ${total_sales:,.2f}
    - **Average Sales:** ${avg_sales:,.2f}
    - **Products:** {len(filtered_df)}
    \"\"\")
else:
    mo.md("No data loaded")''',
    dependencies=["filtered_df", "mo"],
    returns=["total_sales", "avg_sales"]
)

# Step 10: Save
filename = "sales_dashboard.py"
gen.save(filename)

# Step 11: Validate
helper = MarimoCliHelper()
result = helper.validate_notebook(filename)

if result["valid"]:
    print(f"✓ Created {filename} ({result['cell_count']} cells)")
    print(f"\\nTo run:")
    print(f"  marimo edit {filename}")
else:
    print("Issues found:")
    for issue in result["issues"]:
        print(f"  - {issue}")
"""
    return workflow


def workflow_export_for_github():
    """Export notebook for GitHub Pages (WASM)."""
    workflow = """
# WORKFLOW: Export for GitHub Pages
# ==================================

import sys
sys.path.append('helpers/marimo')
from marimo_cli_helper import MarimoCliHelper

helper = MarimoCliHelper()

# Export to WASM (runs in browser without Python)
result = helper.export_notebook(
    "dashboard.py",
    "html-wasm",
    "docs/index.html"  # GitHub Pages looks for docs/index.html
)

if result["success"]:
    print(f\"\"\"
    ✓ Exported to {result['output']}

    To deploy to GitHub Pages:
    1. Commit the file:
       git add docs/index.html
       git commit -m "Add dashboard"
       git push

    2. Enable GitHub Pages in repo settings:
       - Go to Settings → Pages
       - Source: Deploy from branch
       - Branch: main, folder: /docs

    3. Visit: https://USERNAME.github.io/REPO
    \"\"\")
"""
    return workflow


# ============================================================================
# QUICK REFERENCE
# ============================================================================

QUICK_REFERENCE = """
MARIMO QUICK REFERENCE
=====================

## Cell Structure

```python
@app.cell
def __(dependency1, dependency2):
    # Your code here
    result = process(dependency1, dependency2)
    return result,  # Always tuple!
```

## Common Patterns

**Markdown:**
```python
mo.md("# Title")
mo.md(f"Value: {variable}")
```

**Widgets:**
```python
slider = mo.ui.slider(0, 100, value=50)
text = mo.ui.text(placeholder="Enter name")
dropdown = mo.ui.dropdown(options=["A", "B"], value="A")
```

**Layouts:**
```python
mo.hstack([item1, item2], gap=1)  # Horizontal
mo.vstack([item1, item2], gap=1)  # Vertical
mo.ui.tabs({"Tab1": content1, "Tab2": content2})
```

**Conditionals:**
```python
result = value if condition else fallback
mo.md("Yes") if flag else mo.md("No")
```

## Helper Quick Commands

```python
from marimo_generator import create_dashboard_notebook
from marimo_cli_helper import quick_create, quick_edit

# Quick create
filename = quick_create("test", template="dashboard")

# Quick edit
cmd = quick_edit(filename)
print(cmd)  # Run this command
```
"""


if __name__ == "__main__":
    print(INSTALLATION_GUIDE)
    print(CLI_COMMANDS)
    print(BEST_PRACTICES)
