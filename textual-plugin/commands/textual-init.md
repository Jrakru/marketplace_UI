# textual-init

Initialize a new Textual project with a complete, production-ready template structure and configuration.

## Overview

This command scaffolds a new Textual application with best practices, proper structure, and all necessary configuration files for modern TUI development.

## Usage

```
/textual-init <project-name> [options]
```

## Parameters

- **project-name**: Name for the new project (required)
- **--type <type>**: Project type (simple, dashboard, editor, cli-tool, custom)
- **--template <template>**: Template to use (blank, full, minimal, documentation)
- **--python-version <version>**: Python version (3.8, 3.9, 3.10, 3.11, 3.12)
- **--with-tests**: Include test scaffolding
- **--with-docs**: Include documentation structure
- **--install-deps**: Install dependencies after creation

## Examples

### Create Simple TUI App

```
/textual-init my-todo-app --type simple
```

Creates a simple todo application with:
- Basic app structure
- Counter widget example
- Simple styling
- Minimal configuration

### Create Full Dashboard

```
/textual-init system-monitor --type dashboard --with-tests --with-docs
```

Creates a complete dashboard with:
- Multi-panel layout
- Data visualization widgets
- Real-time updates
- Comprehensive testing
- Full documentation

### Create CLI Tool

```
/textual-init my-cli --type cli-tool --python-version 3.11
```

Creates a command-line tool with:
- Command parsing
- Progress indicators
- Status displays
- Error handling

### Create Custom Project

```
/textual-init custom-app --type custom --template full
```

## Project Structure Created

### Basic Structure

```
my_textual_app/
├── main.py                    # Entry point
├── app.py                     # Main App class
├── pyproject.toml             # Project configuration
├── requirements.txt           # Dependencies
├── README.md                  # Documentation
├── .gitignore                 # Git ignore rules
│
├── screens/                   # Screen definitions
│   ├── __init__.py
│   ├── main_screen.py
│   └── settings_screen.py
│
├── widgets/                   # Custom widgets
│   ├── __init__.py
│   ├── navigation.py
│   └── status_bar.py
│
├── models/                    # Data models
│   ├── __init__.py
│   └── data_model.py
│
├── services/                  # Business logic
│   ├── __init__.py
│   └── api_service.py
│
├── styles/                    # Styling
│   ├── main.tcss
│   ├── dark.tcss
│   └── light.tcss
│
├── utils/                     # Utilities
│   ├── __init__.py
│   └── helpers.py
│
└── config/                    # Configuration
    ├── settings.yaml
    └── config.py
```

### Full Structure (with tests and docs)

```
my_textual_app/
├── main.py
├── app.py
├── pyproject.toml
├── requirements.txt
├── requirements-dev.txt       # Dev dependencies
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── .gitignore
├── .pre-commit-config.yaml
│
├── src/                       # Source code
│   └── my_textual_app/
│       ├── __init__.py
│       ├── app.py
│       ├── screens/
│       ├── widgets/
│       ├── models/
│       ├── services/
│       └── utils/
│
├── styles/                    # CSS files
│   ├── main.tcss
│   ├── themes/
│   └── components/
│
├── tests/                     # Tests
│   ├── __init__.py
│   ├── conftest.py
│   ├── unit/
│   ├── integration/
│   └── e2e/
│
├── docs/                      # Documentation
│   ├── index.md
│   ├── user-guide/
│   ├── api/
│   └── examples/
│
├── scripts/                   # Utility scripts
│   ├── build.sh
│   ├── test.sh
│   └── deploy.sh
│
└── examples/                  # Example apps
    ├── example-1.py
    └── example-2.py
```

## Project Templates

### Simple Template

Creates a minimal TUI app with:
- Single screen
- Basic widgets (Button, Input)
- Simple styling
- Basic event handling
- No external dependencies

**Generated Files:**
- `app.py` - Main application
- `main.py` - Entry point
- `requirements.txt` - Basic dependencies
- `styles/main.tcss` - Basic styling

**Use Case:** Learning, prototyping, simple utilities

### Dashboard Template

Creates a dashboard-style app with:
- Multi-panel layout
- Data tables
- Charts/graphs
- Real-time updates
- Settings management

**Generated Files:**
- `app.py` - Main dashboard
- `widgets/chart.py` - Chart widget
- `widgets/data_table.py` - Data table widget
- `models/dashboard_model.py` - Data model
- `services/data_service.py` - Data service
- `styles/dashboard.tcss` - Dashboard styling

**Use Case:** Monitoring, analytics, admin panels

### Editor Template

Creates a text editor with:
- Multi-document interface
- File browser
- Syntax highlighting
- Command palette
- Status bar

**Generated Files:**
- `app.py` - Main editor
- `widgets/editor.py` - Text editor widget
- `widgets/file_tree.py` - File browser
- `widgets/command_palette.py` - Command interface
- `screens/editor_screen.py` - Editor screen
- `services/file_service.py` - File operations

**Use Case:** Code editors, text tools, IDE-like apps

### CLI Tool Template

Creates a command-line tool with:
- Command parsing
- Progress bars
- Tables
- Logging
- Configuration

