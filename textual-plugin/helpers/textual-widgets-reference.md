# textual-widgets-reference

Complete reference guide for Textual widgets with examples, patterns, and best practices.

## Overview

Textual provides a comprehensive set of built-in widgets for building terminal user interfaces. This reference covers all available widgets, their properties, events, and usage patterns.

## Core Widgets

### Static
Display static text that doesn't change frequently.

```python
from textual.widgets import Static

# Basic usage
Static("Hello, World!")

# With styling
Static("Important Message", classes="title highlight")

# Dynamic content
Static("", id="dynamic-text")

# Update content
def update_text(self):
    self.query_one("#dynamic-text", Static).update("New text")
```

**Key Properties:**
- `content`: The text to display
- `renderable`: Text or rich renderable object
- `expand`: Whether to expand to fill space

### Button
Interactive button widget for user actions.

```python
from textual.widgets import Button

# Standard button
Button("Click Me", variant="primary")

# Different variants
Button("Primary", variant="primary")
Button("Success", variant="success")
Button("Warning", variant="warning")
Button("Error", variant="error")

# Disabled button
Button("Disabled", disabled=True)

# Custom size
Button("Wide Button", size=(20, 1))

# With icon
Button("📁 Open File", variant="default")
```

**Events:**
- `Button.Pressed`: Fired when button is activated

**Common Patterns:**
```python
def on_button_pressed(self, event: Button.Pressed) -> None:
    if event.button.id == "save":
        self.save_data()
    elif event.button.id == "cancel":
        self.discard_changes()
```

### Input
Single-line text input widget.

```python
from textual.widgets import Input

# Basic input
Input(placeholder="Enter text...")

# Password input
Input(password=True, placeholder="Password")

# With initial value
Input(value="Default text")

# Validation
Input(validate=True, pattern=r'\d+')

# Custom width
Input(size=(30, 1))

# Label
Input(placeholder="Username", id="username")
```

**Properties:**
- `value`: Current text value
- `placeholder`: Placeholder text
- `password`: Hide text (password mode)
- `validate`: Enable validation
- `pattern`: Validation regex pattern
- `max_length`: Maximum text length

**Events:**
- `Input.Changed`: Text value changed
- `Input.Submitted`: Enter key pressed

### TextArea
Multi-line text editing widget.

```python
from textual.widgets import TextArea

# Basic text area
TextArea()

# Initial content
TextArea("Initial text\nSecond line")

# Read-only
TextArea("Read-only text", read_only=True)

# Syntax highlighting
TextArea(code="python")
TextArea(code="json")
TextArea(code="yaml")

# Line numbers
TextArea(show_line_numbers=True)

# Word wrap
TextArea(word_wrap=True)
```

**Properties:**
- `text`: Current content
- `language`: Syntax language for highlighting
- `theme`: Editor theme
- `read_only`: Prevent editing
- `show_line_numbers`: Display line numbers
- `word_wrap`: Wrap long lines

**Events:**
- `TextArea.Changed`: Content modified
- `TextArea.Submitted`: Ctrl+M pressed

### Label
Display text with styling (similar to Static but more semantic).

```python
from textual.widgets import Label

Label("Status:")
Label("Title", classes="title")
Label("Subtitle", classes="subtitle")
```

## Layout Containers

### Container
Generic container for grouping widgets.

```python
from textual.containers import Container

# Basic container
with Container():
    yield Button("OK")
    yield Button("Cancel")

# Styled container
with Container(classes="panel"):
    yield Static("Panel content")

# Scrollable container
with Container(classes="scrollable"):
    # Many widgets
    for i in range(100):
        yield Button(f"Item {i}")
```

### Vertical
Stack widgets vertically (top to bottom).

```python
from textual.containers import Vertical

with Vertical():
    yield Static("Top")
    yield Static("Middle")
    yield Static("Bottom")

# With alignment
with Vertical(align="center"):
    yield Button("Centered")
```

### Horizontal
Arrange widgets horizontally (left to right).

```python
from textual.containers import Horizontal

with Horizontal():
    yield Button("Left")
    yield Static("Center")
    yield Button("Right")

# With expansion
with Horizontal():
    yield Button("Fixed", size=(10, 1))
    yield Static("Expands", classes="expand")
```

### Grid
Grid-based layout with rows and columns.

```python
from textual.containers import Grid

with Grid():
    # Row 1
    yield Button("A", grid_size=(1, 1))
    yield Button("B", grid_size=(1, 1))
    # Row 2
    yield Button("C", grid_size=(2, 1))

# With column/row sizes
with Grid(column_sizes=[1, 2, 1], row_sizes=[1, 1]):
    # Widgets with grid positions
```

### DockPane
Dock widgets to screen edges.

