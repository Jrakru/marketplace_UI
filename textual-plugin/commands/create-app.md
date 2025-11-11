# /create-app

Create new Textual TUI applications with pre-built templates and scaffolding.

## Usage

```
/create-app [options] <app_name>
```

## Parameters

### Required
- `app_name`: Name for your new Textual application (will be used as directory name)

### Optional Flags

- `--template <type>` - Application template to use
- `--directory <path>` - Target directory for the application
- `--with-examples` - Include example widgets and features
- `--python-version <version>` - Python version requirement (default: 3.8+)
- `--package-manager <manager>` - Choose pip/poetry/conda (default: pip)

## Templates

### Basic
Simple TUI application with a single screen and basic widget.
```python
from textual.app import App
from textual.widgets import Label

class BasicApp(App):
    def compose(self):
        yield Label("Hello, Textual!")

if __name__ == "__main__":
    app = BasicApp()
    app.run()
```

### Dashboard
Multi-screen dashboard with navigation and status widgets.
- Sidebar navigation
- Status bar
- Content area with multiple widgets
- Clock and system info display

### Todo App
Interactive todo list application with full CRUD operations.
- Text input for adding todos
- Checkbox widgets for completion
- List display with selection
- File persistence

### Data Viewer
Table-based data visualization application.
- CSV/JSON data loading
- Sortable columns
- Search and filter capabilities
- Export functionality

### Chat Interface
Multi-user chat application with real-time messaging.
- Message history
- User list
- Input area
- Auto-scroll behavior

### File Manager
Terminal-based file browser with navigation.
- Directory tree view
- File operations (copy, move, delete)
- Preview pane
- Search functionality

## Project Structure

When creating an application, the following structure is generated:

```
<app_name>/
├── src/
│   ├── <app_name>/
│   │   ├── __init__.py
│   │   ├── app.py          # Main application class
│   │   ├── screens/        # Screen classes
│   │   ├── widgets/        # Custom widgets
│   │   ├── services/       # Business logic
│   │   └── models/         # Data models
├── tests/
│   ├── __init__.py
│   ├── test_app.py
│   └── test_widgets.py
├── docs/
│   └── README.md
├── pyproject.toml
├── requirements.txt
├── .gitignore
├── Makefile
└── README.md
```

## Examples

### Create a basic app
```bash
# Create in current directory
/create-app my_first_app

# Create in specific directory
/create-app --directory ~/projects my_first_app
```

### Create with template
```bash
# Create a dashboard app
/create-app --template dashboard system_monitor

# Create a todo app with examples
/create-app --template todo --with-examples task_manager
```

### Create with package manager
```bash
# Use Poetry for dependency management
/create-app --package-manager poetry my_app

# Create with Python 3.11 requirement
/create-app --python-version 3.11 my_app
```

## Configuration Options

### Template Customization
Each template can be customized with additional options:

```bash
# Dashboard with specific widgets
/create-app --template dashboard \
    --dashboard-widgets "clock,system_info,network_status" \
    --with-sidebar \
    my_monitor
```

### Widget Selection
Choose specific widgets to include:

```bash
# Create app with selected widgets
/create-app --widgets "button,input,table,tabs" \
    my_custom_app
```

## Advanced Features

### Custom Styling
Templates include pre-configured CSS files:
- `theme.css` - Main theme configuration
- `dark.theme` - Dark mode styles
- `light.theme` - Light mode styles

### State Management
- Built-in state persistence
- Session management
- Configuration loading

### Testing Setup
- Pytest configuration
- Widget testing utilities
- App testing helpers
- Coverage reporting

## Generated Files

### Core Files

**app.py**
```python
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Label

class <AppName>App(App):
    """Main application class."""

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Label("Welcome to <AppName>!")
        yield Footer()

    def on_mount(self) -> None:
        """Called when the app is first mounted."""
        pass

if __name__ == "__main__":
    app = <AppName>App()
    app.run()
```

**pyproject.toml**
```toml
[project]
name = "<app_name>"
version = "0.1.0"
description = "A Textual TUI application"
authors = [
    {name = "Your Name", email = "your.email@example.com"},
]
requires-python = ">=3.8"
dependencies = [
    "textual>=0.40.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0",
    "pytest-cov>=4.0",
    "black>=23.0",
    "isort>=5.0",
]

[build-system]
requires = ["setuptools>=64", "wheel"]
build-backend = "setuptools.build_meta"

[tool.black]
line-length = 88
target-version = ['py38']

[tool.isort]
profile = "black"

[tool.pytest.ini_options]
testpaths = ["tests"]
```

### Documentation

**README.md**
- Project description
- Installation instructions
- Usage examples
- Development setup
- Contributing guidelines

## Post-Creation Steps

After creating an app, the following commands are run automatically:

```bash
cd <app_name>
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e ".[dev]"
```

## Troubleshooting

### Common Issues

**Issue: Permission denied when creating directory**
```
Solution: Check directory permissions or use --directory flag to specify a writable location
```

**Issue: Template not found**
```
Solution: Ensure you have the latest Textual templates installed:
pip install --upgrade textual
```

**Issue: Python version mismatch**
```
Solution: Check your Python version:
python --version
Use --python-version flag to specify correct version
```

### Error Messages

**"Invalid app name"**
- App names must be valid Python identifiers
- Must not contain spaces or special characters
- Cannot be a Python reserved word

**"Template failed to generate"**
- Check disk space
- Verify template files exist: `pip show textual`
- Try with `--verbose` flag for more details

**"Dependencies installation failed"**
- Check internet connection
- Verify package manager availability
- Try using different package manager: `--package-manager`

### Getting Help

If you encounter issues:

1. Check the generated `README.md` for template-specific instructions
2. Review Textual documentation: https://textual.textualize.io/
3. Join the Textual Discord: https://discord.gg/textual
4. Report issues on GitHub: https://github.com/Textualize/textual

## Integration

This command integrates with:
- Textual documentation links
- Template repository updates
- Version compatibility checks
- Dependency resolution

## See Also

- `/validate-structure` - Validate your Textual application structure
- `/deploy-app` - Deploy your Textual application
- Textual Documentation: https://textual.textualize.io/
- Textual Examples: https://github.com/Textualize/textual/tree/main/examples
