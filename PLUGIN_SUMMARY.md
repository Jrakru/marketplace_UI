# Textual Plugin - Quick Reference Guide

## 🎯 Plugin Overview

A comprehensive collection of **12 skills**, **5 helper scripts**, **20+ templates**, and **examples** for building Text-based User Interface (TUI) applications with the Textual framework.

### Key Components

| Component | Count | Purpose |
|-----------|-------|---------|
| **Skills** | 12 | Learn Textual through runnable examples |
| **Helper Scripts** | 5 | Generate code and find resources |
| **Templates** | 20+ | Quick-start templates for common patterns |
| **Examples** | 5+ | Complete runnable applications |
| **Learning Paths** | 4 | Structured progression from beginner to expert |

---

## 🚀 Quick Start Checklist

### Step 1: Verify Installation

```bash
# Check Python version (3.8+ required)
python --version

# Install Textual
pip install textual textual-dev

# Test with quick example
python examples/quick_start.py
```

✅ **Expected result:** A working TUI application launches in your terminal

### Step 2: Run Your First Skill

```bash
cd skills/textual/core
python 01_getting_started.py
```

✅ **Expected result:** Basic Textual app demonstrating app structure

### Step 3: Generate Code

```python
from helpers.textual_generator import TextualGenerator, WidgetSpec

# Create a simple app
generator = TextualGenerator()
code = generator.generate_app(
    "MyApp",
    widgets=[
        WidgetSpec("Button", id="click", properties={"label": "Click Me"})
    ]
)
print(code)
```

### Step 4: Choose Your Path

- **Beginner** (2-4 hrs): Start with `skills/textual/core/01_getting_started.py`
- **Intermediate** (4-6 hrs): Try `skills/textual/widgets/02_custom_widgets.py`
- **Expert** (6-10 hrs): Explore `skills/textual/testing/01_snapshot_testing.py`

---

## 📦 Skills Catalog

### Core Foundation (2 skills)

| Skill | File | What You'll Learn |
|-------|------|-------------------|
| **Getting Started** | `skills/textual/core/01_getting_started.py` | App structure, compose method, running apps |
| **App Lifecycle** | `skills/textual/core/02_app_lifecycle.py` | Initialization, configuration, CLI args |

### Widgets (2 skills)

| Skill | File | What You'll Learn |
|-------|------|-------------------|
| **Built-in Widgets** | `skills/textual/widgets/01_builtin_widgets.py` | Button, Input, DataTable, Tree, Checkbox, etc. |
| **Custom Widgets** | `skills/textual/widgets/02_custom_widgets.py` | Create reusable components with reactivity |

### Layout & Design (2 skills)

| Skill | File | What You'll Learn |
|-------|------|-------------------|
| **Layout Systems** | `skills/textual/layout/01_layouts.py` | Vertical, Horizontal, Grid, Dock layouts |
| **CSS Styling** | `skills/textual/layout/02_css_styling.py` | TCSS syntax, selectors, colors, themes |

### Advanced Topics (5 skills)

| Skill | File | What You'll Learn |
|-------|------|-------------------|
| **Events & Messages** | `skills/textual/interactivity/01_events_messages.py` | Event handlers, @on decorator, custom messages |
| **Reactive Attributes** | `skills/textual/reactivity/01_reactive_attributes.py` | Auto-updating state, watch/compute methods |
| **Screens & Navigation** | `skills/textual/navigation/01_screens.py` | Multi-screen apps, modals, async handling |
| **Snapshot Testing** | `skills/textual/testing/01_snapshot_testing.py` | Visual regression testing with pytest |

### UI/UX Design (2 skills)

| Skill | File | What You'll Learn |
|-------|------|-------------------|
| **CLI UX Principles** | `skills/design/01_cli_ux_principles.py` | Human-first design, progressive discovery |
| **General UI/UX** | `skills/design/02_general_ui_ux.py` | Color theory, typography, accessibility |

---

## 🛠️ Helper Scripts Reference

### 1. textual_generator.py

**Generate complete Textual applications programmatically**

```python
from helpers.textual_generator import TextualGenerator, WidgetSpec

# Generate app with widgets
generator = TextualGenerator()
widgets = [
    WidgetSpec("Button", id="submit", properties={"label": "Submit"}),
    WidgetSpec("Input", id="name", properties={"placeholder": "Name"}),
]
code = generator.generate_app("FormApp", widgets=widgets)
```

**Features:**
- ✅ Auto-import collection
- ✅ Full app generation
- ✅ Widget specifications
- ✅ CSS and bindings support

---

### 2. template_manager.py

**Access pre-built code templates**

```python
from helpers.template_manager import TemplateManager, TemplateType

manager = TemplateManager()

# Get template
app_template = manager.get_template(
    TemplateType.APP,
    "basic",
    app_name="MyApp"
)
```

**Template Types:**
- `APP` - Application templates (4 variants)
- `WIDGET` - Custom widgets (4 variants)
- `SCREEN` - Multi-screen templates (2 variants)
- `MODAL` - Dialog boxes (2 variants)
- `TEST` - Testing patterns (2 variants)
- `CSS` - Styling examples (3 variants)
- `EVENT_HANDLER` - Event patterns (3 variants)
- `REACTIVE` - State management (3 variants)

