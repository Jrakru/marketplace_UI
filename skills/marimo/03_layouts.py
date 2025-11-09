"""
Skill: Marimo Layouts and UI Organization

This skill covers layout functions in Marimo for organizing UI elements,
including stacks, grids, tabs, accordions, sidebars, and navigation menus.
"""

import marimo

__generated_with = "0.10.11"
app = marimo.App()


# ============================================================================
# LAYOUT BASICS
# ============================================================================

@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def __(mo):
    mo.md(
        """
        # Marimo Layout Guide

        Marimo provides powerful layout functions to organize your notebook content:
        - **mo.hstack()** - Horizontal stacking (rows)
        - **mo.vstack()** - Vertical stacking (columns)
        - **mo.accordion()** - Collapsible sections
        - **mo.ui.tabs()** - Tabbed interface
        - **mo.sidebar()** - Sidebar navigation
        - **mo.nav_menu()** - Navigation menu
        - **mo.callout()** - Highlighted callout boxes
        """
    )
    return


# ============================================================================
# HORIZONTAL STACKS (ROWS)
# ============================================================================

@app.cell
def __(mo):
    mo.md("## 📏 Horizontal Stacks (mo.hstack)")
    return


@app.cell
def __(mo):
    """Basic horizontal stack."""
    mo.hstack([
        mo.md("**Column 1**"),
        mo.md("**Column 2**"),
        mo.md("**Column 3**")
    ], gap=2)
    return


@app.cell
def __(mo):
    """Horizontal stack with custom justification."""
    mo.hstack([
        mo.ui.button(label="Left"),
        mo.ui.button(label="Center"),
        mo.ui.button(label="Right")
    ], justify="space-between", gap=1)
    return


@app.cell
def __(mo):
    """Horizontal stack with custom alignment."""
    mo.hstack([
        mo.md("# Big"),
        mo.md("Small"),
        mo.md("## Medium")
    ], align="center", gap=2)
    return


@app.cell
def __(mo):
    """Horizontal stack with custom widths."""
    mo.hstack([
        mo.md("25% width"),
        mo.md("50% width"),
        mo.md("25% width")
    ], widths=[1, 2, 1], gap=1)
    return


@app.cell
def __(mo):
    """Horizontal stack with wrapping."""
    items = [mo.ui.button(label=f"Button {i}") for i in range(10)]
    mo.hstack(items, wrap=True, gap=0.5)
    return


# ============================================================================
# VERTICAL STACKS (COLUMNS)
# ============================================================================

@app.cell
def __(mo):
    mo.md("## 📐 Vertical Stacks (mo.vstack)")
    return


@app.cell
def __(mo):
    """Basic vertical stack."""
    mo.vstack([
        mo.md("## Title"),
        mo.md("This is some content."),
        mo.ui.button(label="Action Button"),
        mo.md("_Footer text_")
    ], gap=1)
    return


@app.cell
def __(mo):
    """Vertical stack with custom alignment."""
    mo.vstack([
        mo.md("Left aligned"),
        mo.md("Content here"),
        mo.ui.button(label="Click me")
    ], align="start", gap=1)
    return


@app.cell
def __(mo):
    """Vertical stack with custom heights."""
    mo.vstack([
        mo.md("30% height"),
        mo.md("50% height"),
        mo.md("20% height")
    ], heights=[0.3, 0.5, 0.2], gap=1)
    return


# ============================================================================
# GRIDS (COMBINING STACKS)
# ============================================================================

@app.cell
def __(mo):
    mo.md("## 🔲 Grids (Combining Stacks)")
    return


@app.cell
def __(mo):
    """Create a 2x2 grid."""
    mo.vstack([
        mo.hstack([
            mo.md("**Top Left**"),
            mo.md("**Top Right**")
        ], gap=1),
        mo.hstack([
            mo.md("**Bottom Left**"),
            mo.md("**Bottom Right**")
        ], gap=1)
    ], gap=1)
    return


@app.cell
def __(mo):
    """Dashboard-style grid layout."""
    mo.hstack([
        # Left sidebar
        mo.vstack([
            mo.md("## Navigation"),
            mo.ui.button(label="Home"),
            mo.ui.button(label="Settings"),
            mo.ui.button(label="Profile")
        ], gap=0.5),

        # Main content area
        mo.vstack([
            mo.md("## Main Content"),
            mo.hstack([
                mo.md("**Widget 1**"),
                mo.md("**Widget 2**")
            ], gap=1),
            mo.md("Additional content here...")
        ], gap=1)
    ], widths=[1, 3], gap=2)
    return


# ============================================================================
# TABS
# ============================================================================

@app.cell
def __(mo):
    mo.md("## 📑 Tabs (mo.ui.tabs)")
    return


