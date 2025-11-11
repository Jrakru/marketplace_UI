# /validate-structure

Validate Textual application code for best practices, structure, and common issues.

## Usage

```
/validate-structure [options] <path>
```

## Parameters

### Required
- `path`: Path to the Textual application directory or file to validate

### Optional Flags

- `--strict` - Enable strict validation mode with all checks
- `--level <level>` - Validation level: basic, standard, or strict (default: standard)
- `--report-format <format>` - Output format: text, json, or html (default: text)
- `--output <file>` - Save report to file
- `--no-color` - Disable colored output
- `--exclude <patterns>` - Comma-separated patterns to exclude from validation

## Validation Checks

### Code Quality

#### Import Structure
- ✓ Validates proper import statements
- ✓ Checks for circular imports
- ✓ Verifies Textual version compatibility
- ✓ Validates widget availability

```python
# Good - Clean imports
from textual.app import App, ComposeResult
from textual.widgets import Button, Input
from textual.containers import Container

# Bad - Unused imports and version issues
import textual  # Version check needed
from textual.widgets import *  # Wildcard imports
```

#### Class Structure
- ✓ Validates App class inheritance
- ✓ Checks for required methods (compose, on_mount)
- ✓ Verifies proper type hints
- ✓ Ensures event handler naming conventions

```python
# Good - Proper structure
class MyApp(App):
    """Application description."""

    def compose(self) -> ComposeResult:
        """Create child widgets."""
        yield Container(Button("Click me"))

    def on_mount(self) -> None:
        """Initialize app on mount."""
        self.title = "My App"
```

### Widget Validation

#### Widget Composition
- ✓ Validates widget hierarchy
- ✓ Checks for deprecated widgets
- ✓ Verifies widget properties
- ✓ Ensures proper container usage

```python
# Good - Valid widget structure
def compose(self) -> ComposeResult:
    with Container(id="main"):
        yield Button("Submit", variant="primary")
        yield Input(placeholder="Enter text")

# Bad - Invalid widget structure
def compose(self) -> ComposeResult:
    yield Button("Text")  # Missing required props
    with Container:  # Missing parentheses
        yield "invalid"  # String instead of widget
```

#### Layout Validation
- ✓ Checks CSS classes and IDs
- ✓ Validates responsive design patterns
- ✓ Verifies layout constraints
- ✓ Ensures proper alignment

```css
/* Good - Valid CSS */
#main {
    dock: top;
    height: 3;
}

.button-panel {
    align: center middle;
}

/* Bad - Invalid CSS */
#main {
    dock: invalid-value;  # Not a valid dock position
    height: auto;  # Auto height not always supported
}
```

### Best Practices

#### Performance
- ✓ Identifies inefficient rendering patterns
- ✓ Checks for memory leaks
- ✓ Validates event handler cleanup
- ✓ Suggests optimizations

```python
# Good - Efficient rendering
class MyApp(App):
    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.query_one("#status", Label).update("Processing...")

# Bad - Inefficient rendering
class MyApp(App):
    def on_button_pressed(self, event: Button.Pressed) -> None:
        for widget in self.query("*"):  # Querying all widgets
            if isinstance(widget, Label):
                widget.update("Processing...")
```

#### Event Handling
- ✓ Validates event handler signatures
- ✓ Checks for proper event propagation
- ✓ Ensures async/sync consistency
- ✓ Verifies event cleanup

```python
# Good - Proper event handling
def on_key(self, event: Key) -> None:
    if event.key == "q":
        self.exit()

# Bad - Improper event handling
def on_key(self, event):  # Missing type hint
    if event.key == "q":
        exit()  # Should use self.exit()
```

### Structure Validation

#### File Organization
- ✓ Validates project structure
- ✓ Checks module organization
- ✓ Verifies configuration files
- ✓ Ensures proper separation of concerns

```
Valid Structure:
my_app/
├── src/my_app/
│   ├── __init__.py
│   ├── app.py
│   ├── screens/
│   ├── widgets/
│   └── services/
├── tests/
├── docs/
├── pyproject.toml
└── README.md

Invalid Structure:
my_app/
├── main.py  # Should be in src/my_app/
├── utils.py  # Scattered modules
├── config.json  # Configuration in root
```

#### Configuration
- ✓ Validates pyproject.toml structure
- ✓ Checks dependency versions
- ✓ Verifies entry points
- ✓ Ensures proper packaging

## Validation Levels

### Basic
Minimal checks for critical issues:
- Import errors
- Basic syntax validation
- Required file structure

### Standard (Default)
Comprehensive validation:
- All basic checks
- Widget structure validation
- Event handler validation
- Performance checks
- Documentation requirements

