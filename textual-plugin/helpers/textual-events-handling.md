# textual-events-handling

Textual event system, message handling, action patterns, and event-driven architecture for Textual applications.

## Overview

Textual uses an event-driven architecture built on message passing. Understanding this system is crucial for building interactive TUI applications with proper user feedback and state management.

## Event System Fundamentals

### Event-Driven Architecture

```python
from textual.app import App
from textual.widgets import Button
from textual.message import Message

class MyApp(App):
    """Event-driven Textual app."""

    def compose(self):
        yield Button("Click Me", id="click-btn")

    # Event handler
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        self.log(f"Button {event.button.id} was pressed!")

    # Alternatively, use specific handler
    def on_button_pressed_click_btn(self, event: Button.Pressed) -> None:
        """Handle specific button by ID."""
        self.log(f"Click button pressed!")
```

### Message Base Class

```python
from textual.message import Message

class CustomEvent(Message):
    """Custom event class."""

    def __init__(self, data: str):
        self.data = data
        super().__init__()

    class Avaliable:
        pass  # Event types

# Emit custom event
widget.post_message(CustomEvent("Hello"))

# Handle custom event
def on_custom_event(self, event: CustomEvent) -> None:
    print(f"Received: {event.data}")
```

## Event Types

### Built-in Events

```python
# Widget lifecycle events
def on_mount(self) -> None:
    """Widget added to DOM."""

def on_unmount(self) -> None:
    """Widget removed from DOM."""

# Focus events
def on_focus(self, event) -> None:
    """Widget received focus."""

def on_blur(self, event) -> None:
    """Widget lost focus."""

# Keyboard events
def on_key(self, event) -> None:
    """Key pressed while widget has focus."""

def on_key_variant(self, event) -> None:
    """Special key pressed (arrow keys, function keys, etc.)."""

# Mouse events
def on_click(self, event) -> None:
    """Mouse clicked on widget."""

def on_mouse_move(self, event) -> None:
    """Mouse moved over widget."""

def on_mouse_up(self, event) -> None:
    """Mouse button released."""

def on_mouse_down(self, event) -> None:
    """Mouse button pressed."""

def on_enter(self, event) -> None:
    """Mouse entered widget area."""

def on_leave(self, event) -> None:
    """Mouse left widget area."""

# Scroll events
def on_scroll(self, event) -> None:
    """Widget scrolled."""

def on_scroll_y(self, event) -> None:
    """Vertical scroll."""

def on_scroll_x(self, event) -> None:
    """Horizontal scroll."""

# Timer events
def on_timer(self, event) -> None:
    """Timer event (created with set_interval or set_timer)."""

# Screen events
def on_screen_resume(self, event) -> None:
    """Screen became active."""

def on_screen_suspend(self, event) -> None:
    """Screen became inactive."""
```

### Widget-Specific Events

```python
# Button events
def on_button_pressed(self, event: Button.Pressed) -> None:
    """Button clicked."""

# Input events
def on_input_changed(self, event: Input.Changed) -> None:
    """Input value changed."""
    print(f"New value: {event.value}")

def on_input_submitted(self, event: Input.Submitted) -> None:
    """Input submitted (Enter pressed)."""

# TextArea events
def on_text_area_changed(self, event: TextArea.Changed) -> None:
    """TextArea content changed."""

def on_text_area_submitted(self, event: TextArea.Submitted) -> None:
    """TextArea submitted."""

# DataTable events
def on_data_table_row_selected(self, event: DataTable.RowSelected) -> None:
    """Table row selected."""

def on_data_table_cell_selected(self, event: DataTable.CellSelected) -> None:
    """Table cell selected."""

# Tab events
def on_tabs_tab_changed(self, event: Tabs.TabChanged) -> None:
    """Tab changed."""
    print(f"New tab: {event.tab.id}")

# Switch events
def on_switch_changed(self, event: Switch.Changed) -> None:
    """Switch toggled."""
    print(f"Switch value: {event.value}")

# Checkbox events
def on_checkbox_changed(self, event: Checkbox.Changed) -> None:
    """Checkbox toggled."""

# Select events
def on_select_changed(self, event: Select.Busy) -> None:
    """Select value changed."""
    print(f"Selected: {event.value}")
```

## Event Handling Patterns

### Direct Event Handling

```python
class MyApp(App):
    """App with direct event handling."""

    def compose(self):
        yield Button("Save", id="save-btn")
        yield Button("Cancel", id="cancel-btn")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle all button presses."""
        if event.button.id == "save-btn":
            self.save_data()
        elif event.button.id == "cancel-btn":
            self.cancel_action()
```