@app.cell
def __(mo):
    """Basic tabs."""
    tabs = mo.ui.tabs({
        "Overview": mo.md("""
        # Welcome!

        This is the overview tab with introductory content.
        """),

        "Data": mo.md("""
        ## Data Section

        Here's where your data visualizations would go.
        """),

        "Settings": mo.vstack([
            mo.md("### Configuration"),
            mo.ui.checkbox(label="Enable feature A"),
            mo.ui.checkbox(label="Enable feature B"),
            mo.ui.slider(start=0, stop=100, value=50, label="Threshold")
        ], gap=1)
    })

    tabs
    return tabs,


@app.cell
def __(mo, tabs):
    """Show selected tab."""
    mo.md(f"**Currently viewing:** {tabs.value}")
    return


# ============================================================================
# ACCORDIONS
# ============================================================================

@app.cell
def __(mo):
    mo.md("## 🪗 Accordions (mo.accordion)")
    return


@app.cell
def __(mo):
    """Accordion for collapsible sections."""
    mo.accordion({
        "Section 1: Introduction": mo.md("""
        This is the first section of content.
        It can contain any marimo elements.
        """),

        "Section 2: Details": mo.md("""
        Here are more detailed explanations and examples.
        """),

        "Section 3: Advanced": mo.vstack([
            mo.md("Advanced configuration options:"),
            mo.ui.text(placeholder="API Key"),
            mo.ui.number(start=0, stop=1000, value=100, label="Timeout (ms)")
        ], gap=1)
    })
    return


# ============================================================================
# SIDEBAR
# ============================================================================

@app.cell
def __(mo):
    mo.md("## 📌 Sidebar (mo.sidebar)")
    return


@app.cell
def __(mo):
    """Create a sidebar with controls."""
    with mo.sidebar():
        mo.md("## Controls")

        slider = mo.ui.slider(
            start=1,
            stop=100,
            value=50,
            label="Sample Size"
        )

        plot_type = mo.ui.dropdown(
            options=["Line", "Bar", "Scatter"],
            value="Line",
            label="Plot Type"
        )

        show_grid = mo.ui.checkbox(
            value=True,
            label="Show Grid"
        )

        mo.vstack([slider, plot_type, show_grid])

    mo.md("Main content area - sidebar controls are on the left →")
    return


# ============================================================================
# NAVIGATION MENU
# ============================================================================

@app.cell
def __(mo):
    mo.md("## 🧭 Navigation Menu (mo.nav_menu)")
    return


@app.cell
def __(mo):
    """Navigation menu."""
    nav = mo.nav_menu({
        "Home": "/",
        "Dashboard": "/dashboard",
        "Settings": "/settings",
        "Profile": "/profile"
    })

    nav
    return nav,


# ============================================================================
# CALLOUTS
# ============================================================================

@app.cell
def __(mo):
    mo.md("## 💬 Callouts (mo.callout)")
    return


@app.cell
def __(mo):
    """Different types of callouts."""
    mo.vstack([
        mo.callout(
            mo.md("This is an informational callout."),
            kind="info"
        ),

        mo.callout(
            mo.md("⚠️ Warning: This action cannot be undone."),
            kind="warn"
        ),

        mo.callout(
            mo.md("❌ Error: Something went wrong."),
            kind="danger"
        ),

        mo.callout(
            mo.md("✅ Success: Operation completed!"),
            kind="success"
        )
    ], gap=1)
    return


# ============================================================================
# COMPLEX LAYOUT EXAMPLE
# ============================================================================

@app.cell
def __(mo):
    mo.md("## 🎨 Complex Layout Example")
    return


@app.cell
def __(mo):
    """
    Build a complete dashboard layout combining multiple layout elements.
    """
    # Header
    header = mo.md("# 📊 Analytics Dashboard")

    # Metrics row
    metrics = mo.hstack([
        mo.callout(mo.md("**Users**\n1,234"), kind="info"),
        mo.callout(mo.md("**Revenue**\n$56,789"), kind="success"),
        mo.callout(mo.md("**Errors**\n12"), kind="warn")
    ], gap=1)

    # Main content with tabs
    content_tabs = mo.ui.tabs({
        "Charts": mo.md("📈 Chart visualizations would go here"),
        "Tables": mo.md("📋 Data tables would go here"),
        "Reports": mo.md("📄 Generated reports would go here")
    })

    # Settings accordion
    settings = mo.accordion({
        "Display Settings": mo.vstack([
            mo.ui.dropdown(
                options=["Light", "Dark", "Auto"],
                value="Auto",
                label="Theme"
            ),
            mo.ui.slider(start=10, stop=24, value=14, label="Font Size")
        ], gap=1),

        "Data Settings": mo.vstack([
            mo.ui.number(start=1, stop=100, value=10, label="Rows per page"),
            mo.ui.checkbox(value=True, label="Auto-refresh")
        ], gap=1)
    })

    # Combine everything
    mo.vstack([
        header,
        metrics,
        content_tabs,
        settings
    ], gap=2)
    return


