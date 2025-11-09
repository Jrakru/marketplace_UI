# UI Development Marketplace - Skills & Helpers for AI Agents

A comprehensive collection of skills, examples, and helper tools to help AI agents build:
- **Python TUI (Text User Interface)** applications using Textual
- **Reactive Python notebooks** using Marimo
- **Well-designed interfaces** following UI/UX best practices

## 🚀 Installation

### Add to Claude Code

To add this marketplace to Claude Code:

```bash
# In Claude Code, run:
/marketplace add https://github.com/Jrakru/marketplace_UI
```

Or manually add to your `.claude/settings.json`:

```json
{
  "marketplaces": [
    "https://github.com/Jrakru/marketplace_UI"
  ]
}
```

Then install individual skills using:
```bash
/skills install textual-getting-started
/skills install marimo-getting-started
/skills install cli-ux-principles
```

Or browse all available skills:
```bash
/skills browse
```

## 📚 Overview

This marketplace provides:
- **16 Skills** covering:
  - Textual TUI development (10 skills)
  - Marimo reactive notebooks (4 skills)
  - UI/UX design principles (2 skills)
- **Helper Scripts** for code generation and assistance
- **Templates** for common patterns
- **Testing Examples** with pytest and snapshot testing
- **Quick Reference** guides for fast lookups
- **Best Practices** for CLI, notebook, and general UI design

## 🗂️ Repository Structure

```
marketplace_UI/
├── .claude-plugin/      # Claude Code marketplace configuration
│   └── marketplace.json     # Plugin registry with 16 skills
│
├── skills/              # Organized by framework/category
│   ├── textual/         # Textual TUI framework skills (10 skills)
│   │   ├── core/            # Getting started, app lifecycle
│   │   ├── widgets/         # Built-in and custom widgets
│   │   ├── layout/          # Layouts and CSS styling
│   │   ├── interactivity/   # Events, messages, actions
│   │   ├── reactivity/      # Reactive attributes
│   │   ├── navigation/      # Screens and navigation
│   │   └── testing/         # Testing patterns
│   ├── marimo/          # Marimo reactive notebooks (4 skills)
│   │   ├── 01_getting_started.py
│   │   ├── 02_widgets_ui.py
│   │   ├── 03_layouts.py
│   │   └── 04_working_with_marimo.py
│   └── design/          # UI/UX design principles (2 skills)
│       ├── 01_cli_ux_principles.py
│       └── 02_general_ui_ux.py
│
├── helpers/             # AI agent helper scripts
│   ├── textual_generator.py    # Generate Textual apps/widgets
│   ├── template_manager.py     # Code templates (Textual)
│   ├── skill_finder.py         # Find relevant skills
│   ├── quick_reference.py      # Quick lookup guide (Textual)
│   └── marimo/                  # Marimo integration helpers
│       ├── marimo_generator.py      # Generate marimo notebooks
│       ├── marimo_cli_helper.py     # CLI wrapper for marimo commands
│       └── README.md                # Marimo helpers documentation
│
├── examples/            # Complete example apps
├── templates/           # Project templates
├── SKILLS_INDEX.md      # Complete skills catalog
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

### Marimo (Reactive Notebooks) ⭐ NEW
26. **Getting Started with Marimo** - Reactive notebooks, cells, basic structure
27. **Marimo Widgets** - Interactive UI components, forms, data tables
28. **Marimo Layouts** - Organizing notebooks with stacks, tabs, grids

### UI/UX Design ⭐ NEW
29. **CLI UX Principles** - Human-first design, progressive discovery, helpful errors
30. **General UI/UX** - Color theory, typography, accessibility, layout principles

## 🚀 Quick Start for AI Agents

### For Textual TUI Development

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

### For Marimo Reactive Notebooks ⭐ NEW

#### 1. Create Your First Notebook

```bash
# Install marimo
pip install marimo

# Create a new notebook
marimo edit my_notebook.py

# Run interactive tutorial
marimo tutorial intro
```

#### 2. Basic Notebook Structure

```python
import marimo

__generated_with = "0.10.11"
app = marimo.App()

@app.cell
def __():
    import marimo as mo
    import pandas as pd
    return mo, pd

@app.cell
def __(mo):
    # Create interactive widget
    slider = mo.ui.slider(0, 100, value=50, label="Value:")
    slider
    return slider,

@app.cell
def __(mo, slider):
    # Use reactive value
    mo.md(f"**Selected value:** {slider.value}")
    return

if __name__ == "__main__":
    app.run()
```

#### 3. Create Interactive Dashboards

```python
@app.cell
def __(mo):
    # Dashboard layout with controls
    controls = mo.hstack([
        mo.ui.dropdown(
            options=["2024", "2023", "2022"],
            value="2024",
            label="Year"
        ),
        mo.ui.checkbox(value=True, label="Show Grid")
    ], gap=2)
    controls
    return

