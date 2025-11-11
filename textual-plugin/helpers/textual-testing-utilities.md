# textual-testing-utilities

Testing strategies, test utilities, testing patterns, and best practices for Textual applications.

## Overview

Testing Textual applications requires understanding both traditional unit testing and UI-specific testing patterns. This guide covers comprehensive testing strategies for TUI applications.

## Testing Fundamentals

### Testing Stack

```python
# Required testing dependencies
# pytest>=7.0.0
# pytest-textual>=0.1.0
# rich>=12.0.0
# hypothesis>=6.0.0

# Install
pip install pytest pytest-textual rich hypothesis
```

### Basic Test Setup

```python
# tests/conftest.py
import pytest
from textual.app import App
from textual.testing import AppTest, press, click

@pytest.fixture
def test_app():
    """Create test app."""
    class TestApp(App):
        def compose(self):
            yield Button("Click Me")
            yield Input(placeholder="Type here...")

    return TestApp()

@pytest.fixture
async def app_test(test_app):
    """Create app test."""
    async with test_app.run_test() as pilot:
        yield pilot
```

## Unit Testing

### Widget Testing

```python
# tests/test_widgets.py
import pytest
from textual.widgets import Button, Input, Label
from textual.containers import Vertical

class TestButton:
    """Test Button widget."""

    def test_button_creation(self):
        """Test button creation."""
        button = Button("Test Button")
        assert button.label == "Test Button"

    def test_button_variant(self):
        """Test button variants."""
        primary = Button("Primary", variant="primary")
        assert primary.variant == "primary"

        success = Button("Success", variant="success")
        assert success.variant == "success"

    def test_button_disabled(self):
        """Test disabled button."""
        disabled = Button("Disabled", disabled=True)
        assert disabled.disabled is True

    def test_button_size(self):
        """Test button sizing."""
        button = Button("Sized", size=(10, 2))
        assert button.size.width == 10
        assert button.size.height == 2

class TestInput:
    """Test Input widget."""

    def test_input_creation(self):
        """Test input creation."""
        input_widget = Input()
        assert input_widget.value == ""

    def test_input_with_value(self):
        """Test input with initial value."""
        input_widget = Input(value="Initial")
        assert input_widget.value == "Initial"

    def test_input_placeholder(self):
        """Test input placeholder."""
        input_widget = Input(placeholder="Enter text...")
        assert input_widget.placeholder == "Enter text..."

    def test_input_password(self):
        """Test password input."""
        password = Input(password=True)
        assert password.password is True

class TestLabel:
    """Test Label widget."""

    def test_label_creation(self):
        """Test label creation."""
        label = Label("Test Label")
        assert label.renderable == "Test Label"

    def test_label_styling(self):
        """Test label with styling."""
        styled = Label("Styled", classes="title")
        assert "title" in styled.classes
```

### App Testing

```python
# tests/test_app.py
import pytest
from textual.app import App

class CounterApp(App):
    """Test app for counter."""

    CSS = """
    Button {
        margin: 1;
    }
    """

    def __init__(self):
        super().__init__()
        self.count = 0

    def compose(self):
        yield Button("Increment", id="inc")
        yield Button("Decrement", id="dec")
        yield Label("0", id="count-label")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "inc":
            self.count += 1
        elif event.button.id == "dec":
            self.count -= 1

        label = self.query_one("#count-label", Label)
        label.update(str(self.count))

class TestCounterApp:
    """Test Counter app."""

    @pytest.fixture
    async def app_test(self):
        async with CounterApp().run_test() as pilot:
            yield pilot

    async def test_app_mount(self, app_test):
        """Test app mounts successfully."""
        assert app_test.app.is_running

    async def test_increment_button(self, app_test):
        """Test increment button."""
        await app_test.click("#inc")
        label = app_test.app.query_one("#count-label", Label)
        assert label.renderable == "1"

    async def test_decrement_button(self, app_test):
        """Test decrement button."""
        await app_test.click("#dec")
        label = app_test.app.query_one("#count-label", Label)
        assert label.renderable == "-1"

    async def test_multiple_clicks(self, app_test):
        """Test multiple button clicks."""
        await app_test.click("#inc")
        await app_test.click("#inc")
        await app_test.click("#dec")

        label = app_test.app.query_one("#count-label", Label)
        assert label.renderable == "1"

    async def test_keyboard_input(self, app_test):
        """Test keyboard input."""
        # Some apps respond to keyboard
        await app_test.press("q")
        # Verify app behavior
```