### Specific Event Handlers

```python
class MyApp(App):
    """App with specific event handlers."""

    def compose(self):
        yield Button("Save", id="save-btn")
        yield Button("Cancel", id="cancel-btn")

    def on_button_pressed_save_btn(self, event: Button.Pressed) -> None:
        """Handle save button specifically."""
        self.save_data()

    def on_button_pressed_cancel_btn(self, event: Button.Pressed) -> None:
        """Handle cancel button specifically."""
        self.cancel_action()
```

### Event Filtering

```python
def on_key(self, event) -> None:
    """Filter specific keys."""
    # Only handle Enter and Escape
    if event.key == "enter":
        self.submit_form()
    elif event.key == "escape":
        self.cancel_form()
    # Ignore all other keys
    return

# Filter by modifier keys
def on_key(self, event) -> None:
    """Filter by modifiers."""
    if event.key == "s" and event.ctrl:
        self.save()
    elif event.key == "q" and event.ctrl:
        self.quit()
```

## Custom Messages and Events

### Creating Custom Messages

```python
from textual.message import Message

class DataLoaded(Message):
    """Message emitted when data finishes loading."""

    def __init__(self, data: dict):
        self.data = data
        super().__init__()

class StatusUpdate(Message):
    """Message for status updates."""

    def __init__(self, status: str):
        self.status = status
        super().__init__()

class UserAction(Message):
    """Generic user action message."""

    def __init__(self, action_type: str, data=None):
        self.action_type = action_type
        self.data = data
        super().__init__()
```

### Emitting Custom Messages

```python
class DataWidget(Widget):
    """Widget that emits custom messages."""

    def load_data(self):
        """Load data and emit message."""
        data = {"name": "Test", "value": 42}
        # Emit custom message to parent
        self.post_message(DataLoaded(data))

class StatusWidget(Widget):
    """Widget that provides status updates."""

    def update_status(self, status: str):
        """Update status and notify."""
        self.post_message(StatusUpdate(status))

# Emit from anywhere
def trigger_action(self, action_type: str):
    self.post_message(UserAction(action_type, {"timestamp": time.time()}))
```

### Handling Custom Messages

```python
class MyApp(App):
    """App that handles custom messages."""

    def compose(self):
        yield DataWidget()
        yield StatusWidget()

    def on_data_loaded(self, event: DataLoaded) -> None:
        """Handle data loaded event."""
        print(f"Data loaded: {event.data}")

    def on_status_update(self, event: StatusUpdate) -> None:
        """Handle status update event."""
        print(f"Status: {event.status}")

    def on_user_action(self, event: UserAction) -> None:
        """Handle user action event."""
        print(f"Action: {event.action_type}")
        if event.data:
            print(f"Data: {event.data}")
```

## Event Propagation

### Stopping Event Propagation

```python
def on_button_pressed(self, event: Button.Pressed) -> None:
    """Handle button and stop propagation."""
    self.log("Button pressed!")
    # Stop event from bubbling up to parent widgets
    event.stop()

def on_key(self, event) -> None:
    """Handle key globally but stop after."""
    if event.key == "q":
        self.quit()
        # Don't let other widgets handle 'q'
        event.stop()
```

### Event Bubbling

```python
from textual.containers import Container
from textual.widgets import Button

class MyContainer(Container):
    """Container that handles child events."""

    def compose(self):
        yield Button("Child Button", id="child-btn")

    def on_button_pressed_child_btn(self, event: Button.Pressed) -> None:
        """Handle child's button press."""
        self.log("Container received button event from child")

class MyApp(App):
    """App demonstrating event bubbling."""

    def compose(self):
        yield MyContainer()

    def on_button_pressed_child_btn(self, event: Button.Pressed) -> None:
        """App also receives the event (bubbled up)."""
        self.log("App received button event")
```

### Preventing Default Behavior

```python
def on_key(self, event) -> None:
    """Override default key behavior."""
    if event.key == "q":
        # Custom quit behavior
        self.confirm_quit()
        # Prevent default 'q' behavior
        event.prevent_default()
```

## Timer Events

### Creating Timers

```python
class TimedApp(App):
    """App with timer events."""

    def compose(self):
        yield Static("Timer: 0", id="timer-display")

    def on_mount(self) -> None:
        """Start timer when app mounts."""
        self.count = 0
        # Update every second
        self.set_interval(1.0, self.update_timer)

    def update_timer(self) -> None:
        """Update timer display."""
        self.count += 1
        display = self.query_one("#timer-display", Static)
        display.update(f"Timer: {self.count}")

    def on_unmount(self) -> None:
        """Clean up timers."""
        # Timers are automatically cleaned up, but you can stop explicitly
        for timer in self.timers:
            timer.stop()
```

