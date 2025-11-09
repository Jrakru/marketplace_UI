"""
Skill: Custom Widget Development

Learn to create custom, reusable widgets with proper encapsulation.
"""

from textual.app import App, ComposeResult
from textual.widget import Widget
from textual.widgets import Static, Button, Label, Input
from textual.containers import Container, Horizontal, Vertical
from textual.reactive import reactive
from textual.message import Message
from rich.text import Text


# ============================================================================
# BASIC CUSTOM WIDGET
# ============================================================================

class Counter(Widget):
    """A simple counter widget."""

    DEFAULT_CSS = """
    Counter {
        width: 100%;
        height: auto;
        background: $panel;
        border: solid $primary;
        padding: 1;
    }

    Counter Static {
        text-align: center;
        color: $text;
    }

    Counter Horizontal {
        width: 100%;
        height: auto;
        align: center middle;
    }

    Counter Button {
        margin: 0 1;
    }
    """

    count = reactive(0)  # Reactive attribute

    def compose(self) -> ComposeResult:
        """Build the widget UI."""
        with Horizontal():
            yield Button("-", id="decrement", variant="error")
            yield Static(str(self.count), id="display")
            yield Button("+", id="increment", variant="success")

    def watch_count(self, new_count: int) -> None:
        """Called when count changes."""
        display = self.query_one("#display", Static)
        display.update(str(new_count))

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button clicks."""
        if event.button.id == "increment":
            self.count += 1
        elif event.button.id == "decrement":
            self.count -= 1


# ============================================================================
# CUSTOM WIDGET WITH MESSAGES
# ============================================================================

class UserCard(Widget):
    """A user profile card widget."""

    DEFAULT_CSS = """
    UserCard {
        width: 40;
        height: 10;
        background: $surface;
        border: solid $accent;
        padding: 1;
    }

    UserCard .name {
        text-style: bold;
        color: $accent;
    }

    UserCard .email {
        color: $text-muted;
    }

    UserCard Button {
        margin-top: 1;
    }
    """

    # Custom message
    class Selected(Message):
        """Posted when user card is selected."""

        def __init__(self, user_id: str) -> None:
            self.user_id = user_id
            super().__init__()

    def __init__(
        self,
        user_id: str,
        name: str,
        email: str,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.user_id = user_id
        self._name = name
        self._email = email

    def compose(self) -> ComposeResult:
        yield Static(self._name, classes="name")
        yield Static(self._email, classes="email")
        yield Button("View Profile", variant="primary")

    def on_button_pressed(self) -> None:
        """Post a Selected message when button is clicked."""
        self.post_message(self.Selected(self.user_id))


# ============================================================================
# COMPOSABLE WIDGET
# ============================================================================

class SearchBox(Widget):
    """A search box with button."""

    DEFAULT_CSS = """
    SearchBox {
        height: auto;
        background: $panel;
        padding: 1;
    }

    SearchBox Horizontal {
        width: 100%;
        height: auto;
    }

    SearchBox Input {
        width: 1fr;
    }

    SearchBox Button {
        margin-left: 1;
    }
    """

    class Searched(Message):
        """Posted when search is performed."""

        def __init__(self, query: str) -> None:
            self.query = query
            super().__init__()

    def __init__(self, placeholder: str = "Search...", **kwargs):
        super().__init__(**kwargs)
        self.placeholder = placeholder

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Input(placeholder=self.placeholder, id="search_input")
            yield Button("Search", variant="primary", id="search_btn")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle search button click."""
        if event.button.id == "search_btn":
            input_widget = self.query_one("#search_input", Input)
            self.post_message(self.Searched(input_widget.value))

    def on_input_submitted(self, event: Input.Submitted) -> None:
        """Handle Enter key in input."""
        self.post_message(self.Searched(event.value))

    def clear(self) -> None:
        """Clear the search input."""
        input_widget = self.query_one("#search_input", Input)
        input_widget.value = ""


# ============================================================================
# REACTIVE WIDGET
# ============================================================================

class StatusIndicator(Widget):
    """A status indicator with reactive state."""

    DEFAULT_CSS = """
    StatusIndicator {
        width: auto;
        height: auto;
        padding: 0 2;
        border-left: thick $success;
    }

    StatusIndicator.online {
        border-left: thick $success;
        background: $success 10%;
    }

    StatusIndicator.offline {
        border-left: thick $error;
        background: $error 10%;
    }

    StatusIndicator.away {
        border-left: thick $warning;
        background: $warning 10%;
    }
    """

    status = reactive("offline")  # online, offline, away

    def __init__(self, initial_status: str = "offline", **kwargs):
        super().__init__(**kwargs)
        self.status = initial_status

    def compose(self) -> ComposeResult:
        yield Static(id="status_text")

    def watch_status(self, new_status: str) -> None:
        """Update display when status changes."""
        # Update classes
        self.remove_class("online", "offline", "away")
        self.add_class(new_status)

        # Update text
        status_text = self.query_one("#status_text", Static)
        emoji = {
            "online": "🟢",
            "offline": "🔴",
            "away": "🟡"
        }.get(new_status, "⚪")
        status_text.update(f"{emoji} {new_status.upper()}")


# ============================================================================
# CONTAINER WIDGET
# ============================================================================

class Card(Widget):
    """A reusable card container."""

    DEFAULT_CSS = """
    Card {
        width: 100%;
        height: auto;
        background: $panel;
        border: round $primary;
        padding: 1 2;
    }

    Card > .card-title {
        text-style: bold;
        color: $accent;
        margin-bottom: 1;
    }

    Card > .card-content {
        color: $text;
    }
    """

    def __init__(
        self,
        title: str = "",
        *children: Widget,
        **kwargs
    ):
        super().__init__(**kwargs)
        self._title = title
        self._children = children

    def compose(self) -> ComposeResult:
        if self._title:
            yield Static(self._title, classes="card-title")

        with Vertical(classes="card-content"):
            yield from self._children


