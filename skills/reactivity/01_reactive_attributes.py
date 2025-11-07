"""
Skill: Reactive Attributes

Master reactive programming in Textual for dynamic, responsive UIs.
"""

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Button, Input, Label
from textual.containers import Container, Horizontal
from textual.reactive import reactive, var
from textual.widget import Widget


# ============================================================================
# BASIC REACTIVE ATTRIBUTES
# ============================================================================

class Counter(Widget):
    """A counter with reactive count."""

    DEFAULT_CSS = """
    Counter {
        height: auto;
        padding: 1;
        background: $panel;
        border: solid $primary;
    }

    Counter Static {
        text-align: center;
        margin: 1;
    }
    """

    # Reactive attribute - automatically triggers updates
    count = reactive(0)

    def compose(self) -> ComposeResult:
        yield Static(f"Count: {self.count}", id="display")
        with Horizontal():
            yield Button("-", id="dec")
            yield Button("+", id="inc")

    def watch_count(self, new_value: int) -> None:
        """Called automatically when count changes."""
        display = self.query_one("#display", Static)
        display.update(f"Count: {new_value}")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button clicks."""
        if event.button.id == "inc":
            self.count += 1
        elif event.button.id == "dec":
            self.count -= 1


class ReactiveBasicsApp(App):
    """Demonstrates basic reactive attributes."""

    def compose(self) -> ComposeResult:
        yield Header()
        yield Counter()
        yield Footer()


# ============================================================================
# WATCH METHODS
# ============================================================================

class StatusWidget(Widget):
    """Widget with multiple reactive attributes."""

    DEFAULT_CSS = """
    StatusWidget {
        height: auto;
        padding: 1;
        background: $panel;
    }

    StatusWidget.online {
        border-left: thick $success;
    }

    StatusWidget.offline {
        border-left: thick $error;
    }

    StatusWidget.loading {
        border-left: thick $warning;
    }
    """

    status = reactive("offline")  # online, offline, loading
    message = reactive("")

    def compose(self) -> ComposeResult:
        yield Static(id="status_text")
        yield Static(id="message_text")

    def watch_status(self, old_status: str, new_status: str) -> None:
        """Called when status changes."""
        # Update CSS classes
        self.remove_class("online", "offline", "loading")
        self.add_class(new_status)

        # Update display
        status_text = self.query_one("#status_text", Static)
        emoji = {"online": "🟢", "offline": "🔴", "loading": "🟡"}
        status_text.update(f"{emoji.get(new_status, '⚪')} {new_status.upper()}")

        # Log transition
        self.log(f"Status changed: {old_status} -> {new_status}")

    def watch_message(self, new_message: str) -> None:
        """Called when message changes."""
        message_text = self.query_one("#message_text", Static)
        message_text.update(new_message)


class WatchMethodsApp(App):
    """Demonstrates watch methods."""

    def compose(self) -> ComposeResult:
        yield Header()
        yield StatusWidget(id="status")
        yield Horizontal(
            Button("Online", variant="success"),
            Button("Offline", variant="error"),
            Button("Loading", variant="warning"),
        )
        yield Input(placeholder="Enter message...", id="msg_input")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Change status based on button."""
        status_widget = self.query_one("#status", StatusWidget)
        status_widget.status = event.button.label.lower()

    def on_input_changed(self, event: Input.Changed) -> None:
        """Update message."""
        status_widget = self.query_one("#status", StatusWidget)
        status_widget.message = event.value


# ============================================================================
# COMPUTE METHODS
# ============================================================================

