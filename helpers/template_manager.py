#!/usr/bin/env python3
"""
Template Manager - Provides templates for common Textual patterns.

This helper provides quick access to code templates for AI agents.
"""

from typing import Dict, List, Optional
from enum import Enum


class TemplateType(Enum):
    """Types of templates available."""
    APP = "app"
    WIDGET = "widget"
    SCREEN = "screen"
    MODAL = "modal"
    TEST = "test"
    CSS = "css"
    EVENT_HANDLER = "event_handler"
    REACTIVE = "reactive"


class TemplateManager:
    """Manage and provide code templates."""

    def __init__(self):
        self.templates = self._load_templates()

    def _load_templates(self) -> Dict:
        """Load all templates."""
        return {
            TemplateType.APP: self._app_templates(),
            TemplateType.WIDGET: self._widget_templates(),
            TemplateType.SCREEN: self._screen_templates(),
            TemplateType.MODAL: self._modal_templates(),
            TemplateType.TEST: self._test_templates(),
            TemplateType.CSS: self._css_templates(),
            TemplateType.EVENT_HANDLER: self._event_handler_templates(),
            TemplateType.REACTIVE: self._reactive_templates(),
        }

    def get_template(
        self,
        template_type: TemplateType,
        variant: str = "basic",
        **kwargs
    ) -> str:
        """
        Get a template.

        Args:
            template_type: Type of template
            variant: Template variant
            **kwargs: Template variables

        Returns:
            Formatted template code
        """
        templates = self.templates.get(template_type, {})
        template = templates.get(variant, templates.get("basic", ""))
        return template.format(**kwargs)

    def list_templates(self, template_type: Optional[TemplateType] = None) -> Dict:
        """List available templates."""
        if template_type:
            return {template_type: list(self.templates[template_type].keys())}
        return {t: list(self.templates[t].keys()) for t in TemplateType}

    def _app_templates(self) -> Dict[str, str]:
        """Application templates."""
        return {
            "basic": '''from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static


class {app_name}(App):
    """A basic Textual application."""

    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Hello, Textual!")
        yield Footer()


if __name__ == "__main__":
    app = {app_name}()
    app.run()
''',
            "with_css": '''from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Button
from textual.containers import Container


class {app_name}(App):
    """A Textual application with CSS."""

    CSS = """
    Screen {{
        background: $surface;
    }}

    Container {{
        padding: 1;
        height: auto;
    }}

    Button {{
        margin: 1;
    }}
    """

    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Static("Welcome!"),
            Button("Click Me", variant="primary"),
        )
        yield Footer()


if __name__ == "__main__":
    app = {app_name}()
    app.run()
''',
            "multi_screen": '''from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Static, Button
from textual.containers import Container


class HomeScreen(Screen):
    """Home screen."""

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Static("Home Screen"),
            Button("Go to Settings", id="settings"),
        )
        yield Footer()

    def on_button_pressed(self) -> None:
        self.app.push_screen("settings")


class SettingsScreen(Screen):
    """Settings screen."""

    BINDINGS = [("escape", "app.pop_screen", "Back")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Static("Settings Screen"),
            Button("Back"),
        )
        yield Footer()

    def on_button_pressed(self) -> None:
        self.app.pop_screen()


class {app_name}(App):
    """Multi-screen application."""

    SCREENS = {{
        "home": HomeScreen,
        "settings": SettingsScreen,
    }}

    def on_mount(self) -> None:
        self.push_screen("home")


if __name__ == "__main__":
    app = {app_name}()
    app.run()
''',
            "with_config": '''from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static
import argparse
import json
from pathlib import Path


class {app_name}(App):
    """Application with configuration."""

    def __init__(self, config_file: str = None, **kwargs):
        super().__init__(**kwargs)
        self.config = self.load_config(config_file)

    def load_config(self, config_file: str = None) -> dict:
        """Load configuration from file."""
        if config_file and Path(config_file).exists():
            with open(config_file) as f:
                return json.load(f)
        return {{"theme": "dark", "debug": False}}

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static(f"Config: {{self.config}}")
        yield Footer()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", help="Config file")
    args = parser.parse_args()

    app = {app_name}(config_file=args.config)
    app.run()


if __name__ == "__main__":
    main()
''',
        }

    def _widget_templates(self) -> Dict[str, str]:
        """Widget templates."""
        return {
            "basic": '''from textual.widget import Widget
from textual.app import ComposeResult
from textual.widgets import Static


class {widget_name}(Widget):
    """A custom widget."""

    DEFAULT_CSS = """
    {widget_name} {{
        width: 100%;
        height: auto;
        background: $panel;
        padding: 1;
    }}
    """

    def compose(self) -> ComposeResult:
        yield Static("Widget content")
''',
            "reactive": '''from textual.widget import Widget
from textual.app import ComposeResult
from textual.widgets import Static, Button
from textual.reactive import reactive
from textual.containers import Horizontal


class {widget_name}(Widget):
    """A reactive widget."""

    DEFAULT_CSS = """
    {widget_name} {{
        width: 100%;
        height: auto;
        background: $panel;
        border: solid $primary;
        padding: 1;
    }}
    """

    {reactive_attr} = reactive({default_value})

    def compose(self) -> ComposeResult:
        with Horizontal():
            yield Static(str(self.{reactive_attr}), id="display")
            yield Button("Update")

    def watch_{reactive_attr}(self, new_value) -> None:
        """Called when {reactive_attr} changes."""
        display = self.query_one("#display", Static)
        display.update(str(new_value))

    def on_button_pressed(self) -> None:
        """Update the reactive attribute."""
        self.{reactive_attr} += 1
''',
            "with_message": '''from textual.widget import Widget
from textual.app import ComposeResult
from textual.widgets import Static, Button
from textual.message import Message


class {widget_name}(Widget):
    """A widget that posts custom messages."""

    class {message_name}(Message):
        """Posted when {event_description}."""

        def __init__(self, data: str) -> None:
            self.data = data
            super().__init__()

    DEFAULT_CSS = """
    {widget_name} {{
        height: auto;
        padding: 1;
    }}
    """

    def compose(self) -> ComposeResult:
        yield Static("Content")
        yield Button("Trigger Event")

    def on_button_pressed(self) -> None:
        """Post custom message."""
        self.post_message(self.{message_name}("value"))
''',
            "container": '''from textual.widget import Widget
from textual.app import ComposeResult
from textual.containers import Vertical


class {widget_name}(Widget):
    """A container widget."""

    DEFAULT_CSS = """
    {widget_name} {{
        width: 100%;
        height: auto;
        background: $panel;
        border: round $primary;
        padding: 1;
    }}
    """

    def __init__(self, *children: Widget, **kwargs):
        super().__init__(**kwargs)
        self._children = children

    def compose(self) -> ComposeResult:
        with Vertical():
            yield from self._children
''',
        }

    def _screen_templates(self) -> Dict[str, str]:
        """Screen templates."""
        return {
            "basic": '''from textual.screen import Screen
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
            Static("Screen content"),
            Button("Action"),
        )
        yield Footer()
''',
            "with_return": '''from textual.screen import Screen
from textual.app import ComposeResult
from textual.widgets import Header, Footer, Static, Button
from textual.containers import Container, Horizontal


class {screen_name}(Screen[{return_type}]):
    """A screen that returns data."""

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Static("Enter data:"),
            # Add input widgets here
            Horizontal(
                Button("Submit", variant="success"),
                Button("Cancel", variant="error"),
            ),
        )
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button press."""
        if event.button.label == "Submit":
            # Collect data and return
            self.dismiss({return_value})
        else:
            self.dismiss(None)
''',
        }

    def _modal_templates(self) -> Dict[str, str]:
        """Modal templates."""
        return {
            "confirm": '''from textual.screen import ModalScreen
from textual.app import ComposeResult
from textual.widgets import Static, Button
from textual.containers import Vertical, Horizontal


class {modal_name}(ModalScreen[bool]):
    """Confirmation modal."""

    CSS = """
    {modal_name} {{
        align: center middle;
    }}

    #dialog {{
        width: 60;
        height: 11;
        background: $panel;
        border: thick $primary;
        padding: 1;
    }}
    """

    def compose(self) -> ComposeResult:
        with Vertical(id="dialog"):
            yield Static("{question}")
            with Horizontal():
                yield Button("Yes", variant="success", id="yes")
                yield Button("No", variant="error", id="no")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.dismiss(event.button.id == "yes")
''',
            "input": '''from textual.screen import ModalScreen
from textual.app import ComposeResult
from textual.widgets import Static, Input, Button, Label
from textual.containers import Vertical, Horizontal


class {modal_name}(ModalScreen[str]):
    """Input modal."""

    CSS = """
    {modal_name} {{
        align: center middle;
    }}

    #dialog {{
        width: 60;
        height: 13;
        background: $panel;
        border: thick $accent;
        padding: 2;
    }}
    """

    def __init__(self, prompt: str = "Enter value:", **kwargs):
        super().__init__(**kwargs)
        self.prompt = prompt

    def compose(self) -> ComposeResult:
        with Vertical(id="dialog"):
            yield Label(self.prompt)
            yield Input(id="input")
            with Horizontal():
                yield Button("Submit", variant="primary")
                yield Button("Cancel")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.label == "Submit":
            value = self.query_one(Input).value
            self.dismiss(value)
        else:
            self.dismiss("")
''',
        }

    def _test_templates(self) -> Dict[str, str]:
        """Test templates."""
        return {
            "snapshot": '''import pytest
from {module} import {app_name}


def test_{test_name}_initial(snap_compare):
    """Test initial state."""
    app = {app_name}()
    assert snap_compare(app)


def test_{test_name}_interaction(snap_compare):
    """Test with user interaction."""
    async def run_before(pilot):
        await pilot.click("#{button_id}")

    app = {app_name}()
    assert snap_compare(app, run_before=run_before)
''',
            "unit": '''import pytest
from {module} import {class_name}


def test_{test_name}_creation():
    """Test widget creation."""
    widget = {class_name}()
    assert widget is not None


def test_{test_name}_reactive():
    """Test reactive attribute."""
    widget = {class_name}()
    widget.{reactive_attr} = {test_value}
    assert widget.{reactive_attr} == {test_value}
''',
        }

    def _css_templates(self) -> Dict[str, str]:
        """CSS templates."""
        return {
            "basic": '''Screen {{
    background: $surface;
}}

Container {{
    padding: 1;
}}

Button {{
    margin: 1;
}}

Button:hover {{
    background: $primary-lighten-1;
}}
''',
            "card": '''.card {{
    background: $panel;
    border: round $primary;
    padding: 2;
    margin: 1;
}}

.card .title {{
    text-style: bold;
    color: $accent;
    margin-bottom: 1;
}}

.card .content {{
    color: $text;
}}
''',
            "grid_layout": '''.grid-container {{
    layout: grid;
    grid-size: {columns};
    grid-gutter: {gutter};
    padding: 1;
}}

.grid-item {{
    background: $panel;
    border: solid $primary;
    height: {item_height};
    content-align: center middle;
}}
''',
        }

    def _event_handler_templates(self) -> Dict[str, str]:
        """Event handler templates."""
        return {
            "button": '''def on_button_pressed(self, event: Button.Pressed) -> None:
    """Handle button press."""
    if event.button.id == "{button_id}":
        {action}
''',
            "input": '''def on_input_changed(self, event: Input.Changed) -> None:
    """Handle input change."""
    value = event.value
    {action}

def on_input_submitted(self, event: Input.Submitted) -> None:
    """Handle input submission."""
    value = event.value
    {action}
''',
            "on_decorator": '''@on(Button.Pressed, "#{button_id}")
def handle_{handler_name}(self) -> None:
    """Handle button press."""
    {action}
''',
        }

    def _reactive_templates(self) -> Dict[str, str]:
        """Reactive attribute templates."""
        return {
            "basic": '''{attr_name} = reactive({default_value})

def watch_{attr_name}(self, new_value) -> None:
    """Called when {attr_name} changes."""
    {action}
''',
            "computed": '''{attr_name} = reactive({default_value})

def compute_{computed_name}(self) -> {return_type}:
    """Compute {computed_name}."""
    return {computation}

def watch_{computed_name}(self, new_value: {return_type}) -> None:
    """Called when {computed_name} changes."""
    {action}
''',
            "validated": '''{attr_name} = reactive({default_value})

def validate_{attr_name}(self, value: {value_type}) -> {value_type}:
    """Validate {attr_name}."""
    {validation}
    return value

def watch_{attr_name}(self, new_value: {value_type}) -> None:
    """Called when {attr_name} changes."""
    {action}
''',
        }


def main():
    """Example usage."""
    manager = TemplateManager()

    # List all templates
    print("Available templates:")
    for template_type, variants in manager.list_templates().items():
        print(f"\n{template_type.value}:")
        for variant in variants:
            print(f"  - {variant}")

    print("\n" + "=" * 80 + "\n")

    # Get a template
    app_code = manager.get_template(
        TemplateType.APP,
        "basic",
        app_name="MyApp"
    )
    print(app_code)


if __name__ == "__main__":
    main()
