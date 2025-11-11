# textual-debug

Debug and troubleshoot Textual applications with comprehensive diagnostic tools, error tracking, and performance analysis.

## Overview

This command provides a comprehensive debugging toolkit for Textual applications, including error diagnosis, performance profiling, widget inspection, and automated troubleshooting.

## Usage

```
/textual-debug <command> [options]
```

## Commands

- `diagnose <app>` - Analyze app and identify issues
- `trace <app>` - Trace execution flow
- `profile <app>` - Performance profiling
- `inspect <app>` - Interactive widget inspector
- `verify <app>` - Verify app structure and configuration
- `test <app>` - Run diagnostic tests
- `fix <issue>` - Auto-fix common issues

## Examples

### Diagnose Application Issues

```
/textual-debug diagnose app.py
```

Analyzes:
- App structure validation
- CSS syntax errors
- Missing event handlers
- Performance bottlenecks
- Memory leaks
- Common pitfalls

### Trace Execution Flow

```
/textual-debug trace app.py --verbose
```

Shows:
- Message flow
- Event handling
- Widget lifecycle
- State changes
- Render cycles

### Profile Performance

```
/textual-debug profile app.py --memory --cpu --output report.html
```

Generates:
- CPU usage analysis
- Memory profiling
- Render performance
- Event timing
- Optimization recommendations

## Diagnose Command

### Basic Diagnosis

```
/textual-debug diagnose <app-file> [options]
```

#### Options

- **--fix**: Auto-fix issues when possible
- **--output <file>**: Save report to file
- **--format <format>**: Report format (text, json, html)
- **--strict**: Enable strict mode checks
- **--comprehensive**: Run all diagnostic checks

#### Example Output

```bash
$ textual-debug diagnose app.py

Textual App Diagnostic Report
============================

✓ PASS: App class properly defined
✓ PASS: compose() method implemented
✗ FAIL: CSS_PATH file not found
✗ FAIL: Missing error handling in event handlers
⚠ WARN: Reactive property 'count' not initialized
⚠ WARN: Potential memory leak in timer cleanup

Issues Found: 2
Warnings: 2
Elapsed Time: 0.234s

Recommendations:
1. Create missing CSS file or set CSS_PATH correctly
2. Add try/except blocks in event handlers
3. Initialize reactive properties in __init__
4. Clean up timers in on_unmount()

See report.html for detailed analysis.
```

### Comprehensive Diagnosis

```
/textual-debug diagnose app.py --comprehensive --output report.json
```

**Checks Performed:**

1. **Structure Validation**
   - App class inheritance
   - compose() method presence
   - Proper widget hierarchy
   - Required imports

2. **CSS Validation**
   - File existence
   - Syntax errors
   - Reference validation
   - Naming conventions

3. **Event Handling**
   - Missing event handlers
   - Incorrect signatures
   - Exception handling
   - Message emission

4. **Reactive Properties**
   - Initialization
   - Type hints
   - Watcher methods
   - Update patterns

5. **Performance**
   - Widget count
   - Nested container depth
   - Potential loops
   - Memory usage

6. **Best Practices**
   - Code organization
   - Documentation
   - Testing coverage
   - Security issues

### Auto-Fix Issues

```
/textual-debug diagnose app.py --fix --output fixed-app.py
```

**Auto-Fixes Available:**
- Add missing CSS_PATH
- Fix event handler signatures
- Initialize reactive properties
- Add error handling
- Remove unused imports
- Fix naming conventions

## Trace Command

### Execution Tracing

```
/textual-debug trace <app-file> [options]
```

#### Options

- **--level <level>**: Trace level (error, warn, info, debug, verbose)
- **--output <file>**: Save trace to file
- **--filter <pattern>**: Filter trace by pattern
- **--duration <seconds>**: Trace for duration
- **--events**: Trace event flow
- **--messages**: Trace message passing
- **--renders**: Trace render cycles

#### Example Output