# ============================================================================
# LAYOUT HELPER FUNCTIONS
# ============================================================================

def create_grid_layout(rows, cols, content=None):
    """
    Generate code for a grid layout.

    Args:
        rows: Number of rows
        cols: Number of columns
        content: Optional 2D array of content

    Returns:
        str: Code for grid layout
    """
    if content is None:
        content = [[f"Cell ({i},{j})" for j in range(cols)] for i in range(rows)]

    code = "mo.vstack([\n"
    for i, row in enumerate(content):
        code += "    mo.hstack([\n"
        for j, cell in enumerate(row):
            code += f'        mo.md("{cell}"),\n'
        code += "    ], gap=1),\n"
    code += "], gap=1)"

    return code


def create_dashboard_layout(sidebar_content=None, main_content=None, header=None):
    """
    Generate code for a dashboard layout with sidebar.

    Args:
        sidebar_content: Content for sidebar
        main_content: Main content area
        header: Optional header content

    Returns:
        str: Code for dashboard layout
    """
    template = """
mo.vstack([
    {header}
    mo.hstack([
        mo.vstack([
            {sidebar}
        ], gap=1),
        mo.vstack([
            {main}
        ], gap=1)
    ], widths=[1, 3], gap=2)
], gap=2)
"""
    return template.format(
        header=f'mo.md("{header}"),' if header else "",
        sidebar=sidebar_content or 'mo.md("Sidebar")',
        main=main_content or 'mo.md("Main Content")'
    )


LAYOUT_REFERENCE = """
MARIMO LAYOUT REFERENCE
======================

## mo.hstack() - Horizontal Stack

Arranges items in a horizontal row.

**Parameters:**
- items: List of elements to stack
- justify: "start", "center", "end", "space-between", "space-around"
- align: "start", "end", "center", "stretch"
- gap: Float, spacing between items (default 0.5)
- widths: List of floats or "equal" for equal widths
- wrap: Boolean, enable wrapping

**Example:**
```python
mo.hstack([
    mo.md("Left"),
    mo.md("Middle"),
    mo.md("Right")
], justify="space-between", gap=2)
```

## mo.vstack() - Vertical Stack

Arranges items in a vertical column.

**Parameters:**
- items: List of elements to stack
- align: "start", "center", "end", "stretch"
- justify: "start", "center", "end", "space-between", "space-around"
- gap: Float, spacing between items
- heights: List of floats or "equal" for equal heights

**Example:**
```python
mo.vstack([
    mo.md("## Title"),
    mo.md("Content"),
    mo.ui.button(label="Action")
], gap=1)
```

## mo.ui.tabs() - Tabbed Interface

Creates a tabbed interface.

**Parameters:**
- tabs: Dictionary mapping tab names to content

**Example:**
```python
tabs = mo.ui.tabs({
    "Tab 1": mo.md("Content 1"),
    "Tab 2": mo.md("Content 2")
})
```

## mo.accordion() - Collapsible Sections

Creates collapsible accordion sections.

**Parameters:**
- sections: Dictionary mapping section titles to content

**Example:**
```python
mo.accordion({
    "Section 1": mo.md("Content 1"),
    "Section 2": mo.md("Content 2")
})
```

## mo.sidebar() - Sidebar

Creates a sidebar (context manager).

**Example:**
```python
with mo.sidebar():
    mo.md("## Sidebar Content")
    mo.ui.slider(0, 100, label="Control")
```

## mo.nav_menu() - Navigation Menu

Creates a navigation menu.

**Parameters:**
- items: Dictionary mapping labels to URLs

**Example:**
```python
mo.nav_menu({
    "Home": "/",
    "About": "/about"
})
```

## mo.callout() - Callout Box

Creates highlighted callout boxes.

**Parameters:**
- content: Content to display
- kind: "info", "warn", "danger", "success", "neutral"

**Example:**
```python
mo.callout(
    mo.md("Important message"),
    kind="warn"
)
```

## Layout Patterns

**Dashboard Layout:**
```python
mo.hstack([
    mo.vstack([...]),  # Sidebar
    mo.vstack([...])   # Main content
], widths=[1, 3])
```

**Grid Layout:**
```python
mo.vstack([
    mo.hstack([cell1, cell2]),
    mo.hstack([cell3, cell4])
])
```

**Card Layout:**
```python
mo.hstack([
    mo.callout(content1, kind="info"),
    mo.callout(content2, kind="success"),
    mo.callout(content3, kind="warn")
], gap=1)
```

## Best Practices

1. Use consistent gap values for visual harmony
2. Prefer vstack for main content flow
3. Use hstack for controls and metrics
4. Combine layouts for complex UIs
5. Use tabs to organize related content
6. Use accordion for optional/advanced content
7. Keep sidebar for persistent controls
8. Use callouts to highlight important info
"""


if __name__ == "__main__":
    app.run()
