# textual-new-widget

Create a new custom Textual widget with proper structure, styling, events, and documentation following best practices.

## Overview

This command scaffolds a custom widget with all necessary files, proper class structure, CSS styling, event handling, and comprehensive documentation.

## Usage

```
/textual-new-widget <widget-name> [options]
```

## Parameters

- **widget-name**: Name for the new widget (required, PascalCase)
- **--type <type>**: Widget type (basic, container, input, display, custom)
- **--with-styles**: Include CSS styling file
- **--with-tests**: Include test file
- **--with-docs**: Include documentation
- **--parent <class>**: Parent widget class (Widget, Container, Input, etc.)
- **--export**: Export as reusable package
- **--template <template>**: Template to use (blank, form-field, data-display, control)

## Examples

### Create Basic Widget

```
/textual-new-widget StatusDisplay --type basic
```

Creates a simple display widget with:
- Basic widget class
- Minimal styling
- Example usage
- Unit tests

### Create Container Widget

```
/textual-new-widget CardPanel --type container --with-styles --with-tests
```

Creates a container widget with:
- Container functionality
- Custom CSS styling
- Layout management
- Responsive design
- Test coverage

### Create Input Widget

```
/textual-new-widget SearchBox --type input --with-docs
```

Creates an input widget with:
- Input handling
- Validation
- Events (on_change, on_submit)
- Auto-completion support
- Accessibility features

### Create Complex Custom Widget

```
/textual-new-widget DataGrid --type custom --parent Container --with-styles --with-tests --with-docs
```

Creates a complex widget with:
- Custom parent class
- Advanced functionality
- Comprehensive styling
- Full test suite
- Documentation

## Widget Types

### Basic Widget

```python
from textual.widget import Widget
from textual.reactive import reactive
from textual.message import Message

class StatusDisplay(Widget):
    """A simple status display widget."""

    # Reactive properties
    status = reactive("Ready")

    # Messages emitted by this widget
    class StatusChanged(Message):
        def __init__(self, status: str):
            self.status = status
            super().__init__()

    def compose(self):
        yield None  # Basic widgets don't compose children

    def watch_status(self, status: str) -> None:
        """Called when status changes."""
        self.update(status)

    def render(self):
        """Render the widget."""
        return self.status

    def set_status(self, status: str) -> None:
        """Set status and emit message."""
        self.status = status
        self.post_message(self.StatusChanged(status))
```

### Container Widget

```python
from textual.containers import Container
from textual.widgets import Static

class CardPanel(Container):
    """A card container widget."""

    DEFAULT_CSS = """
    CardPanel {
        background: $panel;
        border: solid $accent;
        border-radius: 2;
        padding: 1;
        margin: 1;
    }

    CardPanel > .title {
        background: $primary;
        color: white;
        text-align: center;
        padding: 1;
        margin: -1 -1 1 -1;
        text-style: bold;
    }

    CardPanel > .content {
        padding: 1;
    }

    CardPanel:hover {
        border: solid $primary;
    }
    """

    def __init__(self, title: str = "", content: str = ""):
        super().__init__()
        self.title = title
        self.content = content

    def compose(self):
        yield Static(self.title, classes="title")
        yield Static(self.content, classes="content")

    def set_title(self, title: str) -> None:
        """Update card title."""
        self.title = title
        self.query_one(".title", Static).update(title)

    def set_content(self, content: str) -> None:
        """Update card content."""
        self.content = content
        self.query_one(".content", Static).update(content)
```

### Input Widget

