"""
Skill: Events and Messages

Master Textual's event system, message handlers, and the @on decorator.
"""

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Button, Input, Label
from textual.containers import Container, Vertical
from textual.message import Message
from textual import on, events


# ============================================================================
# BASIC EVENT HANDLING
# ============================================================================

class BasicEventsApp(App):
    """Demonstrates basic event handling."""

    CSS = """
    Container {
        padding: 1;
        height: auto;
    }

    #log {
        height: 15;
        border: solid green;
        padding: 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Button("Click Me!", id="my_button"),
            Input(placeholder="Type something...", id="my_input"),
            Static("", id="log"),
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press events."""
        log = self.query_one("#log", Static)
        log.update(f"Button clicked: {event.button.id}\nTime: {event.time}")

    def on_input_changed(self, event: Input.Changed) -> None:
        """Handle input change events."""
        log = self.query_one("#log", Static)
        log.update(f"Input changed: {event.value}")

    def on_input_submitted(self, event: Input.Submitted) -> None:
        """Handle input submission (Enter key)."""
        log = self.query_one("#log", Static)
        log.update(f"Input submitted: {event.value}")


# ============================================================================
# @ON DECORATOR
# ============================================================================

class OnDecoratorApp(App):
    """Demonstrates the @on decorator for event handling."""

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Button("Primary", id="primary", variant="primary"),
            Button("Success", id="success", variant="success"),
            Button("Error", id="error", variant="error"),
            Static("", id="output"),
        )
        yield Footer()

    @on(Button.Pressed, "#primary")
    def handle_primary(self) -> None:
        """Handle primary button - @on decorator with selector."""
        self.query_one("#output", Static).update("Primary clicked!")

    @on(Button.Pressed, "#success")
    def handle_success(self) -> None:
        """Handle success button."""
        self.query_one("#output", Static).update("Success clicked!")

    @on(Button.Pressed, "#error")
    def handle_error(self) -> None:
        """Handle error button."""
        self.query_one("#output", Static).update("Error clicked!")


# ============================================================================
# CUSTOM MESSAGES
# ============================================================================

from textual.widget import Widget


class ColorPicker(Widget):
    """A custom widget that posts a ColorSelected message."""

    class ColorSelected(Message):
        """Posted when a color is selected."""

        def __init__(self, color: str) -> None:
            self.color = color
            super().__init__()

    DEFAULT_CSS = """
    ColorPicker {
        height: auto;
        padding: 1;
    }

    ColorPicker Button {
        margin: 0 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Label("Choose a color:")
        yield Container(
            Button("Red", id="red", variant="error"),
            Button("Green", id="green", variant="success"),
            Button("Blue", id="blue", variant="primary"),
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Post ColorSelected message when button clicked."""
        color = event.button.id
        self.post_message(self.ColorSelected(color))