@app.cell
def __(mo, df):
    # Interactive data explorer
    explorer = mo.ui.dataframe(df)
    explorer
    return
```

### For UI/UX Design ⭐ NEW

#### Key Design Principles

**CLI Design:**
- Progressive discovery (guide users step-by-step)
- Helpful error messages with solutions
- Consistent command patterns
- Both human and machine-readable output

**General UI/UX:**
- Clarity and simplicity first
- Maintain 4.5:1 color contrast (WCAG AA)
- Visual hierarchy guides attention
- Provide immediate feedback for actions
- Design for accessibility from the start

**Notebook Design:**
- Use reactive execution (like Marimo) for reproducibility
- Clear code organization (imports first)
- Progressive disclosure of complexity
- Graceful error handling with helpful messages

## 📖 Skill Categories

### Textual Skills

#### Core Skills (skills/textual/core/)
- **01_getting_started.py** - Project setup, basic app structure, async
- **02_app_lifecycle.py** - Lifecycle events, configuration, CLI args

#### Widget Skills (skills/textual/widgets/)
- **01_builtin_widgets.py** - All built-in widgets with examples
- **02_custom_widgets.py** - Create custom, reusable components

#### Layout Skills (skills/textual/layout/)
- **01_layouts.py** - Vertical, Horizontal, Grid, Dock, Scrollable
- **02_css_styling.py** - TCSS syntax, selectors, colors, themes

#### Interactivity Skills (skills/textual/interactivity/)
- **01_events_messages.py** - Events, @on decorator, custom messages
- **02_actions.py** - Key bindings, action methods

#### Reactivity Skills (skills/textual/reactivity/)
- **01_reactive_attributes.py** - Reactive state, watch/compute methods

#### Navigation Skills (skills/textual/navigation/)
- **01_screens.py** - Multi-screen apps, modals, navigation

#### Testing Skills (skills/textual/testing/)
- **01_snapshot_testing.py** - Visual regression testing
- **02_unit_testing.py** - Component testing
- **03_integration_testing.py** - End-to-end testing

### Marimo Skills (skills/marimo/) ⭐ NEW

- **01_getting_started.py** - Reactive notebooks, cells, basic structure, running notebooks
- **02_widgets_ui.py** - Interactive UI components (text, slider, dropdown, tables, forms)
- **03_layouts.py** - Organizing notebooks (hstack, vstack, tabs, accordion, sidebar)
- **04_working_with_marimo.py** - Using marimo with Claude Code, helper scripts, CLI commands, workflows

### UI/UX Design Skills (skills/design/) ⭐ NEW

- **01_cli_ux_principles.py** - Human-first design, progressive discovery, error messages, CLI patterns, accessibility
- **02_general_ui_ux.py** - Color theory, typography, layout, WCAG accessibility, notebook design best practices

## 🛠️ Helper Scripts

### Marimo Helpers ⭐ NEW

Located in `helpers/marimo/`, these scripts help Claude Code work seamlessly with marimo notebooks:

#### marimo_generator.py
Programmatically generate marimo notebooks.

**Features:**
- `MarimoNotebookGenerator` class for building notebooks cell-by-cell
- Template generators (`create_basic_notebook`, `create_data_analysis_notebook`, `create_dashboard_notebook`)
- Pattern library for common reactive components
- Type-safe cell dependencies and returns

**Example:**
```python
from helpers.marimo.marimo_generator import MarimoNotebookGenerator

gen = MarimoNotebookGenerator()
gen.add_imports_cell(["import marimo as mo", "import pandas as pd"])
gen.add_markdown_cell("# My Analysis")
gen.add_widget_cell("slider", "slider", start=0, stop=100)
gen.save("analysis.py")
```

#### marimo_cli_helper.py
Wrapper around marimo CLI for programmatic control.

**Features:**
- Installation checking
- Notebook creation from templates
- Edit/run command generation
- Export to HTML, WASM, Markdown
- Notebook validation
- Tutorial launcher

**Example:**
```python
from helpers.marimo.marimo_cli_helper import MarimoCliHelper

helper = MarimoCliHelper()

# Create from template
helper.create_notebook("dashboard.py", template="dashboard")

# Validate
result = helper.validate_notebook("dashboard.py")

