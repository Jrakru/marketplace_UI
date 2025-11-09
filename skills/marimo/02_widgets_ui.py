"""
Skill: Marimo Widgets and UI Components

This skill covers all the interactive UI widgets available in Marimo,
how to use them, combine them, and handle their values.
"""

import marimo

__generated_with = "0.10.11"
app = marimo.App()


# ============================================================================
# INPUT WIDGETS
# ============================================================================

@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def __(mo):
    mo.md(
        """
        # Marimo UI Widgets Comprehensive Guide

        Marimo provides 20+ interactive widgets for building reactive notebooks.
        All widgets are reactive - when their value changes, dependent cells auto-run.
        """
    )
    return


@app.cell
def __(mo):
    mo.md("## 📝 Text Input Widgets")
    return


@app.cell
def __(mo):
    """Text input examples."""
    text_input = mo.ui.text(
        value="",
        placeholder="Enter your name",
        label="Name:",
        max_length=100
    )

    text_area = mo.ui.text_area(
        value="",
        placeholder="Enter a longer description...",
        label="Description:",
        rows=5
    )

    mo.vstack([text_input, text_area], gap=1)
    return text_input, text_area


@app.cell
def __(mo, text_input, text_area):
    """Display text input values."""
    if text_input.value or text_area.value:
        mo.md(f"""
        **Text Input:** {text_input.value or '(empty)'}

        **Text Area:** {text_area.value or '(empty)'}
        """)
    else:
        mo.md("_Enter some text above to see the reactive values._")
    return


@app.cell
def __(mo):
    mo.md("## 🔢 Numeric Input Widgets")
    return


@app.cell
def __(mo):
    """Numeric input examples."""
    number_input = mo.ui.number(
        start=0,
        stop=100,
        value=50,
        step=1,
        label="Choose a number:"
    )

    slider = mo.ui.slider(
        start=0,
        stop=100,
        value=25,
        step=5,
        label="Slider:",
        show_value=True
    )

    range_slider = mo.ui.range_slider(
        start=0,
        stop=100,
        value=[25, 75],
        step=1,
        label="Range:"
    )

    mo.vstack([number_input, slider, range_slider], gap=1)
    return number_input, slider, range_slider


@app.cell
def __(mo, number_input, slider, range_slider):
    """Display numeric values."""
    mo.md(f"""
    - **Number:** {number_input.value}
    - **Slider:** {slider.value}
    - **Range:** {range_slider.value[0]} to {range_slider.value[1]}
    """)
    return


@app.cell
def __(mo):
    mo.md("## ☑️ Selection Widgets")
    return


@app.cell
def __(mo):
    """Selection widget examples."""
    checkbox = mo.ui.checkbox(
        value=False,
        label="Subscribe to newsletter"
    )

    switch = mo.ui.switch(
        value=True,
        label="Enable notifications"
    )

    dropdown = mo.ui.dropdown(
        options=["Python", "JavaScript", "Rust", "Go", "TypeScript"],
        value="Python",
        label="Favorite language:"
    )

    radio = mo.ui.radio(
        options=["Light", "Dark", "Auto"],
        value="Auto",
        label="Theme:"
    )

    multiselect = mo.ui.multiselect(
        options=["React", "Vue", "Angular", "Svelte"],
        value=["React"],
        label="Frameworks you know:"
    )

    mo.vstack([checkbox, switch, dropdown, radio, multiselect], gap=1)
    return checkbox, switch, dropdown, radio, multiselect


@app.cell
def __(mo, checkbox, switch, dropdown, radio, multiselect):
    """Display selection values."""
    mo.md(f"""
    **Selections:**
    - Checkbox: {checkbox.value}
    - Switch: {switch.value}
    - Dropdown: {dropdown.value}
    - Radio: {radio.value}
    - Multiselect: {', '.join(multiselect.value) if multiselect.value else 'None'}
    """)
    return


@app.cell
def __(mo):
    mo.md("## 📅 Date and Time Widgets")
    return


@app.cell
def __(mo):
    """Date and time widgets."""
    date_picker = mo.ui.date(
        value="2025-01-01",
        label="Select a date:"
    )

    date_picker
    return date_picker,


@app.cell
def __(mo, date_picker):
    mo.md(f"**Selected date:** {date_picker.value}")
    return


@app.cell
def __(mo):
    mo.md("## 🔘 Action Widgets")
    return


@app.cell
def __(mo):
    """Button examples."""
    button_primary = mo.ui.button(
        label="Primary Action",
        value=0,
        kind="success"
    )

    button_danger = mo.ui.button(
        label="Delete",
        value=0,
        kind="danger"
    )

    button_neutral = mo.ui.button(
        label="Cancel",
        value=0,
        kind="neutral"
    )

    mo.hstack([button_primary, button_danger, button_neutral], gap=1)
    return button_primary, button_danger, button_neutral