class CustomMessageApp(App):
    """App using custom widget with custom messages."""

    CSS = """
    #display {
        height: 5;
        content-align: center middle;
        margin: 1;
        border: solid white;
    }

    #display.red { background: red; }
    #display.green { background: green; }
    #display.blue { background: blue; }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield ColorPicker()
        yield Static("No color selected", id="display")
        yield Footer()

    def on_color_picker_color_selected(self, event: ColorPicker.ColorSelected) -> None:
        """Handle ColorSelected message from ColorPicker widget."""
        display = self.query_one("#display", Static)
        display.update(f"Selected: {event.color}")
        display.remove_class("red", "green", "blue")
        display.add_class(event.color)


# ============================================================================
# MESSAGE BUBBLING
# ============================================================================

class ChildWidget(Widget):
    """Child widget that posts messages."""

    class Clicked(Message):
        """Posted when child is clicked."""
        pass

    def compose(self) -> ComposeResult:
        yield Button("Click Child Widget")

    def on_button_pressed(self) -> None:
        """Post message that bubbles up."""
        self.post_message(self.Clicked())


class ParentWidget(Widget):
    """Parent widget that contains children."""

    class ChildClicked(Message):
        """Posted when any child is clicked."""
        pass

    def compose(self) -> ComposeResult:
        yield Label("Parent Widget:")
        yield ChildWidget()
        yield ChildWidget()

    def on_child_widget_clicked(self, event: ChildWidget.Clicked) -> None:
        """Handle child clicked event and re-post."""
        # Stop event from bubbling further
        event.stop()
        # Post our own message
        self.post_message(self.ChildClicked())


class BubblingApp(App):
    """Demonstrates message bubbling."""

    def compose(self) -> ComposeResult:
        yield Header()
        yield ParentWidget()
        yield Static("", id="status")
        yield Footer()

    def on_parent_widget_child_clicked(self, event: ParentWidget.ChildClicked) -> None:
        """Handle message that bubbled up through hierarchy."""
        status = self.query_one("#status", Static)
        status.update("Child was clicked (bubbled to App)!")


# ============================================================================
# KEYBOARD EVENTS
# ============================================================================

class KeyEventsApp(App):
    """Demonstrates keyboard event handling."""

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("", id="key_display")
        yield Static("Press any key or combination", id="help")
        yield Footer()

    def on_key(self, event: events.Key) -> None:
        """Handle any key press."""
        display = self.query_one("#key_display", Static)
        display.update(
            f"Key: {event.key}\n"
            f"Character: {event.character}\n"
            f"Ctrl: {event.ctrl}\n"
            f"Shift: {event.shift}\n"
            f"Alt: {event.alt}"
        )


# ============================================================================
# MOUSE EVENTS
# ============================================================================

class MouseEventsApp(App):
    """Demonstrates mouse event handling."""

    CSS = """
    #mouse_area {
        width: 100%;
        height: 20;
        background: $panel;
        border: solid $primary;
    }

    #mouse_info {
        height: 10;
        padding: 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Mouse Area\n\nClick, move, and scroll here", id="mouse_area")
        yield Static("", id="mouse_info")
        yield Footer()

    def on_mouse_move(self, event: events.MouseMove) -> None:
        """Handle mouse movement."""
        info = self.query_one("#mouse_info", Static)
        info.update(f"Mouse position: ({event.x}, {event.y})\nButton: {event.button}")

    def on_click(self, event: events.Click) -> None:
        """Handle mouse clicks."""
        info = self.query_one("#mouse_info", Static)
        info.update(
            f"Clicked at: ({event.x}, {event.y})\n"
            f"Button: {event.button}\n"
            f"Ctrl: {event.ctrl}\n"
            f"Shift: {event.shift}"
        )

    def on_mouse_scroll_down(self, event: events.MouseScrollDown) -> None:
        """Handle scroll down."""
        self.notify("Scrolled down")

    def on_mouse_scroll_up(self, event: events.MouseScrollUp) -> None:
        """Handle scroll up."""
        self.notify("Scrolled up")


# ============================================================================
# FOCUS EVENTS
# ============================================================================

class FocusEventsApp(App):
    """Demonstrates focus events."""

    CSS = """
    Container {
        padding: 1;
        height: auto;
    }

    Input {
        margin: 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Input(placeholder="Field 1", id="field1"),
            Input(placeholder="Field 2", id="field2"),
            Input(placeholder="Field 3", id="field3"),
            Static("", id="focus_log"),
        )
        yield Footer()

    def on_input_focused(self, event: Input.Focused) -> None:
        """Called when an input gains focus."""
        log = self.query_one("#focus_log", Static)
        log.update(f"Focused: {event.input.placeholder}")

    def on_input_blurred(self, event: Input.Blurred) -> None:
        """Called when an input loses focus."""
        log = self.query_one("#focus_log", Static)
        log.update(f"Blurred: {event.input.placeholder}")


# ============================================================================
# MOUNT/UNMOUNT EVENTS
# ============================================================================

class LifecycleEventsApp(App):
    """Demonstrates lifecycle events."""

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("", id="log")
        yield Button("Toggle Widget", id="toggle")
        yield Container(id="container")
        yield Footer()

    def on_mount(self) -> None:
        """Called when app is mounted."""
        log = self.query_one("#log", Static)
        log.update("App mounted")

    def on_button_pressed(self) -> None:
        """Toggle a widget to show mount/unmount."""
        container = self.query_one("#container", Container)
        if container.children:
            widget = container.children[0]
            widget.remove()
        else:
            container.mount(Static("Dynamic Widget"))

    def on_descendant_mounted(self, event: events.DescendantMounted) -> None:
        """Called when any descendant is mounted."""
        if isinstance(event.widget, Static) and event.widget.id != "log":
            log = self.query_one("#log", Static)
            log.update(f"Widget mounted: {event.widget}")

    def on_descendant_unmounted(self, event: events.DescendantUnmounted) -> None:
        """Called when any descendant is unmounted."""
        if isinstance(event.widget, Static) and event.widget.id != "log":
            log = self.query_one("#log", Static)
            log.update(f"Widget unmounted: {event.widget}")


# ============================================================================
# EVENT GUIDE AND HELPERS
# ============================================================================

EVENTS_GUIDE = """
EVENTS AND MESSAGES GUIDE
=========================