class Calculator(Widget):
    """Calculator using compute methods."""

    DEFAULT_CSS = """
    Calculator {
        height: auto;
        padding: 1;
        background: $panel;
        border: solid $primary;
    }

    Calculator Input {
        margin: 1;
    }

    Calculator Static {
        margin: 1;
        text-style: bold;
        color: $success;
    }
    """

    value1 = reactive(0)
    value2 = reactive(0)

    def compose(self) -> ComposeResult:
        yield Label("Enter two numbers:")
        yield Input(placeholder="Number 1", id="num1", type="number")
        yield Input(placeholder="Number 2", id="num2", type="number")
        yield Static("", id="sum")
        yield Static("", id="product")

    def compute_sum(self) -> int:
        """Computed reactive value."""
        return self.value1 + self.value2

    def compute_product(self) -> int:
        """Computed reactive value."""
        return self.value1 * self.value2

    def watch_sum(self, new_sum: int) -> None:
        """Update sum display."""
        self.query_one("#sum", Static).update(f"Sum: {new_sum}")

    def watch_product(self, new_product: int) -> None:
        """Update product display."""
        self.query_one("#product", Static).update(f"Product: {new_product}")

    def on_input_changed(self, event: Input.Changed) -> None:
        """Update reactive values."""
        try:
            value = int(event.value) if event.value else 0
        except ValueError:
            value = 0

        if event.input.id == "num1":
            self.value1 = value
        elif event.input.id == "num2":
            self.value2 = value


class ComputeApp(App):
    """Demonstrates compute methods."""

    def compose(self) -> ComposeResult:
        yield Header()
        yield Calculator()
        yield Footer()


# ============================================================================
# REACTIVE VALIDATION
# ============================================================================

class ValidatedInput(Widget):
    """Input with reactive validation."""

    DEFAULT_CSS = """
    ValidatedInput {
        height: auto;
        padding: 1;
    }

    ValidatedInput Input {
        margin-bottom: 1;
    }

    ValidatedInput .valid {
        color: $success;
    }

    ValidatedInput .invalid {
        color: $error;
    }
    """

    email = reactive("")
    is_valid = reactive(False)

    def compose(self) -> ComposeResult:
        yield Input(placeholder="Enter email...", id="email_input")
        yield Static("", id="validation")

    def validate_email(self, value: str) -> str:
        """Validate and sanitize email."""
        # Basic validation
        value = value.strip().lower()
        return value

    def watch_email(self, new_email: str) -> None:
        """Validate email when it changes."""
        # Simple validation
        self.is_valid = "@" in new_email and "." in new_email

    def watch_is_valid(self, valid: bool) -> None:
        """Update validation display."""
        validation = self.query_one("#validation", Static)
        if not self.email:
            validation.update("")
        elif valid:
            validation.remove_class("invalid")
            validation.add_class("valid")
            validation.update("✓ Valid email")
        else:
            validation.remove_class("valid")
            validation.add_class("invalid")
            validation.update("✗ Invalid email")

    def on_input_changed(self, event: Input.Changed) -> None:
        """Update email reactive."""
        self.email = event.value


class ValidationApp(App):
    """Demonstrates reactive validation."""

    def compose(self) -> ComposeResult:
        yield Header()
        yield ValidatedInput()
        yield Footer()


# ============================================================================
# APP-LEVEL REACTIVITY
# ============================================================================

class ReactiveApp(App):
    """App with reactive state."""

    CSS = """
    #theme_display {
        height: 10;
        content-align: center middle;
        margin: 1;
        border: solid $primary;
    }

    #counter_display {
        height: 5;
        content-align: center middle;
        margin: 1;
        background: $panel;
    }
    """

    # App-level reactive attributes
    counter = reactive(0)
    theme_name = reactive("Default")

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("", id="theme_display")
        yield Static("", id="counter_display")
        yield Horizontal(
            Button("Dark", variant="primary"),
            Button("Light", variant="success"),
            Button("+ Count", variant="warning"),
        )
        yield Footer()

    def watch_counter(self, new_count: int) -> None:
        """Update counter display."""
        display = self.query_one("#counter_display", Static)
        display.update(f"Counter: {new_count}")

    def watch_theme_name(self, new_theme: str) -> None:
        """Update theme display."""
        display = self.query_one("#theme_display", Static)
        display.update(f"Theme: {new_theme}")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        label = event.button.label.lower()
        if label == "dark":
            self.dark = True
            self.theme_name = "Dark"
        elif label == "light":
            self.dark = False
            self.theme_name = "Light"
        elif label == "+ count":
            self.counter += 1


# ============================================================================
# REACTIVE WITH INIT
# ============================================================================