### One-Time Timers

```python
class DelayedApp(App):
    """App with delayed actions."""

    def compose(self):
        yield Button("Delayed Action", id="delayed-btn")

    def on_button_pressed_delayed_btn(self, event: Button.Pressed) -> None:
        """Start delayed action."""
        # Show "loading" state
        self.query_one("#delayed-btn", Button).disabled = True
        # Schedule actual action
        self.set_timer(2.0, self.perform_action)

    def perform_action(self) -> None:
        """Perform the delayed action."""
        self.query_one("#delayed-btn", Button).disabled = False
        self.bell()  # Notify user
```

### Multiple Timers

```python
class MultiTimerApp(App):
    """App with multiple timers."""

    def compose(self):
        yield Static("", id="clock")
        yield Static("", id="stopwatch")

    def on_mount(self) -> None:
        self.stopwatch_seconds = 0

        # Real-time clock (every 1 second)
        self.set_interval(1.0, self.update_clock)

        # Stopwatch (every 0.1 seconds)
        self.set_interval(0.1, self.update_stopwatch)

    def update_clock(self) -> None:
        """Update clock display."""
        import datetime
        now = datetime.datetime.now()
        clock = self.query_one("#clock", Static)
        clock.update(f"Clock: {now.strftime('%H:%M:%S')}")

    def update_stopwatch(self) -> None:
        """Update stopwatch display."""
        self.stopwatch_seconds += 0.1
        stopwatch = self.query_one("#stopwatch", Static)
        stopwatch.update(f"Stopwatch: {self.stopwatch_seconds:.1f}s")
```

## Async Event Handling

### Async Event Handlers

```python
import asyncio

class AsyncApp(App):
    """App with async event handlers."""

    def compose(self):
        yield Button("Load Data", id="load-btn")
        yield Static("", id="status")

    async def on_button_pressed_load_btn(self, event: Button.Pressed) -> None:
        """Async event handler."""
        # Update UI to show loading
        status = self.query_one("#status", Static)
        status.update("Loading...")

        # Disable button during loading
        button = event.button
        button.disabled = True

        try:
            # Perform async operation
            data = await self.fetch_data()
            status.update(f"Loaded: {data}")
        except Exception as e:
            status.update(f"Error: {e}")
        finally:
            # Re-enable button
            button.disabled = False

    async def fetch_data(self) -> str:
        """Simulate async data fetch."""
        await asyncio.sleep(2)  # Simulate network delay
        return "Data loaded successfully"
```

### Async Timer Callbacks

```python
class AsyncTimerApp(App):
    """App with async timer callbacks."""

    def compose(self):
        yield Static("", id="progress")

    def on_mount(self) -> None:
        # Async timer callback
        self.set_timer(0.1, self.async_progress_update)

    async def async_progress_update(self) -> None:
        """Async callback for progress updates."""
        progress = 0
        while progress < 100:
            progress += 1
            display = self.query_one("#progress", Static)
            display.update(f"Progress: {progress}%")
            await asyncio.sleep(0.1)  # Non-blocking delay

        display.update("Complete!")
```

## Event State Management

### Using Reactive Properties

```python
from textual.reactive import reactive

class StatefulApp(App):
    """App using reactive properties."""

    # Reactive property
    count = reactive(0)

    def compose(self):
        yield Button("Increment", id="inc-btn")
        yield Button("Decrement", id="dec-btn")
        yield Static("0", id="count-display")

    def watch_count(self, value: int) -> None:
        """Called when count changes."""
        display = self.query_one("#count-display", Static)
        display.update(str(value))

    def on_button_pressed_inc_btn(self, event: Button.Pressed) -> None:
        """Increment count."""
        self.count += 1

    def on_button_pressed_dec_btn(self, event: Button.Pressed) -> None:
        """Decrement count."""
        self.count -= 1
```

### Event-Driven State Updates

