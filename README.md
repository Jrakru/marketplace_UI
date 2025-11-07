# Textual Marketplace - Skills & Helpers for AI Agents

A comprehensive collection of skills, examples, and helper tools to help AI agents build Python TUI (Text User Interface) applications using Textual.

## 📚 Overview

This marketplace provides:
- **37+ Skills** covering all aspects of Textual development
- **Helper Scripts** for code generation and assistance
- **Templates** for common patterns
- **Testing Examples** with pytest and snapshot testing
- **Quick Reference** guides for fast lookups

## 🗂️ Repository Structure

```
marketplace_textual/
├── skills/              # Organized by category
│   ├── core/            # Getting started, app lifecycle
│   ├── widgets/         # Built-in and custom widgets
│   ├── layout/          # Layouts and CSS styling
│   ├── interactivity/   # Events, messages, actions
│   ├── reactivity/      # Reactive attributes
│   ├── navigation/      # Screens and navigation
│   ├── testing/         # Testing patterns
│   ├── dom/             # DOM queries and manipulation
│   ├── input/           # Input handling and validation
│   ├── advanced/        # Workers, animation, timers
│   ├── development/     # Debugging and devtools
│   ├── accessibility/   # Accessibility features
│   └── integration/     # Integrations (Rich, CLI)
│
├── helpers/             # AI agent helper scripts
│   ├── textual_generator.py    # Generate apps/widgets
│   ├── template_manager.py     # Code templates
│   ├── skill_finder.py         # Find relevant skills
│   └── quick_reference.py      # Quick lookup guide
│
├── examples/            # Complete example apps
├── templates/           # Project templates
└── README.md
```

## 🎯 Skills Catalog

### Core Foundation (Essential)
1. **Getting Started** - Basic app structure, project setup, hot reload
2. **App Lifecycle** - Initialization, mount/unmount, shutdown

### Widgets
3. **Built-in Widgets** - Button, Input, DataTable, Tree, ListView, etc.
4. **Custom Widgets** - Create reusable, encapsulated components

### Layout & Design
5. **Layout Systems** - Vertical, Horizontal, Grid, Dock
6. **CSS Styling (TCSS)** - Selectors, colors, borders, text styling
7. **Themes & Design** - Color systems, design tokens, theming

### Interactivity
8. **Events & Messages** - Event handling, @on decorator, message passing
9. **Actions & Bindings** - Key bindings, action methods
10. **Message Bubbling** - Custom messages, parent-child communication

### Reactivity & State
11. **Reactive Attributes** - Auto-updating state, watch methods
12. **Computed Values** - Derived reactive attributes
13. **Reactive Validation** - Input validation with reactivity

### Navigation
14. **Screens** - Multi-screen apps, screen lifecycle
15. **Modal Dialogs** - ModalScreen, returning values
16. **Navigation Patterns** - Push/pop, screen stacks

### Testing
17. **Snapshot Testing** - Visual regression testing with pytest
18. **Unit Testing** - Testing widgets and components
19. **Integration Testing** - User interaction testing

### Advanced Features
20. **Workers** - Background async tasks
21. **Animation** - Transitions and effects
22. **Timers** - Scheduled callbacks, intervals
23. **Command Palette** - Built-in command system

### Development
24. **DevTools** - Debugging, console, inspection
25. **Best Practices** - Patterns and anti-patterns

## 🚀 Quick Start for AI Agents

### 1. Find Relevant Skills

```python
from helpers.skill_finder import SkillFinder

finder = SkillFinder()

# Search for skills
results = finder.find_skills("button events")

# Get recommendations for a task
task = "Create a data entry form with validation"
recommendations = finder.find_by_task(task)

# Get learning path
path = finder.get_learning_path("beginner")
```

### 2. Generate Code

```python
from helpers.textual_generator import TextualGenerator

generator = TextualGenerator()

# Generate complete app
from helpers.textual_generator import WidgetSpec

widgets = [
    WidgetSpec("Button", id="submit", properties={"label": "Submit"}),
    WidgetSpec("Input", id="name", properties={"placeholder": "Name"}),
]

app_code = generator.generate_app(
    "MyFormApp",
    widgets=widgets,
    css="Button { margin: 1; }",
    bindings=[("q", "quit", "Quit")]
)

print(app_code)
```

