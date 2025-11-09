"""
Skill: CLI UX Design Principles

This skill covers best practices for designing command-line interfaces
with excellent user experience, including modern CLI patterns, helpful
error messages, progressive discovery, and accessibility.
"""


# ============================================================================
# CLI UX CORE PRINCIPLES
# ============================================================================

CLI_UX_PRINCIPLES = """
CLI UX DESIGN PRINCIPLES
========================

## 1. Human-First Design

Modern CLIs are primarily used by humans, not just scripts.
Design for the human experience first.

**Key Principles:**
- Clear, readable output
- Helpful error messages
- Progressive discovery
- Consistent patterns
- Good defaults

## 2. Progressive Discovery

Users start knowing little about your tool. Guide them step-by-step.

**How to implement:**
- Provide helpful --help output
- Show examples in help text
- Suggest next steps in output
- Use interactive prompts when appropriate
- Offer tutorials or getting-started commands

**Example:**
```bash
# Bad
$ mytool
Error: missing required argument

# Good
$ mytool
Error: missing required argument 'file'

Usage: mytool <file> [options]

Try 'mytool --help' for more information
or 'mytool tutorial' to get started
```

## 3. Provide Feedback

Always let users know what's happening.

**Progress Indicators:**
- **Spinner** - For indeterminate operations
- **Progress Bar** - For operations with known duration
- **X of Y Pattern** - For batch operations (e.g., "Processing 3 of 10 files")

**Status Messages:**
- Start: "Loading data..."
- Success: "✓ Data loaded successfully (1.2s)"
- Error: "✗ Failed to load data: file not found"

## 4. Arguments vs Flags

**Arguments** - Required, positional
```bash
git commit -m "message"  # -m is a flag
docker run image         # image is an argument
```

**Flags** - Optional, named
```bash
ls -la                   # -l and -a are flags
npm install --save-dev   # --save-dev is a flag
```

**Best Practice:**
- Required inputs → positional arguments
- Optional inputs → flags
- Use both long (--verbose) and short (-v) forms
- Keep short flags to single letter

## 5. Helpful Error Messages

Every error should guide users to a solution.

**Bad Error:**
```
Error: invalid input
```

**Good Error:**
```
Error: invalid date format

Expected: YYYY-MM-DD
Received: 01/15/2025

Try: mytool --date 2025-01-15
```

**Error Message Template:**
1. What went wrong
2. Why it went wrong (if helpful)
3. How to fix it
4. Where to get more help

## 6. Consistency

**Command Structure:**
```bash
# Use consistent patterns
docker container ls
docker image ls
docker network ls

# Not mixed patterns
docker ps         # (list containers)
docker images     # (list images)
```

**Flag Naming:**
- Use same flag names across commands
- Follow conventions: -v/--verbose, -h/--help, -V/--version
- Keep short forms to one letter
- Use full words for long forms

## 7. Sensible Defaults

Choose defaults that work for 80% of use cases.

**Good Defaults:**
```bash
# Assume current directory
git status
# vs forcing: git status .

# Use standard output
mytool process file.txt
# vs forcing: mytool process file.txt --output stdout
```

## 8. Composability

Design for pipes and composition.

**Example:**
```bash
# Each tool does one thing well
cat file.txt | grep "error" | wc -l

# Your tool should work the same way
mytool extract --json data.db | jq '.users[] | .email'
```

**Guidelines:**
- Read from stdin if no file specified
- Write to stdout by default
- Use stderr for errors and messages
- Exit codes: 0 for success, non-zero for errors
- Support --quiet mode for scripting

## 9. Interactive When Helpful

Use interactivity for dangerous or complex operations.

**When to Use:**
- Confirming destructive actions
- Multi-step wizards
- Complex configuration

**Example:**
```bash
$ rm -rf important-data/
Are you sure you want to delete 'important-data/'?
This action cannot be undone. [y/N]: _
```

**Override for Scripts:**
```bash
# Always provide non-interactive mode
rm -rf important-data/ --yes
rm -rf important-data/ -y
```

## 10. Colors and Formatting

Use colors to aid comprehension, not just decoration.

**Color Guidelines:**
- Green → Success, safe actions
- Red → Errors, dangerous actions
- Yellow → Warnings, important info
- Blue → Information, neutral
- Dim/Gray → Less important info

**Respect Terminals:**
- Detect if output is terminal or pipe
- Disable colors when piped (unless --color=always)
- Support NO_COLOR environment variable
- Provide --no-color flag

## 11. Output Modes

Support both human and machine output.

**Human Output:**
```
┌─────────┬────────┬──────────┐
│ Name    │ Status │ Uptime   │
├─────────┼────────┼──────────┤
│ web-1   │ ✓ UP   │ 2d 3h    │
│ api-1   │ ✗ DOWN │ -        │
└─────────┴────────┴──────────┘
```

**Machine Output (--json):**
```json
[
  {"name": "web-1", "status": "up", "uptime": "2d3h"},
  {"name": "api-1", "status": "down", "uptime": null}
]
```

**Other Formats:**
- --json for JSON
- --yaml for YAML
- --csv for CSV
- --quiet for minimal output

## 12. Documentation

**In-Tool Help:**
```bash
mytool --help           # Overall help
mytool command --help   # Command-specific help
mytool --version        # Version info
```

**Help Output Structure:**
1. Brief description
2. Usage pattern
3. Arguments and flags
4. Examples
5. Additional resources

**Example:**
```
mytool - A tool for processing data

USAGE:
    mytool <command> [options]

COMMANDS:
    process    Process input files
    convert    Convert between formats
    validate   Validate data structure

OPTIONS:
    -v, --verbose    Enable verbose output
    -h, --help       Show this help message
    -V, --version    Show version

EXAMPLES:
    # Process a single file
    mytool process input.txt

    # Convert with custom output
    mytool convert data.json --to yaml --output data.yml

For more information, visit: https://docs.mytool.com
```
"""