@app.cell
def __(mo, button_primary, button_danger, button_neutral):
    """Display button click counts."""
    mo.md(f"""
    **Button clicks:**
    - Primary: {button_primary.value}
    - Danger: {button_danger.value}
    - Neutral: {button_neutral.value}
    """)
    return


@app.cell
def __(mo):
    mo.md("## 📊 Data Widgets")
    return


@app.cell
def __():
    """Create sample data."""
    import pandas as pd
    import numpy as np

    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 28, 32],
        'City': ['New York', 'San Francisco', 'Seattle', 'Austin', 'Boston'],
        'Score': [92, 88, 95, 78, 85]
    })
    return pd, np, df


@app.cell
def __(mo, df):
    """Interactive data table."""
    data_table = mo.ui.table(
        data=df,
        selection='multi',
        label="Employee Data"
    )

    data_table
    return data_table,


@app.cell
def __(mo, data_table):
    """Show selected rows."""
    if data_table.value:
        mo.md(f"**Selected {len(data_table.value)} row(s)**")
    else:
        mo.md("_Click rows to select them_")
    return


@app.cell
def __(mo, df):
    """Interactive dataframe explorer."""
    dataframe_explorer = mo.ui.dataframe(df)
    dataframe_explorer
    return dataframe_explorer,


@app.cell
def __(mo):
    mo.md("## 📁 File Upload Widget")
    return


@app.cell
def __(mo):
    """File upload widget."""
    file_upload = mo.ui.file(
        filetypes=[".csv", ".txt", ".json"],
        multiple=False,
        label="Upload a file:"
    )

    file_upload
    return file_upload,


@app.cell
def __(mo, file_upload):
    """Display uploaded file info."""
    if file_upload.value:
        content = file_upload.contents()
        mo.md(f"""
        **File uploaded:**
        - Name: {file_upload.name()}
        - Size: {len(content)} bytes
        """)
    else:
        mo.md("_No file uploaded yet_")
    return


@app.cell
def __(mo):
    mo.md("## 📝 Code Editor Widget")
    return


@app.cell
def __(mo):
    """Code editor widget."""
    code_editor = mo.ui.code_editor(
        value="def hello():\n    print('Hello, World!')",
        language="python",
        label="Edit Python code:"
    )

    code_editor
    return code_editor,


@app.cell
def __(mo, code_editor):
    """Display code."""
    mo.md(f"```python\n{code_editor.value}\n```")
    return


@app.cell
def __(mo):
    mo.md("## 🎨 Composite Widgets")
    return


@app.cell
def __(mo):
    """Form widget - group multiple inputs."""
    user_form = mo.ui.form({
        "username": mo.ui.text(placeholder="Username"),
        "email": mo.ui.text(placeholder="Email"),
        "age": mo.ui.number(start=0, stop=120, value=25),
        "country": mo.ui.dropdown(
            options=["USA", "UK", "Canada", "Australia"],
            value="USA"
        ),
        "subscribe": mo.ui.checkbox(label="Subscribe to newsletter")
    })

    user_form
    return user_form,


@app.cell
def __(mo, user_form):
    """Display form submission."""
    if user_form.value:
        data = user_form.value
        mo.md(f"""
        ### Form Submitted ✅

        - **Username:** {data['username']}
        - **Email:** {data['email']}
        - **Age:** {data['age']}
        - **Country:** {data['country']}
        - **Subscribe:** {'Yes' if data['subscribe'] else 'No'}
        """)
    else:
        mo.md("_Fill out the form and click Submit_")
    return


@app.cell
def __(mo):
    """Array widget - multiple instances of same widget."""
    todo_array = mo.ui.array(
        [mo.ui.text(placeholder=f"Todo {i+1}") for i in range(3)],
        label="To-Do List"
    )

    todo_array
    return todo_array,


@app.cell
def __(mo, todo_array):
    """Display todos."""
    todos = [item for item in todo_array.value if item]
    if todos:
        todo_list = "\n".join([f"{i+1}. {todo}" for i, todo in enumerate(todos)])
        mo.md(f"**Your To-Dos:**\n\n{todo_list}")
    else:
        mo.md("_Add some todos above_")
    return


@app.cell
def __(mo):
    """Dictionary widget - named collection of widgets."""
    settings_dict = mo.ui.dictionary({
        "theme": mo.ui.radio(options=["Light", "Dark"], value="Light"),
        "font_size": mo.ui.slider(start=10, stop=24, value=14, label="Font Size"),
        "notifications": mo.ui.switch(value=True, label="Enable notifications")
    })

    settings_dict
    return settings_dict,