---

### 3. skill_finder.py

**Find relevant skills for your task**

```python
from helpers.skill_finder import SkillFinder

finder = SkillFinder()

# Search by keyword
skills = finder.find_skills("button events")

# Get recommendations
task = "Create a counter with auto-updating display"
recommendations = finder.find_by_task(task)

# Get learning path
path = finder.get_learning_path("beginner")
```

---

### 4. quick_reference.py

**Fast syntax lookup**

```python
from helpers.quick_reference import QUICK_REFERENCE, get_pattern

# View all patterns
print(QUICK_REFERENCE)

# Get specific pattern
counter_pattern = get_pattern("counter")
form_pattern = get_pattern("form")
```

**Available Patterns:**
- `counter` - Reactive counter
- `form` - Input form
- `modal` - Confirmation dialog
- `reactive` - Reactive attributes
- `grid` - Grid layout
- `event_handler` - Event patterns
- `custom_widget` - Custom widget structure

---

### 5. marimo_generator.py

**Generate Marimo reactive notebooks (bonus!)**

```python
from helpers.marimo.marimo_generator import MarimoNotebookGenerator

gen = MarimoNotebookGenerator()
gen.add_imports_cell(["import marimo as mo"])
gen.add_markdown_cell("# My Analysis")
gen.add_widget_cell("slider", "threshold", start=0, stop=100)
gen.save("analysis.py")
```

---

## 📚 Common Commands & Patterns

### Basic App Structure

```python
from textual.app import App, ComposeResult
from textual.widgets import Static

class MyApp(App):
    """A simple Textual app."""

    def compose(self) -> ComposeResult:
        """Create child widgets."""
        yield Static("Hello, Textual!")

if __name__ == "__main__":
    app = MyApp()
    app.run()
```

### Button Click Handler

```python
from textual.widgets import Button
from textual.on import on

@on(Button.Pressed, "#submit")
def handle_submit(self, event: Button.Pressed) -> None:
    """Handle button press."""
    self.notify("Button clicked!")

# Or without decorator:
def on_button_pressed(self, event: Button.Pressed) -> None:
    if event.button.id == "submit":
        self.notify("Button clicked!")
```

### Reactive Counter

```python
from textual.reactive import reactive
from textual.widgets import Button, Static

class CounterApp(App):
    count = reactive(0)

    def compose(self) -> ComposeResult:
        yield Button("-", id="dec")
        yield Static("0", id="display")
        yield Button("+", id="inc")

    def watch_count(self, new_count: int) -> None:
        """Auto-update display."""
        self.query_one("#display", Static).update(str(new_count))

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "inc":
            self.count += 1
        elif event.button.id == "dec":
            self.count -= 1
```

### Modal Dialog

```python
from textual.screen import ModalScreen
from textual.widgets import Button, Static

class ConfirmDialog(ModalScreen[bool]):
    def compose(self) -> ComposeResult:
        with Static():
            yield Static("Are you sure?")
            with Horizontal():
                yield Button("Yes", id="yes")
                yield Button("No", id="no")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.dismiss(event.button.id == "yes")

# Show modal
async def show_confirm(self):
    result = await self.push_screen_wait(ConfirmDialog())
    if result:
        self.notify("Confirmed!")
```

### CSS Styling

```python
CSS = '''
Screen {
    background: $primary;
}

Button {
    margin: 1;
    padding: 0 2;
}

#special {
    background: $success;
}
'''
```

### Data Table

```python
from textual.widgets import DataTable

table = DataTable()
table.add_columns("Name", "Age", "City")
table.add_rows([
    ["Alice", 30, "NYC"],
    ["Bob", 25, "LA"],
])
```

---

## 🎓 Learning Paths

### Path 1: Textual Beginner (2-4 hours)

```
1. ⭐ skills/textual/core/01_getting_started.py
2. ⭐ skills/textual/widgets/01_builtin_widgets.py
3. ⭐ skills/textual/layout/01_layouts.py
4. ⭐ skills/textual/interactivity/01_events_messages.py
5. ⭐ skills/textual/layout/02_css_styling.py
```

**Goal:** Create simple, functional TUI applications

---

### Path 2: Textual Intermediate (4-6 hours)

```
1. skills/textual/widgets/02_custom_widgets.py
2. skills/textual/reactivity/01_reactive_attributes.py
3. skills/textual/navigation/01_screens.py
4. skills/textual/testing/01_snapshot_testing.py
```

**Goal:** Build multi-screen, reactive applications

---

### Path 3: UI/UX Excellence (4-6 hours)

```
1. ⭐ skills/design/01_cli_ux_principles.py
2. ⭐ skills/design/02_general_ui_ux.py
3. Apply to Textual apps
4. Apply to Marimo notebooks
```

**Goal:** Master UI/UX design principles

---

## 🎯 Quick Task Guide

### I Want To...

