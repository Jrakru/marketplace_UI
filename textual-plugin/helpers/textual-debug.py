#!/usr/bin/env python3
"""
Textual Debugging Utilities

This script provides comprehensive debugging and diagnostic tools for
Textual TUI applications. It includes widget tree inspection, event
debugging, layout debugging, performance profiling, and error diagnostics.

Features:
- Widget tree inspection
- Event debugging and tracing
- Layout debugging
- Performance profiling
- Error diagnostics and reporting
- Live debugging mode

Usage:
    python textual-debug.py --inspect app.py
    python textual-debug.py --events app.py
    python textual-debug.py --profile app.py
    python textual-debug.py --live app.py
"""

import argparse
import ast
import cProfile
import inspect
import io
import os
import pstats
import sys
import time
import traceback
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple, Callable
import re


# ============================================================================
# DEBUGGING UTILITIES
# ============================================================================

@dataclass
class DebugConfig:
    """Configuration for debugging."""
    trace_events: bool = False
    trace_widgets: bool = False
    trace_layout: bool = False
    profile_performance: bool = False
    log_file: Optional[str] = None
    verbose: bool = False


@dataclass
class WidgetInfo:
    """Information about a widget."""
    name: str
    type: str
    id: Optional[str]
    classes: List[str]
    parent: Optional[str]
    children: List[str] = field(default_factory=list)
    size: Optional[Tuple[int, int]] = None
    visible: bool = True


@dataclass
class EventInfo:
    """Information about an event."""
    event_type: str
    timestamp: float
    source: str
    target: str
    data: Dict[str, Any] = field(default_factory=dict)


@dataclass
class PerformanceMetric:
    """Performance metric data."""
    function_name: str
    call_count: int
    total_time: float
    per_call_time: float
    cumulative_time: float


# ============================================================================
# DEBUG HELPER FUNCTIONS
# ============================================================================

def get_widget_tree(app_instance) -> List[WidgetInfo]:
    """Extract widget tree from app instance."""
    widgets = []

    try:
        if hasattr(app_instance, '_context') and app_instance._context:
            screen = app_instance.screen
            widgets.extend(_extract_widgets_from_node(screen, None))
    except Exception as e:
        print(f"Error extracting widget tree: {e}")

    return widgets


def _extract_widgets_from_node(node: Any, parent: Optional[str]) -> List[WidgetInfo]:
    """Recursively extract widget information from node."""
    widgets = []

    try:
        widget_type = type(node).__name__
        widget_name = f"{widget_type}_{id(node)}"

        widget_info = WidgetInfo(
            name=widget_name,
            type=widget_type,
            id=getattr(node, 'id', None),
            classes=list(getattr(node, 'classes', [])),
            parent=parent,
        )

        widgets.append(widget_info)

        if hasattr(node, '_nodes'):
            for child in node._nodes:
                child_widgets = _extract_widgets_from_node(child, widget_name)
                widgets.extend(child_widgets)
                widget_info.children.extend([w.name for w in child_widgets])

    except Exception as e:
        print(f"Error extracting widget from {node}: {e}")

    return widgets


def format_widget_tree(widgets: List[WidgetInfo], max_depth: int = 5) -> str:
    """Format widget tree as a string."""
    if not widgets:
        return "No widgets found"

    lines = []
    lines.append("WIDGET TREE")
    lines.append("=" * 70)

    widget_map = {w.name: w for w in widgets}
    root_widgets = [w for w in widgets if w.parent is None or w.parent not in widget_map]

    def render_widget(widget: WidgetInfo, depth: int = 0):
        """Render a widget and its children."""
        if depth > max_depth:
            return

        indent = "  " * depth
        widget_info = f"{indent}├─ {widget.type}"

        if widget.id:
            widget_info += f" (id: {widget.id})"

        if widget.classes:
            widget_info += f" [classes: {', '.join(widget.classes)}]"

        if not widget.visible:
            widget_info += " (hidden)"

        lines.append(widget_info)

        for child_name in widget.children:
            if child_name in widget_map:
                render_widget(widget_map[child_name], depth + 1)

    for root_widget in root_widgets:
        render_widget(root_widget)

    lines.append("=" * 70)
    return "\n".join(lines)