```bash
$ textual-debug trace app.py --events --messages

Event Flow Trace
===============

10:23:45.123 [INFO] App mounted
├── 10:23:45.124 [DEBUG] Screen composed
│   ├── 10:23:45.125 [DEBUG] Container created
│   │   ├── 10:23:45.126 [DEBUG] Button (#save) mounted
│   │   │   └── 10:23:45.127 [TRACE] Added click handler
│   │   └── 10:23:45.128 [DEBUG] Input (#name) mounted
│   └── 10:23:45.129 [TRACE] Input validation added

10:23:46.234 [INFO] User clicked button (#save)
├── 10:23:46.235 [DEBUG] Button.Pressed event emitted
├── 10:23:46.236 [DEBUG] Event queued
├── 10:23:46.237 [INFO] Handler: on_button_pressed
│   ├── 10:23:46.238 [DEBUG] Validating input
│   ├── 10:23:46.239 [DEBUG] Input value: "Test User"
│   ├── 10:23:46.240 [DEBUG] Validation passed
│   ├── 10:23:46.241 [DEBUG] Calling save_user()
│   ├── 10:23:46.242 [DEBUG] User saved to database
│   └── 10:23:46.243 [INFO] User saved successfully
└── 10:23:46.244 [DEBUG] UI updated
    ├── 10:23:46.245 [DEBUG] Status message displayed
    └── 10:23:46.246 [DEBUG] Button state updated

10:23:47.100 [DEBUG] Render cycle started
├── 10:23:47.101 [DEBUG] Widget tree traversed
├── 10:23:47.102 [DEBUG] 12 widgets rendered
└── 10:23:47.103 [DEBUG] Render cycle completed (0.003s)
```

### Message Flow Tracing

```
/textual-debug trace app.py --messages --verbose
```

**Tracks:**
- Message emission
- Message routing
- Handler execution
- Message timing
- Queue length
- Dropped messages

```bash
Message Flow: ButtonClicked
===========================

[10:23:45.123] Message created: ButtonClicked {button: #save}
[10:23:45.124] Route: Button -> Container -> App
[10:23:45.125] Handler: on_button_pressed (duration: 0.002s)
[10:23:45.126] Message processed: SUCCESS

[10:23:45.234] Message created: DataSaved {user_id: 42}
[10:23:45.235] Route: Service -> App
[10:23:45.236] Handler: on_data_saved (duration: 0.001s)
[10:23:45.237] Message processed: SUCCESS

[10:23:45.345] Message created: UIUpdate
[10:23:45.346] Route: App -> Screen
[10:23:45.347] Handler: update_ui (duration: 0.003s)
[10:23:45.348] Message processed: SUCCESS
```

### Render Cycle Tracing

```
/textual-debug trace app.py --renders
```

**Analyzes:**
- Render frequency
- Widget render times
- DOM update efficiency
- Redundant renders
- Performance bottlenecks

```bash
Render Performance Analysis
===========================

Total Renders: 156
Average Render Time: 0.003s
Min Render Time: 0.001s
Max Render Time: 0.015s

Widget Render Breakdown:
- Button (#save): 45 renders, avg 0.001s
- Input (#name): 23 renders, avg 0.001s
- DataTable (#users): 12 renders, avg 0.008s
- Container (#main): 156 renders, avg 0.000s

Slow Renders (>0.005s):
- 10:23:45.123: DataTable (0.015s) - 25 rows
- 10:23:47.456: DataTable (0.012s) - 23 rows
- 10:23:49.789: DataTable (0.011s) - 22 rows

Recommendations:
1. Optimize DataTable rendering for large datasets
2. Implement virtual scrolling
3. Cache render results
4. Batch updates
```

## Profile Command

### Performance Profiling

```
/textual-debug profile <app-file> [options]
```

#### Options

- **--cpu**: Enable CPU profiling
- **--memory**: Enable memory profiling
- **--output <file>**: Save profile to file
- **--format <format>**: Output format (text, html, json)
- **--duration <seconds>**: Profile for duration
- **--sample-rate <rate>**: Sample rate (Hz)

#### CPU Profiling

```
/textual-debug profile app.py --cpu --output cpu-profile.html
```