### Custom Widget Testing

```python
# tests/test_custom_widget.py
from textual.widget import Widget
from textual.reactive import reactive

class StatusDisplay(Widget):
    """Custom status display widget."""

    status = reactive("Ready")

    def watch_status(self, status: str) -> None:
        self.update(status)

    def compose(self):
        yield Label("", id="status-label")

    def render(self):
        return self.status

class TestStatusDisplay:
    """Test StatusDisplay widget."""

    def test_status_creation(self):
        """Test status display creation."""
        widget = StatusDisplay()
        assert widget.status == "Ready"

    def test_status_update(self):
        """Test status updates."""
        widget = StatusDisplay()
        widget.status = "Loading..."
        assert widget.status == "Loading..."

    def test_reactive_update(self):
        """Test reactive property updates."""
        widget = StatusDisplay()
        updates = []

        # Subscribe to changes
        widget.status.subscribe(lambda v: updates.append(v))

        # Update status
        widget.status = "Processing"
        widget.status = "Complete"

        assert updates == ["Processing", "Complete"]
```

## Integration Testing

### Screen Testing

```python
# tests/test_screens.py
import pytest
from textual.screen import Screen
from textual.widgets import Button, Label

class DetailScreen(Screen):
    """Detail screen."""

    def __init__(self, item_id: str):
        super().__init__()
        self.item_id = item_id

    def compose(self):
        yield Label(f"Item: {self.item_id}", id="item-label")
        yield Button("Back", id="back")

    def on_button_pressed_back(self, event: Button.Pressed) -> None:
        self.app.pop_screen()

class TestScreenNavigation:
    """Test screen navigation."""

    @pytest.fixture
    async def app_with_screens(self):
        """App with multiple screens."""
        class MultiScreenApp(App):
            def compose(self):
                yield Button("Open Detail", id="open")

            def on_button_pressed_open(self, event: Button.Pressed) -> None:
                self.push_screen(DetailScreen("123"))

        async with MultiScreenApp().run_test() as pilot:
            yield pilot

    async def test_screen_push(self, app_with_screens):
        """Test pushing a screen."""
        await app_with_screens.click("#open")

        # Check if detail screen is active
        detail_label = app_with_screens.app.query_one("#item-label", Label)
        assert detail_label.renderable == "Item: 123"

    async def test_screen_pop(self, app_with_screens):
        """Test popping a screen."""
        # Push detail screen
        await app_with_screens.click("#open")

        # Pop it back
        await app_with_screens.click("#back")

        # Should be back to main screen
        open_button = app_with_screens.app.query_one("#open", Button)
        assert open_button is not None
```

### Event Testing

```python
# tests/test_events.py
import pytest
from textual.widgets import Button
from textual.message import Message

class CustomEvent(Message):
    """Custom test event."""
    def __init__(self, value: str):
        self.value = value
        super().__init__()

class EventTestApp(App):
    """App for event testing."""

    def __init__(self):
        super().__init__()
        self.events = []

    def compose(self):
        yield Button("Trigger Event", id="trigger")

    def on_custom_event(self, event: CustomEvent) -> None:
        """Handle custom event."""
        self.events.append(event.value)

    def on_button_pressed_trigger(self, event: Button.Pressed) -> None:
        """Trigger custom event."""
        self.post_message(CustomEvent("test"))

class TestEventHandling:
    """Test event handling."""

    @pytest.fixture
    async def event_app(self):
        async with EventTestApp().run_test() as pilot:
            yield pilot

    async def test_button_triggers_event(self, event_app):
        """Test button triggers custom event."""
        app = event_app.app
        assert len(app.events) == 0

        await event_app.click("#trigger")

        assert len(app.events) == 1
        assert app.events[0] == "test"

    async def test_message_posting(self, event_app):
        """Test direct message posting."""
        app = event_app.app
        app.post_message(CustomEvent("direct"))

        assert "direct" in app.events
```

## UI Testing

### Visual Regression Testing