| Task | Skills Needed | Quick Code |
|------|---------------|------------|
| **Create a counter** | `reactivity/01_reactive_attributes.py` | Use `reactive` and `watch_` methods |
| **Build a form** | `widgets/01_builtin_widgets.py` | Use `Input` and `Button` widgets |
| **Show a dialog** | `navigation/01_screens.py` | Use `ModalScreen` |
| **Arrange widgets** | `layout/01_layouts.py` | Use `Horizontal`, `Vertical`, `Grid` |
| **Style my app** | `layout/02_css_styling.py` | Use TCSS syntax |
| **Handle events** | `interactivity/01_events_messages.py` | Use `on_*` methods or `@on` decorator |
| **Test my app** | `testing/01_snapshot_testing.py` | Use `pytest-textual-snapshot` |

---

## 🔧 Common Issues & Solutions

### Issue: Widget Not Updating

**Problem:** UI doesn't reflect state changes

**Solution:**
```python
# ✅ Use reactive attributes
count = reactive(0)

def watch_count(self, new_count):
    self.query_one("#display").update(str(new_count))
```

### Issue: Layout Broken

**Problem:** Widgets not positioned correctly

**Solution:**
```python
# Check CSS grid settings
CSS = '''
Container {
    grid-size: 2 2;  /* 2 columns, 2 rows */
}
'''
```

### Issue: Events Not Firing

**Problem:** Event handlers not called

**Solution:**
```python
# Ensure IDs match
yield Button("Click", id="my-button")

@on(Button.Pressed, "#my-button")  # Match the ID
def handle_click(self):
    pass
```

### Issue: Import Errors

**Problem:** Module not found

**Solution:**
```bash
pip install textual textual-dev
```

---

## 📖 Testing Commands

```bash
# Install test dependencies
pip install pytest pytest-asyncio pytest-textual-snapshot

# Run all tests
pytest

# Update snapshots
pytest --snapshot-update

# Run specific test
pytest tests/test_app.py -v

# Run with dev mode (hot reload)
textual run --dev your_app.py
```

---

## 🔗 Essential Links

### Official Resources
- **Textual Docs:** https://textual.textualize.io
- **Tutorial:** https://textual.textualize.io/tutorial/
- **Widget Gallery:** https://textual.textualize.io/widget_gallery/
- **GitHub:** https://github.com/Textualize/textual
- **Discord:** https://discord.gg/Enf6Z3qhVr

### Plugin Resources
- **Full Documentation:** See `README.md`
- **Skills Index:** See `SKILLS_INDEX.md`
- **Getting Started:** See `GETTING_STARTED.md`
- **Quick Reference:** Run `python helpers/quick_reference.py`

### Community
- **GitHub Discussions:** https://github.com/Textualize/textual/discussions
- **Stack Overflow:** Use "textual" tag
- **Reddit:** r/Python (Textual posts)

---

## 📊 Plugin Statistics

| Metric | Value |
|--------|-------|
| **Total Skills** | 12 |
| **Helper Scripts** | 5 |
| **Code Templates** | 20+ |
| **Example Apps** | 5+ |
| **Learning Paths** | 4 |
| **Skill Categories** | 8 |
| **Lines of Documentation** | 1500+ |
| **Code Examples** | 100+ |

---

## 🎨 Marimo Bonus Feature

Generate reactive notebooks with Marimo!

```python
from helpers.marimo.marimo_generator import MarimoNotebookGenerator

gen = MarimoNotebookGenerator()
gen.add_imports_cell(["import marimo as mo", "import pandas as pd"])
gen.add_markdown_cell("# Data Analysis")
gen.add_widget_cell("slider", "threshold", start=0, stop=100)
gen.add_code_cell("filtered = data[data['value'] > threshold]")
gen.save("analysis.py")
```

**Run the notebook:**
```bash
marimo edit analysis.py
```

---

## 🎯 Best Practices Summary

### ✅ DO
- Use reactive attributes for state
- Keep compose() simple (widgets only)
- Use IDs for unique widgets
- Use classes for groups of widgets
- Test with snapshot testing
- Add type hints
- Use workers for long operations
- Follow the learning paths

### ❌ DON'T
- Put business logic in compose()
- Query widgets by content
- Manually update UI (use reactivity)
- Block the event loop
- Ignore error handling
- Skip testing
- Over-complicate layouts

---

## 🚀 Next Steps

1. **Run the quick start:**
   ```bash
   python examples/quick_start.py
   ```

2. **Pick a learning path:**
   - Beginner: `skills/textual/core/01_getting_started.py`
   - Intermediate: `skills/textual/widgets/02_custom_widgets.py`
   - Expert: `skills/textual/testing/01_snapshot_testing.py`

3. **Use helpers:**
   - Generate code: `helpers/textual_generator.py`
   - Get templates: `helpers/template_manager.py`
   - Find skills: `helpers/skill_finder.py`

4. **Join the community:**
   - Discord: https://discord.gg/Enf6Z3qhVr

5. **Build something amazing! 🎉**

---

**Happy Coding! ✨**

*For complete documentation, see README.md*