# ============================================================================
# CLI DESIGN PATTERNS
# ============================================================================

CLI_PATTERNS = """
COMMON CLI PATTERNS
==================

## Pattern 1: Git-Style Subcommands

**Structure:** `tool <subcommand> [options] [arguments]`

**Example:**
```bash
docker container ls
docker image pull ubuntu
docker network create mynet
```

**When to Use:**
- Complex tools with multiple capabilities
- Logical grouping of related commands
- Need for extensibility

## Pattern 2: Flag-Based Configuration

**Structure:** `tool [flags] <arguments>`

**Example:**
```bash
ls -la /home
grep -r "pattern" .
curl -X POST -H "Content-Type: application/json" url
```

**When to Use:**
- Simple tools with few operations
- Many optional parameters
- Unix-style tools

## Pattern 3: Interactive Prompts

**Structure:** Tool asks questions to gather input

**Example:**
```bash
$ create-app
? What is your app name? my-app
? Select a template: (Use arrow keys)
❯ react
  vue
  angular
? Install dependencies? (Y/n) y
```

**When to Use:**
- Initial setup/configuration
- User-friendly tools for non-experts
- Complex multi-step processes

**Library Suggestions:**
- Python: inquirer, questionary, click.prompt()
- Node.js: inquirer, prompts, enquirer

## Pattern 4: Wizard Mode

**Structure:** Step-by-step guided process

**Example:**
```bash
$ mytool init --wizard

Step 1/5: Project Configuration
─────────────────────────────────
? Project name: my-project
? Description: A sample project
✓ Project configured

Step 2/5: Choose Template
─────────────────────────────────
...
```

**When to Use:**
- Complex initial setup
- First-time users
- Error-prone configuration

## Pattern 5: REPL (Read-Eval-Print Loop)

**Structure:** Interactive shell within your tool

**Example:**
```bash
$ mytool shell
mytool> load data.json
✓ Loaded 1,234 records
mytool> filter status = "active"
✓ Filtered to 856 records
mytool> export output.csv
✓ Exported to output.csv
mytool> exit
```

**When to Use:**
- Exploratory workflows
- Chaining multiple operations
- Data analysis tools

## Pattern 6: Watch Mode

**Structure:** Continuous monitoring and re-execution

**Example:**
```bash
$ mytool watch --file "src/**/*.js" --exec "npm test"
👀 Watching for changes...
✓ src/app.js changed - running tests...
✓ Tests passed (23/23)
```

**When to Use:**
- Development workflows
- File processing
- Continuous validation

## Pattern 7: Dry Run

**Structure:** Show what would happen without doing it

**Example:**
```bash
$ mytool delete --pattern "*.tmp" --dry-run
Would delete:
  - /tmp/cache.tmp (1.2 MB)
  - /tmp/temp.tmp (0.5 MB)
  - /tmp/session.tmp (0.1 MB)

Total: 3 files, 1.8 MB
Run without --dry-run to actually delete
```

**When to Use:**
- Destructive operations
- Bulk operations
- Operations with side effects

## Pattern 8: Pipeline Friendly

**Structure:** Read from stdin, write to stdout

**Example:**
```bash
cat data.json | mytool filter --key "status" | mytool format --to csv > output.csv
```

**Best Practices:**
- Accept stdin if no file argument
- Write primary output to stdout
- Write logs/errors to stderr
- Support --output flag for file output
"""