```python
from textual.widgets import Input
from textual.widgets import Button

class SearchBox(Container):
    """A search input with submit button."""

    DEFAULT_CSS = """
    SearchBox {
        layout: horizontal;
        height: 3;
    }

    SearchBox Input {
        width: 1fr;
        margin: 0 1;
    }

    SearchBox Button {
        margin: 0 1;
    }
    """

    # Message when search is submitted
    class SearchSubmitted(Message):
        def __init__(self, query: str):
            self.query = query
            super().__init__()

    def __init__(self, placeholder: str = "Search..."):
        super().__init__()
        self.placeholder = placeholder
        self.query = ""

    def compose(self):
        self.input = Input(placeholder=self.placeholder, id="search-input")
        self.button = Button("Search", variant="primary", id="search-btn")
        yield self.input
        yield self.button

    def on_input_submitted(self, event: Input.Submitted) -> None:
        """Handle Enter key in input."""
        self.submit_search()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle search button press."""
        if event.button.id == "search-btn":
            self.submit_search()

    def submit_search(self):
        """Submit search query."""
        self.query = self.input.value
        self.post_message(self.SearchSubmitted(self.query))

    def clear(self):
        """Clear search input."""
        self.input.value = ""
        self.query = ""
```

### Custom Widget Template

```python
from textual.widget import Widget
from textual.containers import Container
from textual.widgets import Static, Button
from textual.reactive import reactive
from textual.message import Message
from typing import Optional, Callable

class DataGrid(Container):
    """A data grid widget for displaying tabular data."""

    DEFAULT_CSS = """
    DataGrid {
        background: $panel;
        border: solid $accent;
        overflow: auto;
    }

    DataGrid > .header {
        background: $primary;
        color: white;
        text-style: bold;
    }

    DataGrid > .row {
        border-bottom: solid $surface;
    }

    DataGrid > .row:hover {
        background: $surface;
    }

    DataGrid > .cell {
        padding: 0 1;
        width: 1fr;
    }
    """

    # Messages
    class CellSelected(Message):
        def __init__(self, row: int, col: int, value: str):
            self.row = row
            self.col = col
            self.value = value
            super().__init__()

    class RowSelected(Message):
        def __init__(self, row: int, data: list):
            self.row = row
            self.data = data
            super().__init__()

    # Reactive properties
    data = reactive([], always_update=True)
    columns = reactive([], always_update=True)
    selected_cell = reactive(None)

    def __init__(self, columns: list = None, data: list = None):
        super().__init__()
        self.columns = columns or []
        self.data = data or []

    def compose(self):
        # Header
        with Container(classes="header"):
            for col in self.columns:
                yield Static(col, classes="cell")

        # Data rows
        for row_idx, row_data in enumerate(self.data):
            with Container(classes="row", id=f"row-{row_idx}"):
                for col_idx, cell_data in enumerate(row_data):
                    yield Static(
                        str(cell_data),
                        classes="cell",
                        id=f"cell-{row_idx}-{col_idx}"
                    )

    def watch_data(self, data: list) -> None:
        """Called when data changes."""
        self.refresh()

    def watch_columns(self, columns: list) -> None:
        """Called when columns change."""
        self.refresh()

    def on_click(self, event) -> None:
        """Handle cell clicks."""
        # Find clicked cell
        cell = event.widget
        if cell.id and cell.id.startswith("cell-"):
            parts = cell.id.split("-")
            row = int(parts[1])
            col = int(parts[2])
            value = str(cell.renderable)

            # Emit messages
            self.post_message(self.CellSelected(row, col, value))
            self.post_message(self.RowSelected(row, self.data[row]))

    def add_row(self, row_data: list):
        """Add a new row."""
        new_data = self.data.copy()
        new_data.append(row_data)
        self.data = new_data

    def remove_row(self, row_idx: int):
        """Remove a row."""
        new_data = [row for i, row in enumerate(self.data) if i != row_idx]
        self.data = new_data

    def clear(self):
        """Clear all data."""
        self.data = []
```

## File Structure Generated

### Basic Widget Structure

```
widgets/
├── __init__.py
├── status_display.py         # Widget implementation
├── status_display.tcss       # Styling (if --with-styles)
├── status_display_test.py    # Tests (if --with-tests)
└── README.md                 # Documentation (if --with-docs)
```

### Complete Widget Package

