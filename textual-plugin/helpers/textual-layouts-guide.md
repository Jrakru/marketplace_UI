# textual-layouts-guide

Master Textual layouts: Vertical, Horizontal, Grid, Dock, and advanced layout patterns for responsive TUI applications.

## Overview

Textual provides multiple layout systems to arrange widgets in terminal space. Understanding these layouts is crucial for creating responsive, well-organized TUIs.

## Layout Fundamentals

### Layout Concepts

**1. Composition**
- Widgets are arranged hierarchically
- Parent containers control child positioning
- Layout flows from parent to children

**2. Sizing**
- `auto`: Size based on content
- `fraction`: Proportional size
- `fill`: Fill available space
- Fixed: Exact pixel size

**3. Alignment**
- Horizontal: left, center, right
- Vertical: top, middle, bottom

### Layout Priority

1. **Explicit sizing**: Fixed sizes set directly
2. **Content sizing**: Size based on widget content
3. **Available space**: Remaining space distributed
4. **Layout defaults**: Container-level defaults

## Vertical Layout

Stack widgets vertically (top to bottom).

### Basic Usage

```python
from textual.containers import Vertical

class VerticalLayoutApp(App):
    def compose(self):
        with Vertical():
            yield Static("First item")
            yield Static("Second item")
            yield Static("Third item")
```

### Vertical with Spacing

```python
with Vertical(classes="stack", gap=1):
    yield Static("Item 1")
    yield Static("Item 2")
    yield Static("Item 3")
```

### Vertical with Alignment

```python
# Center align
with Vertical(align="center"):
    yield Static("Centered text")

# Right align
with Vertical(align="right"):
    yield Static("Right aligned")
```

### Vertical with Expansion

```python
with Vertical():
    yield Static("Fixed height header")
    # This expands to fill remaining space
    yield Static("Expands", classes="expand")
    yield Static("Fixed height footer")
```

### Real Example: Navigation Menu

```python
with Vertical(classes="menu", id="sidebar"):
    yield Static("MENU", classes="menu-title")
    yield Button("Dashboard", variant="default")
    yield Button("Users", variant="default")
    yield Button("Settings", variant="default")
    yield Button("Help", variant="default")
    # Expand to push logout to bottom
    yield Static("", classes="expand")
    yield Button("Logout", variant="error")
```

## Horizontal Layout

Arrange widgets horizontally (left to right).

### Basic Usage

```python
from textual.containers import Horizontal

class HorizontalLayoutApp(App):
    def compose(self):
        with Horizontal():
            yield Static("Left")
            yield Static("Center")
            yield Static("Right")
```

### Horizontal with Expansion

```python
with Horizontal():
    yield Static("Fixed width", size=(15, 1))
    # Expands to fill remaining space
    yield Static("Expands", classes="expand")
    yield Static("Fixed width", size=(15, 1))
```

### Horizontal with Spacing

```python
with Horizontal(classes="toolbar", gap=2):
    yield Button("New", variant="primary")
    yield Button("Open")
    yield Button("Save")
    yield Static("", classes="expand")  # Spacer
    yield Button("Help")
```

### Real Example: Toolbar

```python
with Horizontal(classes="toolbar"):
    yield Button("◀", variant="default", size=(3, 1))
    yield Button("▶", variant="default", size=(3, 1))
    yield Static("", classes="expand")
    yield Input(placeholder="Search...", size=(30, 1))
    yield Button("Search", variant="primary")
```

## Grid Layout

Grid-based layout with rows and columns.

### Basic Grid

```python
from textual.containers import Grid

with Grid():
    yield Button("A", grid_size=(1, 1))
    yield Button("B", grid_size=(1, 1))
    yield Button("C", grid_size=(1, 1))
    yield Button("D", grid_size=(1, 1))
```

### Grid with Specific Positions

```python
with Grid():
    # Row 0, Column 0-1 (spans 2 columns)
    yield Static("Header", grid_size=(2, 1))
    # Row 1, Column 0
    yield Button("A", grid_gutter=1, column=0, row=1)
    # Row 1, Column 1
    yield Button("B", grid_gutter=1, column=1, row=1)
    # Row 2, Spans full width
    yield Button("Footer", grid_size=(2, 1), row=2)
```

### Grid with Size Definitions

