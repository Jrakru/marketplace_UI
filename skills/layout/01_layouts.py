"""
Skill: Layout Systems

Master Textual's layout systems: Vertical, Horizontal, Grid, and Dock.
"""

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Button, Label, Placeholder
from textual.containers import (
    Container, Vertical, Horizontal, Grid,
    VerticalScroll, HorizontalScroll, ScrollableContainer
)


# ============================================================================
# VERTICAL LAYOUT (Default)
# ============================================================================

class VerticalLayoutDemo(App):
    """Demonstrates vertical layout (default)."""

    CSS = """
    Vertical {
        background: $panel;
        height: auto;
        padding: 1;
    }

    Static {
        background: $primary 20%;
        border: solid $primary;
        height: 3;
        margin: 1;
        content-align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        with Vertical():
            yield Static("Item 1")
            yield Static("Item 2")
            yield Static("Item 3")
        yield Footer()


# ============================================================================
# HORIZONTAL LAYOUT
# ============================================================================

class HorizontalLayoutDemo(App):
    """Demonstrates horizontal layout."""

    CSS = """
    Horizontal {
        background: $panel;
        height: auto;
        padding: 1;
    }

    Static {
        background: $success 20%;
        border: solid $success;
        width: 20;
        height: 5;
        content-align: center middle;
        margin: 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        with Horizontal():
            yield Static("Left")
            yield Static("Center")
            yield Static("Right")
        yield Footer()


# ============================================================================
# GRID LAYOUT
# ============================================================================

class GridLayoutDemo(App):
    """Demonstrates grid layout."""

    CSS = """
    Grid {
        grid-size: 3 2;  /* 3 columns, 2 rows */
        grid-gutter: 1;
        background: $panel;
        padding: 1;
    }

    .grid-item {
        background: $accent 20%;
        border: solid $accent;
        height: 5;
        content-align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        with Grid():
            yield Static("1", classes="grid-item")
            yield Static("2", classes="grid-item")
            yield Static("3", classes="grid-item")
            yield Static("4", classes="grid-item")
            yield Static("5", classes="grid-item")
            yield Static("6", classes="grid-item")
        yield Footer()


class ResponsiveGridDemo(App):
    """Demonstrates responsive grid with auto-sizing."""

    CSS = """
    Grid {
        grid-size: 4;  /* 4 columns, auto rows */
        grid-gutter: 1 2;  /* vertical horizontal */
        padding: 1;
    }

    .card {
        background: $surface;
        border: round $primary;
        height: 8;
        padding: 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        with Grid():
            for i in range(12):
                yield Static(f"Card {i+1}", classes="card")
        yield Footer()


# ============================================================================
# DOCK LAYOUT
# ============================================================================

class DockLayoutDemo(App):
    """Demonstrates dock layout for sticky elements."""

    CSS = """
    .sidebar {
        dock: left;
        width: 20;
        background: $panel;
        border-right: solid $primary;
        padding: 1;
    }

    .header-bar {
        dock: top;
        height: 3;
        background: $accent;
        color: $text;
        content-align: center middle;
    }

    .footer-bar {
        dock: bottom;
        height: 3;
        background: $accent;
        color: $text;
        content-align: center middle;
    }

    .content {
        background: $surface;
        padding: 2;
    }
    """

    def compose(self) -> ComposeResult:
        yield Static("Header (Docked Top)", classes="header-bar")
        yield Static("Sidebar\n(Docked Left)", classes="sidebar")
        yield Static("Footer (Docked Bottom)", classes="footer-bar")
        yield Static("Main Content\n\nThis content scrolls while docked items stay in place.", classes="content")


# ============================================================================
# SCROLLABLE CONTAINERS
# ============================================================================

class ScrollDemo(App):
    """Demonstrates scrollable containers."""

    CSS = """
    Container {
        height: 100%;
    }

    VerticalScroll {
        width: 1fr;
        background: $panel;
        border: solid $primary;
    }

    HorizontalScroll {
        height: 10;
        background: $panel;
        border: solid $success;
    }

    ScrollableContainer {
        width: 1fr;
        height: 1fr;
        background: $panel;
        border: solid $accent;
    }

    .tall-content {
        height: 100;
        background: $primary 10%;
        padding: 1;
    }

    .wide-content {
        width: 200;
        height: 8;
        background: $success 10%;
        padding: 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()

        with Horizontal():
            # Vertical scroll
            with VerticalScroll():
                yield Static("Scroll vertically ↕\n\n" + "\n".join([f"Line {i}" for i in range(50)]), classes="tall-content")

            # Horizontal scroll
            with VerticalScroll():
                yield Label("Horizontal scroll:")
                with HorizontalScroll():
                    yield Static("Scroll horizontally → " * 20, classes="wide-content")

                yield Label("Both directions:")
                with ScrollableContainer():
                    yield Static(
                        "\n".join([f"Wide line {i} " * 20 for i in range(30)]),
                        classes="tall-content wide-content"
                    )

        yield Footer()


# ============================================================================
# NESTED LAYOUTS
# ============================================================================

class NestedLayoutDemo(App):
    """Demonstrates complex nested layouts."""

    CSS = """
    .main-container {
        background: $surface;
    }

    .sidebar {
        dock: left;
        width: 25;
        background: $panel;
        border-right: solid $primary;
    }

    .top-bar {
        height: 5;
        background: $accent 20%;
        border-bottom: solid $accent;
        padding: 1;
    }

    .content-grid {
        grid-size: 2;
        grid-gutter: 1;
        padding: 1;
    }

    .card {
        background: $panel;
        border: round $primary;
        height: 10;
        padding: 1;
    }

    .button-bar {
        height: auto;
        padding: 1;
        background: $surface-darken-1;
    }

    Button {
        margin: 0 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()

        with Container(classes="main-container"):
            # Sidebar (docked)
            with Vertical(classes="sidebar"):
                yield Label("Navigation")
                yield Button("Home")
                yield Button("Settings")
                yield Button("About")

            # Main content area
            with VerticalScroll():
                # Top bar
                with Horizontal(classes="top-bar"):
                    yield Label("Dashboard")
                    yield Static("", expand=True)  # Spacer
                    yield Button("Refresh", variant="primary")

                # Content grid
                with Grid(classes="content-grid"):
                    yield Static("Analytics", classes="card")
                    yield Static("Users", classes="card")
                    yield Static("Revenue", classes="card")
                    yield Static("Tasks", classes="card")

                # Button bar
                with Horizontal(classes="button-bar"):
                    yield Button("Action 1")
                    yield Button("Action 2", variant="success")
                    yield Button("Action 3", variant="warning")

        yield Footer()


# ============================================================================
# FLEXIBLE LAYOUTS
# ============================================================================

class FlexibleLayoutDemo(App):
    """Demonstrates flexible sizing with fr units."""

    CSS = """
    Horizontal {
        height: 10;
        padding: 1;
    }

    .sidebar {
        width: 20;  /* Fixed width */
        background: $primary 20%;
        border: solid $primary;
        content-align: center middle;
    }

    .main {
        width: 1fr;  /* Takes remaining space */
        background: $success 20%;
        border: solid $success;
        content-align: center middle;
    }

    .panel {
        width: 30;  /* Fixed width */
        background: $accent 20%;
        border: solid $accent;
        content-align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("Fixed(20) + Flexible(1fr) + Fixed(30):")
        with Horizontal():
            yield Static("Sidebar\n20 wide", classes="sidebar")
            yield Static("Main Content\n(Flexible)", classes="main")
            yield Static("Panel\n30 wide", classes="panel")

        yield Label("\nMultiple flexible columns (1fr, 2fr, 1fr):")
        with Horizontal():
            yield Static("1fr", classes="sidebar")
            yield Static("2fr (double width)", classes="main")
            yield Static("1fr", classes="panel")

        yield Footer()


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

LAYOUT_GUIDE = """
LAYOUT SYSTEMS GUIDE
===================

VERTICAL LAYOUT (Default):
- Stacks children top to bottom
- Each child takes full width
- Height is auto or specified

with Vertical():
    yield Widget1()
    yield Widget2()

HORIZONTAL LAYOUT:
- Places children left to right
- Each child takes auto width
- Height matches parent

with Horizontal():
    yield Widget1()
    yield Widget2()

GRID LAYOUT:
- 2D grid of cells
- Specify grid-size: columns [rows]
- Use grid-gutter for spacing
- Auto-flow or explicit placement

Grid {
    grid-size: 3 2;  /* 3 cols, 2 rows */
    grid-gutter: 1 2;  /* vert horiz */
}

DOCK LAYOUT:
- Pin widgets to edges
- Docked widgets don't scroll
- Great for headers/footers/sidebars

.widget {
    dock: top | right | bottom | left;
}

SCROLLABLE CONTAINERS:
- VerticalScroll: Y-axis scrollbar
- HorizontalScroll: X-axis scrollbar
- ScrollableContainer: Both axes

FLEXIBLE SIZING:
- Use 'fr' units for flexible sizing
- 1fr = 1 fraction of remaining space
- Mix with fixed sizes (%, px)

width: 1fr;  /* Takes remaining space */
width: 2fr;  /* Takes 2x remaining space */

BEST PRACTICES:
1. Start with Vertical (default)
2. Use Horizontal for toolbars
3. Grid for card layouts
4. Dock for sticky UI elements
5. ScrollableContainer for overflow
6. fr units for responsive sizing
7. Nest layouts for complex UIs
"""


def get_layout_template(layout_type: str) -> str:
    """Get code template for layout type."""
    templates = {
        "vertical": """with Vertical():
    yield Widget1()
    yield Widget2()
    yield Widget3()
""",
        "horizontal": """with Horizontal():
    yield Widget1()
    yield Widget2()
    yield Widget3()
""",
        "grid": """# In CSS:
Grid {
    grid-size: 3;  /* 3 columns */
    grid-gutter: 1;
}

# In compose():
with Grid():
    for i in range(9):
        yield Widget(f"Item {i}")
""",
        "dock": """# In CSS:
.sidebar {
    dock: left;
    width: 20;
}

# In compose():
yield Widget(classes="sidebar")
""",
        "scroll": """with VerticalScroll():
    yield TallContent()

with HorizontalScroll():
    yield WideContent()

with ScrollableContainer():
    yield TallAndWideContent()
""",
    }
    return templates.get(layout_type, "# Template not found")


if __name__ == "__main__":
    app = NestedLayoutDemo()
    app.run()