```
widgets/
├── __init__.py
├── status_display/
│   ├── __init__.py
│   ├── status_display.py
│   ├── styles/
│   │   ├── __init__.py
│   │   └── status_display.tcss
│   ├── py.typed
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_status_display.py
│   │   └── test_widget.py
│   ├── examples/
│   │   ├── basic_usage.py
│   │   └── advanced_usage.py
│   └── docs/
│       ├── index.md
│       ├── api.md
│       └── examples.md
└── pyproject.toml           # For export
```

## Widget Components

### 1. Widget Class

```python
from textual.widget import Widget
from textual.reactive import reactive
from textual.message import Message

class WidgetName(Widget):
    """Brief description of the widget.

    Extended description with usage examples,
    features, and behavior.
    """

    # Reactive properties
    property1 = reactive(default_value)
    property2 = reactive(default_value, always_update=True)

    # Messages
    class EventName(Message):
        """Description of the event."""

        def __init__(self, data):
            self.data = data
            super().__init__()

    def __init__(self, param1: str, param2: int = 0):
        super().__init__()
        self.param1 = param1
        self.param2 = param2

    def compose(self):
        """Create child widgets if any."""
        yield None

    def on_mount(self) -> None:
        """Called when widget is mounted."""
        pass

    def watch_property1(self, value):
        """Called when reactive property changes."""
        pass

    def render(self):
        """Return renderable content."""
        return "Content"

    # Public methods
    def update_property1(self, value):
        """Update property with validation."""
        self.property1 = value

    def clear(self):
        """Reset widget to initial state."""
        self.property1 = default_value
```

### 2. CSS Styling

```css
/* Widget name styling */
WidgetName {
    /* Layout */
    width: auto;
    height: auto;

    /* Spacing */
    padding: 1;
    margin: 0;

    /* Colors */
    background: $panel;
    color: $text;

    /* Border */
    border: solid $accent;

    /* Typography */
    text-align: center;
}

WidgetName:hover {
    background: $primary;
    color: white;
}

WidgetName:disabled {
    background: $surface;
    color: $text-disabled;
}

/* Child elements */
WidgetName > .child-element {
    background: $surface;
    padding: 1;
}

/* States */
WidgetName.-active {
    border: solid $success;
}

WidgetName.-error {
    border: solid $error;
}
```

### 3. Tests

```python
import pytest
from textual.app import App
from textual.testing import AppTest
from widgets.widget_name import WidgetName

class TestWidgetName:
    """Test cases for WidgetName."""

    def test_widget_creation(self):
        """Test widget creation."""
        widget = WidgetName()
        assert widget is not None

    def test_widget_with_params(self):
        """Test widget with parameters."""
        widget = WidgetName(param1="test", param2=42)
        assert widget.param1 == "test"
        assert widget.param2 == 42

    def test_reactive_property(self):
        """Test reactive property updates."""
        widget = WidgetName()
        updates = []

        widget.property1.subscribe(lambda v: updates.append(v))

        widget.property1 = "new_value"

        assert "new_value" in updates

    async def test_widget_render(self):
        """Test widget rendering."""
        app = App()
        widget = WidgetName()

        async with app.run_test() as pilot:
            app.query_one("Screen").mount(widget)
            await pilot.pause()

            # Verify rendering
            assert widget.is_mounted

    async def test_events(self):
        """Test widget events."""
        app = App()
        widget = WidgetName()
        event_received = []

        def on_event(event):
            event_received.append(event)

        widget.EventName.subscribe(on_event)

        async with app.run_test() as pilot:
            app.query_one("Screen").mount(widget)
            await pilot.pause()

            # Trigger event
            widget.post_message(widget.EventName("test"))

            # Verify event received
            assert len(event_received) == 1
            assert event_received[0].data == "test"

    async def test_interaction(self):
        """Test user interactions."""
        class TestApp(App):
            def compose(self):
                yield WidgetName(id="test-widget")

        app = TestApp()
        async with app.run_test() as pilot:
            await pilot.click("#test-widget")
            # Verify interaction handled
```

### 4. Documentation

