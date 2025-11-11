# Textual Development Helper Scripts

A comprehensive suite of helper scripts for Textual TUI application development. These tools streamline the development process from generation to deployment.

## 📦 Scripts Overview

### 1. `textual-generator.py` - Application Generator

Generate Textual TUI applications from templates with best practices built-in.

**Features:**
- Basic TUI application templates
- Widget-based templates (Button, Input, Table, ListView, DataGrid)
- Layout templates (Horizontal, Vertical, Grid, Sidebar)
- Interactive application templates
- Professional code structure

**Usage:**

```bash
# Generate a basic app
python textual-generator.py --type basic --name MyApp

# Generate a widget-based app
python textual-generator.py --type widget --name MyWidget --widget button

# Generate a layout-based app
python textual-generator.py --type layout --name MyLayout --layout grid

# Generate an interactive app with tabs and controls
python textual-generator.py --type interactive --name MyInteractive

# Custom output directory
python textual-generator.py --type basic --name MyApp --output ./apps
```

**Available Widgets:**
- `button` - Interactive buttons
- `input` - Text input fields
- `table` - Table display
- `listview` - List view component
- `datagrid` - Advanced data grid

**Available Layouts:**
- `horizontal` - Side-by-side layout
- `vertical` - Stacked layout
- `grid` - Grid-based layout
- `sidebar` - Sidebar navigation layout

---

### 2. `textual-validator.py` - Code Validator

Validate Textual applications for proper structure, best practices, and common issues.

**Features:**
- Widget validation and compatibility checks
- Layout structure validation
- Event handler validation
- CSS styling validation
- Best practices recommendations
- Performance hints
- Auto-fix capabilities

**Usage:**

```bash
# Validate a single file
python textual-validator.py app.py

# Verbose output
python textual-validator.py --verbose app.py

# Auto-fix issues
python textual-validator.py --fix app.py

# Scan directory
python textual-validator.py --dir ./src

# Recursive scan
python textual-validator.py --dir ./src --recursive

# Custom file pattern
python textual-validator.py --dir ./apps --pattern "*.py" --recursive
```

**Validation Checks:**
- ✅ Required imports (App, ComposeResult)
- ✅ Class structure (inheritance from App)
- ✅ Method definitions (compose, on_mount, etc.)
- ✅ Widget compatibility
- ✅ CSS syntax
- ✅ Event handler patterns
- ✅ Performance best practices

---

### 3. `textual-debug.py` - Debugging Utilities

Comprehensive debugging and diagnostic tools for Textual applications.

**Features:**
- Widget tree inspection
- Event debugging and tracing
- Layout structure analysis
- Performance profiling
- Error diagnosis
- Live debugging mode

**Usage:**

```bash
# Inspect widget tree
python textual-debug.py --inspect app.py

# Trace event handlers
python textual-debug.py --events app.py

# Analyze layout structure
python textual-debug.py --layout app.py

# Profile performance
python textual-debug.py --profile app.py

# Full analysis
python textual-debug.py --analyze app.py --verbose

# Live debug mode
python textual-debug.py --live app.py --verbose

# Save report to file
python textual-debug.py --analyze app.py --output debug_report.txt

# Log events to file
python textual-debug.py --events app.py --log events.log
```

**Debug Modes:**
- **Inspect**: View widget hierarchy and structure
- **Events**: Trace event handler calls
- **Layout**: Analyze layout performance and issues
- **Profile**: Measure performance metrics
- **Live**: Interactive debugging session

---

### 4. `textual-deploy.py` - Deployment Utilities

Complete deployment and distribution toolkit for Textual applications.

**Features:**
- Static HTML export
- Docker containerization
- PyInstaller packaging
- Distribution helpers
- Version management
- Build optimization

**Usage:**

```bash
# Export to HTML
python textual-deploy.py --export-html app.py

# Create Docker image
python textual-deploy.py --docker app.py

# Package with PyInstaller
python textual-deploy.py --package app.py

# Create distribution package
python textual-deploy.py --dist app.py

# Create launcher script
python textual-deploy.py --script app.py

# Run all deployment steps
python textual-deploy.py --all app.py

# Show app information
python textual-deploy.py --info app.py

# Optimize for production
python textual-deploy.py --optimize app.py --optimized-output optimized.py

# Check dependencies
python textual-deploy.py --check-deps app.py

# Custom output directory
python textual-deploy.py --all app.py --output ./build
```