```python
from textual.containers import DockPane

# Left dock
yield DockPane("Navigation", edge="left")

# Right dock
yield DockPane("Properties", edge="right")

# Top dock
yield DockPane("Toolbar", edge="top")

# Bottom dock
yield DockPane("Status Bar", edge="bottom")
```

### Tabs
Tabbed interface for multiple views.

```python
from textual.widgets import Tabs, TabPane

with Tabs("Tab 1", "Tab 2", "Tab 3"):
    with TabPane("Content 1", id="tab1"):
        yield Static("First tab content")
    with TabPane("Content 2", id="tab2"):
        yield Static("Second tab content")
    with TabPane("Content 3", id="tab3"):
        yield Static("Third tab content")

# Programmatic tab switching
tabs = self.query_one(Tabs)
tabs.active = "tab2"

# Handle tab changes
def on_tabs_tab_changed(self, event: Tabs.TabChanged) -> None:
    self.log(f"Tab changed to: {event.tab.id}")
```

## Data Display Widgets

### DataTable
Spreadsheet-like table for tabular data.

```python
from textual.widgets import DataTable

# Create table
table = DataTable()
table.add_columns("Name", "Age", "City")
table.add_rows([
    ("Alice", 30, "New York"),
    ("Bob", 25, "Los Angeles"),
    ("Charlie", 35, "Chicago"),
])

# Selection mode
table.cursor_type = "row"  # or "cell" or "none"

# Cell types
table.add_columns("Price", "Stock")
table.add_row("$19.99", 42, cell_types=[Numeric(), Progress()])

# Events
def on_data_table_row_selected(self, event: DataTable.RowSelected) -> None:
    row = event.row
    # Handle row selection
```

**Cell Types:**
- `CellType`: Default text cell
- `Numeric`: Numeric display with alignment
- `Progress`: Progress bar in cell
- `Checkbox`: Checkbox for boolean values

### Log
Display scrolling logs/messages.

```python
from textual.widgets import Log

log = Log()
log.write("Log entry 1")
log.write("Log entry 2", severity="info")
log.write("Error message", severity="error")
log.write_line("Auto newline")

# Auto-scroll
log.auto_scroll = True

# Clear log
log.clear()
```

**Severity Levels:**
- `info`: Information message
- `warn`: Warning message
- `error`: Error message
- `debug`: Debug message

### Tree
Hierarchical tree view.

```python
from textual.widgets import Tree

tree = Tree("Root")
root = tree.root

# Add children
child1 = root.add("Folder 1")
child1.add_leaf("File 1.txt")
child1.add_leaf("File 2.txt")

child2 = root.add("Folder 2")
grandchild = child2.add("Subfolder")
grandchild.add_leaf("File 3.txt")

# Events
def on_tree_node_selected(self, event: Tree.NodeSelected) -> None:
    node = event.node
    self.log(f"Selected: {node.label}")
```

### Select
Dropdown selection widget.

```python
from textual.widgets import Select

# Basic options
Select([
    ("opt1", "Option 1"),
    ("opt2", "Option 2"),
    ("opt3", "Option 3"),
])

# With initial value
Select([...], value="opt2")

# Allow custom values
Select(..., allow_custom=True)
```

### Switch
Toggle switch widget.

```python
from textual.widgets import Switch

# Basic switch
Switch()

# With initial state
Switch(value=True)

# Events
def on_switch_changed(self, event: Switch.Changed) -> None:
    if event.value:
        self.enable_feature()
    else:
        self.disable_feature()
```

### Checkbox
Checkbox widget.

```python
from textual.widgets import Checkbox

# Basic checkbox
Checkbox("Enable feature")

# Initial state
Checkbox("Enable feature", value=True)

# Events
def on_checkbox_changed(self, event: Checkbox.Changed) -> None:
    if event.value:
        self.enable_feature()
    else:
        self.disable_feature()
```

### RadioSet
Radio button group.

```python
from textual.widgets import RadioSet, RadioButton

with RadioSet():
    yield RadioButton("Option 1", value=True)
    yield RadioButton("Option 2")
    yield RadioButton("Option 3")

# Handle selection
def on_radio_set_changed(self, event: RadioSet.Changed) -> None:
    self.log(f"Selected: {event.pressed.label}")
```

## Progress and Status

### ProgressBar
Display progress indication.

```python
from textual.widgets import ProgressBar

# Basic progress bar
progress = ProgressBar()
progress.update(0.5)  # 50% complete

# With total
progress = ProgressBar(total=100)
progress.update(42)

# Events
def on_progress_bar_updated(self, event: ProgressBar.Updated) -> None:
    self.log(f"Progress: {event.progress}/{event.total}")
```

### Spinner
Animated loading spinner.

```python
from textual.widgets import Spinner

spinner = Spinner()

# Different types
Spinner(spinner="dots")
Spinner(spinner="dots")
Spinner(spinner="line")
Spinner(spinner="grow")
Spinner(spinner="pulse")

# Start/stop
spinner.start()
spinner.stop()
```