```python
# tests/test_visual.py
import pytest
from textual.snapshot import compare_snapshots

class VisualTestApp(App):
    """Simple app for visual testing."""

    def compose(self):
        yield Button("Test Button", variant="primary")
        yield Input(placeholder="Test Input")

class TestVisual:
    """Test visual appearance."""

    @pytest.mark.snapshot
    async def test_app_snapshot(self, tmp_path):
        """Test app snapshot."""
        app = VisualTestApp()
        async with app.run_test():
            # Capture snapshot
            path = tmp_path / "test_app.png"
            await app.export_screenshot(path)

            # Compare with baseline
            baseline = "tests/snapshots/test_app.png"
            if baseline.exists():
                assert compare_snapshots(path, baseline)
```

### Interaction Testing

```python
# tests/test_interactions.py
import pytest
from textual.widgets import Button, Input, Checkbox

class InteractionApp(App):
    """App for interaction testing."""

    def compose(self):
        yield Input(placeholder="Username", id="username")
        yield Input(placeholder="Password", id="password", password=True)
        yield Checkbox("Remember me", id="remember")
        yield Button("Login", id="login", variant="primary")

    def on_button_pressed_login(self, event: Button.Pressed) -> None:
        username = self.query_one("#username", Input).value
        password = self.query_one("#password", Input).value
        remember = self.query_one("#remember", Checkbox).value

        # Store for testing
        self.login_data = {
            "username": username,
            "password": password,
            "remember": remember,
        }

class TestInteractions:
    """Test user interactions."""

    @pytest.fixture
    async def interaction_app(self):
        async with InteractionApp().run_test() as pilot:
            yield pilot

    async def test_form_fill(self, interaction_app):
        """Test filling form fields."""
        await interaction_app.type("user123", into="#username")
        await interaction_app.type("password456", into="#password")

        username = interaction_app.app.query_one("#username", Input)
        assert username.value == "user123"

        password = interaction_app.app.query_one("#password", Input)
        assert password.value == "password456"

    async def test_checkbox_toggle(self, interaction_app):
        """Test checkbox toggle."""
        checkbox = interaction_app.app.query_one("#remember", Checkbox)

        # Initially unchecked
        assert checkbox.value is False

        # Click to check
        await interaction_app.click("#remember")

        assert checkbox.value is True

    async def test_form_submission(self, interaction_app):
        """Test form submission."""
        # Fill form
        await interaction_app.type("testuser", into="#username")
        await interaction_app.type("testpass", into="#password")
        await interaction_app.click("#remember")

        # Submit
        await interaction_app.click("#login")

        # Verify submission
        app = interaction_app.app
        assert app.login_data["username"] == "testuser"
        assert app.login_data["password"] == "testpass"
        assert app.login_data["remember"] is True

    async def test_tab_navigation(self, interaction_app):
        """Test tab navigation through form."""
        # Tab through fields
        await interaction_app.press("tab")
        await interaction_app.type("value1")

        await interaction_app.press("tab")
        await interaction_app.type("value2")

        # Verify focus moved
        # (Textual handles focus automatically)
```

### Data Table Testing

```python
# tests/test_datatable.py
from textual.widgets import DataTable

class TableApp(App):
    """App with data table."""

    def compose(self):
        self.table = DataTable(id="data-table")
        self.table.add_columns("Name", "Age", "City")
        self.table.add_rows([
            ("Alice", 30, "New York"),
            ("Bob", 25, "Los Angeles"),
            ("Charlie", 35, "Chicago"),
        ])
        yield self.table

    def on_data_table_row_selected(self, event: DataTable.RowSelected) -> None:
        """Handle row selection."""
        self.selected_row = event.row

class TestDataTable:
    """Test DataTable widget."""

    @pytest.fixture
    async def table_app(self):
        async with TableApp().run_test() as pilot:
            yield pilot

    async def test_table_creation(self, table_app):
        """Test table creation."""
        table = table_app.app.query_one("#data-table", DataTable)
        assert table is not None

    async def test_table_rows(self, table_app):
        """Test table rows."""
        table = table_app.app.query_one("#data-table", DataTable)
        rows = list(table.rows)
        assert len(rows) == 3

    async def test_row_selection(self, table_app):
        """Test row selection."""
        table = table_app.app.query_one("#data-table", DataTable)

        # Select first row
        await table_app.click(DataTable.RowIndex(0))

        # Verify selection
        assert table_app.app.selected_row == table.rows[0]

    async def test_cell_editing(self, table_app):
        """Test cell editing."""
        table = table_app.app.query_one("#data-table", DataTable)

        # Navigate to cell and edit
        await table_app.click(DataTable.CellCoordinate(0, 0))
        await table_app.type("Alicia")

        # Verify change
        cell_value = table.get_cell_at((0, 0))
        assert cell_value == "Alicia"
```

