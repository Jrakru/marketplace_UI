"""
Skill: Getting Started with Textual

This skill provides the foundation for creating basic Textual applications.
It covers project setup, basic app structure, and the event loop.
"""

from textual.app import App
from textual.widgets import Header, Footer, Static


# ============================================================================
# BASIC TEXTUAL APP TEMPLATE
# ============================================================================

class BasicTextualApp(App):
    """A minimal Textual application."""

    CSS = """
    Screen {
        background: $surface;
    }

    Static {
        width: 100%;
        height: 100%;
        content-align: center middle;
        color: $text;
    }
    """

    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    def compose(self):
        """Create child widgets for the app."""
        yield Header()
        yield Static("Hello, Textual!")
        yield Footer()


# ============================================================================
# APP WITH HOT RELOAD SUPPORT
# ============================================================================

class DevelopmentApp(App):
    """
    App configured for development with hot reload.

    Run with: textual run --dev app.py
    """

    CSS_PATH = "styles.tcss"  # External stylesheet for hot reload

    def compose(self):
        yield Header()
        yield Static("Hot reload enabled!")
        yield Footer()


# ============================================================================
# ASYNC APP EXAMPLE
# ============================================================================

class AsyncApp(App):
    """
    Demonstrates async/await patterns in Textual.
    Textual is built on asyncio.
    """

    async def on_mount(self):
        """Called when app is mounted."""
        # You can use await here for async operations
        await self.run_async_task()

    async def run_async_task(self):
        """Example async task."""
        import asyncio
        await asyncio.sleep(1)
        self.notify("Async task completed!")


# ============================================================================
# HELPER FUNCTIONS FOR AI AGENTS
# ============================================================================

def create_basic_app(app_name="MyApp", title="My Textual App"):
    """
    Generate a basic Textual app template.

    Args:
        app_name: Class name for the app
        title: Display title for the app

    Returns:
        str: Python code for a basic app
    """
    template = f'''from textual.app import App
from textual.widgets import Header, Footer, Static


class {app_name}(App):
    """A Textual application."""

    TITLE = "{title}"

    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    def compose(self):
        yield Header()
        yield Static("Hello from {app_name}!")
        yield Footer()


if __name__ == "__main__":
    app = {app_name}()
    app.run()
'''
    return template


def create_project_structure(project_name):
    """
    Generate recommended project structure.

    Returns:
        dict: Directory structure with file templates
    """
    return {
        "structure": f"""
{project_name}/
├── {project_name}/
│   ├── __init__.py
│   ├── app.py           # Main application
│   ├── styles.tcss      # Stylesheets
│   ├── widgets/         # Custom widgets
│   │   └── __init__.py
│   └── screens/         # Screen definitions
│       └── __init__.py
├── tests/
│   ├── __init__.py
│   └── test_app.py
├── requirements.txt
├── pyproject.toml
└── README.md
        """,
        "requirements.txt": "textual>=0.50.0\npytest>=7.0.0\npytest-asyncio>=0.21.0\npytest-textual-snapshot>=1.0.0",
        "pyproject.toml": f"""[project]
name = "{project_name}"
version = "0.1.0"
description = "A Textual TUI application"
dependencies = ["textual>=0.50.0"]

[project.optional-dependencies]
dev = ["pytest>=7.0.0", "pytest-asyncio>=0.21.0", "pytest-textual-snapshot>=1.0.0"]
"""
    }


# ============================================================================
# QUICK START GUIDE
# ============================================================================

QUICK_START_GUIDE = """
TEXTUAL QUICK START GUIDE
=========================

1. INSTALLATION
   pip install textual textual-dev

2. CREATE YOUR FIRST APP
   - Import App and widgets
   - Create an App subclass
   - Implement compose() method
   - Add widgets via yield
   - Run with app.run()

3. DEVELOPMENT WORKFLOW
   - Use 'textual run --dev app.py' for hot reload
   - Create external .tcss file for styles
   - Use textual console for debugging
   - Press Ctrl+\\ for DevTools

4. KEY CONCEPTS
   - Everything is a widget
   - Widgets are composed in compose()
   - Styles via CSS (TCSS)
   - Events via on_* methods
   - Async by default

5. NEXT STEPS
   - Explore built-in widgets
   - Learn CSS styling
   - Understand events and messages
   - Add custom widgets
"""


if __name__ == "__main__":
    # Example: Create and run basic app
    app = BasicTextualApp()
    app.run()