EVENT HANDLER NAMING:
  on_<event_name>(event)
  on_<widget>_<message>(event)

Examples:
  on_button_pressed()
  on_input_changed()
  on_key()
  on_mouse_move()

@ON DECORATOR:
  @on(Event)                    # Any instance
  @on(Event, "#id")            # Specific ID
  @on(Event, ".class")         # Specific class
  @on(Event, "Widget")         # Widget type

COMMON EVENTS:

Keyboard:
  - on_key(event)              Any key
  - on_key.ctrl_c()           Specific key combo
  - event.key                  Key name
  - event.character           Character typed
  - event.ctrl, .shift, .alt  Modifiers

Mouse:
  - on_click(event)           Click
  - on_mouse_move(event)      Movement
  - on_mouse_scroll_up()      Scroll up
  - on_mouse_scroll_down()    Scroll down

Focus:
  - on_focus(event)           Gain focus
  - on_blur(event)            Lose focus

Lifecycle:
  - on_mount()                Widget mounted
  - on_unmount()              Widget removed
  - on_descendant_mounted()   Child mounted
  - on_descendant_unmounted() Child removed

Widget-specific:
  - on_button_pressed()
  - on_input_changed()
  - on_input_submitted()
  - on_checkbox_changed()
  - on_select_changed()

CUSTOM MESSAGES:

Define:
  class MyMessage(Message):
      def __init__(self, data):
          self.data = data
          super().__init__()

Post:
  self.post_message(MyMessage("value"))

Handle:
  def on_my_widget_my_message(self, event):
      print(event.data)

MESSAGE BUBBLING:
  - Messages bubble up the DOM
  - event.stop() prevents bubbling
  - event.prevent_default() cancels action

EVENT PROPERTIES:
  - event.time          When event occurred
  - event.widget        Widget that posted
  - event.sender        Original sender
  - event.is_stopped    Stopped from bubbling

BEST PRACTICES:
1. Use @on for clarity
2. Stop events when handled
3. Use custom messages for widget communication
4. Name messages clearly
5. Include relevant data in messages
6. Document message contracts
7. Handle errors in handlers
8. Don't block in handlers (use workers)
"""


def create_event_handler_template(event_type: str) -> str:
    """Generate event handler template."""
    templates = {
        "button": """@on(Button.Pressed, "#my_button")
def handle_button(self) -> None:
    \"\"\"Handle button press.\"\"\"
    self.notify("Button clicked!")
""",
        "input": """def on_input_changed(self, event: Input.Changed) -> None:
    \"\"\"Handle input changes.\"\"\"
    value = event.value
    # Process value

def on_input_submitted(self, event: Input.Submitted) -> None:
    \"\"\"Handle input submission.\"\"\"
    value = event.value
    # Submit value
""",
        "keyboard": """def on_key(self, event: events.Key) -> None:
    \"\"\"Handle keyboard input.\"\"\"
    if event.key == "enter":
        # Handle Enter
        pass
    elif event.ctrl and event.key == "s":
        # Handle Ctrl+S
        pass
""",
        "mouse": """def on_click(self, event: events.Click) -> None:
    \"\"\"Handle mouse clicks.\"\"\"
    x, y = event.x, event.y
    # Handle click at position

def on_mouse_move(self, event: events.MouseMove) -> None:
    \"\"\"Handle mouse movement.\"\"\"
    # Track mouse position
""",
        "custom": """# Define custom message
class MyWidget(Widget):
    class ValueChanged(Message):
        def __init__(self, value: str) -> None:
            self.value = value
            super().__init__()

    def some_method(self) -> None:
        # Post message
        self.post_message(self.ValueChanged("new value"))

# Handle in parent
def on_my_widget_value_changed(self, event: MyWidget.ValueChanged) -> None:
    print(f"Value changed: {event.value}")
""",
    }
    return templates.get(event_type, "# Template not found")


if __name__ == "__main__":
    app = OnDecoratorApp()
    app.run()