### LoadingIndicator
Simple loading animation.

```python
from textual.widgets import LoadingIndicator

# Basic loading
LoadingIndicator()

# With label
LoadingIndicator("Loading data...")
```

## Media and Rich Content

### Markdown
Render Markdown text.

```python
from textual.widgets import Markdown

markdown = Markdown("""
# Heading

Text with **bold** and *italic*.

- List item 1
- List item 2
""")
```

### Code
Display code with syntax highlighting.

```python
from textual.widgets import Code

code = Code('print("Hello, World!")', language="python")

# Read-only code view
code = Code(read_only=True)
```

### FileTree
Browse filesystem directory tree.

```python
from textual.widgets import FileTree

# Current directory
tree = FileTree()

# Specific directory
tree = FileTree(path="/path/to/directory")

# Events
def on_file_tree_file_selected(self, event: FileTree.FileSelected) -> None:
    path = event.path
    # Handle file selection
```

## Widget Styling

### CSS Classes

```python
# Apply classes
Button("OK", classes="primary button")

# Remove classes
button.remove_class("disabled")
button.add_class("highlighted")
```

### Common Classes

```python
# Layout
"container"    # Basic container
"panel"        # Panel with border
"scrollable"   # Scrollable content

# Sizing
"expand"       # Expand to fill space
"fit"          # Fit to content
"large"        # Large widgets
"small"        # Small widgets

# Alignment
"center"       # Center align
"left"         # Left align
"right"        # Right align

# Typography
"title"        # Large title
"subtitle"     # Subtitle
"monospace"    # Monospace font
"bold"         # Bold text
"italic"       # Italic text
```

### Variants

```python
# Button variants
"primary"      # Primary action
"success"      # Success action
"warning"      # Warning action
"error"        # Error action
"default"      # Default button
```

## Widget Patterns

### Modal Dialog Pattern

```python
from textual.widgets import ModalScreen

class ConfirmDialog(ModalScreen):
    """Confirmation dialog."""

    def compose(self):
        with Container(classes="dialog"):
            yield Static("Are you sure?")
            with Horizontal():
                yield Button("Yes", variant="primary", id="yes")
                yield Button("No", variant="default", id="no")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "yes":
            self.app.pop_screen_with_result(True)
        else:
            self.app.pop_screen_with_result(False)

# Show dialog
def confirm_action(self):
    self.app.push_screen(ConfirmDialog(), self.on_confirm_result)

def on_confirm_result(self, result: bool):
    if result:
        self.execute_action()
```

### Notification Pattern

```python
from textual.widgets import Toast

class NotificationScreen(ModalScreen):
    def compose(self):
        with Container(classes="notification"):
            yield Static("Action completed successfully!", id="message")

    def on_mount(self):
        self.set_timer(2.0, self.dismiss)
```

### Widget Composition Pattern

```python
from textual.widget import Widget

class Card(Widget):
    """Card container widget."""

    def compose(self):
        with Container(classes="card"):
            with Vertical():
                yield Static("Card Title", classes="card-title")
                yield Static("Card content", classes="card-content")

# Usage
with Horizontal():
    yield Card(id="card1")
    yield Card(id="card2")
    yield Card(id="card3")
```

## Event Handling

### Common Events

```python
# Focus events
def on_focus(self, event) -> None:
    """Widget gained focus."""

def on_blur(self, event) -> None:
    """Widget lost focus."""

# Mouse events
def on_click(self, event) -> None:
    """Widget clicked."""

def on_mouse_move(self, event) -> None:
    """Mouse moved over widget."""

# Keyboard events
def on_key(self, event) -> None:
    """Key pressed."""

def on_key_variant(self, event) -> None:
    """Special key pressed."""
```

### Event Filtering

```python
# Only handle specific keys
def on_key(self, event) -> None:
    if event.key == "enter":
        self.submit()
    elif event.key == "escape":
        self.cancel()

# Event propagation
def on_button_pressed(self, event: Button.Pressed) -> None:
    # Handle button
    event.stop()  # Stop propagation
```

## Best Practices

1. **Use appropriate widgets** for the content type
2. **Combine simple widgets** instead of complex custom widgets when possible
3. **Handle events properly** and clean up resources
4. **Use CSS classes** for consistent styling
5. **Implement accessibility** with proper labels and navigation
6. **Test widgets** independently and in combination
7. **Optimize rendering** by minimizing DOM updates
8. **Use reactive properties** for dynamic content

## See Also

- [Textual Layouts Guide](../helpers/textual-layouts-guide.md)
- [Textual CSS Styling](../helpers/textual-css-styling.md)
- [Textual Events Handling](../helpers/textual-events-handling.md)