```markdown
# WidgetName

Brief description of the widget.

## Features

- Feature 1
- Feature 2
- Feature 3

## Usage

### Basic Usage

```python
from widgets import WidgetName

class MyApp(App):
    def compose(self):
        yield WidgetName(
            param1="value1",
            param2=42
        )
```

### Advanced Usage

```python
class MyApp(App):
    def compose(self):
        yield WidgetName(id="custom-widget")

    def on_mount(self) -> None:
        widget = self.query_one("#custom-widget", WidgetName)

        # Update properties
        widget.property1 = "new_value"

        # Handle events
        widget.EventName.subscribe(self.on_widget_event)

    def on_widget_event(self, event: WidgetName.EventName) -> None:
        print(f"Event received: {event.data}")
```

## API Reference

### Class: WidgetName

#### Parameters

- `param1` (str): Description of param1
- `param2` (int, optional): Description of param2 (default: 0)

#### Properties

- `property1` (str): Description of property1
- `property2` (int): Description of property2

#### Events

- `EventName`: Emitted when event occurs
  - `data` (str): Event data

#### Methods

##### set_property1(value: str)

Set property1 with validation.

##### clear()

Reset widget to initial state.

## Styling

### CSS Classes

- `.active`: Active state
- `.disabled`: Disabled state
- `.error`: Error state

### CSS Variables

```css
WidgetName {
    --widget-primary: $primary;
    --widget-background: $panel;
}
```

## Examples

### Example 1: Basic Display

[Complete example code]

### Example 2: Interactive Widget

[Complete example code]

### Example 3: Custom Styling

[Complete example code]

## Best Practices

1. Use reactive properties for state
2. Emit messages for events
3. Clean up resources on unmount
4. Test all functionality
5. Document all parameters
6. Follow naming conventions
```

## Widget Templates

### Blank Template

```python
from textual.widget import Widget

class WidgetName(Widget):
    """Template for basic widget."""

    def compose(self):
        yield None

    def render(self):
        return "Widget"
```

### Form Field Template

```python
from textual.widgets import Label, Input
from textual.containers import Container, Horizontal

class FormField(Container):
    """Template for form field."""

    DEFAULT_CSS = """
    FormField {
        height: 3;
    }

    FormField Label {
        width: 20;
        text-align: right;
        margin: 0 1;
    }

    FormField Input {
        width: 1fr;
    }
    """

    def __init__(self, label: str, input_type: str = "text"):
        super().__init__()
        self.label_text = label
        self.input_type = input_type

    def compose(self):
        with Horizontal():
            yield Label(self.label_text)
            yield Input(type=self.input_type)
```

### Data Display Template

```python
from textual.widgets import Static
from textual.containers import Container

class DataDisplay(Container):
    """Template for data display widget."""

    DEFAULT_CSS = """
    DataDisplay {
        background: $panel;
        padding: 1;
        border: solid $accent;
    }

    DataDisplay .title {
        text-style: bold;
        margin-bottom: 1;
    }

    DataDisplay .value {
        font-size: 2;
    }
    """

    def __init__(self, title: str = "", value: str = ""):
        super().__init__()
        self.title_text = title
        self.value_text = value

    def compose(self):
        yield Static(self.title_text, classes="title")
        yield Static(self.value_text, classes="value")
```

### Control Template

```python
from textual.widgets import Button, Static
from textual.containers import Horizontal

class Control(Container):
    """Template for control widget."""

    DEFAULT_CSS = """
    Control {
        layout: horizontal;
        height: 3;
    }

    Control Label {
        width: 1fr;
        text-align: left;
    }

    Control Button {
        margin: 0 1;
    }
    """

    def __init__(self, label: str, on_click: callable = None):
        super().__init__()
        self.label_text = label
        self.on_click = on_click

    def compose(self):
        yield Static(self.label_text)
        yield Button("Click", id="control-btn")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if self.on_click:
            self.on_click()
```

## Widget Development Best Practices

### 1. Naming Conventions

