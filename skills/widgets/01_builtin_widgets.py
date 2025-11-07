"""
Skill: Built-in Widget Usage

Comprehensive guide to all built-in Textual widgets with examples.
"""

from textual.app import App, ComposeResult
from textual.widgets import (
    Button, Input, Label, Static, Header, Footer,
    DataTable, Tree, ListView, ListItem,
    Checkbox, RadioButton, RadioSet, Switch,
    ProgressBar, LoadingIndicator,
    Select, SelectionList, OptionList,
    Tabs, TabbedContent, TabPane,
    Log, RichLog, Sparkline,
    Placeholder, Rule, Markdown
)
from textual.containers import Container, Vertical, Horizontal, Grid


# ============================================================================
# BUTTON WIDGETS
# ============================================================================

class ButtonDemo(App):
    """Demonstrates button widgets and variants."""

    CSS = """
    Container {
        height: auto;
        padding: 1;
    }

    Button {
        margin: 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Label("Button Variants:"),
            Button("Default Button", id="default"),
            Button("Primary", variant="primary", id="primary"),
            Button("Success", variant="success", id="success"),
            Button("Warning", variant="warning", id="warning"),
            Button("Error", variant="error", id="error"),
            Button("Disabled", disabled=True),
        )
        yield Static(id="output")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press."""
        output = self.query_one("#output", Static)
        output.update(f"Pressed: {event.button.id}")


# ============================================================================
# INPUT WIDGETS
# ============================================================================

class InputDemo(App):
    """Demonstrates input widgets."""

    CSS = """
    Container {
        padding: 1;
        height: auto;
    }

    Input {
        margin-bottom: 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Label("Text Input Examples:"),
            Input(placeholder="Enter your name", id="name"),
            Input(placeholder="Password", password=True, id="password"),
            Input(
                placeholder="Email",
                id="email",
                validators=[lambda v: "@" in v]
            ),
            Input(
                value="Initial value",
                id="prefilled"
            ),
            Static(id="output"),
        )
        yield Footer()

    def on_input_changed(self, event: Input.Changed) -> None:
        """Handle input changes."""
        output = self.query_one("#output", Static)
        output.update(f"{event.input.id}: {event.value}")

    def on_input_submitted(self, event: Input.Submitted) -> None:
        """Handle input submission (Enter key)."""
        self.notify(f"Submitted: {event.value}")


# ============================================================================
# SELECTION WIDGETS
# ============================================================================

class SelectionDemo(App):
    """Demonstrates selection widgets."""

    CSS = """
    Container {
        padding: 1;
        height: auto;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()

        # Select widget
        yield Container(
            Label("Select Widget:"),
            Select([
                ("Option 1", "opt1"),
                ("Option 2", "opt2"),
                ("Option 3", "opt3"),
            ], prompt="Choose an option", id="select1"),
        )

        # SelectionList (multiple selection)
        yield Container(
            Label("SelectionList (Multiple):"),
            SelectionList[str](
                ("Python", "py"),
                ("JavaScript", "js"),
                ("Rust", "rust"),
                ("Go", "go"),
            ),
        )

        # Radio buttons
        yield Container(
            Label("Radio Buttons:"),
            RadioSet(
                RadioButton("Option A", id="radio_a"),
                RadioButton("Option B", id="radio_b"),
                RadioButton("Option C", id="radio_c"),
                id="radio_set"
            ),
        )

        # Checkbox
        yield Container(
            Label("Checkboxes:"),
            Checkbox("Enable feature 1", id="check1"),
            Checkbox("Enable feature 2", value=True, id="check2"),
            Switch(value=True, id="switch1"),
        )

        yield Footer()


# ============================================================================
# DATA DISPLAY WIDGETS
# ============================================================================

class DataTableDemo(App):
    """Demonstrates DataTable widget."""

    def compose(self) -> ComposeResult:
        yield Header()
        yield DataTable(id="table")
        yield Footer()

    def on_mount(self) -> None:
        """Setup table when mounted."""
        table = self.query_one(DataTable)

        # Add columns
        table.add_columns("Name", "Age", "City")

        # Add rows
        table.add_rows([
            ("Alice", 30, "New York"),
            ("Bob", 25, "San Francisco"),
            ("Charlie", 35, "London"),
            ("Diana", 28, "Paris"),
        ])

        # Enable cursor
        table.cursor_type = "row"
        table.zebra_stripes = True


class TreeDemo(App):
    """Demonstrates Tree widget."""

    def compose(self) -> ComposeResult:
        yield Header()
        yield Tree("Root", id="tree")
        yield Footer()

    def on_mount(self) -> None:
        """Build tree structure."""
        tree = self.query_one(Tree)
        tree.root.expand()

        # Add nodes
        folder1 = tree.root.add("Folder 1", expand=True)
        folder1.add_leaf("File 1.1")
        folder1.add_leaf("File 1.2")

        folder2 = tree.root.add("Folder 2")
        subfolder = folder2.add("Subfolder")
        subfolder.add_leaf("File 2.1")


class ListViewDemo(App):
    """Demonstrates ListView widget."""

    def compose(self) -> ComposeResult:
        yield Header()
        yield ListView(
            ListItem(Label("Item 1")),
            ListItem(Label("Item 2")),
            ListItem(Label("Item 3")),
            ListItem(Label("Item 4")),
            ListItem(Label("Item 5")),
        )
        yield Footer()


# ============================================================================
# PROGRESS WIDGETS
# ============================================================================

class ProgressDemo(App):
    """Demonstrates progress indicators."""

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Label("Progress Bar:"),
            ProgressBar(total=100, show_eta=True, id="progress"),
            Label("Loading Indicator:"),
            LoadingIndicator(),
        )
        yield Footer()

    def on_mount(self) -> None:
        """Start progress simulation."""
        self.update_progress()

    def update_progress(self) -> None:
        """Simulate progress updates."""
        progress = self.query_one(ProgressBar)

        def advance():
            if progress.progress < 100:
                progress.advance(10)
                self.set_timer(0.5, advance)

        advance()