## Async Testing

### Async Operation Testing

```python
# tests/test_async.py
import asyncio
import pytest
from textual.widgets import LoadingIndicator, Button

class AsyncApp(App):
    """App with async operations."""

    def __init__(self):
        super().__init__()
        self.operation_complete = False
        self.result = None

    def compose(self):
        yield Button("Start Async", id="start")
        yield LoadingIndicator("Working...", id="spinner")
        yield Static("", id="result")

    async def on_button_pressed_start(self, event: Button.Pressed) -> None:
        """Start async operation."""
        # Show loading
        spinner = self.query_one("#spinner", LoadingIndicator)
        spinner.visible = True

        # Perform async work
        try:
            result = await self.long_operation()
            self.result = result
            self.operation_complete = True
        finally:
            spinner.visible = False

        # Show result
        result_display = self.query_one("#result", Static)
        result_display.update(f"Result: {result}")

    async def long_operation(self) -> str:
        """Simulate long async operation."""
        await asyncio.sleep(0.1)
        return "Success"

class TestAsyncOperations:
    """Test async operations."""

    @pytest.fixture
    async def async_app(self):
        async with AsyncApp().run_test() as pilot:
            yield pilot

    async def test_async_operation(self, async_app):
        """Test async operation execution."""
        app = async_app.app

        # Verify initial state
        assert app.operation_complete is False
        assert app.result is None

        # Trigger async operation
        await async_app.click("#start")

        # Wait for completion
        await asyncio.sleep(0.2)

        # Verify completion
        assert app.operation_complete is True
        assert app.result == "Success"

    async def test_loading_indicator(self, async_app):
        """Test loading indicator visibility."""
        spinner = async_app.app.query_one("#spinner", LoadingIndicator)

        # Should be hidden initially
        assert spinner.visible is False

        # Click start
        await async_app.click("#start")

        # Should be visible during operation
        await asyncio.sleep(0.05)
        assert spinner.visible is True

        # Wait for completion
        await asyncio.sleep(0.2)
        assert spinner.visible is False
```

### Timer Testing

```python
# tests/test_timers.py
from textual.app import App
from textual.widgets import Button, Label

class TimerApp(App):
    """App with timers."""

    def compose(self):
        yield Button("Start", id="start")
        yield Button("Stop", id="stop")
        yield Label("0", id="count")

    def on_mount(self):
        self.count = 0
        self.timer = None

    def on_button_pressed_start(self, event: Button.Pressed) -> None:
        """Start timer."""
        if not self.timer:
            self.timer = self.set_interval(0.01, self.increment)

    def on_button_pressed_stop(self, event: Button.Pressed) -> None:
        """Stop timer."""
        if self.timer:
            self.timer.stop()
            self.timer = None

    def increment(self):
        """Increment counter."""
        self.count += 1
        label = self.query_one("#count", Label)
        label.update(str(self.count))

class TestTimers:
    """Test timer functionality."""

    @pytest.fixture
    async def timer_app(self):
        async with TimerApp().run_test() as pilot:
            yield pilot

    async def test_timer_start(self, timer_app):
        """Test timer starts."""
        app = timer_app.app

        # Initial count
        assert app.count == 0

        # Start timer
        await timer_app.click("#start")

        # Wait for increments
        await asyncio.sleep(0.05)

        # Count should increase
        assert app.count > 0

    async def test_timer_stop(self, timer_app):
        """Test timer stops."""
        app = timer_app.app

        # Start timer
        await timer_app.click("#start")

        # Wait
        await asyncio.sleep(0.05)

        # Stop timer
        await timer_app.click("#stop")

        # Get count
        count_before = app.count

        # Wait more
        await asyncio.sleep(0.05)

        # Count should not change
        assert app.count == count_before
```

## Performance Testing

### Rendering Performance

