"""
Skill: Screens and Navigation

Master multi-screen applications, modals, and navigation patterns.
"""

from textual.app import App, ComposeResult
from textual.screen import Screen, ModalScreen
from textual.widgets import Header, Footer, Static, Button, Input, Label
from textual.containers import Container, Vertical, Horizontal


# ============================================================================
# BASIC SCREENS
# ============================================================================

class HomeScreen(Screen):
    """Home screen."""

    BINDINGS = [
        ("s", "goto_settings", "Settings"),
        ("a", "goto_about", "About"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Static("Welcome to the Home Screen!", id="welcome"),
            Button("Go to Settings", id="settings_btn", variant="primary"),
            Button("Go to About", id="about_btn", variant="success"),
            Button("Show Modal", id="modal_btn", variant="warning"),
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        if event.button.id == "settings_btn":
            self.app.push_screen("settings")
        elif event.button.id == "about_btn":
            self.app.push_screen("about")
        elif event.button.id == "modal_btn":
            self.app.push_screen(ConfirmModal())

    def action_goto_settings(self) -> None:
        """Navigate to settings."""
        self.app.push_screen("settings")

    def action_goto_about(self) -> None:
        """Navigate to about."""
        self.app.push_screen("about")


class SettingsScreen(Screen):
    """Settings screen."""

    BINDINGS = [
        ("escape", "app.pop_screen", "Back"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Static("Settings Screen"),
            Label("Configure your application:"),
            Input(placeholder="Username", id="username"),
            Input(placeholder="Email", id="email"),
            Button("Save", variant="success"),
            Button("Cancel", variant="error"),
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle buttons."""
        if event.button.label == "Save":
            # Save settings
            self.notify("Settings saved!")
            self.app.pop_screen()
        elif event.button.label == "Cancel":
            self.app.pop_screen()


class AboutScreen(Screen):
    """About screen."""

    BINDINGS = [
        ("escape", "app.pop_screen", "Back"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Static("About This App"),
            Label("Version: 1.0.0"),
            Label("Author: Your Name"),
            Button("Back to Home"),
        )
        yield Footer()

    def on_button_pressed(self) -> None:
        """Go back to home."""
        self.app.pop_screen()


class BasicScreenApp(App):
    """App with multiple screens."""

    SCREENS = {
        "home": HomeScreen,
        "settings": SettingsScreen,
        "about": AboutScreen,
    }

    def on_mount(self) -> None:
        """Start on home screen."""
        self.push_screen("home")


# ============================================================================
# MODAL SCREENS
# ============================================================================

class ConfirmModal(ModalScreen[bool]):
    """A confirmation modal that returns a boolean."""

    CSS = """
    ConfirmModal {
        align: center middle;
    }

    #dialog {
        width: 60;
        height: 11;
        background: $panel;
        border: thick $primary;
        padding: 1;
    }

    #question {
        text-align: center;
        margin: 1;
    }

    #buttons {
        width: 100%;
        height: auto;
        align: center middle;
    }

    Button {
        margin: 0 2;
    }
    """

    def compose(self) -> ComposeResult:
        with Vertical(id="dialog"):
            yield Static("Are you sure you want to continue?", id="question")
            with Horizontal(id="buttons"):
                yield Button("Confirm", variant="success", id="confirm")
                yield Button("Cancel", variant="error", id="cancel")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press."""
        if event.button.id == "confirm":
            self.dismiss(True)
        else:
            self.dismiss(False)


class InputModal(ModalScreen[str]):
    """Modal for text input."""

    CSS = """
    InputModal {
        align: center middle;
    }

    #dialog {
        width: 60;
        height: 15;
        background: $panel;
        border: thick $accent;
        padding: 2;
    }

    Input {
        margin: 1 0;
    }
    """

    def __init__(self, prompt: str = "Enter value:", **kwargs):
        super().__init__(**kwargs)
        self.prompt_text = prompt

    def compose(self) -> ComposeResult:
        with Vertical(id="dialog"):
            yield Label(self.prompt_text)
            yield Input(placeholder="Type here...", id="input")
            with Horizontal():
                yield Button("Submit", variant="primary", id="submit")
                yield Button("Cancel", id="cancel")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press."""
        if event.button.id == "submit":
            input_widget = self.query_one(Input)
            self.dismiss(input_widget.value)
        else:
            self.dismiss("")

    def on_input_submitted(self) -> None:
        """Handle Enter key."""
        input_widget = self.query_one(Input)
        self.dismiss(input_widget.value)


class ModalApp(App):
    """App demonstrating modal screens."""

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Static("Modal Demo", id="title"),
            Button("Show Confirm Dialog", id="confirm"),
            Button("Show Input Dialog", id="input"),
            Static("", id="result"),
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press."""
        if event.button.id == "confirm":
            self.push_screen(ConfirmModal(), self.handle_confirm)
        elif event.button.id == "input":
            self.push_screen(
                InputModal("What's your name?"),
                self.handle_input
            )

    def handle_confirm(self, result: bool) -> None:
        """Handle confirm modal result."""
        result_widget = self.query_one("#result", Static)
        result_widget.update(f"Confirmed: {result}")

    def handle_input(self, result: str) -> None:
        """Handle input modal result."""
        result_widget = self.query_one("#result", Static)
        if result:
            result_widget.update(f"Hello, {result}!")
        else:
            result_widget.update("Cancelled")


# ============================================================================
# PUSH SCREEN WITH CALLBACK
# ============================================================================

class DataEntryScreen(Screen[dict]):
    """Screen for entering data that returns a dict."""

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Label("Enter User Information:"),
            Input(placeholder="Name", id="name"),
            Input(placeholder="Email", id="email"),
            Input(placeholder="Age", id="age", type="number"),
            Horizontal(
                Button("Submit", variant="success"),
                Button("Cancel", variant="error"),
            ),
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle buttons."""
        if event.button.label == "Submit":
            # Collect data
            data = {
                "name": self.query_one("#name", Input).value,
                "email": self.query_one("#email", Input).value,
                "age": self.query_one("#age", Input).value,
            }
            self.dismiss(data)
        else:
            self.dismiss({})


class CallbackApp(App):
    """App using screen callbacks."""

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Button("Enter Data", variant="primary"),
            Static("", id="display"),
        )
        yield Footer()

    def on_button_pressed(self) -> None:
        """Show data entry screen."""
        self.push_screen(DataEntryScreen(), self.handle_data)

    def handle_data(self, data: dict) -> None:
        """Process returned data."""
        display = self.query_one("#display", Static)
        if data:
            display.update(
                f"Name: {data['name']}\n"
                f"Email: {data['email']}\n"
                f"Age: {data['age']}"
            )
        else:
            display.update("Cancelled")


# ============================================================================
# ASYNC SCREEN HANDLING
# ============================================================================

class AsyncApp(App):
    """App using async screen methods."""

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Button("Async Confirm", id="async_confirm"),
            Button("Async Input", id="async_input"),
            Static("", id="result"),
        )
        yield Footer()

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle buttons asynchronously."""
        if event.button.id == "async_confirm":
            # Wait for modal result
            result = await self.push_screen_wait(ConfirmModal())
            result_widget = self.query_one("#result", Static)
            result_widget.update(f"Async result: {result}")

        elif event.button.id == "async_input":
            # Wait for input
            name = await self.push_screen_wait(
                InputModal("Enter your name:")
            )
            if name:
                result_widget = self.query_one("#result", Static)
                result_widget.update(f"Async input: {name}")


# ============================================================================
# SCREEN STACK MANAGEMENT
# ============================================================================

class StackScreen(Screen):
    """Screen showing stack depth."""

    def __init__(self, level: int, **kwargs):
        super().__init__(**kwargs)
        self.level = level

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Static(f"Screen Level: {self.level}"),
            Button("Push Another Screen", id="push"),
            Button("Pop Screen", id="pop"),
            Button("Pop to Root", id="root"),
            Static(f"Stack depth: {len(self.app.screen_stack)}", id="depth"),
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle navigation."""
        if event.button.id == "push":
            self.app.push_screen(StackScreen(self.level + 1))
        elif event.button.id == "pop":
            if len(self.app.screen_stack) > 1:
                self.app.pop_screen()
        elif event.button.id == "root":
            # Pop all screens except root
            while len(self.app.screen_stack) > 1:
                self.app.pop_screen()

    def on_mount(self) -> None:
        """Update depth display."""
        depth = self.query_one("#depth", Static)
        depth.update(f"Stack depth: {len(self.app.screen_stack)}")


class StackApp(App):
    """App demonstrating screen stack."""

    def on_mount(self) -> None:
        """Start with level 1 screen."""
        self.push_screen(StackScreen(1))


# ============================================================================
# SCREENS GUIDE
# ============================================================================

SCREENS_GUIDE = """
SCREENS AND NAVIGATION GUIDE
============================

DEFINING SCREENS:

class MyScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Content()
        yield Footer()

REGISTERING SCREENS:

class MyApp(App):
    SCREENS = {
        "home": HomeScreen,
        "settings": SettingsScreen,
    }

NAVIGATION:

Push screen:
  self.app.push_screen("screen_name")
  self.app.push_screen(ScreenInstance())

Pop screen:
  self.app.pop_screen()

Switch screen (replace current):
  self.app.switch_screen("screen_name")

SCREEN WITH CALLBACK:

def show_dialog(self) -> None:
    self.push_screen(DialogScreen(), self.handle_result)

def handle_result(self, data: str) -> None:
    print(f"Got: {data}")

ASYNC SCREEN (wait for result):

async def show_dialog(self) -> None:
    result = await self.push_screen_wait(DialogScreen())
    print(f"Got: {result}")

MODAL SCREENS:

class MyModal(ModalScreen[ReturnType]):
    def compose(self) -> ComposeResult:
        # Build modal UI
        pass

    def on_button_pressed(self) -> None:
        self.dismiss(return_value)

RETURNING VALUES:

In screen:
  self.dismiss(result)  # Close and return

In app:
  result = await self.push_screen_wait(MyScreen())

SCREEN BINDINGS:

class MyScreen(Screen):
    BINDINGS = [
        ("escape", "app.pop_screen", "Back"),
        ("h", "goto_home", "Home"),
    ]

SCREEN STACK:

Current screen:
  self.app.screen

All screens:
  self.app.screen_stack

Stack depth:
  len(self.app.screen_stack)

LIFECYCLE:

def on_mount(self) -> None:
    # Screen is mounted

def on_unmount(self) -> None:
    # Screen is being removed

MODAL STYLING:

ModalScreen {
    align: center middle;
}

#dialog {
    width: 60;
    height: 20;
    background: $panel;
    border: thick $primary;
}

