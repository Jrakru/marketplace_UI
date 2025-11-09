"""
Skill: Getting Started with Marimo

This skill provides the foundation for creating reactive Python notebooks with Marimo.
It covers installation, basic notebook structure, reactivity, and the core concepts.
"""

import marimo

__generated_with = "0.10.11"
app = marimo.App()


# ============================================================================
# BASIC MARIMO NOTEBOOK TEMPLATE
# ============================================================================

@app.cell
def __():
    """
    Import marimo and other essential libraries.

    Best Practice: Always include marimo import in the first cell.
    Import all modules at the beginning of your notebook.
    """
    import marimo as mo
    return mo,


@app.cell
def __(mo):
    """
    Basic markdown cell with title and description.

    Use mo.md() to render markdown content in your notebook.
    """
    mo.md(
        """
        # Welcome to Marimo!

        This is a reactive Python notebook. When you run a cell,
        marimo automatically runs all cells that depend on it.
        """
    )
    return


@app.cell
def __(mo):
    """
    Create interactive UI elements.

    UI elements assigned to global variables become reactive.
    When you interact with them, dependent cells auto-run.
    """
    slider = mo.ui.slider(start=0, stop=100, value=50, label="Choose a value:")
    slider
    return slider,


@app.cell
def __(mo, slider):
    """
    Use reactive values from UI elements.

    This cell automatically re-runs when the slider changes.
    """
    mo.md(f"**Current value:** {slider.value}")
    return


# ============================================================================
# REACTIVITY EXAMPLE: COUNTER
# ============================================================================

@app.cell
def __(mo):
    """
    Create buttons for a counter.

    Buttons can trigger state changes in your notebook.
    """
    increment_button = mo.ui.button(label="Increment", value=0)
    decrement_button = mo.ui.button(label="Decrement", value=0)

    mo.hstack([decrement_button, increment_button], gap=1)
    return increment_button, decrement_button


@app.cell
def __(increment_button, decrement_button):
    """
    Track counter state using button clicks.

    This cell re-runs whenever either button is clicked.
    """
    count = increment_button.value - decrement_button.value
    return count,


@app.cell
def __(mo, count):
    """
    Display the counter value.

    Automatically updates when count changes.
    """
    mo.md(f"## Count: {count}")
    return


# ============================================================================
# DATA VISUALIZATION EXAMPLE
# ============================================================================

@app.cell
def __():
    """
    Import data visualization libraries.
    """
    import matplotlib.pyplot as plt
    import numpy as np
    return plt, np


@app.cell
def __(mo):
    """
    Create UI for plot customization.
    """
    num_points = mo.ui.slider(start=10, stop=200, value=50, label="Number of points:")
    plot_type = mo.ui.dropdown(
        options=["line", "scatter", "bar"],
        value="line",
        label="Plot type:"
    )

    mo.vstack([num_points, plot_type])
    return num_points, plot_type


@app.cell
def __(plt, np, num_points, plot_type, mo):
    """
    Generate and display a reactive plot.

    This plot updates automatically when UI elements change.
    """
    x = np.linspace(0, 10, num_points.value)
    y = np.sin(x)

    fig, ax = plt.subplots()

    if plot_type.value == "line":
        ax.plot(x, y)
    elif plot_type.value == "scatter":
        ax.scatter(x, y)
    else:  # bar
        ax.bar(x, y, width=0.3)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title(f"Sine Wave - {plot_type.value.capitalize()} Plot")

    mo.mpl.interactive(fig)
    return x, y, fig, ax


# ============================================================================
# HELPER FUNCTIONS FOR AI AGENTS
# ============================================================================