# ============================================================================
# LAYOUT WIDGETS
# ============================================================================

class TabsDemo(App):
    """Demonstrates Tabs and TabbedContent."""

    def compose(self) -> ComposeResult:
        yield Header()
        with TabbedContent():
            with TabPane("Tab 1", id="tab1"):
                yield Label("Content for tab 1")
            with TabPane("Tab 2", id="tab2"):
                yield Label("Content for tab 2")
            with TabPane("Tab 3", id="tab3"):
                yield Label("Content for tab 3")
        yield Footer()


# ============================================================================
# TEXT DISPLAY WIDGETS
# ============================================================================

class TextDisplayDemo(App):
    """Demonstrates text display widgets."""

    CSS = """
    Container {
        height: auto;
        padding: 1;
    }

    #log {
        height: 10;
        border: solid green;
    }

    #markdown {
        height: auto;
        border: solid blue;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()

        # Static text
        yield Container(
            Label("This is a label"),
            Static("This is static text"),
            Rule(),
        )

        # Rich Log
        yield RichLog(id="log", markup=True)

        # Markdown
        yield Markdown("""
# Markdown Support

- **Bold** text
- *Italic* text
- `Code` blocks

## Lists work too!
1. First item
2. Second item
        """, id="markdown")

        yield Footer()

    def on_mount(self) -> None:
        """Add log entries."""
        log = self.query_one(RichLog)
        log.write("[bold green]Success![/bold green]")
        log.write("[bold red]Error![/bold red]")
        log.write("Regular text")


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

WIDGET_REFERENCE = """
BUILT-IN WIDGETS REFERENCE
=========================

INPUT WIDGETS:
- Button: Clickable button with variants (primary, success, warning, error)
- Input: Text input field with validation and password mode
- Checkbox: Boolean checkbox
- RadioButton/RadioSet: Mutually exclusive options
- Switch: Toggle switch
- Select: Dropdown selection
- SelectionList: Multiple selection list
- OptionList: List of selectable options

DISPLAY WIDGETS:
- Label: Simple text label
- Static: Static text with Rich markup
- Markdown: Render markdown content
- RichLog: Scrollable log with Rich formatting
- Rule: Horizontal or vertical line
- Sparkline: Tiny data visualization

DATA WIDGETS:
- DataTable: Tabular data with sorting and cursor
- Tree: Hierarchical tree structure
- ListView: Scrollable list of items
- DirectoryTree: File system tree

PROGRESS WIDGETS:
- ProgressBar: Progress indicator with percentage
- LoadingIndicator: Animated loading spinner

LAYOUT WIDGETS:
- Header: Application header
- Footer: Application footer with key bindings
- Tabs/TabbedContent/TabPane: Tabbed interface
- Placeholder: Development placeholder

USAGE TIPS:
1. All widgets support CSS styling
2. Use id="" for query_one() lookups
3. Use classes="" for query() lookups
4. Widgets emit events (on_<widget>_<event>)
5. Disabled widgets don't respond to input
6. Most widgets support focus
"""


def get_widget_template(widget_type: str) -> str:
    """Get code template for a specific widget type."""
    templates = {
        "button": """Button("Click me", id="my_button", variant="primary")

# Handler:
def on_button_pressed(self, event: Button.Pressed) -> None:
    if event.button.id == "my_button":
        self.notify("Button clicked!")
""",
        "input": """Input(placeholder="Enter text", id="my_input")

# Handlers:
def on_input_changed(self, event: Input.Changed) -> None:
    self.log(f"Value: {event.value}")

def on_input_submitted(self, event: Input.Submitted) -> None:
    self.notify(f"Submitted: {event.value}")
""",
        "datatable": """table = DataTable(id="my_table")

# Setup:
def on_mount(self) -> None:
    table = self.query_one(DataTable)
    table.add_columns("Col1", "Col2", "Col3")
    table.add_rows([("A", "B", "C"), ("D", "E", "F")])
    table.cursor_type = "row"
""",
        "tree": """Tree("Root", id="my_tree")

# Setup:
def on_mount(self) -> None:
    tree = self.query_one(Tree)
    node = tree.root.add("Child")
    node.add_leaf("Leaf")
""",
    }
    return templates.get(widget_type, "# Template not found")


if __name__ == "__main__":
    # Run the button demo
    app = ButtonDemo()
    app.run()