def trace_events(app_class, events_to_trace: Optional[Set[str]] = None):
    """Generate event tracing code for an app class."""
    if events_to_trace is None:
        events_to_trace = {'on_key', 'on_click', 'on_mount', 'on_unmount'}

    event_handlers = []

    for method_name in dir(app_class):
        if method_name.startswith('on_') and method_name in events_to_trace:
            method = getattr(app_class, method_name)
            if callable(method):
                event_handlers.append(method_name)

    if not event_handlers:
        return "No event handlers found for tracing"

    lines = []
    lines.append("EVENT TRACING CODE")
    lines.append("=" * 70)
    lines.append("\nAdd these event handlers to your app class:\n")

    for handler in event_handlers:
        lines.append(f"""
def {handler}(self, event) -> None:
    \"\"\"Trace {handler} event.\"\"\"
    print(f"[DEBUG] {handler}: {event}")
    timestamp = time.time()
    event_logger.log_event({{
        'type': '{handler}',
        'timestamp': timestamp,
        'event': str(event),
    }})

    # Call original handler if exists
    if hasattr(self, 'original_{handler}'):
        self.original_{handler}(event)
""")

    lines.append("\nTo enable tracing, call:")
    lines.append("enable_event_tracing(your_app_instance)")
    lines.append("=" * 70)

    return "\n".join(lines)


def profile_performance(app_class_or_func, iterations: int = 1):
    """Profile performance of an app or function."""
    profiler = cProfile.Profile()

    start_time = time.time()

    try:
        profiler.enable()

        for _ in range(iterations):
            if inspect.isclass(app_class_or_func):
                app = app_class_or_func()
                app.run()
            else:
                app_class_or_func()

        profiler.disable()

    except KeyboardInterrupt:
        profiler.disable()
    except Exception as e:
        profiler.disable()
        print(f"Error during profiling: {e}")
        return None

    end_time = time.time()

    s = io.StringIO()
    ps = pstats.Stats(profiler, stream=s).sort_stats('cumulative')
    ps.print_stats(50)

    output = s.getvalue()

    lines = []
    lines.append("PERFORMANCE PROFILE")
    lines.append("=" * 70)
    lines.append(f"Total time: {end_time - start_time:.4f}s")
    lines.append(f"Iterations: {iterations}")
    lines.append("=" * 70)
    lines.append("\nTop 50 functions by cumulative time:\n")
    lines.append(output)
    lines.append("=" * 70)

    return "\n".join(lines)


def analyze_layout(widgets: List[WidgetInfo]) -> str:
    """Analyze layout structure and issues."""
    lines = []
    lines.append("LAYOUT ANALYSIS")
    lines.append("=" * 70)

    containers = [w for w in widgets if w.type in ['Container', 'Horizontal', 'Vertical', 'Grid']]
    widgets_without_containers = [w for w in widgets if w.type not in containers]

    lines.append(f"\nTotal widgets: {len(widgets)}")
    lines.append(f"Containers: {len(containers)}")
    lines.append(f"Regular widgets: {len(widgets_without_containers)}")

    if widgets_without_containers > 5:
        lines.append("\n⚠️  WARNING: Many widgets without containers may cause layout issues")

    container_types = {}
    for container in containers:
        container_types[container.type] = container_types.get(container.type, 0) + 1

    lines.append("\nContainer distribution:")
    for container_type, count in container_types.items():
        lines.append(f"  {container_type}: {count}")

    max_depth = 0
    for widget in widgets:
        if widget.parent:
            depth = 1
            parent = widget.parent
            while parent:
                depth += 1
                parent_widget = next((w for w in widgets if w.name == parent), None)
                parent = parent_widget.parent if parent_widget else None
            max_depth = max(max_depth, depth)

    lines.append(f"\nMaximum nesting depth: {max_depth}")

    if max_depth > 5:
        lines.append("\n⚠️  WARNING: Deep nesting may impact performance")

    lines.append("\nLayout recommendations:")
    lines.append("  • Use Horizontal/Vertical for simple layouts")
    lines.append("  • Use Grid for complex layouts")
    lines.append("  • Avoid excessive nesting (>5 levels)")
    lines.append("  • Consider using CSS grid for 2D layouts")
    lines.append("  • Use content-align for simple alignment")

    lines.append("=" * 70)
    return "\n".join(lines)


def diagnose_errors(app_file: Path, errors: List[str]) -> str:
    """Diagnose common errors and provide solutions."""
    lines = []
    lines.append("ERROR DIAGNOSIS")
    lines.append("=" * 70)

    if not errors:
        lines.append("No errors to diagnose.")
        return "\n".join(lines)

    common_issues = {
        'ImportError': [
            "• Ensure Textual is installed: pip install textual",
            "• Check Python version (requires 3.7+)",
            "• Verify import statements are correct",
        ],
        'SyntaxError': [
            "• Check for missing colons (:) at end of lines",
            "• Verify proper indentation",
            "• Ensure parentheses are balanced",
        ],
        'AttributeError': [
            "• Verify widget names are spelled correctly",
            "• Check that widgets are properly imported",
            "• Ensure widgets exist in this Textual version",
        ],
        'TypeError': [
            "• Check method signatures",
            "• Verify event handlers accept correct parameters",
            "• Ensure CSS is properly formatted",
        ],
        'KeyError': [
            "• Verify all widget IDs exist",
            "• Check for typos in widget IDs",
            "• Ensure widgets are created before being queried",
        ],
    }

    for error in errors:
        lines.append(f"\n{error}")
        error_type = error.split(':')[0] if ':' in error else 'Unknown'

        if error_type in common_issues:
            lines.append("\nPossible solutions:")
            for solution in common_issues[error_type]:
                lines.append(f"  {solution}")

    lines.append("\nGeneral debugging steps:")
    lines.append("  1. Check the full traceback for error location")
    lines.append("  2. Verify all imports are correct")
    lines.append("  3. Check widget names and IDs")
    lines.append("  4. Ensure proper indentation")
    lines.append("  5. Run with --verbose for more details")

    lines.append("=" * 70)
    return "\n".join(lines)