```python
class StateManager:
    """Centralized state management."""

    def __init__(self):
        self.state = {
            "user": None,
            "is_loading": False,
            "data": [],
            "error": None,
        }
        self.listeners = []

    def set_state(self, key, value):
        """Update state and notify listeners."""
        self.state[key] = value
        self.notify_listeners()

    def subscribe(self, listener):
        """Subscribe to state changes."""
        self.listeners.append(listener)

    def notify_listeners(self):
        """Notify all listeners of state change."""
        for listener in self.listeners:
            listener(self.state)

class MyApp(App):
    """App using centralized state."""

    def compose(self):
        yield Button("Load", id="load-btn")
        yield Static("", id="status")

    def on_mount(self) -> None:
        """Initialize state manager."""
        self.state_manager = StateManager()
        self.state_manager.subscribe(self.on_state_change)

    def on_state_change(self, state):
        """React to state changes."""
        if state["is_loading"]:
            self.query_one("#status", Static).update("Loading...")
        elif state["error"]:
            self.query_one("#status", Static).update(f"Error: {state['error']}")
        else:
            self.query_one("#status", Static).update("Ready")

    def on_button_pressed_load_btn(self, event: Button.Pressed) -> None:
        """Trigger data load."""
        self.state_manager.set_state("is_loading", True)

        # Simulate async operation
        self.set_timer(2.0, lambda: self.state_manager.set_state("is_loading", False))
```

## Event Debouncing and Throttling

### Debouncing Events

```python
from typing import Callable
import time

class Debouncer:
    """Event debouncer."""

    def __init__(self, delay: float, callback: Callable):
        self.delay = delay
        self.callback = callback
        self.timer = None

    def __call__(self, *args, **kwargs):
        """Debounced function call."""
        if self.timer:
            self.timer.stop()

        self.timer = self.set_timer(self.delay, lambda: self.callback(*args, **kwargs))

class SearchApp(App):
    """App with debounced search."""

    def compose(self):
        yield Input(placeholder="Search...", id="search-input")

    def on_mount(self) -> None:
        """Initialize debouncer."""
        # Debounce search by 0.5 seconds
        self.debounced_search = Debouncer(0.5, self.perform_search)

    def on_input_changed(self, event: Input.Changed) -> None:
        """Handle search input with debouncing."""
        if event.input.id == "search-input":
            self.debounced_search(event.value)

    def perform_search(self, query: str):
        """Actual search implementation."""
        if query:
            self.log(f"Searching for: {query}")
```

### Throttling Events

```python
class Throttler:
    """Event throttler."""

    def __init__(self, interval: float, callback: Callable):
        self.interval = interval
        self.callback = callback
        self.last_call = 0

    def __call__(self, *args, **kwargs):
        """Throttled function call."""
        import time
        now = time.time()
        if now - self.last_call >= self.interval:
            self.last_call = now
            self.callback(*args, **kwargs)

class MouseApp(App):
    """App with throttled mouse events."""

    def compose(self):
        yield Static("Move mouse here", id="mouse-area")

    def on_mount(self) -> None:
        """Initialize throttler."""
        # Throttle mouse events to 10 per second
        self.throttled_mouse = Throttler(0.1, self.handle_mouse_move)

    def on_mouse_move(self, event) -> None:
        """Handle mouse movement with throttling."""
        if event.widget.id == "mouse-area":
            self.throttled_mouse(event)

    def handle_mouse_move(self, event):
        """Actual mouse move handler."""
        self.log(f"Mouse at: {event.screen_x}, {event.screen_y}")
```

## Screen Events

### Screen Lifecycle

```python
from textual.screen import Screen

class CustomScreen(Screen):
    """Custom screen with lifecycle events."""

    def on_mount(self) -> None:
        """Screen mounted."""
        self.log("Screen mounted")

    def on_foreground(self) -> None:
        """Screen became active."""
        self.log("Screen in foreground")

    def on_background(self) -> None:
        """Screen became inactive."""
        self.log("Screen in background")

    def on_unmount(self) -> None:
        """Screen unmounted."""
        self.log("Screen unmounted")

class MyApp(App):
    """App with custom screen."""

    def compose(self):
        yield Button("Open Screen", id="open-btn")

    def on_button_pressed_open_btn(self, event: Button.Pressed) -> None:
        """Push custom screen."""
        self.push_screen(CustomScreen())
```

### Screen Communication

```python
class ModalScreen(Screen):
    """Modal dialog screen."""

    def __init__(self, message: str):
        super().__init__()
        self.message = message
        self.result = None

    def compose(self):
        yield Static(self.message)
        with Horizontal():
            yield Button("Yes", id="yes")
            yield Button("No", id="no")

    def on_button_pressed_yes(self, event: Button.Pressed) -> None:
        """Return success result."""
        self.result = True
        self.app.pop_screen()

    def on_button_pressed_no(self, event: Button.Pressed) -> None:
        """Return failure result."""
        self.result = False
        self.app.pop_screen()

class MyApp(App):
    """App with modal dialog."""

    def compose(self):
        yield Button("Confirm Action", id="confirm-btn")

    async def on_button_pressed_confirm_btn(self, event: Button.Pressed) -> None:
        """Show modal and wait for result."""
        def callback(result):
            if result:
                self.log("Action confirmed")
            else:
                self.log("Action cancelled")

        self.push_screen(ModalScreen("Are you sure?"), callback)
```