**Generates HTML report:**
```html
CPU Profile Report
==================

Top Functions:
  1. Widget.render()           - 234 calls, 1.234s (45.2%)
  2. App.on_button_pressed()   - 156 calls, 0.456s (16.7%)
  3. Container.compose()       - 89 calls, 0.234s (8.6%)
  4. Input.validate()          - 445 calls, 0.123s (4.5%)

Call Graph:
App.on_button_pressed() [0.456s]
├── DataService.save() [0.123s]
│   ├── Database.query() [0.045s]
│   └── Database.commit() [0.078s]
└── UI.update() [0.234s]
    ├── Widget.render() [0.123s]
    └── Screen.refresh() [0.111s]

Bottlenecks Identified:
- Widget.render() called 234 times
  → Consider caching render results
- Database.query() takes 0.045s each
  → Implement connection pooling
- UI.update() triggers full re-render
  → Use selective updates
```

#### Memory Profiling

```
/textual-debug profile app.py --memory --output mem-profile.html
```

**Memory Analysis:**
```html
Memory Profile Report
=====================

Memory Usage:
- Peak: 45.2 MB
- Current: 23.1 MB
- Average: 28.4 MB

Object Breakdown:
- Widget instances: 124 objects, 12.4 MB (53.7%)
- DataTable rows: 450 objects, 8.9 MB (38.5%)
- Event listeners: 89 objects, 1.2 MB (5.2%)
- Other: 45 objects, 0.6 MB (2.6%)

Memory Leaks Detected:
✗ Timer not cleaned up (Widget #23)
  Created: app.py:156
  References: 1

✗ Event listener not removed (Button #7)
  Created: app.py:89
  References: 1

✗ Cache growing unbounded (DataService)
  Created: app.py:234
  Current size: 1,234 entries
  Growth rate: +10/sec

Recommendations:
1. Clean up timers in on_unmount()
2. Remove event listeners when done
3. Implement cache size limits
4. Use weak references for callbacks
```

#### Combined Profile

```
/textual-debug profile app.py --cpu --memory --duration 60
```

**Comprehensive Report:**
```html
Full Profile Report
===================

Performance Score: 72/100

CPU Usage:
- Average: 15.3%
- Peak: 34.2%
- Hot functions:
  1. Widget.render() [45.2%]
  2. App.on_button_pressed() [16.7%]

Memory Usage:
- Peak: 45.2 MB
- Growth: +0.1 MB/min
- Leaks: 3 detected

Render Performance:
- Avg FPS: 42 fps
- Slow frames: 12
- Jank detected: 3 times

Event Performance:
- Events/sec: 45
- Avg latency: 0.001s
- Max latency: 0.023s

Optimization Priority:
1. High: Fix memory leaks
2. High: Optimize DataTable rendering
3. Medium: Implement cache limits
4. Medium: Add event debouncing
5. Low: Optimize CSS selectors
```

## Inspect Command

### Interactive Widget Inspector

```
/textual-debug inspect <app-file> [options]
```

#### Options

- **--port <port>**: Inspector port (default: 8080)
- **--host <host>**: Inspector host (default: localhost)
- **--attach**: Attach to running app
- **--snapshot <file>**: Save widget tree snapshot

#### Inspector Interface

```
┌──────────────────────────────────────────────────────────────┐
│ Textual Widget Inspector                                    │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│ Tree View                     │ Properties                   │
│ Screen                        │ Type: Screen                 │
│ ├─ Container (#main)          │ ID: main                     │
│ │  ├─ Button (#save)          │ Classes: primary, large      │
│ │  │  └─ Text: "Save"         │ Size: (15, 3)                │
│ │  │                          │ Position: (5, 10)            │
│ │  └─ Input (#username)       │ Visible: True                │
│ │     └─ Placeholder          │ Disabled: False              │
│ └─ DataTable (#users)         │                               │
│    ├─ Column 0                │ CSS Applied:                 │
│    └─ Column 1                │ - background: blue           │
│                                │ - color: white               │
│                                │ - padding: 1                 │
│                                │                               │
│ Actions                        │ Events                       │
│ [Refresh Tree]                 │ Clicked: 45 times            │
│ [Find Widget]                  │ Focused: 3 times             │
│ [Show Layout]                  │ Hovered: 12 times            │
│ [Export Snapshot]              │                               │
│                                │                               │
└──────────────────────────────────────────────────────────────┘
```

#### Widget Tree Inspection

