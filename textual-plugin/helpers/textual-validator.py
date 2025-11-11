#!/usr/bin/env python3
"""
Textual Code Validator

This script validates Textual TUI applications for proper structure,
best practices, and common issues. It checks widgets, layouts, event
handlers, CSS styling, and provides comprehensive validation reports.

Features:
- Widget validation and compatibility checks
- Layout validation
- Event handler validation
- CSS styling validation
- Best practices checks
- Performance recommendations

Usage:
    python textual-validator.py app.py
    python textual-validator.py --fix app.py
    python textual-validator.py --verbose app.py
"""

import argparse
import ast
import os
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
import re


# ============================================================================
# VALIDATION CONSTANTS
# ============================================================================

REQUIRED_IMPORTS = {
    'App': 'from textual.app import App',
    'ComposeResult': 'from textual.app import ComposeResult',
}

VALID_WIDGETS = {
    'Button', 'Label', 'Input', 'Static', 'TextArea', 'Table',
    'DataTable', 'ListView', 'ListItem', 'Tabs', 'TabPane',
    'Switch', 'Checkbox', 'RadioSet', 'RadioButton', 'ProgressBar',
    'Select', 'OptionList', 'DirectoryTree', 'FileTree',
    'DataGrid', 'Tree', 'Markdown', 'Log', 'Pretty', 'Sparkline',
    'Gauge', 'Horizontal', 'Vertical', 'Container', 'ContentSwitcher',
    'Placeholder', 'LoadingIndicator', 'Collapsible', 'Badge',
    'Tag', 'Toast', 'ScreenSwitch', 'ContentTab',
}

VALID_LAYOUTS = {
    'Container', 'Horizontal', 'Vertical', 'Grid',
}

VALID_CONTAINERS = {
    'Container', 'Horizontal', 'Vertical', 'Tabs', 'TabPane',
    'Collapsible', 'ContentSwitcher', 'ScreenSwitch',
}

VALID_EVENTS = {
    'Mount', 'Unmount', 'Key', 'Click', 'Button', 'Input',
    'ListView', 'Tab', 'Switch', 'CheckBox', 'Tree', 'Log',
    'Message', 'Event',
}

DEPRECATED_WIDGETS = {
    'FooterTui', 'HeaderTui',  # Old names, replaced with Footer/Header
}

PERFORMANCE_TIPS = [
    "Use 'content-align' instead of nested containers for alignment",
    "Cache frequently accessed widgets with query_one()",
    "Use 'disabled' attribute instead of removing/re-adding widgets",
    "Minimize DOM queries by storing widget references",
    "Use CSS classes for common styling instead of inline styles",
    "Consider using 'reactive' for frequently changing values",
    "Use 'Lazy' widgets for large lists or grids",
]


# ============================================================================
# VALIDATION CLASSES
# ============================================================================