```python
# tests/test_performance.py
import time
import pytest
from textual.widgets import Button, Static
from textual.containers import Vertical

class PerformanceApp(App):
    """App for performance testing."""

    def compose(self):
        with Vertical(id="container"):
            for i in range(100):
                yield Button(f"Button {i}", id=f"btn-{i}")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press."""
        # Simulate work
        time.sleep(0.001)

class TestPerformance:
    """Test app performance."""

    @pytest.mark.slow
    async def test_render_performance(self):
        """Test app render performance."""
        app = PerformanceApp()

        start_time = time.time()
        async with app.run_test():
            render_time = time.time() - start_time

        # Should render in reasonable time
        assert render_time < 1.0

    @pytest.mark.slow
    async def test_button_click_performance(self, benchmark):
        """Test button click performance."""
        app = PerformanceApp()
        async with app.run_test() as pilot:
            # Benchmark button click
            def click_button():
                pilot.click("#btn-50")

            result = benchmark(click_button)
            assert result is not None
```

### Memory Testing

```python
# tests/test_memory.py
import pytest
from textual.widgets import Static
from textual.containers import Vertical

class MemoryTestApp(App):
    """App for memory testing."""

    def compose(self):
        with Vertical(id="container"):
            for i in range(50):
                yield Static(f"Item {i}", id=f"item-{i}")

    def clear_items(self):
        """Clear all items."""
        container = self.query_one("#container", Vertical)
        for widget in container.children.copy():
            widget.remove()

class TestMemory:
    """Test memory usage."""

    async def test_no_memory_leaks(self):
        """Test for memory leaks."""
        app = MemoryTestApp()

        async with app.run_test():
            # App is active
            assert len(app.query(Static)) == 50

        # App is disposed
        # Memory should be freed

    async def test_widget_cleanup(self):
        """Test widget cleanup."""
        app = MemoryTestApp()
        async with app.run_test() as pilot:
            # Clear items
            app.clear_items()

            # Check items are removed
            items = list(app.query(Static))
            assert len(items) == 0
```

## Test Utilities

### Custom Test Helpers

```python
# tests/helpers.py
import asyncio
from typing import Any, Optional
from textual.app import App
from textual.testing import AppTest

class TestHelper:
    """Custom test helper."""

    def __init__(self, app: App):
        self.app = app
        self.test = AppTest(app)

    async def setup(self):
        """Set up test."""
        await self.test._setup()

    async def cleanup(self):
        """Clean up test."""
        await self.test._teardown()

    async def wait_for_condition(self, condition, timeout=1.0):
        """Wait for condition to be true."""
        start = asyncio.get_event_loop().time()
        while asyncio.get_event_loop().time() - start < timeout:
            if await condition():
                return True
            await asyncio.sleep(0.01)
        return False

    async def click_and_wait(self, selector: str, delay=0.1):
        """Click selector and wait."""
        await self.test.pilot.click(selector)
        await asyncio.sleep(delay)

    async def type_and_wait(self, text: str, into: str, delay=0.1):
        """Type text and wait."""
        await self.test.pilot.type(text, into=into)
        await asyncio.sleep(delay)

class TestDataFactory:
    """Factory for test data."""

    @staticmethod
    def create_user(id: int = 1, name: str = "Test User", email: str = None):
        """Create test user."""
        if email is None:
            email = f"user{id}@example.com"
        return {
            "id": id,
            "name": name,
            "email": email,
            "active": True,
        }

    @staticmethod
    def create_users(count: int = 10):
        """Create multiple test users."""
        return [TestDataFactory.create_user(i) for i in range(1, count + 1)]

    @staticmethod
    def create_todo(id: int = 1, title: str = "Test Todo", completed: bool = False):
        """Create test todo."""
        return {
            "id": id,
            "title": title,
            "completed": completed,
            "created_at": "2024-01-01T00:00:00",
        }

# Usage in tests
# tests/test_with_helpers.py
import pytest
from tests.helpers import TestHelper, TestDataFactory

async def test_with_helpers():
    """Test using custom helpers."""
    app = MyApp()
    helper = TestHelper(app)

    try:
        await helper.setup()

        # Use helper methods
        await helper.click_and_wait("#button")
        await helper.type_and_wait("test", "#input")

        # Verify
        assert app.state == "expected"

    finally:
        await helper.cleanup()
```

### Mocking and Stubbing