# ============================================================================
# CLI IMPLEMENTATION EXAMPLES
# ============================================================================

# Example 1: Using Click (Python)
CLICK_EXAMPLE = '''
import click

@click.group()
@click.version_option(version="1.0.0")
def cli():
    """My awesome CLI tool."""
    pass

@cli.command()
@click.argument("filename", type=click.Path(exists=True))
@click.option("--format", "-f", type=click.Choice(["json", "yaml"]), default="json")
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output")
def process(filename, format, verbose):
    """Process a data file."""
    if verbose:
        click.echo(f"Processing {filename} as {format}...")

    try:
        # Process file
        click.secho("✓ Success!", fg="green")
    except Exception as e:
        click.secho(f"✗ Error: {e}", fg="red", err=True)
        raise click.Abort()

if __name__ == "__main__":
    cli()
'''

# Example 2: Using Rich (Python) for beautiful output
RICH_EXAMPLE = '''
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from rich.panel import Panel

console = Console()

# Colored output
console.print("[green]✓[/green] Operation successful")
console.print("[red]✗[/red] Error occurred", style="bold")

# Tables
table = Table(title="Server Status")
table.add_column("Name", style="cyan")
table.add_column("Status", style="magenta")
table.add_column("Uptime", justify="right")

table.add_row("web-1", "✓ UP", "2d 3h")
table.add_row("api-1", "✗ DOWN", "-")

console.print(table)

# Progress bars
with Progress() as progress:
    task = progress.add_task("[green]Processing...", total=100)
    while not progress.finished:
        progress.update(task, advance=1)

# Panels/Callouts
console.print(Panel("Important message!", title="Warning", border_style="yellow"))
'''

# Example 3: Using Textual (Python) for TUI
TEXTUAL_EXAMPLE = '''
from textual.app import App
from textual.widgets import Header, Footer, Button, Static
from textual.containers import Container

class MyTool(App):
    """A TUI tool."""

    CSS = """
    Container {
        align: center middle;
        height: 100%;
    }

    Button {
        margin: 1;
    }
    """

    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    def compose(self):
        yield Header()
        with Container():
            yield Static("Welcome to MyTool!")
            yield Button("Process Data", id="process")
            yield Button("Settings", id="settings")
        yield Footer()

    def on_button_pressed(self, event):
        if event.button.id == "process":
            self.notify("Processing data...")

if __name__ == "__main__":
    app = MyTool()
    app.run()
'''


# ============================================================================
# ACCESSIBILITY IN CLI
# ============================================================================