class TextualValidator:
    """Validates Textual applications."""

    def __init__(self, verbose: bool = False, fix: bool = False):
        """Initialize the validator.

        Args:
            verbose: Enable verbose output
            fix: Attempt to fix issues automatically
        """
        self.verbose = verbose
        self.fix = fix
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.suggestions: List[str] = []
        self.fixes_applied: List[str] = []
        self.ast_tree: Optional[ast.AST] = None
        self.file_path: Optional[Path] = None

    def validate_file(self, file_path: str) -> bool:
        """Validate a Textual application file.

        Args:
            file_path: Path to the file to validate

        Returns:
            True if validation passes, False otherwise
        """
        self.file_path = Path(file_path)

        if not self.file_path.exists():
            self.errors.append(f"File not found: {file_path}")
            return False

        try:
            with open(self.file_path, 'r') as f:
                content = f.read()

            self.ast_tree = ast.parse(content)

            self._validate_imports()
            self._validate_class_structure()
            self._validate_widgets()
            self._validate_layouts()
            self._validate_event_handlers()
            self._validate_css()
            self._validate_best_practices()
            self._validate_performance()

            if self.fix and self.errors:
                self._attempt_fixes()

            return len(self.errors) == 0

        except SyntaxError as e:
            self.errors.append(f"Syntax error: {e}")
            return False
        except Exception as e:
            self.errors.append(f"Validation error: {e}")
            return False

    def _validate_imports(self) -> None:
        """Validate required imports."""
        if not self.ast_tree:
            return

        imports = set()

        for node in ast.walk(self.ast_tree):
            if isinstance(node, ast.ImportFrom):
                if node.module and 'textual' in node.module:
                    for alias in node.names:
                        imports.add(alias.name)

            elif isinstance(node, ast.Import):
                for alias in node.names:
                    imports.add(alias.name)

        if 'App' not in imports and 'app' not in imports:
            self.errors.append("Missing required import: from textual.app import App")

        if 'ComposeResult' not in imports and 'compose_result' not in imports:
            self.warnings.append("Consider importing ComposeResult for type hints")

        self._log("Validated imports")

    def _validate_class_structure(self) -> None:
        """Validate class structure."""
        if not self.ast_tree:
            return

        app_classes = []

        for node in ast.walk(self.ast_tree):
            if isinstance(node, ast.ClassDef):
                for base in node.bases:
                    if isinstance(base, ast.Attribute):
                        if isinstance(base.value, ast.Name) and base.value.id == 'App':
                            app_classes.append(node)
                            break
                        if base.attr == 'App':
                            app_classes.append(node)
                            break

        if not app_classes:
            self.errors.append("No class inheriting from App found")
            return

        for app_class in app_classes:
            self._validate_app_methods(app_class)

        self._log(f"Validated {len(app_classes)} App class(es)")

    def _validate_app_methods(self, app_class: ast.ClassDef) -> None:
        """Validate App class methods."""
        has_compose = False
        has_mount = False

        for node in app_class.body:
            if isinstance(node, ast.FunctionDef):
                if node.name == 'compose':
                    has_compose = True
                    if not node.returns:
                        self.warnings.append(
                            f"Method 'compose' in {app_class.name} "
                            "should have return type hint (ComposeResult)"
                        )

                    has_compose_return = self._check_return_annotation(
                        node, 'ComposeResult'
                    )
                    if not has_compose_return:
                        self.warnings.append(
                            f"Method 'compose' in {app_class.name} "
                            "should return ComposeResult"
                        )

                elif node.name == 'on_mount':
                    has_mount = True

                elif node.name == 'on_key':
                    self.suggestions.append(
                        f"Consider using BINDINGS instead of on_key in {app_class.name}"
                    )

        if not has_compose:
            self.errors.append(
                f"App class {app_class.name} is missing 'compose' method"
            )

        self._log(f"Validated methods for {app_class.name}")

    def _validate_widgets(self) -> None:
        """Validate widget usage."""
        if not self.ast_tree:
            return

        widget_usage = {}

        for node in ast.walk(self.ast_tree):
            if isinstance(node, ast.Attribute):
                if isinstance(node.value, ast.Name):
                    widget_name = node.value.id

                    if node.attr in VALID_WIDGETS:
                        widget_usage[widget_name] = widget_usage.get(widget_name, 0) + 1

                    if node.attr in DEPRECATED_WIDGETS:
                        self.errors.append(
                            f"Deprecated widget '{node.attr}' found. "
                            f"Use '{node.attr}' replacement instead"
                        )

        self._log(f"Validated {sum(widget_usage.values())} widget(s)")

    def _validate_layouts(self) -> None:
        """Validate layout structure."""
        if not self.ast_tree:
            return

        yield_statements = []

        for node in ast.walk(self.ast_tree):
            if isinstance(node, ast.FunctionDef) and node.name == 'compose':
                yield_statements = [
                    n for n in ast.walk(node)
                    if isinstance(n, ast.Yield)
                ]
                break

        if not yield_statements:
            self.warnings.append("No yield statements found in compose method")

        for yield_node in yield_statements:
            if yield_node.value:
                self._check_widget_in_yield(yield_node.value)

        self._log("Validated layout structure")

    def _check_widget_in_yield(self, node: ast.AST) -> None:
        """Check if a widget is properly used in yield."""
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Attribute):
                widget_name = node.func.attr

                if widget_name in VALID_CONTAINERS:
                    pass
                elif widget_name not in VALID_WIDGETS and widget_name not in VALID_CONTAINERS:
                    self.warnings.append(f"Unknown widget or container: {widget_name}")

    def _validate_event_handlers(self) -> None:
        """Validate event handler methods."""
        if not self.ast_tree:
            return

        event_handlers = {}

        for node in ast.walk(self.ast_tree):
            if isinstance(node, ast.FunctionDef):
                if node.name.startswith('on_'):
                    parts = node.name[3:].split('_')
                    if len(parts) >= 2:
                        event_type = parts[0]
                        event_handlers[node.name] = event_type

                    if not node.args.args:
                        self.warnings.append(
                            f"Event handler '{node.name}' should have event parameter"
                        )

        for handler, event_type in event_handlers.items():
            if event_type not in VALID_EVENTS:
                self.warnings.append(
                    f"Unknown event type '{event_type}' in handler '{handler}'"
                )

        self._log(f"Validated {len(event_handlers)} event handler(s)")

    def _validate_css(self) -> None:
        """Validate CSS styling."""
        if not self.ast_tree:
            return

        css_strings = []

        for node in ast.walk(self.ast_tree):
            if isinstance(node, ast.Assign):
                if isinstance(node.targets[0], ast.Name):
                    if node.targets[0].id == 'CSS':
                        if isinstance(node.value, ast.Constant):
                            css_strings.append(node.value.value)

        for css_content in css_strings:
            self._validate_css_content(css_content)

        self._log("Validated CSS")

    def _validate_css_content(self, css: str) -> None:
        """Validate CSS content."""
        lines = css.split('\n')
        for i, line in enumerate(lines, 1):
            line = line.strip()

            if not line or line.startswith('/*'):
                continue

            if '{' in line and '}' not in line:
                self.errors.append(f"Unclosed CSS block starting at line {i}")

            if line.count('{') != line.count('}'):
                self.errors.append(f"Mismatched braces in CSS at line {i}")

            if 'import' in line.lower():
                self.errors.append(f"CSS import statement found at line {i} (not supported)")

        if 'quantum:' not in css and 'dark:' not in css:
            self.warnings.append(
                "Consider defining 'quantum' or 'dark' theme variants"
            )

    def _validate_best_practices(self) -> None:
        """Validate best practices."""
        if not self.ast_tree:
            return

        for node in ast.walk(self.ast_tree):
            if isinstance(node, ast.FunctionDef):
                if node.name == 'compose':
                    self._check_compose_best_practices(node)

    def _check_compose_best_practices(self, compose_node: ast.FunctionDef) -> None:
        """Check compose method best practices."""
        has_return_hint = compose_node.returns is not None
        if not has_return_hint:
            self.suggestions.append(
                "Add return type hint to compose method"
            )

        yield_count = 0
        for child in ast.walk(compose_node):
            if isinstance(child, ast.Yield):
                yield_count += 1

        if yield_count < 2:
            self.warnings.append(
                "compose method should yield at least Header and Footer"
            )

    def _validate_performance(self) -> None:
        """Validate performance-related code."""
        if not self.ast_tree:
            return

        query_count = 0
        for node in ast.walk(self.ast_tree):
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Attribute):
                    if node.func.attr == 'query_one':
                        query_count += 1
                        if node.func.value.id == 'self':
                            self.suggestions.append(
                                "Consider caching query_one results to avoid repeated DOM queries"
                            )

        if query_count > 5:
            self.warnings.append(
                f"Found {query_count} query_one calls. Consider caching results."
            )

        self._log("Validated performance")

    def _check_return_annotation(self, node: ast.FunctionDef, expected: str) -> bool:
        """Check if function has expected return annotation."""
        if not node.returns:
            return False

        if isinstance(node.returns, ast.Name):
            return node.returns.id == expected

        return False

    def _attempt_fixes(self) -> None:
        """Attempt to fix common issues automatically."""
        if not self.file_path:
            return

        try:
            with open(self.file_path, 'r') as f:
                content = f.read()

            original_content = content

            for error in self.errors:
                if 'Missing required import' in error:
                    content = self._fix_missing_imports(content)

            if content != original_content:
                with open(self.file_path, 'w') as f:
                    f.write(content)
                self.fixes_applied.append("Fixed missing imports")

                self.errors.clear()
                self.warnings.append("Auto-fixes applied. Re-run validation.")

        except Exception as e:
            self.errors.append(f"Failed to apply fixes: {e}")

    def _fix_missing_imports(self, content: str) -> str:
        """Fix missing imports."""
        lines = content.split('\n')

        import_line_idx = -1
        for i, line in enumerate(lines):
            if line.startswith('from textual.app import'):
                import_line_idx = i
                break

        if import_line_idx == -1:
            import_line = 'from textual.app import App, ComposeResult'
            lines.insert(0, import_line)
        else:
            if 'ComposeResult' not in lines[import_line_idx]:
                lines[import_line_idx] = lines[import_line_idx].replace(
                    'from textual.app import',
                    'from textual.app import'
                ) + ', ComposeResult'

        return '\n'.join(lines)

    def _log(self, message: str) -> None:
        """Log a message if verbose mode is enabled."""
        if self.verbose:
            print(f"  ✓ {message}")

    def print_report(self) -> None:
        """Print validation report."""
        print("\n" + "=" * 70)
        print(f"VALIDATION REPORT: {self.file_path.name if self.file_path else 'N/A'}")
        print("=" * 70)

        if self.errors:
            print(f"\n❌ ERRORS ({len(self.errors)}):")
            for i, error in enumerate(self.errors, 1):
                print(f"  {i}. {error}")

        if self.warnings:
            print(f"\n⚠️  WARNINGS ({len(self.warnings)}):")
            for i, warning in enumerate(self.warnings, 1):
                print(f"  {i}. {warning}")

        if self.suggestions:
            print(f"\n💡 SUGGESTIONS ({len(self.suggestions)}):")
            for i, suggestion in enumerate(self.suggestions, 1):
                print(f"  {i}. {suggestion}")

        if self.fixes_applied:
            print(f"\n🔧 FIXES APPLIED ({len(self.fixes_applied)}):")
            for i, fix in enumerate(self.fixes_applied, 1):
                print(f"  {i}. {fix}")

        print("\n" + "=" * 70)

        if not self.errors:
            print("✅ VALIDATION PASSED")
        else:
            print(f"❌ VALIDATION FAILED ({len(self.errors)} error(s))")

        print("=" * 70 + "\n")

        if self.suggestions:
            print("📋 PERFORMANCE TIPS:")
            for tip in PERFORMANCE_TIPS[:5]:
                print(f"  • {tip}")
            print()