```python
# tests/mocks.py
from unittest.mock import AsyncMock, MagicMock
import pytest

class MockApiService:
    """Mock API service."""

    def __init__(self):
        self.fetch_user = AsyncMock(return_value={"id": 1, "name": "Mock User"})
        self.save_user = AsyncMock(return_value=True)
        self.delete_user = AsyncMock(return_value=True)

    async def fetch_users(self):
        """Fetch users."""
        return [
            {"id": 1, "name": "User 1"},
            {"id": 2, "name": "User 2"},
        ]

class MockDatabase:
    """Mock database."""

    def __init__(self):
        self.data = {}
        self.save = MagicMock()
        self.load = MagicMock(return_value=self.data)

class MockEventBus:
    """Mock event bus."""

    def __init__(self):
        self.events = []
        self.publish = MagicMock()
        self.subscribe = MagicMock()

    def publish_event(self, event_type: str, data: Any):
        """Publish event."""
        self.events.append({"type": event_type, "data": data})

# Usage
# tests/test_with_mocks.py
async def test_api_integration():
    """Test with mocked API."""
    api = MockApiService()

    # Use mock in app
    user = await api.fetch_user()
    assert user["name"] == "Mock User"

    await api.save_user(user)
    assert api.save_user.called
```

## Test Patterns

### Page Object Pattern

```python
# tests/pages.py
from textual.widgets import Button, Input
from textual.containers import Vertical

class LoginPage:
    """Page object for login page."""

    def __init__(self, app):
        self.app = app
        self.username_input = app.query_one("#username", Input)
        self.password_input = app.query_one("#password", Input)
        self.login_button = app.query_one("#login", Button)
        self.error_message = app.query_one("#error", Input)

    async def login(self, username: str, password: str):
        """Perform login."""
        await self.app.run_test() as pilot:
            await pilot.type(username, into="#username")
            await pilot.type(password, into="#password")
            await pilot.click("#login")

    def get_error(self) -> str:
        """Get error message."""
        return str(self.error_message.renderable)

class DashboardPage:
    """Page object for dashboard."""

    def __init__(self, app):
        self.app = app
        self.welcome_label = app.query_one("#welcome", Button)

    def get_welcome_text(self) -> str:
        """Get welcome text."""
        return str(self.welcome_label.renderable)

# Usage
# tests/test_pages.py
async def test_login_flow():
    """Test login flow using page objects."""
    app = LoginApp()
    async with app.run_test() as pilot:
        login_page = LoginPage(app)

        # Perform login
        await login_page.login("testuser", "password123")

        # Verify login
        assert login_page.get_error() == ""

    # Check dashboard
    async with DashboardApp().run_test() as pilot:
        dashboard = DashboardPage(pilot.app)
        assert "Welcome" in dashboard.get_welcome_text()
```

### Behavior-Driven Testing

```python
# tests/test_bdd.py
from behave import given, when, then
from textual.app import App

class CalculatorApp(App):
    """Calculator app for BDD testing."""

    def __init__(self):
        super().__init__()
        self.display = "0"
        self.previous_value = 0
        self.operation = None

    def compose(self):
        yield Button("1", id="btn-1")
        yield Button("2", id="btn-2")
        yield Button("+", id="btn-plus")
        yield Button("=", id="btn-equals")
        yield Static("", id="display")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        # Calculator logic
        pass

# features/calculator.feature
Feature: Calculator
  Basic calculator operations

  Scenario: Add two numbers
    Given I have a calculator
    When I press 1
    And I press +
    And I press 2
    And I press =
    Then the display should show 3

# features/steps/calculator_steps.py
from behave import given, when, then

@given("I have a calculator")
def step_given_calculator(context):
    context.app = CalculatorApp()
    context.pilot = context.app.run_test()

@when("I press {number}")
def step_when_press_number(context, number):
    context.pilot.click(f"#btn-{number}")

@when("I press {operator}")
def step_when_press_operator(context, operator):
    if operator == "+":
        context.pilot.click("#btn-plus")
    elif operator == "=":
        context.pilot.click("#btn-equals")

@then("the display should show {expected}")
def step_then_display_shows(context, expected):
    display = context.app.query_one("#display", Static)
    assert str(display.renderable) == expected
```

## Test Configuration

### Pytest Configuration

