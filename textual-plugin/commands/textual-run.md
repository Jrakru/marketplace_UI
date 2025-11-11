# textual-run

Run Textual applications with debug options, profiling, testing modes, and development features.

## Overview

This command provides comprehensive options for running Textual applications in various modes: development, debug, production, and testing.

## Usage

```
/textual-run <app-path> [options]
```

## Parameters

- **app-path**: Path to Textual app file or module (required)
- **--mode <mode>**: Run mode (dev, debug, profile, test, prod)
- **--debug-level <level>**: Debug level (0-3)
- **--log-file <file>**: Log file path
- **--screenshot <file>**: Save screenshot on exit
- **--dump-state <file>**: Dump app state to file
- **--perf-stats**: Enable performance statistics
- **--headless**: Run without TUI (for testing)
- **--dev-tools**: Enable development tools
- **--theme <theme>**: Theme to use (dark, light, auto)

## Examples

### Run in Development Mode

```
/textual-run app.py --mode dev
```

Enables:
- Hot reloading on file changes
- Debug logging
- Error overlay
- Dev tools panel
- Auto-save screenshots

### Run with Debug Mode

```
/textual-run app.py --mode debug --debug-level 3 --log-file debug.log
```

Enables:
- Maximum debug logging
- Detailed error traces
- Performance profiling
- State dumping
- Console logging

### Run with Profiling

```
/textual-run app.py --mode profile --perf-stats
```

Enables:
- CPU profiling
- Memory profiling
- Render performance tracking
- Event timing analysis
- Performance report generation

### Run in Production Mode

```
/textual-run app.py --mode prod --log-file app.log
```

Optimizes for:
- Minimal logging
- Performance
- Error handling
- Resource usage

### Run with Screenshot

```
/textual-run app.py --screenshot final.png --dump-state state.json
```

Captures:
- Final app state screenshot
- Widget hierarchy
- App state data
- Performance metrics

## Run Modes

### Development Mode

```bash
/textual-run app.py --mode dev
```

**Features:**
- File watching for hot reload
- Debug toolbar
- Console error display
- Detailed logging
- Inspector panel

**Auto-reload:**
- Detects file changes
- Recompiles CSS
- Reinitializes app
- Preserves state when possible

**Development Tools:**
```python
# Enabled in dev mode
from textual.dev import ConsoleFeatures

class DevTools:
    file_watcher = True      # Watch for file changes
    debug_panel = True       # Show debug panel
    inspector = True         # Widget inspector
    error_overlay = True     # Error display overlay
```

### Debug Mode

```bash
/textual-run app.py --mode debug --debug-level 3
```

**Debug Levels:**
- **Level 0**: No debug
- **Level 1**: Basic errors
- **Level 2**: Warnings + errors
- **Level 3**: All messages

**Debug Features:**
```python
# Level 3 enables everything
VERBOSE_LOGGING = True
MESSAGE_TRACING = True
EVENT_LOGGING = True
RENDER_LOGGING = True
ERROR_TRACING = True
STACK_TRACES = True
```

**Console Debugging:**
- Error messages displayed
- Stack traces shown
- Variable inspection
- Call stack tracking

### Profiling Mode

```bash
/textual-run app.py --mode profile
```

**Profiling Features:**
- CPU usage tracking
- Memory consumption
- Render time measurement
- Event handler timing
- Widget lifecycle tracking

**Generated Reports:**
```
profile-report.txt
├── Render Performance
│   ├── Average render time
│   ├── Max render time
│   ├── Total renders
│   └── Widget breakdown
├── Event Performance
│   ├── Event handler times
│   ├── Message passing
│   └── Callback statistics
├── Memory Usage
│   ├── Peak memory
│   ├── Widget count
│   ├── Object count
│   └── GC statistics
└── Recommendations
    ├── Performance tips
    ├── Optimization suggestions
    └── Bottleneck identification
```

### Test Mode

```bash
/textual-run app.py --mode test --headless
```

**Test Features:**
- Headless execution
- Snapshot testing
- Event simulation
- Automated screenshots
- Test assertions

**Headless Mode:**
```python
# Run without TUI
app = MyApp()
async with app.run_test() as pilot:
    # Simulate user interactions
    await pilot.click("#button")
    await pilot.type("text", into="#input")
    await pilot.press("enter")

    # Take screenshot
    await pilot.pause()
    await pilot.save_screenshot("test.png")
```

### Production Mode

```bash
/textual-run app.py --mode prod
```

**Production Optimizations:**
- Minimal logging
- Optimized rendering
- Resource pooling
- Error logging only
- Crash reporting

## Debug Options

### Debug Level Configuration

