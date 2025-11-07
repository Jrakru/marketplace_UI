#!/usr/bin/env python3
"""
Quick Reference - Fast lookup guide for AI agents.

Provides instant access to common patterns, syntax, and best practices.
"""

QUICK_REFERENCE = """
==========================================
TEXTUAL QUICK REFERENCE FOR AI AGENTS
==========================================

## BASIC APP STRUCTURE

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static

class MyApp(App):
    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Content")
        yield Footer()

if __name__ == "__main__":
    app = MyApp()
    app.run()

## COMMON WIDGETS

Button:        Button("Click", id="btn", variant="primary")
Input:         Input(placeholder="Text...", id="input")
Label:         Label("Static text")
Static:        Static("Content", id="display")
DataTable:     DataTable(id="table")
Tree:          Tree("Root", id="tree")
Checkbox:      Checkbox("Option", value=True)
Select:        Select([("Label", "value")], id="select")
ProgressBar:   ProgressBar(total=100)

## CONTAINERS

Vertical:      Stacks widgets top-to-bottom (default)
Horizontal:    Places widgets left-to-right
Grid:          2D grid layout
Container:     Generic container

Usage:
with Horizontal():
    yield Widget1()
    yield Widget2()

## CSS BASICS

Selectors:
  Type:        Button { }
  ID:          #my-button { }
  Class:       .my-class { }
  Pseudo:      :hover, :focus

Properties:
  width: 50;  height: 10;
  padding: 1;  margin: 2;
  background: $primary;
  color: $text;
  border: solid $accent;

## EVENTS

Button pressed:
  def on_button_pressed(self, event: Button.Pressed):
      if event.button.id == "my_btn":
          pass

Input changed:
  def on_input_changed(self, event: Input.Changed):
      value = event.value

Input submitted:
  def on_input_submitted(self, event: Input.Submitted):
      value = event.value

Using @on decorator:
  @on(Button.Pressed, "#my_button")
  def handle_click(self):
      pass

Keyboard:
  def on_key(self, event: events.Key):
      if event.key == "enter":
          pass

## REACTIVE ATTRIBUTES

Basic:
  count = reactive(0)

  def watch_count(self, new_value):
      # Called when count changes
      self.query_one("#display").update(str(new_value))

Computed:
  total = reactive(0)

  def compute_total(self) -> int:
      return self.value1 + self.value2

## SCREENS

Define screen:
  class MyScreen(Screen):
      def compose(self):
          yield Header()
          yield Static("Content")
          yield Footer()

Navigate:
  self.app.push_screen("screen_name")   # Navigate to
  self.app.pop_screen()                 # Go back
  self.app.switch_screen("name")        # Replace

Modal:
  class MyModal(ModalScreen[bool]):
      def on_button_pressed(self):
          self.dismiss(True)

  # Usage:
  result = await self.push_screen_wait(MyModal())

## DOM QUERIES

Get one:
  widget = self.query_one("#my_id", Static)
  widget = self.query_one(Button)

Get multiple:
  widgets = self.query(".my_class")
  buttons = self.query(Button)

## LAYOUT

Vertical (default):
  Stacks top-to-bottom
  Each takes full width

Horizontal:
  Places left-to-right
  Auto width

Grid:
  CSS:
    Grid {
        grid-size: 3;  /* columns */
        grid-gutter: 1;
    }

Dock (sticky):
  .sidebar {
      dock: left;
      width: 20;
  }

## KEY BINDINGS

class MyApp(App):
    BINDINGS = [
        ("q", "quit", "Quit"),
        ("d", "toggle_dark", "Toggle Dark"),
    ]

    def action_toggle_dark(self):
        self.dark = not self.dark

## TESTING

Snapshot test:
  def test_app(snap_compare):
      app = MyApp()
      assert snap_compare(app)

With interaction:
  def test_click(snap_compare):
      async def run_before(pilot):
          await pilot.click("#button")

      assert snap_compare(MyApp(), run_before=run_before)

## COMMON PATTERNS

Counter:
  count = reactive(0)

  def on_button_pressed(self, event):
      if event.button.id == "increment":
          self.count += 1

Form submission:
  def on_button_pressed(self):
      name = self.query_one("#name", Input).value
      email = self.query_one("#email", Input).value
      # Process data

Toggle visibility:
  visible = reactive(True)

  def watch_visible(self, is_visible):
      widget = self.query_one("#widget")
      widget.display = is_visible

State machine:
  state = reactive("idle")  # idle, loading, success, error

  def watch_state(self, new_state):
      if new_state == "loading":
          self.show_loading()

## THEME COLORS

Primary colors:
  $primary, $secondary, $accent
  $success, $warning, $error
  $background, $surface, $panel

Text colors:
  $text, $text-muted

Shades:
  $primary-lighten-1, $primary-lighten-2, $primary-lighten-3
  $primary-darken-1, $primary-darken-2, $primary-darken-3

## COMMON CSS PATTERNS

Card:
  .card {
      background: $panel;
      border: round $primary;
      padding: 2;
      margin: 1;
  }

Centered content:
  .centered {
      align: center middle;
      content-align: center middle;
  }

Highlight on hover:
  Button:hover {
      background: $primary-lighten-1;
  }

## LIFECYCLE

def on_load(self):
    # Before DOM ready (async)
    pass

def on_mount(self):
    # DOM ready, setup UI
    pass

def on_unmount(self):
    # Cleanup before exit
    pass

## WORKERS (Async)

@work(exclusive=True)
async def fetch_data(self):
    data = await async_api_call()
    self.update_ui(data)

## ANIMATION

self.animate("opacity", 0.0, duration=0.5)

## NOTIFICATIONS

self.notify("Message")
self.notify("Warning", severity="warning")
self.notify("Error", severity="error")

## FILE STRUCTURE

project/
├── app.py              # Main app
├── styles.tcss         # Stylesheets
├── widgets/            # Custom widgets
│   └── my_widget.py
├── screens/            # Screen definitions
│   └── home.py
└── tests/              # Tests
    └── test_app.py

## BEST PRACTICES

1. Use Header and Footer
2. External CSS file for hot reload
3. ID for unique widgets, classes for groups
4. One widget per task
5. Reactive for state
6. Events for user actions
7. Test with snapshots
8. Use type hints
9. Document with docstrings
10. Keep compose() simple

## DEBUGGING

Run with console:
  textual console

Run app with debugging:
  textual run --dev app.py

Log messages:
  self.log("Debug message")

Show DevTools:
  Press Ctrl+\\ in app

## COMMON ISSUES

Widget not updating:
  - Use reactive attributes
  - Call .refresh() if needed

Layout broken:
  - Check CSS grid-size
  - Verify container hierarchy
  - Use textual console to inspect

Events not firing:
  - Check widget IDs
  - Verify event handler names
  - Check if widget can_focus

## PERFORMANCE TIPS

1. Use workers for slow operations
2. Limit reactive watchers
3. Batch DOM updates
4. Use CSS for styling (not Python)
5. Cache expensive computations

## RESOURCES

Docs: https://textual.textualize.io
Examples: Browse skills/ directory
Templates: Use template_manager.py
Search: Use skill_finder.py

"""