```python
# Define column and row sizes
with Grid(
    column_sizes=[1, 2, 1],  # 3 columns with ratios
    row_sizes=[1, 3, 1],     # 3 rows with ratios
):
    # Widgets will follow these proportions
    yield Button("Top Left")
    yield Button("Top Center")
    yield Button("Top Right")
    yield Button("Middle Left")
    yield Button("Middle Center")
    yield Button("Middle Right")
    yield Button("Bottom Left")
    yield Button("Bottom Center")
    yield Button("Bottom Right")
```

### Grid with Named Areas

```python
with Grid(
    column_sizes=[1, 3, 1],
    row_sizes=[1, 4, 1],
):
    # Named areas
    yield Button("Sidebar", area="left")
    yield Button("Content", area="center")
    yield Button("Panel", area="right")
    yield Button("Footer", area="footer")
```

### Real Example: Dashboard Grid

```python
with Grid(
    column_sizes=[2, 3, 2],
    row_sizes=[1, 3, 1],
    gutter=1,
):
    # Header spans full width
    yield Static("Dashboard", grid_size=(3, 1), classes="title")
    # Stats cards
    yield DataTable(classes="card", area="stats-left")
    yield Static("Main Content", classes="card", area="main")
    yield Log(classes="card", area="stats-right")
    # Footer spans full width
    yield Static("Status Bar", grid_size=(3, 1), classes="footer")
```

## Dock Layout

Dock widgets to screen edges.

### Basic Docking

```python
from textual.containers import DockPane

class DockLayoutApp(App):
    def compose(self):
        # Top dock (toolbar)
        yield DockPane(
            Horizontal(
                Button("File"), Button("Edit"), Button("View"),
            ),
            edge="top",
            size=1,
        )
        # Bottom dock (status)
        yield DockPane(
            Static("Status: Ready"),
            edge="bottom",
            size=1,
        )
        # Left dock (navigation)
        yield DockPane(
            Vertical(
                Button("Dashboard"),
                Button("Reports"),
                Button("Settings"),
            ),
            edge="left",
            size=20,
        )
        # Right dock (properties)
        yield DockPane(
            Static("Properties"),
            edge="right",
            size=25,
        )
        # Center content
        with Container(id="main-content"):
            yield Static("Main application area")
```

### Multiple DockPanes on Same Edge

```python
# Multiple top docks
yield DockPane(Toolbar1(), edge="top", z=1)
yield DockPane(Toolbar2(), edge="top", z=2)

# Order: higher z-index on top
```

### Dock with Toggles

```python
class DockApp(App):
    """App with toggleable docks."""

    def compose(self):
        yield DockPane(
            NavigationPanel(),
            edge="left",
            size=25,
            id="nav-dock",
        )
        yield DockPane(
            PropertiesPanel(),
            edge="right",
            size=25,
            id="prop-dock",
        )

    def on_key(self, event) -> None:
        # Toggle left dock
        if event.key == "f1":
            nav = self.query_one("#nav-dock", DockPane)
            nav.visible = not nav.visible
        # Toggle right dock
        elif event.key == "f2":
            prop = self.query_one("#prop-dock", DockPane)
            prop.visible = not prop.visible
```

### Real Example: IDE Layout

```python
def compose(self):
    # Top: Menu bar
    yield DockPane(
        Horizontal(
            Button("File"), Button("Edit"), Button("View"),
            Button("Run"), Button("Help"),
            classes="menu-bar",
        ),
        edge="top",
        size=1,
    )

    # Left: File explorer
    yield DockPane(
        Vertical(
            Static("Explorer", classes="panel-title"),
            Tree(),
            classes="explorer",
        ),
        edge="left",
        size=25,
    )

    # Center: Editor and panels
    with Container(id="center"):
        with Vertical():
            # Editor tabs
            yield Tabs("main.py", "utils.py")
            # Editor area
            with Horizontal():
                TextArea(id="editor")
                Vertical(
                    Static("Output", classes="panel-title"),
                    Log(id="output"),
                    Static("Console", classes="panel-title"),
                    Log(id="console"),
                )
            )

    # Right: Properties
    yield DockPane(
        Vertical(
            Static("Properties", classes="panel-title"),
            DataTable(id="props"),
        ),
        edge="right",
        size=30,
    )

    # Bottom: Status bar
    yield DockPane(
        Horizontal(
            Static("Line 1, Col 1", id="cursor-pos"),
            Static("", classes="expand"),
            Static("UTF-8", id="encoding"),
            Static("Python", id="language"),
        ),
        edge="bottom",
        size=1,
    )
```

## Complex Layout Patterns

### Master-Detail Pattern

