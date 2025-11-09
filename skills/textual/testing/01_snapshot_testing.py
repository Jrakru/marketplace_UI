"""
Skill: Snapshot Testing

Master snapshot testing with pytest-textual-snapshot for visual regression testing.
"""

import pytest
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Button, Input, DataTable
from textual.containers import Container


# ============================================================================
# BASIC SNAPSHOT TESTING
# ============================================================================

class SimpleApp(App):
    """A simple app for testing."""

    CSS = """
    Static {
        width: 100%;
        height: 5;
        background: $primary;
        color: $text;
        content-align: center middle;
        border: solid $accent;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Hello, Testing!")
        yield Footer()


# Basic snapshot test
def test_simple_app(snap_compare):
    """Test the simple app matches snapshot."""
    app = SimpleApp()
    assert snap_compare(app)


# Test with specific terminal size
def test_simple_app_sized(snap_compare):
    """Test app at specific terminal size."""
    app = SimpleApp()
    assert snap_compare(app, terminal_size=(80, 24))


# ============================================================================
# TESTING WITH USER INTERACTION
# ============================================================================

class InteractiveApp(App):
    """App with interactive elements."""

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Button("Click Me", id="btn1", variant="primary"),
            Button("Don't Click", id="btn2", variant="error"),
            Static("Clicks: 0", id="counter"),
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press."""
        if event.button.id == "btn1":
            counter = self.query_one("#counter", Static)
            current = int(counter.renderable.split(": ")[1])
            counter.update(f"Clicks: {current + 1}")


def test_interactive_app_initial(snap_compare):
    """Test initial state."""
    app = InteractiveApp()
    assert snap_compare(app)


def test_interactive_app_after_click(snap_compare):
    """Test state after button click."""
    async def run_before(pilot):
        # Simulate clicking the button
        await pilot.click("#btn1")

    app = InteractiveApp()
    assert snap_compare(app, run_before=run_before)


def test_interactive_app_multiple_clicks(snap_compare):
    """Test after multiple interactions."""
    async def run_before(pilot):
        # Click button 3 times
        for _ in range(3):
            await pilot.click("#btn1")

    app = InteractiveApp()
    assert snap_compare(app, run_before=run_before)


# ============================================================================
# TESTING WITH KEY PRESS
# ============================================================================

class KeyboardApp(App):
    """App that responds to keyboard input."""

    BINDINGS = [
        ("space", "toggle", "Toggle"),
        ("r", "reset", "Reset"),
    ]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.state = "OFF"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static(f"State: {self.state}", id="status")
        yield Footer()

    def action_toggle(self) -> None:
        """Toggle state."""
        self.state = "ON" if self.state == "OFF" else "OFF"
        status = self.query_one("#status", Static)
        status.update(f"State: {self.state}")

    def action_reset(self) -> None:
        """Reset state."""
        self.state = "OFF"
        status = self.query_one("#status", Static)
        status.update(f"State: {self.state}")


def test_keyboard_app_initial(snap_compare):
    """Test initial keyboard app state."""
    app = KeyboardApp()
    assert snap_compare(app)


def test_keyboard_app_after_space(snap_compare):
    """Test after pressing space."""
    async def run_before(pilot):
        await pilot.press("space")

    app = KeyboardApp()
    assert snap_compare(app, run_before=run_before)


def test_keyboard_app_sequence(snap_compare):
    """Test key sequence."""
    async def run_before(pilot):
        await pilot.press("space")  # Toggle ON
        await pilot.press("space")  # Toggle OFF
        await pilot.press("space")  # Toggle ON
        await pilot.press("r")      # Reset

    app = KeyboardApp()
    assert snap_compare(app, run_before=run_before)


# ============================================================================
# TESTING FORMS AND INPUTS
# ============================================================================

class FormApp(App):
    """App with form inputs."""

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Input(placeholder="Name", id="name"),
            Input(placeholder="Email", id="email"),
            Button("Submit", id="submit", variant="primary"),
            Static("", id="result"),
        )
        yield Footer()

    def on_button_pressed(self) -> None:
        """Handle form submission."""
        name = self.query_one("#name", Input).value
        email = self.query_one("#email", Input).value
        result = self.query_one("#result", Static)
        result.update(f"Submitted: {name} ({email})")


def test_form_empty(snap_compare):
    """Test empty form."""
    app = FormApp()
    assert snap_compare(app)


def test_form_filled(snap_compare):
    """Test form with filled inputs."""
    async def run_before(pilot):
        # Focus and type in name field
        await pilot.click("#name")
        await pilot.press(*"Alice")

        # Focus and type in email field
        await pilot.click("#email")
        await pilot.press(*"alice@example.com")

    app = FormApp()
    assert snap_compare(app, run_before=run_before)


def test_form_submitted(snap_compare):
    """Test form after submission."""
    async def run_before(pilot):
        await pilot.click("#name")
        await pilot.press(*"Bob")
        await pilot.click("#email")
        await pilot.press(*"bob@test.com")
        await pilot.click("#submit")

    app = FormApp()
    assert snap_compare(app, run_before=run_before)


# ============================================================================
# TESTING DATA TABLES
# ============================================================================

class TableApp(App):
    """App with data table."""

    def compose(self) -> ComposeResult:
        yield Header()
        yield DataTable(id="table")
        yield Footer()

    def on_mount(self) -> None:
        """Setup table."""
        table = self.query_one(DataTable)
        table.add_columns("Name", "Age", "City")
        table.add_rows([
            ("Alice", 30, "NYC"),
            ("Bob", 25, "LA"),
            ("Charlie", 35, "Chicago"),
        ])
        table.cursor_type = "row"