### 3. Use Templates

```python
from helpers.template_manager import TemplateManager, TemplateType

manager = TemplateManager()

# Get app template
app_code = manager.get_template(
    TemplateType.APP,
    "basic",
    app_name="MyApp"
)

# Get custom widget template
widget_code = manager.get_template(
    TemplateType.WIDGET,
    "reactive",
    widget_name="Counter",
    reactive_attr="count",
    default_value=0
)
```

### 4. Quick Reference

```python
from helpers.quick_reference import QUICK_REFERENCE, get_pattern

# Display full reference
print(QUICK_REFERENCE)

# Get specific pattern
counter_pattern = get_pattern("counter")
form_pattern = get_pattern("form")
modal_pattern = get_pattern("modal")
```

## 📖 Skill Categories

### Core Skills
- **01_getting_started.py** - Project setup, basic app structure, async
- **02_app_lifecycle.py** - Lifecycle events, configuration, CLI args

### Widget Skills
- **01_builtin_widgets.py** - All built-in widgets with examples
- **02_custom_widgets.py** - Create custom, reusable components

### Layout Skills
- **01_layouts.py** - Vertical, Horizontal, Grid, Dock, Scrollable
- **02_css_styling.py** - TCSS syntax, selectors, colors, themes

### Interactivity Skills
- **01_events_messages.py** - Events, @on decorator, custom messages
- **02_actions.py** - Key bindings, action methods

### Reactivity Skills
- **01_reactive_attributes.py** - Reactive state, watch/compute methods

### Navigation Skills
- **01_screens.py** - Multi-screen apps, modals, navigation

### Testing Skills
- **01_snapshot_testing.py** - Visual regression testing
- **02_unit_testing.py** - Component testing
- **03_integration_testing.py** - End-to-end testing

## 🛠️ Helper Scripts

### textual_generator.py
Generate complete Textual applications, widgets, screens, and tests.

**Features:**
- Generate full apps from specifications
- Create custom widgets with reactivity
- Generate screens and modals
- Create test files

### template_manager.py
Access pre-built templates for common patterns.

**Template Types:**
- Apps (basic, with_css, multi_screen, with_config)
- Widgets (basic, reactive, with_message, container)
- Screens (basic, with_return)
- Modals (confirm, input)
- Tests (snapshot, unit)
- CSS (basic, card, grid_layout)

### skill_finder.py
Find relevant skills for your task.

**Features:**
- Search skills by keyword
- Get recommendations for tasks
- List all available skills
- Get learning paths

### quick_reference.py
Fast lookup for syntax and patterns.

**Includes:**
- Widget signatures
- Event handler patterns
- CSS snippets
- Common patterns
- Best practices

## 📝 Usage Examples

### Example 1: Create a Simple Counter App

```python
from textual.app import App, ComposeResult
from textual.widgets import Button, Static
from textual.containers import Horizontal
from textual.reactive import reactive


class CounterApp(App):
    """A simple counter application."""

    CSS = """
    Screen {
        align: center middle;
    }

    Horizontal {
        width: auto;
        height: auto;
    }

    Static {
        padding: 0 2;
        margin: 0 1;
    }

    Button {
        margin: 0 1;
    }
    """

    count = reactive(0)

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Button("-", id="dec", variant="error")
            yield Static("0", id="display")
            yield Button("+", id="inc", variant="success")

    def watch_count(self, new_count: int) -> None:
        """Update display when count changes."""
        self.query_one("#display", Static).update(str(new_count))

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button clicks."""
        if event.button.id == "inc":
            self.count += 1
        elif event.button.id == "dec":
            self.count -= 1


if __name__ == "__main__":
    app = CounterApp()
    app.run()
```

### Example 2: Create a Modal Dialog