def create_basic_marimo_notebook(title="My Notebook"):
    """
    Generate a basic marimo notebook template.

    Args:
        title: Title for the notebook

    Returns:
        str: Python code for a basic marimo notebook
    """
    template = f'''import marimo

__generated_with = "0.10.11"
app = marimo.App()


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def __(mo):
    mo.md(
        """
        # {title}

        Your reactive notebook starts here.
        """
    )
    return


@app.cell
def __(mo):
    # Add your code here
    mo.md("Hello, world!")
    return


if __name__ == "__main__":
    app.run()
'''
    return template


def create_interactive_cell(widget_type="slider", **kwargs):
    """
    Generate code for an interactive cell.

    Args:
        widget_type: Type of widget (slider, text, checkbox, etc.)
        **kwargs: Widget-specific parameters

    Returns:
        str: Code for creating the widget
    """
    widgets = {
        "slider": "mo.ui.slider(start={start}, stop={stop}, value={value}, label='{label}')",
        "text": "mo.ui.text(value='{value}', label='{label}')",
        "checkbox": "mo.ui.checkbox(value={value}, label='{label}')",
        "dropdown": "mo.ui.dropdown(options={options}, value='{value}', label='{label}')",
        "button": "mo.ui.button(label='{label}', value={value})",
        "number": "mo.ui.number(start={start}, stop={stop}, value={value}, label='{label}')",
        "date": "mo.ui.date(value='{value}', label='{label}')",
    }

    if widget_type in widgets:
        return widgets[widget_type].format(**kwargs)
    return f"mo.ui.{widget_type}()"


def create_layout_example(layout_type="hstack"):
    """
    Generate code for layout examples.

    Args:
        layout_type: Type of layout (hstack, vstack, grid, tabs, etc.)

    Returns:
        str: Code for creating the layout
    """
    layouts = {
        "hstack": """
mo.hstack([
    mo.md("Item 1"),
    mo.md("Item 2"),
    mo.md("Item 3")
], justify="space-between", gap=2)
""",
        "vstack": """
mo.vstack([
    mo.md("## Title"),
    mo.md("Content goes here"),
    mo.ui.button(label="Click me")
], gap=1)
""",
        "grid": """
mo.hstack([
    mo.vstack([mo.md("Left top"), mo.md("Left bottom")]),
    mo.vstack([mo.md("Right top"), mo.md("Right bottom")])
], gap=2)
""",
        "tabs": """
mo.ui.tabs({
    "Tab 1": mo.md("Content for tab 1"),
    "Tab 2": mo.md("Content for tab 2"),
    "Tab 3": mo.md("Content for tab 3")
})
"""
    }
    return layouts.get(layout_type, "mo.md('Layout not found')")


# ============================================================================
# MARIMO QUICK START GUIDE
# ============================================================================