# ============================================================================
# WIDGET WITH RENDER METHOD
# ============================================================================

class Badge(Widget):
    """A badge widget using render method."""

    DEFAULT_CSS = """
    Badge {
        width: auto;
        height: 1;
        padding: 0 1;
        background: $accent;
        color: $text;
    }

    Badge.success {
        background: $success;
    }

    Badge.error {
        background: $error;
    }

    Badge.warning {
        background: $warning;
    }
    """

    text = reactive("Badge")
    variant = reactive("default")

    def __init__(
        self,
        text: str = "Badge",
        variant: str = "default",
        **kwargs
    ):
        super().__init__(**kwargs)
        self.text = text
        self.variant = variant

    def render(self) -> Text:
        """Render the badge text."""
        return Text(self.text, style="bold")

    def watch_variant(self, new_variant: str) -> None:
        """Update CSS class when variant changes."""
        self.remove_class("success", "error", "warning")
        if new_variant != "default":
            self.add_class(new_variant)


# ============================================================================
# DEMO APP
# ============================================================================

class CustomWidgetDemo(App):
    """Demonstrates custom widgets."""

    CSS = """
    Screen {
        background: $surface;
    }

    Container {
        padding: 1;
        height: auto;
    }

    #cards {
        layout: grid;
        grid-size: 2;
        grid-gutter: 1;
    }
    """

    def compose(self) -> ComposeResult:
        # Counter widget
        yield Container(
            Label("Counter Widget:"),
            Counter(),
        )

        # User cards
        yield Container(
            Label("User Cards:"),
            Horizontal(
                UserCard("user1", "Alice Smith", "alice@example.com"),
                UserCard("user2", "Bob Jones", "bob@example.com"),
                id="cards"
            ),
        )

        # Search box
        yield Container(
            Label("Search Box:"),
            SearchBox(placeholder="Search users..."),
        )

        # Status indicator
        yield Container(
            Label("Status Indicators:"),
            Horizontal(
                StatusIndicator(initial_status="online"),
                StatusIndicator(initial_status="away"),
                StatusIndicator(initial_status="offline"),
            ),
        )

        # Card container
        yield Card(
            "Example Card",
            Label("This is content inside a card"),
            Button("Action"),
        )

        # Badges
        yield Container(
            Label("Badges:"),
            Horizontal(
                Badge("Default"),
                Badge("Success", variant="success"),
                Badge("Warning", variant="warning"),
                Badge("Error", variant="error"),
            ),
        )

    def on_user_card_selected(self, event: UserCard.Selected) -> None:
        """Handle user card selection."""
        self.notify(f"Selected user: {event.user_id}")

    def on_search_box_searched(self, event: SearchBox.Searched) -> None:
        """Handle search."""
        self.notify(f"Searching for: {event.query}")


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def create_custom_widget_template(widget_name: str) -> str:
    """Generate a custom widget template."""
    return f'''from textual.widget import Widget
from textual.app import ComposeResult
from textual.widgets import Static
from textual.reactive import reactive
from textual.message import Message


class {widget_name}(Widget):
    """A custom widget."""

    # Default CSS styles
    DEFAULT_CSS = """
    {widget_name} {{
        width: 100%;
        height: auto;
        background: $panel;
        border: solid $primary;
        padding: 1;
    }}
    """

    # Reactive attributes
    value = reactive(0)

    # Custom messages
    class Changed(Message):
        """Posted when value changes."""
        def __init__(self, value: int) -> None:
            self.value = value
            super().__init__()

    def __init__(self, initial_value: int = 0, **kwargs):
        """Initialize the widget."""
        super().__init__(**kwargs)
        self.value = initial_value

    def compose(self) -> ComposeResult:
        """Create child widgets."""
        yield Static(str(self.value), id="display")

    def watch_value(self, new_value: int) -> None:
        """Called when value changes."""
        display = self.query_one("#display", Static)
        display.update(str(new_value))
        self.post_message(self.Changed(new_value))
'''


CUSTOM_WIDGET_GUIDE = """
CUSTOM WIDGET GUIDE
==================

WIDGET STRUCTURE:
1. Inherit from Widget
2. Define DEFAULT_CSS
3. Add reactive attributes
4. Implement compose()
5. Add event handlers
6. Define custom messages

KEY METHODS:

compose() -> ComposeResult:
  - Create child widgets
  - Define widget structure
  - Use yield to add widgets

render() -> RenderableType:
  - Alternative to compose()
  - Return a Rich renderable
  - For simple text display

watch_<attribute>(value):
  - Called when reactive attribute changes
  - Update UI in response
  - Trigger side effects

on_<event>():
  - Handle events from children
  - Process messages
  - Update state

BEST PRACTICES:
1. Use DEFAULT_CSS for styling
2. Keep widgets focused and reusable
3. Use reactive attributes for state
4. Post messages for parent communication
5. Document widget API
6. Provide sensible defaults
7. Support common use cases
8. Test thoroughly

REACTIVE ATTRIBUTES:
- Auto-trigger watch methods
- Efficient updates
- Type-safe
- Support validation

CUSTOM MESSAGES:
- Inherit from Message
- Post with post_message()
- Handle in parent with on_<widget>_<message>
- Include relevant data

COMPOSITION:
- Widgets can contain other widgets
- Use containers for layout
- Support children via *args
- Yield widgets in compose()
"""


if __name__ == "__main__":
    app = CustomWidgetDemo()
    app.run()