```python
class MasterDetailApp(App):
    def compose(self):
        with Horizontal():
            # Master (left)
            with Container(id="master", size=30):
                yield Static("Items", classes="title")
                Tree(id="items-tree")
            # Detail (right)
            with Vertical(id="detail"):
                yield Static("Details", classes="title")
                Static("", id="detail-content")

    def on_tree_node_selected(self, event):
        node = event.node
        detail = self.query_one("#detail-content", Static)
        detail.update(f"Selected: {node.label}")
```

### Card Layout

```python
with Horizontal(classes="cards", gap=2):
    # Card 1
    with Container(classes="card"):
        yield Static("Card 1", classes="card-title")
        yield Static("Content 1")
    # Card 2
    with Container(classes="card"):
        yield Static("Card 2", classes="card-title")
        yield Static("Content 2")
    # Card 3
    with Container(classes="card"):
        yield Static("Card 3", classes="card-title")
        yield Static("Content 3")
```

### Responsive Layout

```python
class ResponsiveApp(App):
    def compose(self):
        self.layout_container = Container()
        yield self.layout_container
        self.set_layout()

    def on_mount(self):
        self.set_interval(0.1, self.check_terminal_size)

    def check_terminal_size(self):
        old_layout = self.current_layout
        width = self.size.width

        if width < 50:
            self.current_layout = "single"
        elif width < 80:
            self.current_layout = "dual"
        else:
            self.current_layout = "triple"

        if old_layout != self.current_layout:
            self.set_layout()

    def set_layout(self):
        if self.current_layout == "single":
            with self.layout_container:
                yield Static("Single column layout")
        elif self.current_layout == "dual":
            with self.layout_container:
                with Horizontal():
                    yield Static("Left column")
                    yield Static("Right column")
        else:
            with self.layout_container:
                with Horizontal():
                    yield Static("Left")
                    yield Static("Center")
                    yield Static("Right")
```

### Nested Layouts

```python
def compose(self):
    with Horizontal():
        # Left side
        with Vertical():
            # Top section
            with Horizontal():
                yield Static("Panel A1")
                yield Static("Panel A2")
            # Bottom section
            yield Static("Panel A3")

        # Right side
        with Vertical():
            yield Static("Panel B1")
            with Horizontal():
                yield Static("Panel B2a")
                yield Static("Panel B2b")
            yield Static("Panel B3")
```

### Dynamic Layout

```python
class DynamicLayoutApp(App):
    def __init__(self):
        super().__init__()
        self.widgets = []

    def compose(self):
        self.container = Container()
        yield self.container

    def add_widget(self):
        """Add a new widget to the layout."""
        widget_id = f"widget-{len(self.widgets)}"
        self.widgets.append(widget_id)

        # Rebuild layout
        with self.container:
            self.build_layout()

    def build_layout(self):
        """Build layout based on number of widgets."""
        count = len(self.widgets)

        if count <= 3:
            # Vertical stack
            with Vertical():
                for widget_id in self.widgets:
                    yield Static(widget_id)
        elif count <= 6:
            # 2x2 grid
            with Grid():
                for widget_id in self.widgets:
                    yield Static(widget_id)
        else:
            # Horizontal wrap
            with Vertical():
                for i in range(0, count, 3):
                    with Horizontal():
                        for widget_id in self.widgets[i:i+3]:
                            yield Static(widget_id)
```

## Layout Utilities

### Layout Helper Functions

```python
def create_centered_container(width=50, height=10):
    """Create a centered container of specified size."""
    return Container(
        classes="centered",
        styles=f"""
            width: {width};
            height: {height};
            dock: center;
        """,
    )

def create_equal_columns(count):
    """Create horizontal layout with equal columns."""
    return Horizontal(
        *[Container(classes="column") for _ in range(count)]
    )

def create_card_grid(columns, rows):
    """Create a grid of cards."""
    with Grid():
        for i in range(columns * rows):
            yield Container(classes="card")
```

### Layout Mixins

```python
class LayoutMixin:
    """Mixin for common layout patterns."""

    def create_sidebar_layout(self, sidebar_width=20):
        """Create a sidebar + main area layout."""
        with Horizontal():
            yield Container(size=sidebar_width, id="sidebar")
            yield Container(id="main")

    def create_header_content_footer(self, header_height=1, footer_height=1):
        """Create header + content + footer layout."""
        with Vertical():
            yield Container(size=header_height, id="header")
            yield Container(id="content", classes="expand")
            yield Container(size=footer_height, id="footer")

    def create_panel_layout(self, panel_size=30):
        """Create main area + side panel layout."""
        with Horizontal():
            yield Container(id="main", classes="expand")
            yield Container(size=panel_size, id="panel")
```