```python
# debug_level=0 - Production
DEBUG_LEVEL_0 = {
    "log_errors": True,
    "log_warnings": False,
    "log_info": False,
    "log_debug": False,
}

# debug_level=1 - Minimal
DEBUG_LEVEL_1 = {
    "log_errors": True,
    "log_warnings": True,
    "log_info": False,
    "log_debug": False,
}

# debug_level=2 - Standard
DEBUG_LEVEL_2 = {
    "log_errors": True,
    "log_warnings": True,
    "log_info": True,
    "log_debug": False,
}

# debug_level=3 - Verbose
DEBUG_LEVEL_3 = {
    "log_errors": True,
    "log_warnings": True,
    "log_info": True,
    "log_debug": True,
    "trace_messages": True,
    "trace_events": True,
    "trace_renders": True,
}
```

### Debug Output Options

**Console Output:**
```bash
# Output to console
/textual-run app.py --log-level info

# Available levels:
# - error
# - warning
# - info
# - debug
# - trace
```

**File Output:**
```bash
# Log to file
/textual-run app.py --log-file app.log

# Rotate logs
/textual-run app.py --log-file logs/app.log --log-rotate
```

**Both Console and File:**
```bash
# Log to both
/textual-run app.py --log-level debug --log-file debug.log
```

## Performance Monitoring

### Real-time Performance Stats

```bash
/textual-run app.py --perf-stats
```

**Live Metrics Displayed:**
```
Performance Monitor
┌─────────────────────────────────────┐
│ Render Time:  0.005s (avg)          │
│ Memory Usage: 15.2 MB              │
│ FPS:          60 fps                │
│ Widgets:      124 active            │
│ Events/s:     45 events             │
└─────────────────────────────────────┘
```

### Performance Profiling

```bash
/textual-run app.py --profile-cpu --profile-memory
```

**CPU Profiling:**
- Function call tracking
- Time spent per function
- Call graph visualization
- Bottleneck identification

**Memory Profiling:**
- Memory allocation tracking
- Object lifetime monitoring
- Memory leak detection
- Peak usage analysis

### Render Performance

```bash
/textual-run app.py --render-stats
```

**Render Statistics:**
- Widget render times
- DOM update counts
- Redraw frequency
- Optimization opportunities

## Debug Tools

### Developer Console

```bash
/textual-run app.py --dev-tools
```

**Console Features:**
- Python REPL access
- Widget inspection
- State examination
- Live code evaluation

**Usage:**
```
> app  # Access app instance
> app.query('Button')  # Query widgets
> app.state  # View app state
> help(widget)  # Get widget help
```

### Widget Inspector

```bash
/textual-run app.py --inspector
```

**Inspector Panel:**
```
Widget Inspector
┌─────────────────────────────────────┐
│ Type:        Button                │
│ ID:          submit-btn            │
│ Classes:     primary, large        │
│ Size:        (20, 3)               │
│ Position:    (10, 15)              │
│ Styles:      background=blue       │
│              color=white           │
│ Parent:      Container (#main)     │
│ Children:    None                  │
└─────────────────────────────────────┘
```

### Message Debugger

```bash
/textual-run app.py --message-debug
```

**Message Flow Tracking:**
```
Message: Button.Pressed
  From:    Button (#submit)
  To:      MyApp
  Time:    2024-01-15 10:23:45.123
  Data:    {'button': <Button>}

  Handler: on_button_pressed
    Duration: 0.001s
    Result:   None
```

### CSS Inspector

```bash
/textual-run app.py --css-debug
```

**CSS Debugging:**
- Applied styles display
- CSS rule matching
- Cascade visualization
- Specificity scores

## Screenshot and State Dumping

### Screenshot Options

```bash
# Save screenshot on exit
/textual-run app.py --screenshot final.png

# Save screenshots periodically
/textual-run app.py --screenshot-period 5 --screenshot-dir screenshots

# Screenshot on specific events
/textual-run app.py --screenshot-on-error --screenshot-on-exit
```

**Screenshot Formats:**
- PNG (default)
- SVG (vector graphics)
- HTML (with CSS)
- JSON (layout data)

### State Dumping

```bash
# Dump complete app state
/textual-run app.py --dump-state state.json

# Dump widget tree
/textual-run app.py --dump-widgets widgets.json

# Dump event log
/textual-run app.py --dump-events events.log
```

**State File Contents:**
```json
{
  "app": {
    "title": "My App",
    "size": (80, 24),
    "mode": "terminal"
  },
  "widgets": {
    "root": {
      "type": "Container",
      "id": "root",
      "children": [...]
    }
  },
  "reactive_properties": {
    "count": 42,
    "name": "Example"
  },
  "message_queue": [],
  "event_log": [...]
}
```

## Testing with textual-run

### Headless Testing

```python
# test_app.py
import pytest
from textual.app import App

class TestableApp(App):
    def compose(self):
        yield Button("Click Me", id="test-btn")

async def test_app():
    """Test app in headless mode."""
    app = TestableApp()
    async with app.run_test() as pilot:
        # Test interactions
        await pilot.click("#test-btn")

        # Assertions
        assert app.clicked is True

        # Screenshot
        await pilot.save_screenshot("test_result.png")

# Run test
textual-run test_app.py --mode test --headless
```

### Snapshot Testing

```bash
# Create baseline
/textual-run app.py --snapshot-create baseline.png

# Test against baseline
/textual-run app.py --snapshot-test baseline.png --snapshot-compare test_result.png
```

