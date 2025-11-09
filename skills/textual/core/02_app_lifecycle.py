"""
Skill: App Lifecycle & Structure

Covers app initialization, mount/unmount handlers, shutdown, and configuration.
"""

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Button
from textual.containers import Container
import argparse


# ============================================================================
# LIFECYCLE EVENTS
# ============================================================================

class LifecycleApp(App):
    """Demonstrates all lifecycle events."""

    def __init__(self, **kwargs):
        """Initialize the app."""
        super().__init__(**kwargs)
        self.log("App __init__ called")

    def on_mount(self) -> None:
        """Called when app is mounted and ready."""
        self.log("App mounted - DOM is ready")
        # Perfect place for initialization tasks
        self.title = "Lifecycle Demo"
        self.sub_title = "App is running"

    async def on_load(self) -> None:
        """Called before DOM is ready."""
        self.log("App loading - before DOM")
        # Load configuration or resources here

    def on_unmount(self) -> None:
        """Called when app is about to close."""
        self.log("App unmounting")
        # Cleanup resources here

    def compose(self) -> ComposeResult:
        """Create child widgets."""
        yield Header()
        yield Static("Check the logs to see lifecycle events")
        yield Footer()


# ============================================================================
# APP CONFIGURATION
# ============================================================================

class ConfigurableApp(App):
    """App with extensive configuration options."""

    # Basic configuration
    TITLE = "My Application"
    SUB_TITLE = "Version 1.0"

    # Visual configuration
    CSS_PATH = "app.tcss"

    # Key bindings
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("d", "toggle_dark", "Toggle Dark Mode"),
        ("?", "show_help", "Help"),
    ]

    # Feature flags
    ENABLE_COMMAND_PALETTE = True  # Ctrl+\\ for command palette

    def __init__(
        self,
        config_file: str | None = None,
        debug: bool = False,
        **kwargs
    ):
        """
        Initialize with custom configuration.

        Args:
            config_file: Path to configuration file
            debug: Enable debug mode
        """
        super().__init__(**kwargs)
        self.config_file = config_file
        self.debug = debug

        if debug:
            self.log("Debug mode enabled")

    def action_show_help(self) -> None:
        """Show help screen."""
        self.notify("Help: Press 'q' to quit, 'd' to toggle dark mode")

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static(f"Config file: {self.config_file or 'None'}")
        yield Static(f"Debug mode: {self.debug}")
        yield Footer()


# ============================================================================
# GRACEFUL SHUTDOWN
# ============================================================================

class GracefulShutdownApp(App):
    """Demonstrates proper shutdown handling."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.unsaved_changes = False

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Static("Try to quit with unsaved changes"),
            Button("Make Changes", id="make_changes"),
            Button("Save", id="save"),
            Button("Quit", id="quit"),
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button clicks."""
        if event.button.id == "make_changes":
            self.unsaved_changes = True
            self.notify("Changes made (unsaved)")
        elif event.button.id == "save":
            self.unsaved_changes = False
            self.notify("Changes saved")
        elif event.button.id == "quit":
            self.action_quit()

    def action_quit(self) -> None:
        """Custom quit action with confirmation."""
        if self.unsaved_changes:
            self.notify("⚠️  You have unsaved changes!", severity="warning")
            # In a real app, show a confirmation dialog
        else:
            self.exit()

    def on_unmount(self) -> None:
        """Cleanup before shutdown."""
        if self.unsaved_changes:
            self.log("Warning: Exiting with unsaved changes")
        # Perform cleanup tasks
        self.log("Cleanup completed")


# ============================================================================
# COMMAND LINE ARGUMENTS
# ============================================================================

class CLIApp(App):
    """App with command-line argument support."""

    def __init__(
        self,
        input_file: str | None = None,
        output_file: str | None = None,
        verbose: bool = False,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.input_file = input_file
        self.output_file = output_file
        self.verbose = verbose

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static(f"Input: {self.input_file or 'stdin'}")
        yield Static(f"Output: {self.output_file or 'stdout'}")
        yield Static(f"Verbose: {self.verbose}")
        yield Footer()


def parse_args():
    """Parse command line arguments for CLIApp."""
    parser = argparse.ArgumentParser(description="Textual CLI Application")
    parser.add_argument("-i", "--input", help="Input file path")
    parser.add_argument("-o", "--output", help="Output file path")
    parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    return parser.parse_args()


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def create_lifecycle_aware_app(app_name: str) -> str:
    """Generate template with all lifecycle hooks."""
    return f"""from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static


class {app_name}(App):
    \"\"\"Application with lifecycle management.\"\"\"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Initialize instance variables

    async def on_load(self) -> None:
        \"\"\"Called before DOM is ready.\"\"\"
        # Load resources or configuration
        pass

    def on_mount(self) -> None:
        \"\"\"Called when app is mounted.\"\"\"
        # Setup initial state
        pass

    def on_unmount(self) -> None:
        \"\"\"Called before app exits.\"\"\"
        # Cleanup resources
        pass

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Application content")
        yield Footer()


if __name__ == "__main__":
    app = {app_name}()
    app.run()
"""


APP_LIFECYCLE_GUIDE = """
APP LIFECYCLE GUIDE
==================

LIFECYCLE ORDER:
1. __init__()        - App instance created
2. on_load()         - Before DOM ready (async)
3. compose()         - Build widget tree
4. on_mount()        - DOM ready, app running
5. [app runs]
6. on_unmount()      - Before shutdown
7. [app exits]

WHEN TO USE EACH:

__init__():
  - Set instance variables
  - Parse configuration
  - Setup non-UI state

on_load() [async]:
  - Load external resources
  - Connect to databases
  - Async initialization

compose():
  - Build UI structure
  - Create widget tree
  - Define layout

on_mount():
  - Setup initial UI state
  - Start timers
  - Set focus
  - Update widget values

on_unmount():
  - Save state
  - Close connections
  - Cleanup resources
  - Log shutdown

BEST PRACTICES:
- Keep __init__ lightweight
- Use on_mount for UI initialization
- Always cleanup in on_unmount
- Handle errors gracefully
- Log important lifecycle events
"""


if __name__ == "__main__":
    # Example with CLI args
    args = parse_args()
    app = CLIApp(
        input_file=args.input,
        output_file=args.output,
        verbose=args.verbose
    )
    app.run()
