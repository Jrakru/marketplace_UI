# Getting Started with Textual Marketplace

Quick guide to start using this marketplace for building Textual TUIs.

## 📦 Installation

```bash
# Install Textual and dependencies
pip install -r requirements.txt

# Or install manually
pip install textual textual-dev pytest pytest-asyncio pytest-textual-snapshot
```

## 🚀 Quick Start (< 5 minutes)

### 1. Run the Example

```bash
cd examples
python quick_start.py
```

This will launch a complete app demonstrating all key features.

### 2. Explore a Skill

```bash
cd skills/core
python 01_getting_started.py
```

Each skill file is runnable and demonstrates specific concepts.

### 3. Use Helper Scripts

```bash
cd helpers

# View quick reference
python quick_reference.py

# Find skills
python skill_finder.py

# Generate code
python textual_generator.py
```

## 📚 For AI Agents

### Step 1: Understand the Structure

```
marketplace_textual/
├── skills/          ← Examples organized by topic
├── helpers/         ← Code generation tools
├── examples/        ← Complete applications
└── templates/       ← Project templates
```

### Step 2: Find What You Need

Use the skill finder to locate relevant examples:

```python
from helpers.skill_finder import SkillFinder

finder = SkillFinder()

# Search for specific functionality
skills = finder.find_skills("button click events")

# Get recommendations for a task
task = "Create a data entry form with validation"
recommendations = finder.find_by_task(task)

# Get learning path
path = finder.get_learning_path("beginner")
```

### Step 3: Generate Code

Use templates or generators:

```python
from helpers.template_manager import TemplateManager, TemplateType

manager = TemplateManager()

# Get a template
app_code = manager.get_template(
    TemplateType.APP,
    "basic",
    app_name="MyApp"
)

print(app_code)
```

### Step 4: Learn from Skills

1. Browse `SKILLS_INDEX.md` for complete catalog
2. Pick relevant skills based on your task
3. Read the skill file (contains examples and guides)
4. Copy and adapt the code

### Step 5: Test Your Code

```bash
# Run tests
pytest

# Update snapshots
pytest --snapshot-update

# Run with dev mode (hot reload)
textual run --dev your_app.py
```

## 🎯 Common Tasks

### Task: Create a Simple Counter

**Skills needed:** `skills/reactivity/01_reactive_attributes.py`

**Quick code:**
```python
from textual.app import App, ComposeResult
from textual.widgets import Button, Static
from textual.reactive import reactive

class CounterApp(App):
    count = reactive(0)

    def compose(self) -> ComposeResult:
        yield Static("0", id="display")
        yield Button("+", id="inc")

    def watch_count(self, new_count):
        self.query_one("#display").update(str(new_count))

    def on_button_pressed(self):
        self.count += 1

if __name__ == "__main__":
    CounterApp().run()
```

### Task: Create a Form

**Skills needed:** `skills/widgets/01_builtin_widgets.py`

**Quick code:**
```python
from textual.app import App, ComposeResult
from textual.widgets import Input, Button, Header, Footer
from textual.containers import Container

class FormApp(App):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Input(placeholder="Name", id="name"),
            Input(placeholder="Email", id="email"),
            Button("Submit", variant="primary"),
        )
        yield Footer()

    def on_button_pressed(self):
        name = self.query_one("#name", Input).value
        email = self.query_one("#email", Input).value
        self.notify(f"Submitted: {name}, {email}")

if __name__ == "__main__":
    FormApp().run()
```

### Task: Create a Modal Dialog

**Skills needed:** `skills/navigation/01_screens.py`

**Quick code:**
```python
from textual.app import App, ComposeResult
from textual.screen import ModalScreen
from textual.widgets import Button, Static
from textual.containers import Vertical, Horizontal

class ConfirmModal(ModalScreen[bool]):
    CSS = """
    ConfirmModal {
        align: center middle;
    }
    #dialog {
        width: 40;
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
                yield Button("Yes", id="yes")
                yield Button("No", id="no")

    def on_button_pressed(self, event):
        self.dismiss(event.button.id == "yes")

class MainApp(App):
    def compose(self) -> ComposeResult:
        yield Button("Show Dialog")

    async def on_button_pressed(self):
        result = await self.push_screen_wait(ConfirmModal())
        self.notify(f"Result: {result}")

if __name__ == "__main__":
    MainApp().run()
```

## 🔍 Finding the Right Skill

Use this quick reference:

| I want to... | Skill to use |
|-------------|-------------|
| Create my first app | `skills/core/01_getting_started.py` |
| Add buttons and inputs | `skills/widgets/01_builtin_widgets.py` |
| Layout widgets | `skills/layout/01_layouts.py` |
| Style my app | `skills/layout/02_css_styling.py` |
| Handle button clicks | `skills/interactivity/01_events_messages.py` |
| Auto-update UI | `skills/reactivity/01_reactive_attributes.py` |
| Add multiple screens | `skills/navigation/01_screens.py` |
| Test my app | `skills/testing/01_snapshot_testing.py` |
| Create custom widget | `skills/widgets/02_custom_widgets.py` |

## 📖 Learning Path

### Beginner (2-4 hours)
1. ✅ Run `examples/quick_start.py`
2. ✅ Read `skills/core/01_getting_started.py`
3. ✅ Study `skills/widgets/01_builtin_widgets.py`
4. ✅ Explore `skills/layout/01_layouts.py`
5. ✅ Practice with `skills/interactivity/01_events_messages.py`

### Intermediate (4-6 hours)
1. ✅ Master `skills/reactivity/01_reactive_attributes.py`
2. ✅ Learn `skills/navigation/01_screens.py`
3. ✅ Create `skills/widgets/02_custom_widgets.py`
4. ✅ Test with `skills/testing/01_snapshot_testing.py`

### Advanced (6-10 hours)
1. ✅ Optimize with advanced features
2. ✅ Build complex state management
3. ✅ Create widget libraries
4. ✅ Master testing strategies

## 💡 Pro Tips

1. **Start with examples** - Run them first, then modify
2. **Use hot reload** - Run with `textual run --dev` for instant feedback
3. **Read the guides** - Each skill has a guide section at the bottom
4. **Copy & adapt** - Don't write from scratch, adapt examples
5. **Test early** - Use snapshot testing from the start
6. **Use helpers** - Generators and templates save time
7. **Check quick reference** - Fast syntax lookup
8. **Explore gradually** - Don't try to learn everything at once

## 🐛 Troubleshooting

### Import errors
```bash
pip install -r requirements.txt
```

### Skills not found
```bash
cd marketplace_textual  # Make sure you're in the right directory
```

### Can't run examples
```bash
chmod +x examples/*.py  # Make executable
python examples/quick_start.py  # Run with python
```

### Widget not updating
- Use reactive attributes for dynamic data
- Check if you're calling `.refresh()` when needed

### Layout issues
- Review `skills/layout/01_layouts.py`
- Use `textual console` to inspect DOM

## 📚 Resources

- **Official Docs**: https://textual.textualize.io
- **Skills Index**: See `SKILLS_INDEX.md`
- **Quick Reference**: Run `helpers/quick_reference.py`
- **Discord**: https://discord.gg/Enf6Z3qhVr

## 🎯 Next Steps

1. ✅ Run `examples/quick_start.py`
2. ✅ Read `README.md` for overview
3. ✅ Browse `SKILLS_INDEX.md` for catalog
4. ✅ Pick a skill and start coding
5. ✅ Use helpers when you need code generation
6. ✅ Test your app with pytest
7. ✅ Build something amazing!

---

**Happy coding! 🚀**
