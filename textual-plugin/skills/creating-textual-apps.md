# creating-textual-apps

Generate complete, production-ready Textual applications with modern TUI patterns, widgets, layouts, styling, and best practices.

## Overview

This skill provides comprehensive scaffolding for Textual terminal applications. It creates well-structured, maintainable TUI apps following Textual conventions and modern Python development practices.

## What I Create

### 1. Complete Application Structure

**Core Application:**
- Main App class with proper lifecycle management
- Message handling and event system
- Reactive data binding
- Configuration management

**Widget System:**
- Custom widgets with proper inheritance
- Composite widget patterns
- Reusable component libraries
- Widget composition techniques

**Layout Management:**
- Responsive layouts (Vertical, Horizontal, Grid, Dock, etc.)
- Dynamic layout switching
- Adaptive UI based on terminal size
- Multi-pane interfaces

**Styling System:**
- Textual CSS integration
- Theme management
- Custom styling classes
- Color schemes and typography

### 2. Advanced Features

**Data Handling:**
- MVVM patterns
- Reactive data models
- Data binding and updates
- Async data loading

**User Interaction:**
- Keyboard navigation
- Mouse event handling
- Command palette
- Modal dialogs

**Developer Experience:**
- Type hints throughout
- Error handling and recovery
- Debug mode integration
- Logging configuration

**Testing Infrastructure:**
- Unit tests for widgets
- Integration test helpers
- Snapshot testing utilities
- UI testing patterns

## Common Patterns I Implement

### Basic TUI Application

```python
from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal
from textual.widgets import Header, Footer, Button, Input
from textual.reactive import reactive

class MyApp(App):
    """A simple Textual application."""

    # Reactive data
    count = reactive(0)

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        with Vertical():
            yield Button("Increment", id="increment")
            yield Button("Decrement", id="decrement")
            yield Input(placeholder="Enter text...")
        yield Footer()

    def watch_count(self, value: int) -> None:
        """Called when count changes."""
        self.title = f"My App - Count: {value}"

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        if event.button.id == "increment":
            self.count += 1
        elif event.button.id == "decrement":
            self.count -= 1

if __name__ == "__main__":
    app = MyApp()
    app.run()
```

### Advanced Dashboard Layout

```python
from textual.app import App
from textual.containers import Container, Horizontal, Vertical, DockPane
from textual.widgets import DataTable, Log, Static, Tabs
from textual.reactive import reactive

class DashboardApp(App):
    """A dashboard-style application."""

    # Reactive data
    status = reactive("Connected")

    def compose(self) -> ComposeResult:
        """Create dashboard layout."""
        with Horizontal():
            # Left sidebar
            with Vertical(id="sidebar"):
                yield Static("Navigation", classes="title")
                # Navigation items
            # Main content
            with Vertical(id="main"):
                yield Tabs("Overview", "Details", "Logs")
                with Container(id="tab-content"):
                    yield DataTable()
        # Right panel
        yield DockPane("Properties", edge="right")

    def on_mount(self) -> None:
        """Initialize the dashboard."""
        table = self.query_one(DataTable)
        table.add_columns("Name", "Status", "Value")
        table.add_rows([("Item 1", "Active", "42")])
```

### Custom Widget Pattern

```python
from textual.widget import Widget
from textual.reactive import reactive
from textual.message import Message

class StatusDisplay(Widget):
    """A custom status display widget."""

    # Message emitted when status changes
    class StatusChanged(Message):
        def __init__(self, status: str):
            self.status = status
            super().__init__()

    # Reactive property
    status = reactive("Ready")

    def watch_status(self, status: str) -> None:
        """Update display when status changes."""
        self.update(status)

    def render(self):
        """Render the widget."""
        return self.status

    def set_status(self, status: str) -> None:
        """Update status and emit message."""
        self.status = status
        self.post_message(self.StatusChanged(status))
```

## Project Structure I Create

```
my_textual_app/
├── main.py                 # Application entry point
├── app.py                  # Main App class
├── screens/                # Screen definitions
│   ├── __init__.py
│   ├── main_screen.py
│   └── settings_screen.py
├── widgets/                # Custom widgets
│   ├── __init__.py
│   ├── navigation.py
│   └── status_bar.py
├── models/                 # Data models
│   ├── __init__.py
│   └── data_model.py
├── services/               # Business logic
│   ├── __init__.py
│   └── api_service.py
├── styles/                 # Styling
│   ├── main.tcss
│   └── themes/
│       └── dark.tcss
├── utils/                  # Utilities
│   ├── __init__.py
│   └── helpers.py
├── tests/                  # Tests
│   ├── test_app.py
│   ├── test_widgets.py
│   └── test_models.py
├── config/
│   ├── settings.yaml
│   └── config.py
├── requirements.txt
├── pyproject.toml
└── README.md
```

## Development Workflow I Follow

### 1. Project Setup
- Create virtual environment
- Install Textual and dependencies
- Initialize project structure
- Set up development tools (black, mypy, pytest)

### 2. Widget Development
- Design widget hierarchy
- Implement reactive properties
- Create message system
- Add styling classes
- Write tests

### 3. Layout Design
- Define responsive layouts
- Implement adaptive behavior
- Handle terminal resize
- Optimize for different screen sizes

### 4. Styling System
- Create CSS files
- Define themes
- Use design tokens
- Implement dark/light mode
- Ensure accessibility

### 5. Testing Strategy
- Unit tests for logic
- Widget rendering tests
- Integration tests
- User interaction tests
- Performance benchmarks

### 6. Documentation
- API documentation
- Usage examples
- Widget catalog
- Styling guide
- Best practices

## Best Practices I Follow

### Code Organization
- Clear separation of concerns
- Modular widget design
- Reusable component patterns
- Consistent naming conventions

### Performance
- Efficient rendering
- Minimal DOM updates
- Async operations where appropriate
- Memory management

### User Experience
- Intuitive navigation
- Clear feedback
- Accessible design
- Responsive layouts

### Maintainability
- Type hints everywhere
- Comprehensive tests
- Documentation
- Error handling

## Commands I Provide

When you use this skill, I can create:
- **Complete applications** with all files and structure
- **Specific widgets** with custom functionality
- **Layout configurations** for complex UIs
- **Styling systems** with themes and CSS
- **Testing suites** with various test types
- **Documentation** and examples
- **Development tools** and utilities

## Examples

Tell me:
- "Create a TODO app with a task list and filters"
- "Build a file browser with navigation and preview"
- "Make a system monitor with real-time charts"
- "Design a settings panel with multiple categories"
- "Create a multi-panel text editor"
- "Build a dashboard with data tables and graphs"

I'll generate a complete, production-ready Textual application with all the necessary files, proper structure, and best practices implemented.