CLI_ACCESSIBILITY = """
CLI ACCESSIBILITY GUIDELINES
============================

## 1. Color Independence

Never rely solely on color to convey information.

**Bad:**
```
✓ Success
✗ Failed
```

**Good:**
```
[SUCCESS] ✓ Operation completed
[ERROR] ✗ Operation failed
```

## 2. Screen Reader Friendly

- Use clear, descriptive text
- Avoid ASCII art as primary information
- Provide text alternatives for symbols

**Example:**
```
# Instead of just icons
✓ ✗ ⚠

# Use descriptive text
[OK] Test passed
[FAIL] Test failed
[WARN] Deprecated API used
```

## 3. Keyboard-Only Navigation

For interactive CLIs:
- Support arrow keys for navigation
- Provide keyboard shortcuts
- Show available keys in help

## 4. Respect Terminal Capabilities

```python
import sys

# Check if terminal supports colors
if sys.stdout.isatty():
    use_colors = True
else:
    use_colors = False

# Check terminal width
import shutil
width = shutil.get_terminal_size().columns
```

## 5. Environment Variables

Respect standard environment variables:
- NO_COLOR - Disable color output
- TERM - Terminal type
- COLUMNS, LINES - Terminal size
- LANG, LC_ALL - Locale settings

## 6. Clear Language

- Use simple, direct language
- Avoid jargon when possible
- Provide glossary for technical terms
- Support multiple languages when appropriate
"""


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def create_cli_help_text(tool_name, description, commands):
    """
    Generate well-formatted help text for a CLI tool.

    Args:
        tool_name: Name of the tool
        description: Brief description
        commands: Dict of command names to descriptions

    Returns:
        str: Formatted help text
    """
    help_text = f"""{tool_name} - {description}

USAGE:
    {tool_name} <command> [options]

COMMANDS:
"""

    # Find longest command name for alignment
    max_len = max(len(cmd) for cmd in commands.keys())

    for cmd, desc in commands.items():
        help_text += f"    {cmd:<{max_len}}    {desc}\n"

    help_text += """
OPTIONS:
    -h, --help       Show this help message
    -v, --verbose    Enable verbose output
    -V, --version    Show version information

Run '{tool_name} <command> --help' for more information on a command.
"""

    return help_text


def format_error_message(error_type, detail, suggestion=None):
    """
    Format a helpful error message.

    Args:
        error_type: Type of error
        detail: Detailed description
        suggestion: Optional suggestion for fixing

    Returns:
        str: Formatted error message
    """
    msg = f"✗ Error: {error_type}\n\n{detail}"

    if suggestion:
        msg += f"\n\nSuggestion: {suggestion}"

    return msg


# ============================================================================
# TESTING CLI UX
# ============================================================================

CLI_TESTING_CHECKLIST = """
CLI UX TESTING CHECKLIST
========================

## Basic Functionality
□ Help text is clear and complete
□ Version flag works
□ Default behavior is sensible
□ Error messages are helpful
□ Exit codes are appropriate (0 = success)

## User Experience
□ Common operations are easy
□ Flags have both short and long forms
□ Examples are provided
□ Progressive discovery is supported
□ Dangerous operations require confirmation

## Output
□ Colors work in terminals
□ Colors disabled when piped
□ NO_COLOR respected
□ Machine-readable format available (--json)
□ Progress indication for long operations

## Compatibility
□ Works on Linux
□ Works on macOS
□ Works on Windows
□ Works in different shells (bash, zsh, fish)
□ Works in CI/CD environments

## Accessibility
□ Color is not sole information carrier
□ Text alternatives for symbols
□ Screen reader friendly
□ Keyboard-only navigation (for TUIs)

## Documentation
□ README with quick start
□ Comprehensive --help output
□ Example usage shown
□ Link to full documentation
□ Common errors documented
"""

if __name__ == "__main__":
    print(CLI_UX_PRINCIPLES)