## Event Testing

### Testing Event Handlers

```python
from textual.testing import AppTest, press

class TestApp(App):
    """Testable app."""

    def compose(self):
        yield Button("Click Me", id="test-btn")

    def on_button_pressed_test_btn(self, event: Button.Pressed) -> None:
        """Test event handler."""
        self.clicked = True

async def test_event_handling():
    """Test event handling."""
    app = TestApp()
    async with app.run_test() as pilot:
        # Click the button
        await pilot.click("#test-btn")

        # Verify event was handled
        assert app.clicked is True

async def test_key_events():
    """Test keyboard events."""
    app = TestApp()
    async with app.run_test() as pilot:
        # Press Enter key
        await pilot.press("enter")

        # Verify key was handled
        assert app.key_pressed == "enter"
```

### Event Harness Testing

```python
def test_custom_message():
    """Test custom message handling."""
    class TestableApp(App):
        def compose(self):
            yield Button("Trigger", id="trigger")

        def on_custom_message(self, event):
            self.received = True

    app = TestableApp()
    async with app.run_test() as pilot:
        # Send custom message
        app.post_message(CustomMessage())

        # Trigger button click
        await pilot.click("#trigger")

        # Verify
        assert app.received
```

## Best Practices

### 1. Use Specific Handlers

```python
# Good: Specific handler
def on_button_pressed_save_btn(self, event: Button.Pressed) -> None:
    self.save()

# Avoid: Generic handler for multiple widgets
def on_button_pressed(self, event: Button.Pressed) -> None:
    if event.button.id == "save-btn":
        self.save()
    elif event.button.id == "cancel-btn":
        self.cancel()
```

### 2. Stop Propagation When Needed

```python
def on_key(self, event) -> None:
    """Handle global keys."""
    if event.key == "ctrl+q":
        self.quit()
        event.stop()  # Prevent other handlers
```

### 3. Clean Up Timers

```python
def on_mount(self) -> None:
    """Start timers."""
    self.timer = self.set_interval(1.0, self.tick)

def on_unmount(self) -> None:
    """Clean up timers."""
    self.timer.stop()
```

### 4. Use Async for Long Operations

```python
async def on_button_pressed_load_btn(self, event: Button.Pressed) -> None:
    """Async handler for long operations."""
    try:
        data = await self.fetch_data()
        self.update_ui(data)
    except Exception as e:
        self.show_error(e)
```

### 5. Emit Custom Messages for Complex State

```python
class DataManager:
    def load_complete(self, data):
        """Emit message instead of calling directly."""
        self.post_message(DataLoaded(data))

class UIComponent:
    def on_data_loaded(self, event: DataLoaded) -> None:
        """Handle loaded data."""
        self.display(event.data)
```

### 6. Test Event Flows

```python
async def test_complete_flow():
    """Test full user interaction flow."""
    app = MyApp()
    async with app.run_test() as pilot:
        # Simulate user actions
        await pilot.click("#button1")
        await pilot.type("hello")
        await pilot.press("enter")

        # Verify state
        assert app.state == "expected"
```

## Common Event Patterns

### Command Pattern

```python
class Command:
    """Command interface."""

    def execute(self):
        pass

    def undo(self):
        pass

class ClickCommand(Command):
    """Command for button clicks."""

    def __init__(self, app, button_id):
        self.app = app
        self.button_id = button_id

    def execute(self):
        self.app.handle_button(self.button_id)

class MyApp(App):
    """App using command pattern."""

    def __init__(self):
        super().__init__()
        self.history = []

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button with command pattern."""
        command = ClickCommand(self, event.button.id)
        command.execute()
        self.history.append(command)
```

### Observer Pattern

```python
class Observable:
    """Observable subject."""

    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify(self, event):
        for observer in self.observers:
            observer.update(event)

class MyApp(App):
    """App with observer pattern."""

    def compose(self):
        yield Button("Update", id="update")

    def on_mount(self) -> None:
        """Set up observers."""
        self.data = Observable()
        self.data.add_observer(self)

    def update(self, event):
        """React to data changes."""
        self.log(f"Received: {event}")

    def on_button_pressed_update(self, event: Button.Pressed) -> None:
        """Notify observers of update."""
        self.data.notify("Data updated")
```

## See Also

- [Textual Widgets Reference](textual-widgets-reference.md)
- [Textual Layouts Guide](textual-layouts-guide.md)
- [Textual CSS Styling](textual-css-styling.md)
- [Textual Data Binding](textual-data-binding.md)