MARIMO_QUICK_START = """
MARIMO QUICK START GUIDE
========================

1. INSTALLATION
   pip install marimo

2. CREATE YOUR FIRST NOTEBOOK
   marimo edit notebook.py

   This opens the marimo editor in your browser.

3. RUN A TUTORIAL
   marimo tutorial intro
   marimo tutorial dataflow
   marimo tutorial ui
   marimo tutorial layout

4. KEY CONCEPTS

   - **Reactive Execution**: Change a cell, and dependent cells auto-run
   - **No Hidden State**: Delete a cell, its variables are removed
   - **Deterministic Order**: Execution order based on dependencies, not position
   - **Pure Python**: Notebooks stored as .py files, not JSON
   - **Git-Friendly**: Version control with standard tools

5. CELL STRUCTURE

   @app.cell
   def __(dependencies):
       # Your code here
       variable = compute_something()
       return variable,  # Always return as tuple!

6. COMMON PATTERNS

   **Markdown:**
   mo.md("# Title")
   mo.md(f"Value: {variable}")

   **UI Elements:**
   slider = mo.ui.slider(0, 100, value=50)
   text = mo.ui.text(placeholder="Enter text")

   **Layouts:**
   mo.hstack([item1, item2])  # Horizontal
   mo.vstack([item1, item2])  # Vertical

   **Accessing Values:**
   slider.value  # Get current value

7. DEVELOPMENT WORKFLOW

   - Create: marimo edit notebook.py
   - Run as app: marimo run notebook.py
   - Run as script: python notebook.py
   - Export HTML: marimo export html notebook.py
   - Export WASM: marimo export html-wasm notebook.py

8. BEST PRACTICES

   - Import marimo as mo in first cell
   - Import all libraries at the top
   - Use descriptive variable names
   - Return all variables you want to reuse
   - Never redeclare variables across cells
   - Prefix temporary variables with underscore (_temp)
   - Avoid circular dependencies

9. UI WIDGETS OVERVIEW

   **Input:**
   - mo.ui.text() - Text input
   - mo.ui.number() - Numeric input
   - mo.ui.slider() - Range slider
   - mo.ui.date() - Date picker
   - mo.ui.checkbox() - Checkbox
   - mo.ui.switch() - Toggle switch
   - mo.ui.dropdown() - Dropdown select
   - mo.ui.multiselect() - Multi-select
   - mo.ui.radio() - Radio buttons

   **Actions:**
   - mo.ui.button() - Clickable button
   - mo.ui.file() - File upload
   - mo.ui.form() - Form container

   **Display:**
   - mo.ui.table() - Data table
   - mo.ui.dataframe() - Interactive dataframe
   - mo.ui.code_editor() - Code editor

   **Composite:**
   - mo.ui.array() - Array of widgets
   - mo.ui.dictionary() - Dict of widgets
   - mo.ui.batch() - Batch multiple widgets

10. DEPLOYMENT OPTIONS

    - **Web App**: marimo run notebook.py
    - **Docker**: Use official marimo Docker images
    - **WASM**: marimo export html-wasm for static hosting
    - **GitHub Pages**: Deploy WASM notebooks
    - **Cloud**: Deploy to Railway, Fly.io, etc.

11. NEXT STEPS

    - Explore built-in widgets (02_widgets_ui.py)
    - Learn layout systems (03_layouts.py)
    - Data visualization (04_visualization.py)
    - State management (05_state_management.py)
"""


# ============================================================================
# COMMON PATTERNS
# ============================================================================

COMMON_PATTERNS = {
    "reactive_counter": """
@app.cell
def __(mo):
    increment = mo.ui.button(label="+", value=0)
    decrement = mo.ui.button(label="-", value=0)
    mo.hstack([decrement, increment])
    return increment, decrement

@app.cell
def __(increment, decrement):
    count = increment.value - decrement.value
    return count,

@app.cell
def __(mo, count):
    mo.md(f"## Count: {count}")
    return
""",
    "form_submission": """
@app.cell
def __(mo):
    form = mo.ui.form({
        "name": mo.ui.text(label="Name"),
        "email": mo.ui.text(label="Email"),
        "subscribe": mo.ui.checkbox(label="Subscribe to newsletter")
    })
    form
    return form,

@app.cell
def __(mo, form):
    if form.value:
        mo.md(f\"\"\"
        **Submitted:**
        - Name: {form.value['name']}
        - Email: {form.value['email']}
        - Subscribe: {form.value['subscribe']}
        \"\"\")
    else:
        mo.md("Fill out the form above")
    return
""",
    "data_explorer": """
@app.cell
def __():
    import pandas as pd
    import numpy as np
    return pd, np

@app.cell
def __(pd, np):
    # Create sample data
    df = pd.DataFrame({
        'A': np.random.randn(100),
        'B': np.random.randn(100),
        'C': np.random.choice(['X', 'Y', 'Z'], 100)
    })
    return df,

@app.cell
def __(mo, df):
    # Interactive data explorer
    explorer = mo.ui.dataframe(df)
    explorer
    return explorer,

@app.cell
def __(mo, explorer):
    # Display filtered data
    mo.md(f"**Rows selected:** {len(explorer.value)}")
    return
"""
}


if __name__ == "__main__":
    app.run()