@app.cell
def __(mo, settings_dict):
    """Display settings."""
    mo.md(f"""
    **Current Settings:**
    - Theme: {settings_dict.value['theme']}
    - Font Size: {settings_dict.value['font_size']}px
    - Notifications: {'On' if settings_dict.value['notifications'] else 'Off'}
    """)
    return


@app.cell
def __(mo):
    """Batch widget - update multiple widgets together."""
    batch_controls = mo.ui.batch(
        mo.md("**Controls:**"),
        mo.ui.slider(start=0, stop=100, value=50, label="Value 1"),
        mo.ui.slider(start=0, stop=100, value=75, label="Value 2"),
        mo.ui.button(label="Apply Changes")
    )

    batch_controls
    return batch_controls,


# ============================================================================
# WIDGET HELPER FUNCTIONS
# ============================================================================

def create_widget_code(widget_type, **params):
    """
    Generate code for creating a widget.

    Args:
        widget_type: Type of widget to create
        **params: Widget parameters

    Returns:
        str: Python code for the widget
    """
    widget_templates = {
        "text": "mo.ui.text(value='{value}', placeholder='{placeholder}', label='{label}')",
        "number": "mo.ui.number(start={start}, stop={stop}, value={value}, label='{label}')",
        "slider": "mo.ui.slider(start={start}, stop={stop}, value={value}, label='{label}')",
        "checkbox": "mo.ui.checkbox(value={value}, label='{label}')",
        "dropdown": "mo.ui.dropdown(options={options}, value='{value}', label='{label}')",
        "button": "mo.ui.button(label='{label}', kind='{kind}')",
        "date": "mo.ui.date(value='{value}', label='{label}')",
        "table": "mo.ui.table(data={data}, selection='{selection}')",
        "form": "mo.ui.form({form_dict})",
    }

    template = widget_templates.get(widget_type, "mo.ui.{widget_type}()")
    return template.format(widget_type=widget_type, **params)


WIDGET_REFERENCE = """
MARIMO WIDGET REFERENCE
======================

## Input Widgets

**mo.ui.text()**
- Text input field
- Parameters: value, placeholder, label, max_length, kind

**mo.ui.text_area()**
- Multi-line text input
- Parameters: value, placeholder, label, rows, max_length

**mo.ui.number()**
- Numeric input with validation
- Parameters: start, stop, value, step, label

**mo.ui.slider()**
- Range slider for numeric values
- Parameters: start, stop, value, step, label, show_value

**mo.ui.range_slider()**
- Dual-handle range slider
- Parameters: start, stop, value (tuple), step, label

## Selection Widgets

**mo.ui.checkbox()**
- Boolean checkbox
- Parameters: value, label

**mo.ui.switch()**
- Toggle switch (like checkbox but different UI)
- Parameters: value, label

**mo.ui.dropdown()**
- Single selection dropdown
- Parameters: options, value, label, allow_select

**mo.ui.radio()**
- Radio button group
- Parameters: options, value, label

**mo.ui.multiselect()**
- Multi-selection dropdown
- Parameters: options, value, label

## Date/Time Widgets

**mo.ui.date()**
- Date picker
- Parameters: value, label, start, stop

## Action Widgets

**mo.ui.button()**
- Clickable button
- Parameters: label, value, kind (success, danger, neutral)
- Value increments on each click

## Data Widgets

**mo.ui.table()**
- Static data table
- Parameters: data (DataFrame/dict), selection (single/multi)

**mo.ui.dataframe()**
- Interactive dataframe explorer
- Parameters: data (DataFrame)

**mo.ui.data_explorer()**
- Advanced data exploration widget
- Parameters: data (DataFrame)

## File Widgets

**mo.ui.file()**
- File upload
- Parameters: filetypes, multiple, label
- Methods: .contents(), .name()

## Code Widgets

**mo.ui.code_editor()**
- Code editor with syntax highlighting
- Parameters: value, language, label

## Composite Widgets

**mo.ui.form()**
- Group widgets into a form with submit button
- Parameters: dictionary of widgets
- Returns values only when submitted

**mo.ui.array()**
- Array of identical widgets
- Parameters: list of widgets, label

**mo.ui.dictionary()**
- Named collection of widgets
- Parameters: dict of widgets

**mo.ui.batch()**
- Batch updates for multiple widgets
- Parameters: multiple widgets and elements

## Widget Value Access

All widgets have a `.value` property:
- Returns current value for most widgets
- For buttons: returns click count
- For forms: returns dict only when submitted
- For files: use .contents() for file data

## Widget Reactivity

- Assign widget to global variable to make it reactive
- When widget value changes, dependent cells auto-run
- Use widget.value in dependent cells
- Cells re-run automatically on interaction
"""


if __name__ == "__main__":
    app.run()