**Deployment Options:**
- **HTML Export**: Create static HTML version
- **Docker**: Containerized deployment
- **PyInstaller**: Standalone executable
- **Distribution**: Complete package with docs
- **Launcher Script**: Easy-to-run shell script

---

## 🚀 Quick Start

### 1. Generate a New App

```bash
cd textual-plugin/helpers
python textual-generator.py --type interactive --name MyApp --output ../examples
```

### 2. Validate the Code

```bash
python textual-validator.py ../examples/MyApp.py --verbose
```

### 3. Debug and Profile

```bash
python textual-debug.py --profile ../examples/MyApp.py --output profiling.txt
```

### 4. Deploy

```bash
python textual-deploy.py --all ../examples/MyApp.py --output ./build
```

---

## 📁 Project Structure

```
textual-plugin/helpers/
├── textual-generator.py   # Application generator
├── textual-validator.py   # Code validator
├── textual-debug.py       # Debugging utilities
├── textual-deploy.py      # Deployment utilities
└── README.md             # This file
```

---

## 🔧 Installation

These scripts work with Python 3.7+ and require Textual:

```bash
# Install Textual
pip install textual

# Install optional dependencies for deployment
pip install pyinstaller
pip install 'textual[web]'  # For HTML export
```

---

## 💡 Best Practices

### 1. Use Generator Templates
Start with generator templates to ensure proper structure:
- Basic template for simple apps
- Widget templates for specific functionality
- Layout templates for complex UIs
- Interactive template for full-featured apps

### 2. Validate Before Deploy
Always validate your code:
```bash
python textual-validator.py --fix app.py
python textual-validator.py --verbose app.py
```

### 3. Debug Performance Issues
Profile your app before deployment:
```bash
python textual-debug.py --profile --analyze app.py
```

### 4. Use Docker for Distribution
Docker ensures consistent deployment:
```bash
python textual-deploy.py --docker app.py
cd dist/docker
docker build -t my-app .
docker run -it my-app
```

---

## 🎯 Examples

### Example 1: Complete Workflow

```bash
# 1. Generate app
python textual-generator.py --type interactive --name TaskManager

# 2. Validate
python textual-validator.py --fix TaskManager.py --verbose

# 3. Debug
python textual-debug.py --analyze TaskManager.py --output debug_report.txt

# 4. Deploy
python textual-deploy.py --all TaskManager.py --output ./build
```

### Example 2: Widget-Specific Development

```bash
# Generate button-based app
python textual-generator.py --type widget --name ButtonDemo --widget button

# Validate
python textual-validator.py ButtonDemo.py

# Debug events
python textual-debug.py --events ButtonDemo.py

# Package
python textual-deploy.py --package ButtonDemo.py
```

### Example 3: Layout Development

```bash
# Generate grid layout
python textual-generator.py --type layout --name GridDemo --layout grid

# Analyze layout
python textual-debug.py --layout GridDemo.py

# Deploy as Docker
python textual-deploy.py --docker GridDemo.py
```

---

## 🔍 Validation Rules

The validator checks for:

### Imports
- ✅ `from textual.app import App`
- ✅ `from textual.app import ComposeResult` (recommended)
- ✅ Proper widget imports

### Class Structure
- ✅ Class inherits from `App`
- ✅ `compose()` method exists
- ✅ Return type hint on `compose()`

### Widgets
- ✅ Valid widget types
- ✅ No deprecated widgets
- ✅ Proper widget usage

### CSS
- ✅ Proper syntax
- ✅ Balanced braces
- ✅ No imports (not supported)

### Event Handlers
- ✅ Proper method signatures
- ✅ Valid event types

### Performance
- ✅ Cached queries
- ✅ Minimal DOM access
- ✅ Efficient CSS

---

## 🐛 Debugging Tips

### Widget Tree Issues
```bash
python textual-debug.py --inspect --verbose app.py
```
Look for:
- Excessive nesting (>5 levels)
- Missing containers
- Improper widget placement