```bash
$ textual-debug inspect app.py --command tree

Widget Tree:
===========

Screen
├── Container: id="header"
│   ├── Static: "Application Title"
│   └── Button: id="theme-toggle" (pressed=3)
├── Container: id="main"
│   ├── Container: id="sidebar" (width=20)
│   │   ├── Tree: id="navigation" (nodes=45)
│   │   └── Button: id="expand" (expanded=true)
│   └── Container: id="content" (width=60)
│       ├── DataTable: id="users" (rows=234, cols=5)
│       │   └── Columns: [ID, Name, Email, Status, Actions]
│       ├── Button: id="add-user" (variant="success")
│       └── Button: id="delete-user" (variant="error")
└── Container: id="footer"
    └── Static: "Status: Ready"
```

#### Property Inspection

```bash
$ textual-debug inspect app.py --command properties --widget "#users"

Properties for DataTable (#users):
=================================

Dimensions:
  Size: (60, 20)
  Position: (10, 5)

Styling:
  Classes: ["data-table", "striped"]
  CSS Applied:
    - background: $panel
    - border: solid $accent
    - padding: 1

State:
  Cursor Row: 12
  Cursor Column: 0
  Selected Rows: [3, 7, 15, 23]
  Row Count: 234
  Column Count: 5

Events:
  Registered: 5
  Last Event: RowSelected (row=12)
  Event History: [RowSelected, CellSelected, RowSelected, ...]

Memory:
  Widget ID: 0x12345678
  Parent: Container (#main)
  Children: 0
  References: 1
```

#### Live Updates

```bash
$ textual-debug inspect app.py --command monitor

Monitoring Widget Updates:
=========================

Widget              Updates  Last Update    Avg Time
─────────────────────────────────────────────────────
Button (#save)      45       00:00:05      0.001s
DataTable (#users)  23       00:00:12      0.008s
Input (#search)     156      00:00:01      0.001s
Container (#main)   234      00:00:03      0.000s

Recent Events:
[00:00:15.123] Button.Pressed (#save)
[00:00:14.456] DataTable.RowSelected (row=7)
[00:00:13.789] Input.Changed (#search)
[00:00:12.234] Button.Pressed (#save)
```

## Verify Command

### App Structure Verification

```
/textual-debug verify <app-file> [options]
```

#### Checks Performed

1. **Import Validation**
   ```bash
   $ textual-debug verify app.py --imports

   ✓ All imports successful
   ✓ No circular dependencies
   ⚠ Unused import: 'os' (line 5)
   ✗ Missing import: 'Textual' (line 45)
   ```

2. **Widget Validation**
   ```bash
   $ textual-debug verify app.py --widgets

   ✓ 12 widgets properly defined
   ✓ All widgets have unique IDs
   ⚠ Duplicate ID 'button' used 3 times
   ✗ Unknown widget type: 'MyCustomWidget'
   ```

3. **Event Handler Validation**
   ```bash
   $ textual-debug verify app.py --handlers

   ✓ 8 event handlers found
   ✓ All handlers have correct signatures
   ✗ Missing handler: on_button_pressed
   ⚠ Unused handler: on_mouse_move
   ```

4. **CSS Validation**
   ```bash
   $ textual-debug verify app.py --css

   ✓ CSS file exists: styles/main.tcss
   ✓ Valid CSS syntax
   ⚠ Unused class: '.old-style'
   ✗ Missing class: '.button-primary'
   ```

#### Comprehensive Verification

```
/textual-debug verify app.py --comprehensive
```

