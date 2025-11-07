#!/usr/bin/env python3
"""
Quick Start Example - A complete Textual app showcasing key features.

This example demonstrates:
- Basic app structure
- Multiple widgets
- Event handling
- Reactive attributes
- CSS styling
- Screens and navigation

Run with: python quick_start.py
"""

from textual.app import App, ComposeResult
from textual.screen import Screen, ModalScreen
from textual.widgets import (
    Header, Footer, Button, Input, Static, Label,
    DataTable, Checkbox
)
from textual.containers import Container, Horizontal, Vertical
from textual.reactive import reactive
from textual import on


# ============================================================================
# MODAL DIALOG
# ============================================================================

class ConfirmDialog(ModalScreen[bool]):
    """A simple confirmation dialog."""

    CSS = """
    ConfirmDialog {
        align: center middle;
    }

    #dialog {
        width: 50;
        height: 11;
        background: $panel;
        border: thick $accent;
        padding: 1;
    }

    #question {
        text-align: center;
        margin: 1 0;
    }

    Horizontal {
        width: 100%;
        height: auto;
        align: center middle;
    }

    Button {
        margin: 0 1;
    }
    """

    def __init__(self, question: str, **kwargs):
        super().__init__(**kwargs)
        self.question = question

    def compose(self) -> ComposeResult:
        with Vertical(id="dialog"):
            yield Static(self.question, id="question")
            with Horizontal():
                yield Button("Yes", variant="success", id="yes")
                yield Button("No", variant="error", id="no")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press."""
        self.dismiss(event.button.id == "yes")


# ============================================================================
# SETTINGS SCREEN
# ============================================================================

class SettingsScreen(Screen):
    """Settings screen with various controls."""

    BINDINGS = [
        ("escape", "app.pop_screen", "Back"),
    ]

    CSS = """
    SettingsScreen Container {
        padding: 1;
        background: $surface;
    }

    SettingsScreen Label {
        margin: 1 0;
        text-style: bold;
        color: $accent;
    }

    SettingsScreen Input {
        margin-bottom: 1;
    }

    SettingsScreen Checkbox {
        margin: 1 0;
    }

    SettingsScreen Button {
        margin: 1 0;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Label("Application Settings"),
            Input(placeholder="Username", id="username"),
            Input(placeholder="Email", id="email"),
            Checkbox("Enable notifications", value=True, id="notifications"),
            Checkbox("Dark mode", value=True, id="dark_mode"),
            Horizontal(
                Button("Save", variant="success", id="save"),
                Button("Cancel", variant="error", id="cancel"),
            ),
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press."""
        if event.button.id == "save":
            self.app.notify("Settings saved!", severity="information")
            self.app.pop_screen()
        elif event.button.id == "cancel":
            self.app.pop_screen()


# ============================================================================
# MAIN APP
# ============================================================================

class QuickStartApp(App):
    """A quick start Textual application showcasing key features."""

    CSS = """
    Screen {
        background: $surface;
    }

    .section {
        padding: 1;
        margin: 1;
        background: $panel;
        border: solid $primary;
        height: auto;
    }

    .section-title {
        text-style: bold;
        color: $accent;
        margin-bottom: 1;
    }

    #counter-display {
        text-align: center;
        margin: 1;
        padding: 1;
        background: $primary 20%;
        border: solid $primary;
    }

    #output {
        height: 8;
        border: solid $success;
        padding: 1;
        margin-top: 1;
    }

    #table-container {
        height: 15;
    }

    DataTable {
        height: 100%;
    }

    Button {
        margin: 0 1;
    }
    """

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("d", "toggle_dark", "Toggle Dark Mode"),
        ("s", "show_settings", "Settings"),
    ]

    SCREENS = {
        "settings": SettingsScreen,
    }

    # Reactive attributes for counter
    counter = reactive(0)

    def compose(self) -> ComposeResult:
        """Create the UI."""
        yield Header()

        # Counter Section
        yield Container(
            Static("Counter Demo", classes="section-title"),
            Static("0", id="counter-display"),
            Horizontal(
                Button("-", id="dec", variant="error"),
                Button("Reset", id="reset", variant="warning"),
                Button("+", id="inc", variant="success"),
            ),
            classes="section"
        )

        # Input Section
        yield Container(
            Static("Input Demo", classes="section-title"),
            Input(placeholder="Type something...", id="user-input"),
            Static("", id="output"),
            classes="section"
        )

        # Data Table Section
        yield Container(
            Static("Data Table Demo", classes="section-title"),
            DataTable(id="data-table", classes="table"),
            Horizontal(
                Button("Add Row", variant="primary", id="add-row"),
                Button("Clear Table", variant="error", id="clear-table"),
            ),
            classes="section",
            id="table-container"
        )

        # Navigation Section
        yield Container(
            Static("Navigation Demo", classes="section-title"),
            Horizontal(
                Button("Settings", variant="primary", id="settings-btn"),
                Button("Show Dialog", variant="warning", id="dialog-btn"),
            ),
            classes="section"
        )

        yield Footer()

    def on_mount(self) -> None:
        """Initialize the app."""
        # Setup data table
        table = self.query_one(DataTable)
        table.add_columns("ID", "Name", "Status")
        table.add_rows([
            ("1", "Task One", "Complete"),
            ("2", "Task Two", "In Progress"),
            ("3", "Task Three", "Pending"),
        ])
        table.cursor_type = "row"

    def watch_counter(self, new_value: int) -> None:
        """Update counter display when value changes."""
        display = self.query_one("#counter-display", Static)
        display.update(str(new_value))

    # Counter button handlers using @on decorator
    @on(Button.Pressed, "#inc")
    def increment_counter(self) -> None:
        """Increment the counter."""
        self.counter += 1

    @on(Button.Pressed, "#dec")
    def decrement_counter(self) -> None:
        """Decrement the counter."""
        self.counter -= 1

    @on(Button.Pressed, "#reset")
    def reset_counter(self) -> None:
        """Reset the counter."""
        self.counter = 0

    # Input handlers
    def on_input_changed(self, event: Input.Changed) -> None:
        """Handle input changes."""
        if event.input.id == "user-input":
            output = self.query_one("#output", Static)
            output.update(f"You typed: {event.value}")

    def on_input_submitted(self, event: Input.Submitted) -> None:
        """Handle input submission."""
        self.notify(f"Submitted: {event.value}")

    # Table button handlers
    @on(Button.Pressed, "#add-row")
    def add_table_row(self) -> None:
        """Add a row to the table."""
        table = self.query_one(DataTable)
        row_count = len(table.rows) + 1
        table.add_row(
            str(row_count),
            f"Task {['One', 'Two', 'Three', 'Four', 'Five'][min(row_count-1, 4)]}",
            "New"
        )
        self.notify("Row added")

    @on(Button.Pressed, "#clear-table")
    async def clear_table(self) -> None:
        """Clear the table after confirmation."""
        confirmed = await self.push_screen_wait(
            ConfirmDialog("Clear all table data?")
        )
        if confirmed:
            table = self.query_one(DataTable)
            table.clear()
            self.notify("Table cleared")

    # Navigation handlers
    @on(Button.Pressed, "#settings-btn")
    def show_settings_screen(self) -> None:
        """Show settings screen."""
        self.push_screen("settings")

    @on(Button.Pressed, "#dialog-btn")
    async def show_dialog(self) -> None:
        """Show a dialog and handle result."""
        result = await self.push_screen_wait(
            ConfirmDialog("Do you like Textual?")
        )
        if result:
            self.notify("Great! 🎉", severity="information")
        else:
            self.notify("Give it another try! 😊", severity="warning")

    # Actions
    def action_toggle_dark(self) -> None:
        """Toggle dark mode."""
        self.dark = not self.dark
        mode = "dark" if self.dark else "light"
        self.notify(f"Switched to {mode} mode")

    def action_show_settings(self) -> None:
        """Show settings screen."""
        self.push_screen("settings")


# ============================================================================
# MAIN
# ============================================================================

def main():
    """Run the application."""
    app = QuickStartApp()
    app.run()


if __name__ == "__main__":
    print("""
╔═══════════════════════════════════════════════════════╗
║         Textual Quick Start Example                    ║
╠═══════════════════════════════════════════════════════╣
║                                                        ║
║  This example demonstrates:                           ║
║  ✓ Reactive attributes (counter)                      ║
║  ✓ Event handling (@on decorator)                     ║
║  ✓ Input widgets and validation                       ║
║  ✓ DataTable usage                                    ║
║  ✓ Screens and navigation                             ║
║  ✓ Modal dialogs                                      ║
║  ✓ CSS styling                                        ║
║  ✓ Key bindings                                       ║
║                                                        ║
║  Key bindings:                                        ║
║  • q - Quit                                           ║
║  • d - Toggle dark/light mode                         ║
║  • s - Open settings                                  ║
║                                                        ║
╚═══════════════════════════════════════════════════════╝
    """)
    main()