```ini
# pytest.ini
[tool:pytest]
testpaths = tests
python_files = test_*.py *_test.py
python_classes = Test*
python_functions = test_*
addopts =
    -v
    --tb=short
    --strict-markers
    --disable-warnings
    --color=yes
markers =
    slow: marks tests as slow (deselect with '-m "not slow"')
    snapshot: marks tests as snapshot tests
    integration: marks tests as integration tests
    unit: marks tests as unit tests
```

### Fixture Configuration

```python
# tests/fixtures.py
import pytest
from textual.app import App

@pytest.fixture(scope="session")
def event_loop():
    """Create event loop for session."""
    import asyncio
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture
def sample_app():
    """Sample app for testing."""
    class SampleApp(App):
        def compose(self):
            yield Button("Test")
    return SampleApp()

@pytest.fixture(params=["dark", "light"])
def theme(request):
    """Test with different themes."""
    return request.param
```

## Best Practices

### 1. Test Structure

```python
# Good: Well-structured test
class TestFeature:
    """Test feature name."""

    @pytest.fixture
    async def setup_app(self):
        """Setup for each test."""
        app = MyApp()
        async with app.run_test() as pilot:
            yield pilot

    async def test_scenario_1(self, setup_app):
        """Test scenario 1."""
        # Arrange
        pilot = setup_app

        # Act
        await pilot.click("#button")

        # Assert
        assert app.state == "expected"

    async def test_scenario_2(self, setup_app):
        """Test scenario 2."""
        # Test code
```

### 2. Test Naming

```python
# Good: Descriptive test names
async def test_user_can_login_with_valid_credentials():
    """Test user login with valid credentials."""
    pass

async def test_user_cannot_login_with_invalid_password():
    """Test user login fails with invalid password."""
    pass

async def test_display_updates_when_counter_increments():
    """Test display updates when counter increments."""
    pass

# Avoid: Unclear test names
async def test_login_1():
    pass

async def test_counter():
    pass
```

### 3. Test Isolation

```python
# Good: Isolated test
async def test_increments_count():
    """Test increments count."""
    app = CounterApp()
    async with app.run_test() as pilot:
        initial = app.count
        await pilot.click("#increment")
        assert app.count == initial + 1

# Avoid: Tests affecting each other
counter_app = None

async def test_increment_1():
    global counter_app
    counter_app = CounterApp()
    # Test modifies global state

async def test_increment_2():
    global counter_app
    # Relies on previous test
```

### 4. Assertion Messages

```python
# Good: Clear assertions
def test_button_enabled():
    """Test button enabled state."""
    button = Button("Test", disabled=False)
    assert button.disabled is False, "Button should be enabled"

def test_display_value():
    """Test display shows correct value."""
    display = Static("42")
    assert str(display.renderable) == "42", f"Expected '42', got '{display.renderable}'"

# Avoid: Unclear assertions
def test_button():
    assert button.disabled  # What does this mean?
```

### 5. Cleanup

```python
# Good: Proper cleanup
async def test_with_timers():
    """Test with timers."""
    app = TimerApp()
    async with app.run_test() as pilot:
        app.start_timer()

        # Wait for timer
        await asyncio.sleep(0.1)

        # Timer automatically cleaned up

# Or explicit cleanup
def test_manual_cleanup():
    """Test with manual cleanup."""
    timer = Timer()
    try:
        timer.start()
        # Test code
    finally:
        timer.stop()
```

### 6. Use Markers

```python
# Good: Mark tests appropriately
@pytest.mark.slow
async def test_large_dataset():
    """Test with large dataset."""
    pass

@pytest.mark.integration
async def test_full_workflow():
    """Test complete workflow."""
    pass

@pytest.mark.unit
async def test_widget_unit():
    """Test widget unit."""
    pass
```

### 7. Property-Based Testing

```python
# tests/test_property_based.py
from hypothesis import given, strategies as st
from textual.widgets import Button

@given(st.text(min_size=1, max_size=100))
async def test_button_label(text):
    """Test button with various labels."""
    button = Button(text)
    assert button.label == text

@given(st.integers(min_value=1, max_value=100))
async def test_counter(value):
    """Test counter with various values."""
    app = CounterApp()
    app.count = value
    app.increment()
    assert app.count == value + 1
```

## See Also

- [Textual Testing Documentation](https://textual.textualize.dev/guide/testing/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Textual Events Handling](textual-events-handling.md)
- [Textual Data Binding](textual-data-binding.md)