def get_widget_signature(widget_name: str) -> str:
    """Get widget signature and common parameters."""
    signatures = {
        "Button": """Button(
    label: str = "",
    variant: str = "default",  # primary, success, warning, error
    id: str = None,
    classes: str = None,
    disabled: bool = False
)""",
        "Input": """Input(
    value: str = "",
    placeholder: str = "",
    password: bool = False,
    type: str = "text",  # text, integer, number
    max_length: int = None,
    id: str = None,
    classes: str = None
)""",
        "Static": """Static(
    renderable: str = "",
    id: str = None,
    classes: str = None,
    expand: bool = False
)""",
        "DataTable": """DataTable(
    show_header: bool = True,
    show_row_labels: bool = True,
    cursor_type: str = "none",  # none, cell, row, column
    zebra_stripes: bool = False,
    id: str = None
)""",
        "Container": """Container(
    *widgets: Widget,
    id: str = None,
    classes: str = None
)""",
    }
    return signatures.get(widget_name, f"# Signature for {widget_name} not found")


def get_pattern(pattern_name: str) -> str:
    """Get code pattern."""
    patterns = {
        "counter": '''# Counter pattern
count = reactive(0)

def compose(self):
    yield Static("0", id="display")
    yield Button("+", id="inc")
    yield Button("-", id="dec")

def watch_count(self, new_count):
    self.query_one("#display").update(str(new_count))

def on_button_pressed(self, event):
    if event.button.id == "inc":
        self.count += 1
    elif event.button.id == "dec":
        self.count -= 1
''',
        "form": '''# Form pattern
def compose(self):
    yield Input(placeholder="Name", id="name")
    yield Input(placeholder="Email", id="email")
    yield Button("Submit", variant="primary")

def on_button_pressed(self):
    data = {
        "name": self.query_one("#name", Input).value,
        "email": self.query_one("#email", Input).value
    }
    self.submit_form(data)
''',
        "modal": '''# Modal pattern
class ConfirmModal(ModalScreen[bool]):
    def compose(self):
        with Vertical(id="dialog"):
            yield Static("Are you sure?")
            with Horizontal():
                yield Button("Yes", id="yes")
                yield Button("No", id="no")

    def on_button_pressed(self, event):
        self.dismiss(event.button.id == "yes")

# Usage:
async def show_confirm(self):
    result = await self.push_screen_wait(ConfirmModal())
    if result:
        # User confirmed
        pass
''',
    }
    return patterns.get(pattern_name, f"# Pattern '{pattern_name}' not found")


def main():
    """Display quick reference."""
    print(QUICK_REFERENCE)
    print("\n" + "=" * 80)
    print("\nWIDGET SIGNATURES:")
    print("\nButton:")
    print(get_widget_signature("Button"))
    print("\nInput:")
    print(get_widget_signature("Input"))


if __name__ == "__main__":
    main()