BEST PRACTICES:
1. Use push_screen for navigation
2. Use pop_screen to go back
3. Use ModalScreen for dialogs
4. Return data via dismiss()
5. Use await push_screen_wait for results
6. Bind Escape to pop_screen
7. Keep screens focused
8. Manage screen stack carefully
9. Clean up in on_unmount
10. Use type hints for return types

COMMON PATTERNS:

Wizard flow:
  push_screen(Step1) -> Step2 -> Step3 -> pop to start

Settings:
  push_screen(Settings) -> Save -> pop_screen()

Confirm dialog:
  result = await push_screen_wait(ConfirmModal())
  if result:
      # Do action

Form entry:
  data = await push_screen_wait(FormScreen())
  if data:
      process(data)
"""


def create_screen_template(screen_name: str) -> str:
    """Generate screen template."""
    return f'''from textual.screen import Screen
from textual.app import ComposeResult
from textual.widgets import Header, Footer, Static, Button
from textual.containers import Container


class {screen_name}(Screen):
    """A screen."""

    BINDINGS = [
        ("escape", "app.pop_screen", "Back"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Static("Content for {screen_name}"),
            Button("Action", variant="primary"),
        )
        yield Footer()

    def on_button_pressed(self) -> None:
        """Handle button press."""
        # Perform action
        self.app.pop_screen()  # Go back
'''


def create_modal_template(modal_name: str) -> str:
    """Generate modal template."""
    return f'''from textual.screen import ModalScreen
from textual.app import ComposeResult
from textual.widgets import Static, Button
from textual.containers import Vertical, Horizontal


class {modal_name}(ModalScreen[bool]):
    """A modal dialog."""

    CSS = """
    {modal_name} {{
        align: center middle;
    }}

    #dialog {{
        width: 60;
        height: 15;
        background: $panel;
        border: thick $primary;
        padding: 2;
    }}
    """

    def compose(self) -> ComposeResult:
        with Vertical(id="dialog"):
            yield Static("Question or prompt?")
            with Horizontal():
                yield Button("Confirm", variant="success", id="confirm")
                yield Button("Cancel", variant="error", id="cancel")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press."""
        result = event.button.id == "confirm"
        self.dismiss(result)
'''


if __name__ == "__main__":
    app = ModalApp()
    app.run()