## CSS Layout Properties

### Container CSS

```css
/* Horizontal alignment */
.horizontal-center {
    align: center;
}

.horizontal-left {
    align: left;
}

.horizontal-right {
    align: right;
}

/* Vertical alignment */
.vertical-middle {
    align: center;
}

.vertical-top {
    align: top;
}

.vertical-bottom {
    align: bottom;
}

/* Grid */
.grid {
    grid-size: 2 2;  /* 2 columns, 2 rows */
    grid-gutter: 1 1;
}

/* Expansion */
.expand {
    /* Expands to fill available space */
}

/* Spacing */
.gap-1 {
    gap: 1;
}

.gap-2 {
    gap: 2;
}

/* Scrollable */
.scrollable {
    overflow: auto;
}
```

### Responsive CSS

```css
/* Hide on small screens */
@media (width < 80) {
    .hide-small {
        display: none;
    }
}

/* Stack vertically on small screens */
@media (width < 80) {
    .horizontal {
        layout: vertical;
    }
}

/* Compact on small screens */
@media (width < 60) {
    .compact {
        padding: 0;
        margin: 0;
    }
}
```

## Best Practices

### 1. Plan Your Hierarchy

```python
# Good: Clear hierarchy
with Vertical():
    yield Header()
    with Horizontal():
        yield Container(id="sidebar")
        yield Container(id="main")
    yield Footer()

# Avoid: Deep nesting
with Vertical():
    with Vertical():
        with Vertical():
            yield Widget()
```

### 2. Use Semantic IDs

```python
# Good
with Container(id="user-profile"):
    pass

with Button(id="save-user-button"):
    pass

# Avoid
with Container(id="container1"):
    pass

with Button(id="button2"):
    pass
```

### 3. Leverage Expansion Classes

```python
# Good: Use expansion classes
with Vertical():
    yield Static("Header")
    yield Static("Expands", classes="expand")
    yield Static("Footer")

# Avoid: Fixed sizes for dynamic content
with Vertical():
    yield Static("Header")
    yield Static("Fixed\nHeight\nContent")
    yield Static("Footer")
```

### 4. Combine Layouts Appropriately

```python
# Grid for complex arrangements
# Vertical/Horizontal for lists
# Docks for toolbars and status bars
# Container for custom layouts
```

### 5. Make Layouts Responsive

```python
# Check terminal size
def on_mount(self):
    self.set_interval(0.1, self.adjust_layout)

def adjust_layout(self):
    width = self.size.width
    # Adjust layout based on width
```

### 6. Use Loading and Error States

```python
class ContentArea(Container):
    def compose(self):
        self.content_container = Container(id="content")
        yield self.content_container

    def show_loading(self):
        with self.content_container:
            yield LoadingIndicator("Loading...")

    def show_content(self, content):
        with self.content_container:
            yield content

    def show_error(self, message):
        with self.content_container:
            yield Static(message, classes="error")
```

## Common Layout Templates

### Application Shell

```python
def compose(self):
    yield DockPane(Toolbar(), edge="top", size=1)
    with Horizontal():
        yield DockPane(Navigation(), edge="left", size=20)
        yield Container(id="main-content", classes="expand")
        yield DockPane(Properties(), edge="right", size=25)
    yield DockPane(StatusBar(), edge="bottom", size=1)
```

### Dashboard

```python
def compose(self):
    with Vertical():
        # Header
        with Horizontal():
            yield Static("Dashboard", classes="title")
            yield Static("", classes="expand")
            yield Button("Refresh")
        # Content grid
        with Grid():
            yield DataTable(classes="widget")
            yield Static("Stats", classes="widget")
            yield Log(classes="widget")
        # Footer
        yield Static("Last updated: now")
```

### Settings Panel

```python
def compose(self):
    with Horizontal():
        # Settings categories
        with Container(size=20):
            yield Static("Categories")
            Tree(id="category-tree")
        # Settings content
        with Vertical():
            yield Static("General Settings", id="settings-title")
            Vertical(id="settings-form")
```

## See Also

- [Textual Widgets Reference](textual-widgets-reference.md)
- [Textual CSS Styling](textual-css-styling.md)
- [Textual Events Handling](textual-events-handling.md)