def test_table_initial(snap_compare):
    """Test initial table state."""
    app = TableApp()
    assert snap_compare(app)


def test_table_with_cursor(snap_compare):
    """Test table with cursor movement."""
    async def run_before(pilot):
        # Move cursor down
        await pilot.press("down")
        await pilot.press("down")

    app = TableApp()
    assert snap_compare(app, run_before=run_before)


# ============================================================================
# TESTING DIFFERENT THEMES
# ============================================================================

def test_app_dark_theme(snap_compare):
    """Test app in dark theme."""
    app = SimpleApp()
    app.dark = True
    assert snap_compare(app)


def test_app_light_theme(snap_compare):
    """Test app in light theme."""
    app = SimpleApp()
    app.dark = False
    assert snap_compare(app)


# ============================================================================
# TESTING WITH PRESS SEQUENCE
# ============================================================================

def test_complex_interaction(snap_compare):
    """Test complex interaction sequence."""
    async def run_before(pilot):
        # Wait for app to be ready
        await pilot.pause()

        # Perform a series of actions
        await pilot.press("tab")  # Move focus
        await pilot.press("enter")  # Activate
        await pilot.press("escape")  # Cancel

        # Wait for updates
        await pilot.pause(0.1)

    app = InteractiveApp()
    assert snap_compare(app, run_before=run_before)


# ============================================================================
# SNAPSHOT TESTING GUIDE
# ============================================================================

SNAPSHOT_TESTING_GUIDE = """
SNAPSHOT TESTING GUIDE
=====================

SETUP:
1. Install pytest and pytest-textual-snapshot:
   pip install pytest pytest-asyncio pytest-textual-snapshot

2. Create test file (test_*.py or *_test.py)

3. Import snap_compare fixture (auto-provided)

BASIC TEST:
```python
def test_my_app(snap_compare):
    app = MyApp()
    assert snap_compare(app)
```

WITH INTERACTIONS:
```python
def test_with_click(snap_compare):
    async def run_before(pilot):
        await pilot.click("#button")

    assert snap_compare(MyApp(), run_before=run_before)
```

PILOT METHODS:
- pilot.click(selector)          Click element
- pilot.press(*keys)             Press keys
- pilot.pause(seconds)           Wait
- pilot.hover(selector)          Hover over element
- pilot.focus(selector)          Focus element
- pilot.mouse_down(selector)     Mouse down
- pilot.mouse_up(selector)       Mouse up

WORKFLOW:
1. Write test
2. Run: pytest
3. Tests fail (no snapshot)
4. Check SVG output in __snapshots__/
5. If looks good: pytest --snapshot-update
6. Future runs compare against snapshot
7. If changed: review diff and update if correct

TERMINAL SIZE:
```python
assert snap_compare(app, terminal_size=(80, 24))
```

PRESS SEQUENCES:
```python
async def run_before(pilot):
    # Type text
    await pilot.press(*"Hello")

    # Press special keys
    await pilot.press("enter")
    await pilot.press("tab")
    await pilot.press("escape")

    # Key combinations (press together)
    await pilot.press("ctrl+c")
```

BEST PRACTICES:
1. Test initial state
2. Test after user interactions
3. Test error states
4. Test different terminal sizes
5. Test both themes (dark/light)
6. Use descriptive test names
7. One assertion per test
8. Review SVG outputs carefully
9. Update snapshots deliberately
10. Commit snapshots to git

RUNNING TESTS:
pytest                          # Run all tests
pytest test_app.py             # Run specific file
pytest -k "test_name"          # Run specific test
pytest --snapshot-update       # Update all snapshots
pytest -v                      # Verbose output
pytest -x                      # Stop on first failure

SNAPSHOT LOCATION:
__snapshots__/
└── test_app.py/
    ├── test_my_app.svg
    ├── test_with_click.svg
    └── ...

TIPS:
- Snapshots are SVG images
- Can open in browser to view
- Commit to version control
- Review changes in PRs
- Use for regression testing
- Fast feedback on UI changes
"""


# ============================================================================
# PYTEST CONFIGURATION
# ============================================================================

PYTEST_CONFIG = """
# pytest.ini or pyproject.toml

[tool.pytest.ini_options]
asyncio_mode = "auto"
testpaths = ["tests"]
python_files = "test_*.py"
python_functions = "test_*"

# Snapshot settings
markers = [
    "snapshot: Snapshot tests",
]

# Coverage (optional)
addopts = "--cov=myapp --cov-report=html"
"""


# Helper to create test template
def create_test_template(app_name: str) -> str:
    """Generate test template for an app."""
    return f'''import pytest
from {app_name.lower()} import {app_name}


def test_{app_name.lower()}_initial(snap_compare):
    """Test initial state of {app_name}."""
    app = {app_name}()
    assert snap_compare(app)


def test_{app_name.lower()}_interaction(snap_compare):
    """Test {app_name} with user interaction."""
    async def run_before(pilot):
        # Add interactions here
        await pilot.click("#my_button")
        await pilot.pause()

    app = {app_name}()
    assert snap_compare(app, run_before=run_before)


def test_{app_name.lower()}_keyboard(snap_compare):
    """Test {app_name} keyboard interaction."""
    async def run_before(pilot):
        await pilot.press("tab")
        await pilot.press("enter")

    app = {app_name}()
    assert snap_compare(app, run_before=run_before)
'''


if __name__ == "__main__":
    print(SNAPSHOT_TESTING_GUIDE)
