#!/usr/bin/env python3
"""
Textual Generator - Helper script for AI agents to generate Textual apps.

This script provides utilities to generate complete Textual applications,
widgets, screens, and boilerplate code.
"""

import json
from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class WidgetSpec:
    """Specification for a widget."""
    widget_type: str
    id: Optional[str] = None
    classes: Optional[List[str]] = None
    properties: Optional[Dict] = None
    children: Optional[List['WidgetSpec']] = None


class TextualGenerator:
    """Generate Textual application code."""

    def __init__(self):
        self.imports = set()

    def generate_app(
        self,
        app_name: str,
        widgets: List[WidgetSpec],
        css: Optional[str] = None,
        bindings: Optional[List[tuple]] = None,
        has_header: bool = True,
        has_footer: bool = True
    ) -> str:
        """
        Generate a complete Textual app.

        Args:
            app_name: Name of the app class
            widgets: List of widget specifications
            css: CSS stylesheet
            bindings: List of (key, action, description) tuples
            has_header: Include header
            has_footer: Include footer

        Returns:
            Complete Python code for the app
        """
        self.imports = {"from textual.app import App, ComposeResult"}

        # Collect imports
        if has_header or has_footer:
            self.imports.add("from textual.widgets import Header, Footer")

        for widget in widgets:
            self._collect_imports(widget)

        # Build code
        code = []
        code.append('"""')
        code.append(f"Generated Textual Application: {app_name}")
        code.append('"""')
        code.append("")

        # Add imports
        for imp in sorted(self.imports):
            code.append(imp)
        code.append("")
        code.append("")

        # App class
        code.append(f"class {app_name}(App):")
        code.append(f'    """A Textual application."""')
        code.append("")

        # CSS
        if css:
            code.append("    CSS = '''")
            code.append(css.rstrip())
            code.append("    '''")
            code.append("")

        # Bindings
        if bindings:
            code.append("    BINDINGS = [")
            for key, action, desc in bindings:
                code.append(f'        ("{key}", "{action}", "{desc}"),')
            code.append("    ]")
            code.append("")

        # Compose method
        code.append("    def compose(self) -> ComposeResult:")
        code.append('        """Create child widgets."""')

        if has_header:
            code.append("        yield Header()")

        for widget in widgets:
            code.extend(self._generate_widget_code(widget, indent=2))

        if has_footer:
            code.append("        yield Footer()")

        code.append("")
        code.append("")

        # Main block
        code.append('if __name__ == "__main__":')
        code.append(f"    app = {app_name}()")
        code.append("    app.run()")

        return "\n".join(code)

    def _collect_imports(self, widget: WidgetSpec) -> None:
        """Collect necessary imports for a widget."""
        # Map widget types to imports
        import_map = {
            "Button": "from textual.widgets import Button",
            "Input": "from textual.widgets import Input",
            "Label": "from textual.widgets import Label",
            "Static": "from textual.widgets import Static",
            "DataTable": "from textual.widgets import DataTable",
            "Tree": "from textual.widgets import Tree",
            "ListView": "from textual.widgets import ListView",
            "ListItem": "from textual.widgets import ListItem",
            "Checkbox": "from textual.widgets import Checkbox",
            "Select": "from textual.widgets import Select",
            "ProgressBar": "from textual.widgets import ProgressBar",
            "Container": "from textual.containers import Container",
            "Horizontal": "from textual.containers import Horizontal",
            "Vertical": "from textual.containers import Vertical",
            "Grid": "from textual.containers import Grid",
        }

        if widget.widget_type in import_map:
            self.imports.add(import_map[widget.widget_type])

        if widget.children:
            for child in widget.children:
                self._collect_imports(child)

    def _generate_widget_code(self, widget: WidgetSpec, indent: int = 0) -> List[str]:
        """Generate code for a widget."""
        lines = []
        indent_str = "    " * indent

        # Build widget instantiation
        parts = [widget.widget_type, "("]
        args = []

        # Add properties
        if widget.properties:
            for key, value in widget.properties.items():
                if isinstance(value, str):
                    args.append(f'{key}="{value}"')
                else:
                    args.append(f'{key}={value}')

        # Add id
        if widget.id:
            args.append(f'id="{widget.id}"')

        # Add classes
        if widget.classes:
            classes_str = " ".join(widget.classes)
            args.append(f'classes="{classes_str}"')

        parts.append(", ".join(args))
        parts.append(")")

        # Container with children
        if widget.children:
            lines.append(f"{indent_str}with {''.join(parts)}:")
            for child in widget.children:
                lines.extend(self._generate_widget_code(child, indent + 1))
        else:
            lines.append(f"{indent_str}yield {''.join(parts)}")

        return lines

    def generate_custom_widget(
        self,
        widget_name: str,
        reactive_attrs: Optional[List[tuple]] = None,
        has_compose: bool = True,
        has_css: bool = True
    ) -> str:
        """
        Generate a custom widget.

        Args:
            widget_name: Name of the widget class
            reactive_attrs: List of (name, default_value) tuples
            has_compose: Generate compose method
            has_css: Generate DEFAULT_CSS

        Returns:
            Custom widget code
        """
        code = []
        code.append('"""')
        code.append(f"Custom Widget: {widget_name}")
        code.append('"""')
        code.append("")
        code.append("from textual.widget import Widget")
        code.append("from textual.app import ComposeResult")

        if reactive_attrs:
            code.append("from textual.reactive import reactive")

        code.append("")
        code.append("")
        code.append(f"class {widget_name}(Widget):")
        code.append(f'    """A custom widget."""')
        code.append("")

        # CSS
        if has_css:
            code.append("    DEFAULT_CSS = '''")
            code.append(f"    {widget_name} {{")
            code.append("        width: 100%;")
            code.append("        height: auto;")
            code.append("        background: $panel;")
            code.append("        border: solid $primary;")
            code.append("        padding: 1;")
            code.append("    }")
            code.append("    '''")
            code.append("")

        # Reactive attributes
        if reactive_attrs:
            for name, default in reactive_attrs:
                if isinstance(default, str):
                    code.append(f'    {name} = reactive("{default}")')
                else:
                    code.append(f'    {name} = reactive({default})')
            code.append("")

        # Compose method
        if has_compose:
            code.append("    def compose(self) -> ComposeResult:")
            code.append('        """Create child widgets."""')
            code.append("        from textual.widgets import Static")
            code.append('        yield Static("Widget content")')
            code.append("")

        # Watch methods for reactive attrs
        if reactive_attrs:
            for name, _ in reactive_attrs:
                code.append(f"    def watch_{name}(self, new_value) -> None:")
                code.append(f'        """Called when {name} changes."""')
                code.append("        pass")
                code.append("")

        return "\n".join(code)

    def generate_screen(
        self,
        screen_name: str,
        is_modal: bool = False,
        return_type: Optional[str] = None,
        bindings: Optional[List[tuple]] = None
    ) -> str:
        """
        Generate a screen.

        Args:
            screen_name: Name of the screen class
            is_modal: Generate ModalScreen
            return_type: Return type for modal
            bindings: List of key bindings

        Returns:
            Screen code
        """
        code = []
        code.append('"""')
        code.append(f"Screen: {screen_name}")
        code.append('"""')
        code.append("")

        if is_modal:
            if return_type:
                code.append("from textual.screen import ModalScreen")
                base = f"ModalScreen[{return_type}]"
            else:
                code.append("from textual.screen import ModalScreen")
                base = "ModalScreen"
        else:
            code.append("from textual.screen import Screen")
            base = "Screen"

        code.append("from textual.app import ComposeResult")
        code.append("from textual.widgets import Header, Footer, Static, Button")
        code.append("from textual.containers import Container")
        code.append("")
        code.append("")
        code.append(f"class {screen_name}({base}):")
        code.append(f'    """A screen."""')
        code.append("")

        # Bindings
        if bindings:
            code.append("    BINDINGS = [")
            for key, action, desc in bindings:
                code.append(f'        ("{key}", "{action}", "{desc}"),')
            code.append("    ]")
            code.append("")

        # Compose
        code.append("    def compose(self) -> ComposeResult:")
        code.append('        """Create screen widgets."""')
        if not is_modal:
            code.append("        yield Header()")
        code.append("        yield Container(")
        code.append('            Static("Screen content"),')
        code.append('            Button("Action", variant="primary"),')
        code.append("        )")
        if not is_modal:
            code.append("        yield Footer()")
        code.append("")

        # Button handler for modal
        if is_modal:
            code.append("    def on_button_pressed(self) -> None:")
            code.append('        """Handle button press."""')
            if return_type:
                code.append(f"        self.dismiss({return_type}())")
            else:
                code.append("        self.dismiss()")

        return "\n".join(code)

    def generate_test(
        self,
        app_name: str,
        test_scenarios: Optional[List[Dict]] = None
    ) -> str:
        """
        Generate pytest tests for an app.

        Args:
            app_name: Name of the app to test
            test_scenarios: List of test scenario dicts

        Returns:
            Test code
        """
        code = []
        code.append('"""')
        code.append(f"Tests for {app_name}")
        code.append('"""')
        code.append("")
        code.append("import pytest")
        code.append(f"from app import {app_name}")
        code.append("")
        code.append("")

        # Basic test
        code.append(f"def test_{app_name.lower()}_initial(snap_compare):")
        code.append(f'    """Test initial state of {app_name}."""')
        code.append(f"    app = {app_name}()")
        code.append("    assert snap_compare(app)")
        code.append("")
        code.append("")

        # Add scenario tests
        if test_scenarios:
            for i, scenario in enumerate(test_scenarios, 1):
                name = scenario.get("name", f"scenario_{i}")
                interactions = scenario.get("interactions", [])

                code.append(f"def test_{app_name.lower()}_{name}(snap_compare):")
                code.append(f'    """Test {name}."""')
                code.append("    async def run_before(pilot):")
                for interaction in interactions:
                    code.append(f"        {interaction}")
                code.append("")
                code.append(f"    app = {app_name}()")
                code.append("    assert snap_compare(app, run_before=run_before)")
                code.append("")
                code.append("")

        return "\n".join(code)


def main():
    """Example usage."""
    generator = TextualGenerator()

    # Generate simple app
    widgets = [
        WidgetSpec("Button", id="click_me", properties={"label": "Click Me!"}),
        WidgetSpec("Static", id="output", properties={"text": "Output here"}),
    ]

    css = """
    Button {
        margin: 1;
    }

    #output {
        height: 5;
        border: solid green;
        padding: 1;
    }
    """

    app_code = generator.generate_app(
        "SimpleApp",
        widgets=widgets,
        css=css,
        bindings=[("q", "quit", "Quit")],
    )

    print(app_code)
    print("\n" + "=" * 80 + "\n")

    # Generate custom widget
    widget_code = generator.generate_custom_widget(
        "Counter",
        reactive_attrs=[("count", 0), ("label", "Count")],
    )

    print(widget_code)


if __name__ == "__main__":
    main()