**Verification Report:**
```bash
Textual App Verification
========================

Structure:        ✓ PASS
Imports:          ✓ PASS
Widgets:          ⚠ WARN
Event Handlers:   ✓ PASS
CSS:              ✓ PASS
Reactive Props:   ✗ FAIL
Performance:      ⚠ WARN
Security:         ✓ PASS

Score: 78/100

Details:
─────────

Structure (20/20):
  ✓ App class properly inherits from App
  ✓ compose() method implemented
  ✓ Screen layout is valid
  ✓ Widget hierarchy is correct

Imports (20/20):
  ✓ All required imports present
  ✓ No circular dependencies
  ✓ Version compatibility verified

Widgets (15/20):
  ✓ 12 widgets defined
  ⚠ Duplicate ID warning: 'button' used 3 times
  ✗ Unknown widget: 'MyCustomWidget'

Event Handlers (20/20):
  ✓ All handlers have correct signatures
  ✓ Exception handling present
  ✓ No circular event references

CSS (20/20):
  ✓ Valid syntax
  ✓ No hardcoded colors
  ✓ Responsive design present

Reactive Props (10/20):
  ✗ Missing initializers for 3 properties
  ✗ No watcher methods for reactive properties
  ⚠ Inconsistent naming: 'count' vs 'item_count'

Performance (15/20):
  ✓ Widget count reasonable (12)
  ✓ Nesting depth acceptable (3)
  ⚠ Potential memory leak: Timer cleanup
  ⚠ Frequent re-renders detected

Security (20/20):
  ✓ No hardcoded credentials
  ✓ Input validation present
  ✓ No dangerous operations

Issues to Fix:
1. Initialize reactive properties
2. Add watcher methods
3. Fix duplicate widget IDs
4. Clean up memory leaks
```

## Test Command

### Diagnostic Testing

```
/textual-debug test <app-file> [options]
```

#### Test Categories

1. **Unit Tests**
   ```bash
   $ textual-debug test app.py --unit

   Running Unit Tests:
   ===================

   ✓ test_app_creation: PASSED (0.001s)
   ✓ test_widget_mount: PASSED (0.002s)
   ✓ test_event_handling: PASSED (0.003s)
   ✓ test_reactive_properties: PASSED (0.001s)
   ✓ test_css_loading: PASSED (0.001s)

   Passed: 5/5
   Failed: 0/5
   ```

2. **Integration Tests**
   ```bash
   $ textual-debug test app.py --integration

   Running Integration Tests:
   ==========================

   ✓ test_user_interaction: PASSED (0.123s)
   ✓ test_data_binding: PASSED (0.089s)
   ✓ test_screen_navigation: PASSED (0.067s)
   ✗ test_error_handling: FAILED (0.045s)

   Error: Exception not caught in on_button_pressed
   Location: app.py:156

   Passed: 3/4
   Failed: 1/4
   ```

3. **Performance Tests**
   ```bash
   $ textual-debug test app.py --performance

   Running Performance Tests:
   ==========================

   ✓ test_render_speed: PASSED (avg 0.003s)
   ✓ test_memory_usage: PASSED (peak 12MB)
   ✓ test_event_latency: PASSED (avg 0.001s)
   ⚠ test_large_dataset: WARNING (slow rendering)

   Details:
   - Dataset size: 1000 rows
   - Render time: 0.234s
   - Recommendation: Implement virtual scrolling

   Passed: 3/3
   Warnings: 1/3
   ```

4. **Accessibility Tests**
   ```bash
   $ textual-debug test app.py --accessibility

   Running Accessibility Tests:
   ============================

   ✓ test_keyboard_navigation: PASSED
   ✓ test_screen_reader_support: PASSED
   ⚠ test_color_contrast: WARNING
   ✗ test_focus_indicators: FAILED

   Color Contrast Issues:
   - Button (#secondary): 2.8:1 (needs 4.5:1)
   - Link (#email): 3.2:1 (needs 4.5:1)

   Focus Indicators:
   - Widgets missing focus styles: #button, #input, #table

   Passed: 2/4
   Failed: 1/4
   Warnings: 1/4
   ```

### Automated Test Generation

```
/textual-debug test app.py --generate
```

**Generates:**
```python
# tests/test_app_diagnostic.py
import pytest
from textual.testing import AppTest
from app import MyApp

class TestMyAppDiagnostic:
    """Diagnostic tests for MyApp."""

    @pytest.fixture
    async def app_test(self):
        async with MyApp().run_test() as pilot:
            yield pilot

    async def test_app_mounts(self, app_test):
        """Test app mounts without errors."""
        assert app_test.app.is_running

    async def test_all_widgets_present(self, app_test):
        """Test all expected widgets are mounted."""
        app = app_test.app
        assert app.query_one("#button", Button) is not None
        assert app.query_one("#input", Input) is not None
        assert app.query_one("#table", DataTable) is not None

    async def test_event_handlers_exist(self, app_test):
        """Test all event handlers are callable."""
        app = app_test.app
        assert hasattr(app, 'on_button_pressed')
        assert callable(app.on_button_pressed)
        assert hasattr(app, 'on_input_changed')
        assert callable(app.on_input_changed)

    async def test_reactive_properties(self, app_test):
        """Test reactive properties work correctly."""
        app = app_test.app
        assert hasattr(app, 'count')
        assert hasattr(app, 'watch_count')
```