```python
from textual.app import App, ComposeResult
from textual.screen import ModalScreen
from textual.widgets import Button, Static
from textual.containers import Vertical, Horizontal


class ConfirmDialog(ModalScreen[bool]):
    """Confirmation modal."""

    CSS = """
    ConfirmDialog {
        align: center middle;
    }

    #dialog {
        width: 60;
        height: 11;
        background: $panel;
        border: thick $primary;
        padding: 1;
    }
    """

    def compose(self) -> ComposeResult:
        with Vertical(id="dialog"):
            yield Static("Are you sure?")
            with Horizontal():
                yield Button("Yes", variant="success", id="yes")
                yield Button("No", variant="error", id="no")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press."""
        self.dismiss(event.button.id == "yes")


class MainApp(App):
    """Main application."""

    def compose(self) -> ComposeResult:
        yield Button("Show Dialog")
        yield Static("", id="result")

    async def on_button_pressed(self) -> None:
        """Show modal and get result."""
        result = await self.push_screen_wait(ConfirmDialog())
        self.query_one("#result", Static).update(f"Result: {result}")


if __name__ == "__main__":
    app = MainApp()
    app.run()
```

## 🧪 Testing

All skills include testing examples. Run tests with:

```bash
# Install test dependencies
pip install pytest pytest-asyncio pytest-textual-snapshot

# Run tests
pytest

# Update snapshots
pytest --snapshot-update

# Run specific test
pytest tests/test_app.py -v
```

## 📚 Learning Paths

### Beginner Path
1. Getting Started with Textual
2. Built-in Widget Usage
3. Layout Systems
4. CSS Styling (TCSS)
5. Events and Messages
6. Snapshot Testing

### Intermediate Path
1. Custom Widget Development
2. Reactive Attributes
3. Screens and Navigation
4. DOM Queries
5. Input Validation
6. Unit Testing

### Advanced Path
1. Workers & Async Operations
2. Animation
3. Advanced Testing Strategies
4. Performance Optimization
5. Complex State Management

## 🎨 Design Patterns

### Pattern: Reactive Counter
```python
count = reactive(0)

def watch_count(self, new_count):
    self.query_one("#display").update(str(new_count))
```

### Pattern: Form Submission
```python
def on_button_pressed(self):
    data = {
        "name": self.query_one("#name", Input).value,
        "email": self.query_one("#email", Input).value
    }
    self.process_form(data)
```

### Pattern: State Machine
```python
state = reactive("idle")  # idle, loading, success, error

def watch_state(self, new_state):
    if new_state == "loading":
        self.show_spinner()
    elif new_state == "success":
        self.show_success()
```

## 🔧 Best Practices

1. **Use External CSS** - Enables hot reload during development
2. **ID for Unique, Classes for Groups** - Better query organization
3. **Reactive for State** - Auto-updating UI
4. **Events for Actions** - User interaction handling
5. **Test with Snapshots** - Visual regression testing
6. **Type Hints** - Better code clarity
7. **Docstrings** - Document your widgets and methods
8. **Keep compose() Simple** - One responsibility per widget

## 🐛 Common Issues & Solutions

### Widget Not Updating
**Problem:** Widget doesn't reflect state changes
**Solution:** Use reactive attributes and watch methods

### Layout Broken
**Problem:** Widgets not positioned correctly
**Solution:** Check CSS grid-size, verify container hierarchy

### Events Not Firing
**Problem:** Event handlers not called
**Solution:** Verify widget IDs, check event handler names

### Performance Issues
**Problem:** UI sluggish or unresponsive
**Solution:** Use workers for slow operations, batch DOM updates

## 📖 Resources

- **Official Docs**: https://textual.textualize.io
- **Tutorial**: https://textual.textualize.io/tutorial/
- **Widget Gallery**: https://textual.textualize.io/widget_gallery/
- **GitHub**: https://github.com/Textualize/textual

## 🤝 Contributing

This marketplace is designed for AI agents. To add new skills:

1. Create skill file in appropriate category
2. Follow existing skill format
3. Include working examples
4. Add docstrings and comments
5. Include test cases

## 📄 License

This collection is provided as-is for AI agents to learn and build Textual applications.

## 🙋 Support

For Textual-specific questions:
- Discord: https://discord.gg/Enf6Z3qhVr
- GitHub Issues: https://github.com/Textualize/textual/issues

---

**Happy TUI Building! 🎉**