```python
# Widget class: PascalCase
class StatusDisplay(Widget):

# CSS class: lowercase with hyphens
WidgetName {
    background: red;
}

# Reactive properties: lowercase with underscores
class Widget:
    status_text = reactive("")

# Methods: snake_case
def set_status_text(self, text: str):
    self.status_text = text
```

### 2. Property Management

```python
# Use reactive properties for state
class Widget:
    count = reactive(0)
    items = reactive([], always_update=True)

    # Provide validation in setter
    @reactive
    def value(self):
        return self._value

    @value.setter
    def value(self, val):
        # Validate
        if val < 0:
            val = 0
        self._value = val
```

### 3. Event Handling

```python
# Emit messages for events
class Widget:
    class Updated(Message):
        def __init__(self, data):
            self.data = data
            super().__init__()

    def update(self, data):
        self.data = data
        # Emit message
        self.post_message(self.Updated(data))

# Handle events in parent
class ParentApp(App):
    def on_widget_updated(self, event: Widget.Updated) -> None:
        print(f"Widget updated: {event.data}")
```

### 4. CSS Styling

```python
# Use CSS variables for theming
class Widget:
    DEFAULT_CSS = """
    Widget {
        --widget-primary: $primary;
        --widget-bg: $panel;
        background: var(--widget-bg);
    }

    Widget:hover {
        background: var(--widget-primary);
    }
    """

# Support state classes
def set_state(self, state: str):
    self.set_class(state in ["active", "error", "disabled"], state)
```

### 5. Resource Management

```python
class Widget:
    def on_mount(self) -> None:
        # Start timers, load data, etc.
        self.timer = self.set_interval(1.0, self.update)

    def on_unmount(self) -> None:
        # Clean up resources
        if self.timer:
            self.timer.stop()
```

### 6. Testing

```python
async def test_widget_interaction():
    """Test widget functionality."""
    app = TestApp()
    async with app.run_test() as pilot:
        # Mount widget
        app.query_one("Screen").mount(Widget())

        # Interact with widget
        await pilot.click("#widget")

        # Verify state
        widget = app.query_one(Widget)
        assert widget.state == "expected"
```

## Exporting Widgets

### As Reusable Package

```
/textual-new-widget MyWidget --export
```

Creates:
```
my-widget/
├── pyproject.toml
├── src/
│   └── my_widget/
│       ├── __init__.py
│       ├── widget.py
│       └── styles/
│           └── widget.tcss
├── tests/
├── docs/
└── README.md
```

### Publishing to PyPI

```bash
cd my-widget
pip install build twine
python -m build
python -m twine upload dist/*
```

### Usage After Export

```python
from my_widget.widget import MyWidget

class MyApp(App):
    def compose(self):
        yield MyWidget()
```

## Troubleshooting

### Common Issues

**Issue: Widget not rendering**
```python
# Check render() method returns content
def render(self):
    return "Content"  # Not None

# Or compose() has children
def compose(self):
    yield Static("Content")
```

**Issue: Events not firing**
```python
# Check message class is properly defined
class MyEvent(Message):
    pass  # Must inherit from Message

# Check post_message is called
self.post_message(MyEvent())
```

**Issue: Styling not applied**
```python
# Check CSS_PATH is set
class MyApp(App):
    CSS_PATH = "styles/widget.tcss"

# Or use DEFAULT_CSS in widget
class MyWidget(Widget):
    DEFAULT_CSS = """
    MyWidget {
        background: red;
    }
    """
```

**Issue: Widget not responding to clicks**
```python
# Override on_click or on_button_pressed
def on_click(self, event) -> None:
    print("Clicked!")

# Or emit messages instead
```

## See Also

- [Textual Widgets Reference](../helpers/textual-widgets-reference.md)
- [Textual Events Handling](../helpers/textual-events-handling.md)
- [Textual CSS Styling](../helpers/textual-css-styling.md)
- [Textual Testing Utilities](../helpers/textual-testing-utilities.md)