## Fix Command

### Auto-Fix Common Issues

```
/textual-debug fix <app-file> [issue-type] [options]
```

#### Issue Types

1. **Missing CSS**
   ```bash
   $ textual-debug fix app.py missing-css

   Creating CSS file: styles/main.tcss
   Writing base styles...
   Generating component library...
   CSS file created successfully!
   ```

2. **Initialize Reactive Properties**
   ```bash
   $ textual-debug fix app.py reactive-init

   Analyzing reactive properties...

   Found 3 uninitialized properties:
   - count
   - items
   - is_loading

   Adding initializers...

   Before:
   class MyApp(App):
       count = reactive(0)
       items = reactive([])

   After:
   class MyApp(App):
       count = reactive(0)
       items = reactive([])

       def __init__(self):
           super().__init__()
           self.count = 0
           self.items = []
   ```

3. **Add Error Handling**
   ```bash
   $ textual-debug fix app.py error-handling

   Found 3 event handlers without error handling:
   - on_button_pressed
   - on_input_changed
   - on_timer

   Adding try/except blocks...

   Before:
   def on_button_pressed(self, event: Button.Pressed) -> None:
       self.save_data()

   After:
   def on_button_pressed(self, event: Button.Pressed) -> None:
       try:
           self.save_data()
       except Exception as e:
           self.log(f"Error: {e}")
           self.bell()
   ```

4. **Fix Duplicate IDs**
   ```bash
   $ textual-debug fix app.py duplicate-ids

   Found 3 duplicate IDs:
   - 'button' used 3 times
   - 'input' used 2 times
   - 'table' used 2 times

   Fixing duplicate IDs...

   Before:
   Button("Save", id="button")
   Button("Cancel", id="button")

   After:
   Button("Save", id="save-button")
   Button("Cancel", id="cancel-button")
   ```

5. **Add Cleanup**
   ```bash
   $ textual-debug fix app.py cleanup

   Found resources needing cleanup:
   - 3 timers
   - 2 event listeners
   - 1 file handle

   Adding on_unmount cleanup...

   Before:
   def __init__(self):
       self.timer = self.set_interval(1.0, self.tick)

   After:
   def __init__(self):
       self.timer = self.set_interval(1.0, self.tick)

   def on_unmount(self) -> None:
       if self.timer:
           self.timer.stop()
       super().on_unmount()
   ```

### Batch Fixes

```
/textual-debug fix app.py --all --output fixed-app.py
```

**Applies all auto-fixes:**
- Initialize reactive properties
- Add error handling
- Create missing CSS
- Fix duplicate IDs
- Add cleanup code
- Update imports
- Add type hints

## Troubleshooting Guide

### Common Issues and Solutions

#### Issue: App Won't Start

**Symptoms:**
- App exits immediately
- No error message
- Blank screen

**Diagnosis:**
```bash
$ textual-debug diagnose app.py --strict
```

**Common Causes:**
1. **Missing CSS file**
   ```python
   # Fix
   class MyApp(App):
       CSS = """
       Screen {
           background: #1e1e1e;
       }
       """
   ```

2. **Invalid compose() return**
   ```python
   # Wrong
   def compose(self):
       Button("Click")

   # Correct
   def compose(self):
       yield Button("Click")
   ```

3. **Exception in __init__**
   ```python
   # Add error handling
   def __init__(self):
       try:
           super().__init__()
           # Your code
       except Exception as e:
           print(f"Initialization error: {e}")
   ```

#### Issue: Widget Not Rendering

**Symptoms:**
- Widget exists but not visible
- Space allocated but blank
- Layout broken

**Diagnosis:**
```bash
$ textual-debug trace app.py --filter widget-name
```