def generate_debug_report(
    app_file: Path,
    widgets: Optional[List[WidgetInfo]] = None,
    events: Optional[List[EventInfo]] = None,
    metrics: Optional[List[PerformanceMetric]] = None,
    errors: Optional[List[str]] = None
) -> str:
    """Generate a comprehensive debug report."""
    lines = []
    lines.append("=" * 70)
    lines.append(f"TEXTUAL DEBUG REPORT: {app_file.name}")
    lines.append(f"Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("=" * 70)

    if widgets:
        lines.append("\n" + format_widget_tree(widgets))

    if events:
        lines.append("\n\nRECENT EVENTS (last 20)")
        lines.append("-" * 70)
        for event in events[-20:]:
            lines.append(f"{event.timestamp:.4f} | {event.event_type:20} | {event.source} -> {event.target}")

    if metrics:
        lines.append("\n\nPERFORMANCE METRICS")
        lines.append("-" * 70)
        for metric in metrics[:10]:
            lines.append(f"{metric.function_name:30} | {metric.call_count:5} calls | "
                        f"{metric.total_time:.4f}s total | {metric.per_call_time:.6f}s/call")

    if errors:
        lines.append("\n\nERRORS DETECTED")
        lines.append("-" * 70)
        lines.append(diagnose_errors(app_file, errors))

    lines.append("\n" + "=" * 70)
    return "\n".join(lines)


# ============================================================================
# DEBUG MODE CLASS
# ============================================================================

class TextualDebugger:
    """Interactive debugger for Textual applications."""

    def __init__(self, app_instance, config: DebugConfig):
        """Initialize debugger."""
        self.app = app_instance
        self.config = config
        self.events_log: List[EventInfo] = []
        self.widgets: List[WidgetInfo] = []
        self.performance_metrics: List[PerformanceMetric] = []
        self.start_time = time.time()

    def start_debugging(self):
        """Start debugging session."""
        print("\n🔍 Starting Textual debugger...")
        print("Press Ctrl+C to stop debugging and view report\n")

        try:
            self.widgets = get_widget_tree(self.app)
            self._setup_event_tracing()
            self.app.run()
        except KeyboardInterrupt:
            self._generate_final_report()
        except Exception as e:
            print(f"\n❌ Error during debugging: {e}")
            traceback.print_exc()

    def _setup_event_tracing(self):
        """Setup event tracing if enabled."""
        if not self.config.trace_events:
            return

        original_methods = {}

        for method_name in dir(self.app):
            if method_name.startswith('on_'):
                original_method = getattr(self.app, method_name)
                if callable(original_method):
                    original_methods[method_name] = original_method

                    def make_traced_handler(name):
                        def handler(self, event):
                            self._trace_event(name, event)
                            return original_methods[name](event)
                        return handler

                    setattr(self.app, method_name, make_traced_handler(method_name).__get__(self.app, type(self.app)))

    def _trace_event(self, event_type: str, event):
        """Trace an event."""
        event_info = EventInfo(
            event_type=event_type,
            timestamp=time.time() - self.start_time,
            source=str(event),
            target="app",
            data={'type': type(event).__name__}
        )

        self.events_log.append(event_info)

        if self.config.verbose:
            print(f"[EVENT] {event_type}: {event}")

    def _generate_final_report(self):
        """Generate final debug report."""
        app_file = Path("debugged_app.py")
        report = generate_debug_report(
            app_file=app_file,
            widgets=self.widgets,
            events=self.events_log,
            metrics=self.performance_metrics,
        )

        if self.config.log_file:
            with open(self.config.log_file, 'w') as f:
                f.write(report)
            print(f"\n📝 Debug report saved to: {self.config.log_file}")
        else:
            print("\n" + report)


# ============================================================================
# MAIN FUNCTIONS
# ============================================================================

def analyze_app_file(app_file: Path, config: DebugConfig) -> None:
    """Analyze app file for debugging information."""
    try:
        with open(app_file, 'r') as f:
            content = f.read()

        ast_tree = ast.parse(content)

        widgets = extract_widgets_from_ast(ast_tree)

        if config.trace_widgets or config.verbose:
            widget_tree = format_widget_tree(widgets)
            print(widget_tree)

        if config.trace_layout or config.verbose:
            layout_analysis = analyze_layout(widgets)
            print("\n" + layout_analysis)

        if config.profile_performance:
            try:
                app_class = load_app_class(app_file)
                if app_class:
                    profile = profile_performance(app_class)
                    if profile:
                        print("\n" + profile)
            except Exception as e:
                print(f"Error during profiling: {e}")

    except Exception as e:
        print(f"Error analyzing app: {e}")
        traceback.print_exc()


def extract_widgets_from_ast(ast_tree: ast.AST) -> List[WidgetInfo]:
    """Extract widget information from AST."""
    widgets = []

    for node in ast.walk(ast_tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Attribute):
                widget_type = node.func.attr

                if widget_type in ['Container', 'Button', 'Label', 'Input', 'Static']:
                    widget_info = WidgetInfo(
                        name=f"{widget_type}_{node.lineno}",
                        type=widget_type,
                        id=None,
                        classes=[],
                        parent=None,
                    )
                    widgets.append(widget_info)

    return widgets


def load_app_class(app_file: Path):
    """Load app class from file."""
    module_name = app_file.stem

    import importlib.util
    spec = importlib.util.spec_from_file_location(module_name, app_file)
    module = importlib.util.module_from_spec(spec)

    try:
        spec.loader.exec_module(module)

        for item_name in dir(module):
            item = getattr(module, item_name)
            if (inspect.isclass(item) and
                hasattr(item, '__bases__') and
                any('App' in str(base) for base in item.__bases__)):
                return item
    except Exception as e:
        print(f"Error loading module: {e}")

    return None


def run_live_debug(app_file: Path, config: DebugConfig) -> None:
    """Run app in live debug mode."""
    try:
        app_class = load_app_class(app_file)
        if not app_class:
            print("❌ Could not find App class in file")
            return

        app_instance = app_class()
        debugger = TextualDebugger(app_instance, config)
        debugger.start_debugging()

    except Exception as e:
        print(f"Error running live debug: {e}")
        traceback.print_exc()


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Debug Textual TUI applications",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --inspect app.py
  %(prog)s --events app.py
  %(prog)s --profile app.py
  %(prog)s --live app.py --verbose
  %(prog)s --analyze app.py --output debug_report.txt
        """
    )

    parser.add_argument(
        'app_file',
        nargs='?',
        help='Path to Textual application file'
    )

    parser.add_argument(
        '--inspect',
        action='store_true',
        help='Inspect widget tree'
    )

    parser.add_argument(
        '--events',
        action='store_true',
        help='Trace event handlers'
    )

    parser.add_argument(
        '--layout',
        action='store_true',
        help='Analyze layout structure'
    )

    parser.add_argument(
        '--profile',
        action='store_true',
        help='Profile performance'
    )

    parser.add_argument(
        '--live',
        action='store_true',
        help='Run in live debug mode'
    )

    parser.add_argument(
        '--analyze',
        action='store_true',
        help='Full analysis mode (all checks)'
    )

    parser.add_argument(
        '--output',
        help='Output file for report'
    )

    parser.add_argument(
        '--log',
        help='Log file for debugging'
    )

    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Enable verbose output'
    )

    parser.add_argument(
        '--iterations',
        type=int,
        default=1,
        help='Number of iterations for profiling'
    )

    args = parser.parse_args()

    if not args.app_file:
        parser.print_help()
        sys.exit(1)

    app_path = Path(args.app_file)
    if not app_path.exists():
        print(f"❌ Error: File not found: {app_path}")
        sys.exit(1)

    config = DebugConfig(
        trace_events=args.events,
        trace_widgets=args.inspect,
        trace_layout=args.layout,
        profile_performance=args.profile,
        log_file=args.log,
        verbose=args.verbose or args.analyze,
    )

    print(f"\n🔍 Textual Debugger")
    print(f"Analyzing: {app_path}")
    print(f"Options: {', '.join([opt for opt, enabled in vars(args).items() if enabled and opt not in ['app_file']])}")
    print("-" * 70 + "\n")

    try:
        if args.live:
            run_live_debug(app_path, config)
        else:
            analyze_app_file(app_path, config)

            if args.output:
                with open(args.output, 'w') as f:
                    f.write("Debug analysis complete.\n")
                print(f"\n📝 Report saved to: {args.output}")

    except Exception as e:
        print(f"\n❌ Error: {e}")
        if args.verbose:
            traceback.print_exc()
        sys.exit(1)

    print("\n✅ Debug analysis complete!")


if __name__ == '__main__':
    main()