### Event Handler Problems
```bash
python textual-debug.py --events app.py
```
Check:
- Event handler signatures
- Event type names
- Handler execution order

### Layout Performance
```bash
python textual-debug.py --layout app.py
```
Analyze:
- Container usage
- Nesting depth
- CSS efficiency

### Performance Issues
```bash
python textual-debug.py --profile app.py --iterations 10
```
Profile:
- Function call counts
- Time per function
- Cumulative time

---

## 📦 Deployment Strategies

### 1. Local Development
```bash
python textual-generator.py --type basic --name dev-app
python textual-validator.py dev-app.py
```

### 2. Testing
```bash
python textual-deploy.py --docker app.py
docker run -it --rm app-image
```

### 3. Production
```bash
python textual-deploy.py --package app.py --optimize
```

### 4. Distribution
```bash
python textual-deploy.py --dist app.py
# Shares build/app-package.zip
```

---

## 🛠️ Customization

### Adding Custom Templates

Edit `textual-generator.py` to add new templates:

```python
CUSTOM_TEMPLATE = '''
class {class_name}(App):
    """Custom app template."""
    def compose(self) -> ComposeResult:
        yield Header()
        yield Container()
        yield Footer()
'''

# Add to WIDGET_TEMPLATES or LAYOUT_TEMPLATES
```

### Custom Validation Rules

Edit `textual-validator.py` to add new checks:

```python
def _validate_custom(self) -> None:
    """Custom validation rule."""
    for node in ast.walk(self.ast_tree):
        if isinstance(node, ast.CustomNode):
            self.warnings.append("Custom rule triggered")
```

---

## 📊 Performance Metrics

The debugger provides:
- Function call counts
- Execution time per function
- Cumulative time
- Memory usage (in development)
- Widget render times

---

## 🐳 Docker Integration

Each deployment creates:
- `Dockerfile`
- `requirements.txt`
- `.dockerignore`
- `.docker/` directory with all files

Build and run:
```bash
cd dist/docker
docker build -t my-app .
docker run -it my-app
```

---

## 📚 Additional Resources

- [Textual Documentation](https://textual.textualize.dev/)
- [Textual GitHub](https://github.com/Textualize/textual)
- [Textual Examples](https://github.com/Textualize/textual/tree/main/examples)

---

## 🤝 Contributing

To contribute:
1. Add new features to appropriate scripts
2. Update this README
3. Test with various app types
4. Follow Python best practices

---

## 📝 License

These helper scripts are part of the Textual plugin project and follow the same license terms.

---

## ⚡ Tips & Tricks

### 1. Use Verbose Mode
Always use `--verbose` for detailed output:
```bash
python textual-validator.py --verbose app.py
```

### 2. Save Reports
Save analysis reports:
```bash
python textual-debug.py --analyze app.py --output report.txt
```

### 3. Batch Processing
Validate multiple files:
```bash
python textual-validator.py --dir ./apps --recursive
```

### 4. Auto-Fix
Use auto-fix for common issues:
```bash
python textual-validator.py --fix --verbose app.py
```

### 5. Check Dependencies
Before deployment:
```bash
python textual-deploy.py --check-deps app.py
```

---

## 🔧 Troubleshooting

### Import Errors
```bash
pip install textual
```

### PyInstaller Not Found
```bash
pip install pyinstaller
```

### HTML Export Fails
```bash
pip install 'textual[web]'
```

### Permission Denied
```bash
chmod +x textual-*.py
```

### Docker Build Fails
- Check `dist/docker/` directory exists
- Ensure `requirements.txt` is present
- Verify app file is copied

---

## 📞 Support

For issues or questions:
1. Check validation reports
2. Review debug output
3. Consult Textual documentation
4. Open an issue in the project repository

---

## 🎓 Learning Path

1. **Start with Generator**: Use `textual-generator.py` to create apps
2. **Learn with Validator**: Use `textual-validator.py` to understand best practices
3. **Debug with Debugger**: Use `textual-debug.py` to diagnose issues
4. **Deploy with Deployer**: Use `textual-deploy.py` to share your app

Happy coding! 🎉