**Solutions:**
```python
# Check render() returns content
def render(self):
    return "Content"  # Not None

# Check compose() yields widgets
def compose(self):
    yield Button("Text")

# Verify CSS visibility
.my-widget {
    display: none;  /* Remove this */
}

# Check widget is mounted
def on_mount(self) -> None:
    widget = Button("Test")
    self.mount(widget)
```

#### Issue: Event Handlers Not Firing

**Symptoms:**
- Clicks don't work
- Keyboard input ignored
- No response to actions

**Diagnosis:**
```bash
$ textual-debug trace app.py --events
```

**Solutions:**
```python
# Check method name
# Must be: on_<widget>_<event>
def on_button_pressed(self, event: Button.Pressed) -> None:
    pass

# Check event type
def on_key(self, event) -> None:  # For key events
    pass

# Check widget has focus
widget.focus()  # Give widget focus

# Check event propagation
event.stop()  # If needed to stop propagation
```

#### Issue: Performance Problems

**Symptoms:**
- Slow rendering
- High CPU usage
- Laggy interactions

**Diagnosis:**
```bash
$ textual-debug profile app.py --cpu --memory
```

**Solutions:**
```python
# Reduce widget count
# Batch updates
with self.batch():
    widget1.update(value1)
    widget2.update(value2)

# Cache expensive operations
@cache.memoize
def expensive_calculation(self, value):
    return result

# Use selective updates
def update_display(self):
    widget = self.query_one("#display", Static)
    widget.update(new_value)  # Instead of full re-render

# Clean up timers
def on_unmount(self) -> None:
    if self.timer:
        self.timer.stop()
```

#### Issue: Memory Leaks

**Symptoms:**
- Memory usage increases over time
- App slows down
- Eventual crash

**Diagnosis:**
```bash
$ textual-debug profile app.py --memory --duration 300
```

**Solutions:**
```python
# Clean up timers
def on_unmount(self) -> None:
    for timer in self.timers:
        timer.stop()

# Use weak references
import weakref

class MyWidget(Widget):
    def __init__(self):
        self.callbacks = weakref.WeakSet()

# Clear large data
def clear_data(self):
    self.large_data = None
    import gc
    gc.collect()

# Remove event listeners
def cleanup(self):
    if hasattr(self, 'listener'):
        self.listener.remove()
```

## Best Practices

### Debugging Workflow

1. **Start with diagnosis**
   ```bash
   textual-debug diagnose app.py --comprehensive
   ```

2. **Fix structural issues**
   ```bash
   textual-debug fix app.py --all
   ```

3. **Verify fixes**
   ```bash
   textual-debug verify app.py
   ```

4. **Profile performance**
   ```bash
   textual-debug profile app.py --cpu --memory
   ```

5. **Run tests**
   ```bash
   textual-debug test app.py --all
   ```

6. **Monitor in production**
   ```bash
   textual-debug trace app.py --level info --output production.log
   ```

### Debug Configuration

```python
# Enable debug mode
class MyApp(App):
    DEBUG = True  # Enable debug features

    def on_mount(self) -> None:
        # Enable detailed logging
        import logging
        logging.basicConfig(level=logging.DEBUG)

        # Start performance monitoring
        self.set_interval(60.0, self.log_performance)

    def log_performance(self):
        """Log performance metrics."""
        # Log widget count
        widget_count = len(self.query("*"))
        self.log(f"Active widgets: {widget_count}")

        # Log memory usage
        import psutil
        memory = psutil.Process().memory_info().rss / 1024 / 1024
        self.log(f"Memory usage: {memory:.1f} MB")
```

### Debug Environment

```bash
# Set debug environment
export TEXTUAL_DEBUG=1
export TEXTUAL_LOG_LEVEL=DEBUG
export TEXTUAL_PROFILE=1

# Run with debug
textual-debug diagnose app.py --debug
```

## See Also

- [Textual Testing Utilities](../helpers/textual-testing-utilities.md)
- [Textual Performance](../helpers/textual-performance.md)
- [Textual Events Handling](../helpers/textual-events-handling.md)
- [Textual App Development](../skills/creating-textual-apps.md)