class ConfigurableWidget(Widget):
    """Widget with reactive initialization."""

    DEFAULT_CSS = """
    ConfigurableWidget {
        height: 10;
        padding: 1;
        background: $panel;
        border: solid $primary;
        content-align: center middle;
    }
    """

    value = reactive(0, init=False)  # Don't call watch on init
    color = reactive("blue")

    def __init__(self, initial_value: int = 0, **kwargs):
        super().__init__(**kwargs)
        self.value = initial_value

    def watch_value(self, new_value: int) -> None:
        """Called when value changes (not on init if init=False)."""
        self.notify(f"Value changed to {new_value}")

    def render(self) -> str:
        """Render the widget."""
        return f"Value: {self.value}\nColor: {self.color}"


# ============================================================================
# REACTIVE GUIDE
# ============================================================================

REACTIVE_GUIDE = """
REACTIVE ATTRIBUTES GUIDE
========================

BASIC REACTIVE:
  class MyWidget(Widget):
      count = reactive(0)

      def watch_count(self, new_value):
          # Called when count changes
          pass

FEATURES:
- Auto-updates when assigned
- Triggers watch methods
- Type-safe
- Efficient (only updates when changed)

WATCH METHODS:
  def watch_<attribute>(self, new_value):
      # Called when attribute changes
      pass

  def watch_<attribute>(self, old_value, new_value):
      # Get both old and new values
      pass

COMPUTE METHODS:
  total = reactive(0)

  def compute_total(self) -> int:
      # Compute from other reactives
      return self.value1 + self.value2

  def watch_total(self, new_total):
      # Update UI
      pass

VALIDATION:
  email = reactive("")

  def validate_email(self, value: str) -> str:
      # Validate and return sanitized value
      return value.strip().lower()

INIT PARAMETER:
  value = reactive(0, init=False)
  # Don't call watch on initialization

  value = reactive(0, always_update=True)
  # Call watch even if value didn't change

BEST PRACTICES:
1. Use for UI state
2. Keep watch methods simple
3. Avoid side effects in compute
4. Use validate for input sanitization
5. init=False to avoid initial watch
6. Name reactives clearly
7. Document reactive behavior

COMMON PATTERNS:

Toggle:
  visible = reactive(False)

  def action_toggle(self):
      self.visible = not self.visible

Counter:
  count = reactive(0)

  def action_increment(self):
      self.count += 1

State Machine:
  state = reactive("idle")  # idle, loading, success, error

  def watch_state(self, new_state):
      if new_state == "loading":
          self.show_spinner()
      elif new_state == "success":
          self.show_success()

Computed Values:
  width = reactive(10)
  height = reactive(20)

  def compute_area(self) -> int:
      return self.width * self.height

REACTIVITY VS EVENTS:
- Reactive: For widget state
- Events: For user actions
- Use both together!

Example:
  value = reactive(0)

  def on_button_pressed(self):
      self.value += 1  # Event handler

  def watch_value(self, new_value):
      self.update_display()  # Reactive handler
"""


def create_reactive_template(widget_name: str) -> str:
    """Generate reactive widget template."""
    return f'''from textual.widget import Widget
from textual.reactive import reactive
from textual.app import ComposeResult
from textual.widgets import Static


class {widget_name}(Widget):
    """A reactive widget."""

    # Reactive attributes
    value = reactive(0)
    status = reactive("idle")

    def compose(self) -> ComposeResult:
        yield Static("", id="display")

    def watch_value(self, new_value: int) -> None:
        """Called when value changes."""
        display = self.query_one("#display", Static)
        display.update(f"Value: {{new_value}}")

    def watch_status(self, old_status: str, new_status: str) -> None:
        """Called when status changes."""
        self.log(f"Status: {{old_status}} -> {{new_status}}")

    # Computed reactive
    def compute_doubled(self) -> int:
        return self.value * 2

    def watch_doubled(self, new_doubled: int) -> None:
        self.log(f"Doubled: {{new_doubled}}")
'''


if __name__ == "__main__":
    app = ReactiveApp()
    app.run()