# Export to WASM for GitHub Pages
helper.export_notebook("dashboard.py", "html-wasm", "index.html")
```

See `helpers/marimo/README.md` for complete documentation.

---

### Textual Helpers

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

### Path 1: Textual TUI Development (Beginner)
1. Getting Started with Textual
2. Built-in Widget Usage
3. Layout Systems
4. CSS Styling (TCSS)
5. Events and Messages
6. Snapshot Testing

**Goal:** Create functional TUI applications
**Time:** 2-4 hours

---

### Path 2: Marimo Reactive Notebooks ⭐ NEW
1. Getting Started with Marimo
2. Widgets and UI Components
3. Layouts and Organization
4. General UI/UX Principles (for design)

**Goal:** Build interactive, reactive notebooks
**Time:** 3-5 hours

---

### Path 3: UI/UX Excellence ⭐ NEW
1. CLI UX Design Principles
2. General UI/UX Design
3. Apply to Textual apps (Layout & Styling)
4. Apply to Marimo notebooks (Widgets & Layouts)

**Goal:** Master UI/UX design principles across platforms
**Time:** 4-6 hours

---

### Path 4: Textual Advanced Development
1. Custom Widget Development
2. Reactive Attributes
3. Screens and Navigation
4. DOM Queries
5. Input Validation
6. Unit Testing

**Goal:** Build complex, interactive TUI applications
**Time:** 6-8 hours

---

### Path 5: Expert TUI Development
1. Workers & Async Operations
2. Animation
3. Advanced Testing Strategies
4. Performance Optimization
5. Complex State Management

**Goal:** Production-ready TUI applications
**Time:** 8-12 hours

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

### Textual TUI Development
1. **Use External CSS** - Enables hot reload during development
2. **ID for Unique, Classes for Groups** - Better query organization
3. **Reactive for State** - Auto-updating UI
4. **Events for Actions** - User interaction handling
5. **Test with Snapshots** - Visual regression testing
6. **Type Hints** - Better code clarity
7. **Docstrings** - Document your widgets and methods
8. **Keep compose() Simple** - One responsibility per widget

### Marimo Notebooks ⭐ NEW
1. **Import marimo as mo** - Always in first cell
2. **One Operation per Cell** - Keep cells focused
3. **Return All Variables** - Return values you want to reuse (as tuple)
4. **No Redeclaration** - Never redeclare variables across cells
5. **Prefix Temporaries** - Use underscore for local variables (_temp)
6. **Avoid Cycles** - No circular dependencies between cells
7. **Encapsulate in Functions** - Minimize global variables
8. **Test Reactivity** - Ensure widgets trigger correct cell updates

### UI/UX Design ⭐ NEW
1. **Accessibility First** - Design for WCAG 2.1 AA compliance from start
2. **4.5:1 Contrast** - Minimum for normal text readability
3. **Progressive Discovery** - Guide users step-by-step
4. **Helpful Errors** - Include what, why, and how to fix
5. **Consistent Patterns** - Same actions should work the same way
6. **Visual Hierarchy** - Use size, color, position to guide attention
7. **Mobile-First** - Design for smallest screen, scale up
8. **Color Independence** - Never use color alone to convey information

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

### Textual
- **Official Docs**: https://textual.textualize.io
- **Tutorial**: https://textual.textualize.io/tutorial/
- **Widget Gallery**: https://textual.textualize.io/widget_gallery/
- **GitHub**: https://github.com/Textualize/textual
- **Discord**: https://discord.gg/Enf6Z3qhVr

### Marimo ⭐ NEW
- **Official Docs**: https://docs.marimo.io
- **Website**: https://marimo.io
- **GitHub**: https://github.com/marimo-team/marimo
- **Getting Started**: Run `marimo tutorial intro`
- **Examples**: https://docs.marimo.io/examples/
- **Real Python Tutorial**: https://realpython.com/marimo-notebook/

### UI/UX Design ⭐ NEW
- **CLI Guidelines**: https://clig.dev/
- **WCAG 2.1**: https://www.w3.org/WAI/WCAG21/quickref/
- **WebAIM Contrast Checker**: https://webaim.org/resources/contrastchecker/
- **Material Design**: https://material.io/design
- **Interaction Design Foundation**: https://www.interaction-design.org/
- **A11y Project**: https://www.a11yproject.com/

## 🤝 Contributing

This marketplace is designed for AI agents. To add new skills:

1. Create skill file in appropriate category (textual, marimo, or design)
2. Follow existing skill format
3. Include working examples
4. Add docstrings and comments
5. Include test cases (where applicable)
6. Update SKILLS_INDEX.md with new skill details

## 📄 License

This collection is provided as-is for AI agents to learn and build:
- Textual TUI applications
- Marimo reactive notebooks
- Well-designed user interfaces

## 🙋 Support

### Textual
- Discord: https://discord.gg/Enf6Z3qhVr
- GitHub Issues: https://github.com/Textualize/textual/issues

### Marimo
- GitHub Discussions: https://github.com/marimo-team/marimo/discussions
- GitHub Issues: https://github.com/marimo-team/marimo/issues

### UI/UX Design
- Refer to the design skills for principles and best practices
- Community resources linked in Resources section above

---

**Happy Building! 🎉**
*Create beautiful TUIs with Textual, reactive notebooks with Marimo, and accessible interfaces with great UX!*