### Strict
Maximum validation:
- All standard checks
- Style enforcement
- Advanced performance optimization
- Full type checking
- Security considerations

## Examples

### Basic validation
```bash
# Validate current directory
/validate-structure .

# Validate specific file
/validate-structure src/my_app/app.py

# Validate with custom path
/validate-structure /path/to/textual/app
```

### Advanced validation
```bash
# Strict mode validation
/validate-structure --strict /path/to/app

# Custom validation level
/validate-structure --level strict my_app

# Generate JSON report
/validate-structure --report-format json --output report.json my_app

# Exclude specific patterns
/validate-structure --exclude "tests/*,docs/*" my_app
```

## Output Formats

### Text Output (Default)
```
✓ Validation Report for my_app

Files Validated: 12
Warnings: 3
Errors: 1

✗ src/my_app/app.py:45
  Error: Missing type hint for event handler parameter
  → def on_button_pressed(self, event):

⚠ src/my_app/widgets/custom.py:23
  Warning: Consider using compose() instead of __init__()
  → def __init__(self):

✓ src/my_app/app.py:30
  Info: Good widget composition pattern
  → yield Container(Button("Submit"))
```

### JSON Output
```json
{
  "validation_summary": {
    "total_files": 12,
    "files_validated": 12,
    "errors": 1,
    "warnings": 3,
    "infos": 5
  },
  "issues": [
    {
      "file": "src/my_app/app.py",
      "line": 45,
      "type": "error",
      "category": "type_hints",
      "message": "Missing type hint for event handler parameter",
      "suggestion": "Add type hint: def on_button_pressed(self, event: Button.Pressed) -> None:"
    }
  ],
  "recommendations": [
    "Consider using compose() instead of __init__() for widget initialization"
  ]
}
```

### HTML Output
Generates an HTML report with:
- Color-coded issues
- Filterable sections
- Code snippets with highlighting
- Summary statistics

## Common Issues and Solutions

### Import Errors

**Issue: Module not found**
```python
from textual.widgets import NonExistentWidget  # Error
```
```
Solution: Check Textual version and widget availability
```

**Issue: Version incompatibility**
```python
from textual.app import App  # Textual < 0.40.0
```
```
Solution: Update Textual or use compatible version
```

### Widget Issues

**Issue: Widget composition error**
```python
def compose(self) -> ComposeResult:
    yield Button("Text", id="submit", variant="primary", disabled=True)
```
```
Solution: Check widget documentation for supported properties
```

**Issue: Invalid container nesting**
```python
def compose(self) -> ComposeResult:
    with Container():
        with Container():  # Nested containers
            yield Button()
```
```
Solution: Simplify widget hierarchy or use proper container types
```

### Event Handling Issues

**Issue: Unhandled exception**
```python
def on_button_pressed(self, event: Button.Pressed) -> None:
    raise Exception("Error")  # Unhandled
```
```
Solution: Use try-except or proper error handling
```

**Issue: Missing event type**
```python
def on_key(self, event):  # Missing type hint
    pass
```
```
Solution: Import and use proper event type:
from textual.events import Key
def on_key(self, event: Key) -> None:
```

## Best Practices Enforcement

### Code Style
- ✓ PEP 8 compliance
- ✓ Type hint usage
- ✓ Docstring standards
- ✓ Consistent naming conventions

### Architecture
- ✓ Separation of concerns
- ✓ Single responsibility principle
- ✓ DRY (Don't Repeat Yourself)
- ✓ Dependency injection patterns

### Performance
- ✓ Efficient widget queries
- ✓ Proper event handling
- ✓ Memory management
- ✓ Render optimization

### Testing
- ✓ Test coverage requirements
- ✓ Widget testing patterns
- ✓ Event simulation
- ✓ Integration testing

## Custom Rules

You can create custom validation rules:

```python
# custom_validator.py
from textual_dev import ValidationRule

class CustomRule(ValidationRule):
    name = "no_direct_time_sleep"
    description = "Avoid time.sleep() in event handlers"

    def check(self, node):
        if self.is_time_sleep(node):
            return self.warning(
                "Use asyncio.sleep() instead of time.sleep() in event handlers"
            )
```

## Integration

This command integrates with:
- Textual CLI tools
- Pre-commit hooks
- CI/CD pipelines
- IDE plugins

## See Also

- `/create-app` - Create new Textual applications
- `/deploy-app` - Deploy Textual applications
- Textual Best Practices: https://textual.textualize.io/guide/
- Textual API Reference: https://textual.textualize.io/api/