### Event Simulation

```bash
# Simulate user events
/textual-run app.py --simulate-clicks button-clicks.txt
/textual-run app.py --simulate-keys key-sequences.txt
/textual-run app.py --simulate-events events.json
```

**Event File Format:**
```json
[
  {"type": "click", "selector": "#button", "delay": 0.5},
  {"type": "key", "key": "enter", "delay": 0.1},
  {"type": "type", "text": "Hello, World!", "delay": 0.1}
]
```

## Log Management

### Log Levels

```bash
# Error only
/textual-run app.py --log-level error

# Warning and above
/textual-run app.py --log-level warning

# Info and above (default)
/textual-run app.py --log-level info

# Debug and above
/textual-run app.py --log-level debug

# Everything
/textual-run app.py --log-level trace
```

### Log Rotation

```bash
# Rotate logs when size exceeded
/textual-run app.py --log-file app.log --log-max-size 10MB

# Keep N backup files
/textual-run app.py --log-file app.log --log-backup-count 5

# Compress old logs
/textual-run app.py --log-file app.log --log-compress
```

### Custom Log Format

```bash
# Detailed format
/textual-run app.py --log-format detailed

# Simple format
/textual-run app.py --log-format simple

# JSON format
/textual-run app.py --log-format json
```

**Log Formats:**
```
Simple:     [ERROR] Message
Detailed:   2024-01-15 10:23:45.123 [ERROR] app.py:45 - Message
JSON:       {"time": "...", "level": "ERROR", "message": "..."}
```

## Advanced Options

### Custom Themes

```bash
# Use specific theme
/textual-run app.py --theme dark

# Theme options:
# - dark (default)
# - light
# - auto (system preference)
# - custom (load from file)
/textual-run app.py --theme-file my-theme.tcss
```

### Custom Configuration

```bash
# Load config file
/textual-run app.py --config config.yaml

# Override config values
/textual-run app.py --set theme=dark --set debug=true

# Environment variables
TEXTUAL_THEME=dark textual-run app.py
TEXTUAL_DEBUG=1 textual-run app.py
```

### Exit Options

```bash
# Auto-exit after N seconds
/textual-run app.py --exit-after 60

# Exit on error
/textual-run app.py --exit-on-error

# Exit on keypress
/textual-run app.py --exit-on q
```

### Multiple Instances

```bash
# Run multiple apps
/textual-run app1.py app2.py app3.py

# Run with different modes
/textual-run app1.py --mode dev & textual-run app2.py --mode prod &
```

## Integration with Development Tools

### VS Code Integration

```json
// .vscode/launch.json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Run Textual App (Dev)",
            "type": "python",
            "request": "launch",
            "program": "textual",
            "args": ["run", "${workspaceFolder}/app.py", "--mode", "dev"]
        },
        {
            "name": "Run Textual App (Debug)",
            "type": "python",
            "request": "launch",
            "program": "textual",
            "args": ["run", "${workspaceFolder}/app.py", "--mode", "debug"]
        }
    ]
}
```

### PyCharm Integration

```python
# run_configuration.py
import subprocess
import sys

def run_textual_app(mode="dev"):
    cmd = [sys.executable, "-m", "textual", "run", "app.py", "--mode", mode]
    subprocess.run(cmd)
```

### Make Integration

```makefile
# Makefile
.PHONY: run-dev run-debug run-test

run-dev:
	textual-run app.py --mode dev

run-debug:
	textual-run app.py --mode debug --perf-stats

run-test:
	textual-run app.py --mode test --headless

profile:
	textual-run app.py --mode profile --perf-stats
```

## Troubleshooting

### Common Issues

**Issue: App doesn't start**
```bash
# Check for errors
textual-run app.py --mode debug --log-level error

# Verify dependencies
pip list | grep textual

# Check Python version
python --version
```

**Issue: Performance problems**
```bash
# Profile performance
textual-run app.py --mode profile --perf-stats

# Check memory usage
textual-run app.py --profile-memory

# Monitor rendering
textual-run app.py --render-stats
```

**Issue: Layout issues**
```bash
# Inspect widgets
textual-run app.py --inspector

# Check CSS
textual-run app.py --css-debug

# Screenshot current state
textual-run app.py --screenshot layout.png
```

### Debug Output Analysis

**Error Patterns:**
```
[ERROR] Widget not found: #missing-button
→ Check widget ID spelling
→ Verify widget is created in compose()
→ Check timing (widget not yet mounted)

[ERROR] CSS file not found
→ Check CSS_PATH in App class
→ Verify file exists
→ Check file permissions

[ERROR] Event handler not found
→ Check method name (on_widget_event)
→ Verify method signature
→ Check event type
```

## See Also

- [Textual Testing Utilities](../helpers/textual-testing-utilities.md)
- [Textual Events Handling](../helpers/textual-events-handling.md)
- [Textual Performance](../helpers/textual-performance.md)
- [Textual App Development](../skills/creating-textual-apps.md)