**Generated Files:**
- `app.py` - Main CLI
- `widgets/progress.py` - Progress indicators
- `widgets/table.py` - Table display
- `services/command_service.py` - Command handling
- `utils/logging.py` - Logging utilities
- `config/cli_config.py` - CLI configuration

**Use Case:** Admin tools, data processing, automation

## Configuration Options

### Python Version Selection

```
/textual-init app --python-version 3.11
```

Creates project configured for specific Python version:
- Sets minimum Python requirement
- Uses appropriate dependency versions
- Configures typing for version

### Testing Options

```
/textual-init app --with-tests
```

Includes:
- Test directory structure
- Pytest configuration
- Sample unit tests
- Integration tests
- Test utilities

### Documentation Options

```
/textual-init app --with-docs
```

Includes:
- MkDocs configuration
- API documentation
- User guides
- Example code
- Contribution guidelines

### Dependency Installation

```
/textual-init app --install-deps
```

Automatically:
- Creates virtual environment
- Installs dependencies
- Sets up development tools
- Runs initial setup

## Features Included

### 1. Modern Python Project Structure

- **pyproject.toml** - Modern Python packaging
- **src/layout** - Proper package structure
- **Type hints** - Full type coverage
- **Documentation** - Comprehensive docs

### 2. Development Tools

- **Black** - Code formatting
- **isort** - Import sorting
- **mypy** - Type checking
- **flake8** - Linting
- **pre-commit** - Git hooks

### 3. Testing Infrastructure

- **Pytest** - Testing framework
- **Coverage** - Test coverage
- **pytest-textual** - TUI testing
- **Hypothesis** - Property testing

### 4. Git Integration

- **.gitignore** - Proper ignore rules
- **.gitattributes** - Git attributes
- **pre-commit hooks** - Automated checks

### 5. CI/CD Ready

- **GitHub Actions** - CI workflow
- **Pre-commit** - Code quality
- **Versioning** - Semantic versioning

### 6. Styling System

- **CSS files** - Organized stylesheets
- **Theme support** - Dark/light themes
- **Component library** - Reusable styles
- **Responsive design** - Adaptive layouts

## Custom Templates

### Creating Custom Template

1. Create template directory:
```
templates/
  my-template/
    app.py
    main.py
    styles/
    requirements.txt
    template.yaml
```

2. Template configuration (template.yaml):
```yaml
name: "My Template"
description: "Custom TUI template"
type: "dashboard"
files:
  - src/app.py
  - src/main.py
  - styles/main.tcss
```

3. Use custom template:
```
/textual-init app --template my-template
```

### Template Variables

Templates can use variables:
- `{{ project_name }}` - Project name
- `{{ author_name }}` - Author name
- `{{ year }}` - Current year
- `{{ python_version }}` - Python version

## Best Practices Included

### 1. Code Organization

```
src/my_app/
├── __init__.py
├── app.py              # Main App
├── screens/            # Screen classes
├── widgets/            # Custom widgets
├── models/             # Data models
├── services/           # Business logic
└── utils/              # Utilities
```

### 2. Separation of Concerns

- **Views** - Widgets and screens
- **Models** - Data and state
- **Services** - Business logic
- **Utils** - Helper functions

### 3. Configuration Management

```python
# config/settings.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "My TUI App"
    debug: bool = False
    theme: str = "dark"

    class Config:
        env_file = ".env"
```

### 4. Error Handling

```python
# app.py
from textual.app import App
from textual.logging import TextualHandler

class MyApp(App):
    async def on_mount(self) -> None:
        # Setup error handling
        self.logger = self.setup_logger()

    def handle_error(self, error: Exception) -> None:
        # Log and display error
        self.logger.exception(error)
```

## Post-Initialization Tasks

After running `textual-init`, you should:

1. **Review Configuration**
   - Check `pyproject.toml`
   - Update settings in `config/`
   - Customize styles

2. **Install Dependencies**
   ```bash
   cd project_name
   pip install -r requirements.txt
   ```

3. **Setup Development Environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   pip install -r requirements-dev.txt
   pre-commit install
   ```

4. **Run Tests**
   ```bash
   pytest tests/
   ```

5. **Start Development**
   ```bash
   python main.py
   ```

## Troubleshooting

### Common Issues

**Issue: Import errors after creation**
```bash
# Solution: Install in development mode
pip install -e .
```

**Issue: Type checking fails**
```bash
# Solution: Update mypy configuration
# Edit pyproject.toml [tool.mypy] section
```

**Issue: CSS not loading**
```python
# Solution: Check CSS_PATH in app.py
class MyApp(App):
    CSS_PATH = "styles/main.tcss"
```

**Issue: Tests fail**
```bash
# Solution: Check Textual installation
pip install textual[test]
```

### Getting Help

If you encounter issues:

1. Check the generated `README.md`
2. Review example code in `examples/`
3. Consult Textual documentation
4. Open an issue on GitHub

## See Also

- [Textual Documentation](https://textual.textualize.dev/)
- [Creating Textual Apps](../skills/creating-textual-apps.md)
- [Textual Widgets Reference](../helpers/textual-widgets-reference.md)
- [Textual Layouts Guide](../helpers/textual-layouts-guide.md)