def scan_directory(directory: str, pattern: str = "*.py") -> List[Path]:
    """Scan directory for Python files."""
    directory_path = Path(directory)
    return list(directory_path.glob(pattern))


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Validate Textual TUI applications",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s app.py
  %(prog)s --verbose app.py
  %(prog)s --fix app.py
  %(prog)s --dir ./src --recursive
        """
    )

    parser.add_argument(
        'file',
        nargs='?',
        help='File to validate'
    )

    parser.add_argument(
        '--dir',
        help='Directory to scan for Python files'
    )

    parser.add_argument(
        '--recursive',
        action='store_true',
        help='Scan directory recursively'
    )

    parser.add_argument(
        '--fix',
        action='store_true',
        help='Attempt to fix issues automatically'
    )

    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Enable verbose output'
    )

    parser.add_argument(
        '--pattern',
        default='*.py',
        help='File pattern to match (default: *.py)'
    )

    args = parser.parse_args()

    if not args.file and not args.dir:
        parser.error("Must specify either a file or directory to validate")

    files_to_validate = []

    if args.file:
        if not Path(args.file).exists():
            print(f"❌ Error: File not found: {args.file}")
            sys.exit(1)
        files_to_validate = [Path(args.file)]

    elif args.dir:
        if not Path(args.dir).exists():
            print(f"❌ Error: Directory not found: {args.dir}")
            sys.exit(1)

        if args.recursive:
            pattern = f"**/{args.pattern}"
        else:
            pattern = args.pattern

        files_to_validate = scan_directory(args.dir, pattern)
        files_to_validate = [f for f in files_to_validate if 'venv' not in str(f)]

    total_files = len(files_to_validate)
    passed = 0
    failed = 0

    print(f"\n🔍 Validating {total_files} file(s)...")

    for i, file_path in enumerate(files_to_validate, 1):
        print(f"\n[{i}/{total_files}] Validating: {file_path}")

        validator = TextualValidator(verbose=args.verbose, fix=args.fix)
        is_valid = validator.validate_file(str(file_path))

        validator.print_report()

        if is_valid:
            passed += 1
        else:
            failed += 1

    print("\n" + "=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Total files:   {total_files}")
    print(f"✅ Passed:      {passed}")
    print(f"❌ Failed:      {failed}")
    print(f"Success rate:  {(passed/total_files*100) if total_files > 0 else 0:.1f}%")
    print("=" * 70 + "\n")

    sys.exit(0 if failed == 0 else 1)


if __name__ == '__main__':
    main()
