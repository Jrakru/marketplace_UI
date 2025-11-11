# textual-examples-collection

Common Textual patterns, practical code examples, real-world use cases, and ready-to-use patterns for TUI development.

## Overview

This collection provides practical, ready-to-use Textual patterns and examples. Each example is self-contained and demonstrates best practices for common TUI use cases.

## Basic Application Patterns

### Simple Counter App

```python
from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal
from textual.widgets import Button, Static

class CounterApp(App):
    """Simple counter application."""

    CSS = """
    Screen {
        align: center middle;
    }

    Vertical {
        width: 50;
        height: 10;
        border: solid $primary;
        padding: 1;
    }

    #display {
        text-align: center;
        height: 3;
        content-align: center middle;
    }

    Horizontal {
        height: 3;
    }
    """

    def __init__(self):
        super().__init__()
        self.count = 0

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Static("Counter App", classes="title")
            yield Static("0", id="display")
            with Horizontal():
                yield Button("−", variant="error", id="decrement")
                yield Button("Reset", id="reset")
                yield Button("+", variant="success", id="increment")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "increment":
            self.count += 1
        elif event.button.id == "decrement":
            self.count -= 1
        elif event.button.id == "reset":
            self.count = 0

        self.query_one("#display", Static).update(str(self.count))

if __name__ == "__main__":
    app = CounterApp()
    app.run()
```

### Todo List App

```python
from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal
from textual.widgets import Button, Input, Static, Checkbox
from dataclasses import dataclass

@dataclass
class TodoItem:
    id: str
    text: str
    completed: bool = False

class TodoApp(App):
    """Todo list application."""

    CSS = """
    Vertical {
        padding: 1;
    }

    #header {
        text-align: center;
        height: 3;
        text-style: bold;
        content-align: center middle;
    }

    Horizontal {
        height: 3;
    }

    #todo-list {
        border: solid $panel;
        padding: 1;
    }

    Checkbox {
        margin: 0 1;
    }
    """

    def __init__(self):
        super().__init__()
        self.todos = []

    def compose(self) -> ComposeResult:
        yield Static("Todo List", id="header")
        with Horizontal():
            self.input = Input(placeholder="Add new todo...")
            yield self.input
            yield Button("Add", variant="primary", id="add")
        with Vertical(id="todo-list"):
            for todo in self.todos:
                yield self.create_todo_widget(todo)

    def create_todo_widget(self, todo: TodoItem) -> Horizontal:
        """Create widget for a todo item."""
        with Horizontal(id=todo.id):
            checkbox = Checkbox(todo.text, value=todo.completed)
            checkbox.set_class(todo.completed, "completed")
            yield checkbox
            yield Button("Delete", variant="error", id=f"delete-{todo.id}")

    def on_input_submitted(self, event: Input.Submitted) -> None:
        """Add todo on Enter."""
        if event.input.value.strip():
            self.add_todo(event.input.value)
            event.input.value = ""

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        if event.button.id == "add":
            if self.input.value.strip():
                self.add_todo(self.input.value)
                self.input.value = ""
        elif event.button.id.startswith("delete-"):
            todo_id = event.button.id.replace("delete-", "")
            self.delete_todo(todo_id)

    def on_checkbox_changed(self, event: Checkbox.Changed) -> None:
        """Handle checkbox toggles."""
        # Find todo by checkbox parent ID
        todo_id = event.checkbox.parent.id
        self.toggle_todo(todo_id, event.checkbox.value)

    def add_todo(self, text: str):
        """Add a new todo."""
        import uuid
        todo_id = str(uuid.uuid4())[:8]
        todo = TodoItem(id=todo_id, text=text)

        self.todos.append(todo)

        # Mount new widget
        widget = self.create_todo_widget(todo)
        self.query_one("#todo-list").mount(widget)

    def delete_todo(self, todo_id: str):
        """Delete a todo."""
        # Remove from data
        self.todos = [t for t in self.todos if t.id != todo_id]

        # Remove widget
        widget = self.query_one(f"#{todo_id}")
        widget.remove()

    def toggle_todo(self, todo_id: str, completed: bool):
        """Toggle todo completion."""
        # Update data
        for todo in self.todos:
            if todo.id == todo_id:
                todo.completed = completed
                break

        # Update widget styling
        checkbox = self.query_one(f"#{todo_id} Checkbox")
        checkbox.set_class(completed, "completed")

if __name__ == "__main__":
    app = TodoApp()
    app.run()
```

### File Browser

```python
import os
from pathlib import Path
from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal
from textual.widgets import Static, Button, Label
from textual.widgets import Tree

class FileBrowserApp(App):
    """Simple file browser."""

    CSS = """
    Horizontal {
        height: 1;
    }

    Tree {
        border: solid $panel;
    }

    #preview {
        border: solid $accent;
        padding: 1;
        height: 10;
    }
    """

    def compose(self) -> ComposeResult:
        self.current_path = Path.cwd()
        yield Static(f"Current Directory: {self.current_path}", id="path")

        with Horizontal():
            self.tree = Tree()
            yield self.tree

            Vertical(id="preview"):
                yield Static("Select a file to preview", id="preview-content")

        with Horizontal():
            yield Button("Parent Directory", id="parent")
            yield Button("Refresh", id="refresh")

    def on_mount(self) -> None:
        """Populate tree on mount."""
        self.populate_tree()

    def populate_tree(self):
        """Populate tree with directory contents."""
        root = self.tree.root
        root.reset()

        # Add current directory
        current_node = root.add(f"📁 {self.current_path.name}")

        try:
            # Add directories first
            dirs = sorted(
                [d for d in self.current_path.iterdir() if d.is_dir()],
                key=lambda x: x.name.lower()
            )

            for directory in dirs:
                node = current_node.add(f"📁 {directory.name}", directory)
                # Add dummy child to enable expand icon
                node.add_leaf("")

            # Add files
            files = sorted(
                [f for f in self.current_path.iterdir() if f.is_file()],
                key=lambda x: x.name.lower()
            )

            for file in files:
                icon = self.get_file_icon(file.suffix)
                current_node.add_leaf(f"{icon} {file.name}", file)

        except PermissionError:
            current_node.add_leaf("Permission denied")

    def get_file_icon(self, extension: str) -> str:
        """Get icon for file extension."""
        icons = {
            ".py": "🐍",
            ".txt": "📄",
            ".md": "📝",
            ".json": "📋",
            ".html": "🌐",
            ".css": "🎨",
            ".js": "⚡",
            ".png": "🖼️",
            ".jpg": "🖼️",
        }
        return icons.get(extension.lower(), "📄")

    def on_tree_node_selected(self, event: Tree.NodeSelected) -> None:
        """Handle tree node selection."""
        node = event.node

        if node.data:
            # It's a file or directory
            path = Path(node.data)

            if path.is_file():
                self.preview_file(path)
            elif path.is_dir():
                self.change_directory(path)

    def change_directory(self, path: Path):
        """Change current directory."""
        self.current_path = path
        self.query_one("#path", Static).update(f"Current Directory: {self.current_path}")
        self.populate_tree()

    def preview_file(self, path: Path):
        """Preview file contents."""
        try:
            with open(path, 'r') as f:
                content = f.read(500)  # First 500 chars
                if len(f.read()) > 500:
                    content += "\n\n... (truncated)"

            self.query_one("#preview-content", Static).update(
                f"📄 {path.name}\n\n{content}"
            )
        except Exception as e:
            self.query_one("#preview-content", Static).update(
                f"Cannot preview: {e}"
            )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        if event.button.id == "parent":
            self.change_directory(self.current_path.parent)
        elif event.button.id == "refresh":
            self.populate_tree()

if __name__ == "__main__":
    app = FileBrowserApp()
    app.run()
```

## Data Display Patterns

### Data Table with CRUD Operations

```python
from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal
from textual.widgets import DataTable, Button, Input, Static
from dataclasses import dataclass

@dataclass
class User:
    id: int
    name: str
    email: str
    role: str

class UserManagementApp(App):
    """User management with data table."""

    CSS = """
    Vertical {
        padding: 1;
    }

    #controls {
        height: 3;
    }

    DataTable {
        border: solid $panel;
        height: 15;
    }

    #form {
        border: solid $accent;
        padding: 1;
    }
    """

    def __init__(self):
        super().__init__()
        self.users = [
            User(1, "Alice Johnson", "alice@example.com", "Admin"),
            User(2, "Bob Smith", "bob@example.com", "User"),
            User(3, "Carol Davis", "carol@example.com", "User"),
        ]
        self.next_id = 4
        self.selected_user = None

    def compose(self) -> ComposeResult:
        yield Static("User Management", classes="title")
        with Horizontal(id="controls"):
            yield Button("Add User", variant="success", id="add")
            yield Button("Edit User", variant="primary", id="edit")
            yield Button("Delete User", variant="error", id="delete")
            yield Static("", classes="expand")
            yield Button("Refresh", id="refresh")

        self.table = DataTable()
        self.table.add_columns("ID", "Name", "Email", "Role")
        yield self.table

        with Vertical(id="form"):
            yield Static("User Form", classes="title")
            with Horizontal():
                yield Static("Name:", size=(10, 1))
                self.name_input = Input(placeholder="Enter name...")
                yield self.name_input
            with Horizontal():
                yield Static("Email:", size=(10, 1))
                self.email_input = Input(placeholder="Enter email...")
                yield self.email_input
            with Horizontal():
                yield Static("Role:", size=(10, 1))
                self.role_input = Input(placeholder="Enter role...")
                yield self.role_input
            with Horizontal():
                yield Button("Save", variant="success", id="save")
                yield Button("Cancel", id="cancel")

    def on_mount(self) -> None:
        """Populate table on mount."""
        self.populate_table()

    def populate_table(self):
        """Populate data table."""
        self.table.clear(rows=True)
        for user in self.users:
            self.table.add_row(
                str(user.id),
                user.name,
                user.email,
                user.role,
                key=str(user.id)
            )

    def on_data_table_row_selected(self, event: DataTable.RowSelected) -> None:
        """Handle row selection."""
        row_key = str(event.row_key)
        self.selected_user = next(
            (u for u in self.users if str(u.id) == row_key),
            None
        )

        if self.selected_user:
            self.load_user_form(self.selected_user)

    def load_user_form(self, user: User):
        """Load user into form."""
        self.name_input.value = user.name
        self.email_input.value = user.email
        self.role_input.value = user.role

    def clear_form(self):
        """Clear form inputs."""
        self.name_input.value = ""
        self.email_input.value = ""
        self.role_input.value = ""
        self.selected_user = None

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        if event.button.id == "add":
            self.clear_form()
            self.name_input.focus()
        elif event.button.id == "save":
            self.save_user()
        elif event.button.id == "cancel":
            self.clear_form()
        elif event.button.id == "delete":
            self.delete_user()
        elif event.button.id == "refresh":
            self.populate_table()

    def save_user(self):
        """Save user (create or update)."""
        name = self.name_input.value.strip()
        email = self.email_input.value.strip()
        role = self.role_input.value.strip()

        if not all([name, email, role]):
            self.bell()
            return

        if self.selected_user:
            # Update existing user
            self.selected_user.name = name
            self.selected_user.email = email
            self.selected_user.role = role
        else:
            # Add new user
            new_user = User(self.next_id, name, email, role)
            self.users.append(new_user)
            self.next_id += 1

        self.populate_table()
        self.clear_form()

    def delete_user(self):
        """Delete selected user."""
        if not self.selected_user:
            self.bell()
            return

        self.users = [u for u in self.users if u.id != self.selected_user.id]
        self.populate_table()
        self.clear_form()

if __name__ == "__main__":
    app = UserManagementApp()
    app.run()
```

### Log Viewer with Filtering

```python
import time
from datetime import datetime
from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal
from textual.widgets import Log, Input, Button, Static
from textual.widgets import Tabs, TabPane

class LogViewerApp(App):
    """Log viewer with filtering and categories."""

    CSS = """
    Vertical {
        padding: 1;
    }

    #controls {
        height: 3;
    }

    Input {
        margin: 0 1;
    }

    Tabs {
        height: 3;
    }

    Log {
        border: solid $panel;
    }
    """

    def __init__(self):
        super().__init__()
        self.logs = []
        self.log_buffer_size = 1000

    def compose(self) -> ComposeResult:
        yield Static("Log Viewer", classes="title")

        with Horizontal(id="controls"):
            self.search_input = Input(placeholder="Filter logs...")
            yield self.search_input
            yield Button("Clear", id="clear")
            yield Button("Pause", id="pause")

        with Tabs("All", "Error", "Warning", "Info", "Debug"):
            with TabPane("All", id="all"):
                yield Log(id="log-all")
            with TabPane("Errors", id="error"):
                yield Log(id="log-error")
            with TabPane("Warnings", id="warning"):
                yield Log(id="log-warning")
            with TabPane("Info", id="info"):
                yield Log(id="log-info")
            with TabPane("Debug", id="debug"):
                yield Log(id="log-debug")

        # Start log generator
        self.set_interval(1.0, self.generate_log)

    def generate_log(self):
        """Generate sample logs."""
        import random

        levels = ["ERROR", "WARNING", "INFO", "DEBUG"]
        messages = [
            "Database connection established",
            "User logged in",
            "API request processed",
            "Cache updated",
            "Configuration loaded",
            "Backup completed",
            "Cleanup task started",
        ]

        level = random.choice(levels)
        message = random.choice(messages)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log_entry = f"[{timestamp}] [{level}] {message}"

        self.logs.append({
            "level": level,
            "message": message,
            "entry": log_entry,
            "timestamp": timestamp
        })

        # Keep buffer size in check
        if len(self.logs) > self.log_buffer_size:
            self.logs.pop(0)

        self.update_logs()

    def update_logs(self):
        """Update all log displays."""
        filter_text = self.search_input.value.lower()

        for tab_id, level in [
            ("all", None),
            ("error", "ERROR"),
            ("warning", "WARNING"),
            ("info", "INFO"),
            ("debug", "DEBUG"),
        ]:
            log_widget = self.query_one(f"#log-{tab_id}", Log)
            log_widget.clear()

            filtered_logs = self.logs
            if level:
                filtered_logs = [l for l in filtered_logs if l["level"] == level]

            if filter_text:
                filtered_logs = [
                    l for l in filtered_logs
                    if filter_text in l["message"].lower()
                ]

            for log in filtered_logs[-100:]:  # Show last 100
                level = log["level"]
                if level == "ERROR":
                    log_widget.write(log["entry"], severity="error")
                elif level == "WARNING":
                    log_widget.write(log["entry"], severity="warn")
                elif level == "DEBUG":
                    log_widget.write(log["entry"], severity="debug")
                else:
                    log_widget.write(log["entry"], severity="info")

    def on_input_changed(self, event: Input.Changed) -> None:
        """Handle search filter."""
        if event.input == self.search_input:
            self.update_logs()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        if event.button.id == "clear":
            self.logs.clear()
            self.update_logs()
        elif event.button.id == "pause":
            # Toggle pause state
            button = event.button
            if button.label == "Pause":
                button.label = "Resume"
                self.set_timer(0, self.stop_logging)
            else:
                button.label = "Pause"
                self.set_interval(1.0, self.generate_log)

    def stop_logging(self):
        """Stop log generation."""
        pass  # Interval timers stop automatically when replaced

if __name__ == "__main__":
    app = LogViewerApp()
    app.run()
```

## Interactive Patterns

### Settings Panel

```python
from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal, Container
from textual.widgets import Static, Button, Switch, Select, Slider, Input
from textual.widgets import Tabs, TabPane

class SettingsApp(App):
    """Application settings panel."""

    CSS = """
    Tabs {
        height: 3;
    }

    Container.settings-group {
        border: solid $panel;
        padding: 1;
        margin: 1 0;
    }

    .setting-row {
        height: 3;
        margin: 0 1;
    }

    Static.setting-label {
        width: 20;
        text-align: right;
        margin: 0 1;
    }
    """

    def __init__(self):
        super().__init__()
        self.settings = {
            "theme": "dark",
            "notifications": True,
            "auto_save": True,
            "font_size": 14,
            "language": "en",
        }

    def compose(self) -> ComposeResult:
        yield Static("Settings", classes="title")

        with Tabs("General", "Appearance", "Advanced"):
            with TabPane("General", id="general"):
                self.create_general_settings()
            with TabPane("Appearance", id="appearance"):
                self.create_appearance_settings()
            with TabPane("Advanced", id="advanced"):
                self.create_advanced_settings()

        with Horizontal():
            yield Static("", classes="expand")
            yield Button("Reset", variant="warning", id="reset")
            yield Button("Save", variant="success", id="save")

    def create_general_settings(self):
        """Create general settings."""
        with Container(classes="settings-group"):
            yield Static("General Settings", classes="title")

            with Horizontal(classes="setting-row"):
                yield Static("Language:", classes="setting-label")
                yield Select(
                    [
                        ("English", "en"),
                        ("Spanish", "es"),
                        ("French", "fr"),
                        ("German", "de"),
                    ],
                    value=self.settings["language"],
                    id="language"
                )

            with Horizontal(classes="setting-row"):
                yield Static("Notifications:", classes="setting-label")
                yield Switch(value=self.settings["notifications"], id="notifications")

            with Horizontal(classes="setting-row"):
                yield Static("Auto Save:", classes="setting-label")
                yield Switch(value=self.settings["auto_save"], id="auto-save")

    def create_appearance_settings(self):
        """Create appearance settings."""
        with Container(classes="settings-group"):
            yield Static("Appearance", classes="title")

            with Horizontal(classes="setting-row"):
                yield Static("Theme:", classes="setting-label")
                yield Select(
                    [
                        ("Dark", "dark"),
                        ("Light", "light"),
                        ("Auto", "auto"),
                    ],
                    value=self.settings["theme"],
                    id="theme"
                )

            with Horizontal(classes="setting-row"):
                yield Static("Font Size:", classes="setting-label")
                yield Slider(
                    min=10,
                    max=24,
                    value=self.settings["font_size"],
                    id="font-size"
                )

            # Font size value display
            yield Static(f"Current: {self.settings['font_size']}px", id="font-size-display")

    def create_advanced_settings(self):
        """Create advanced settings."""
        with Container(classes="settings-group"):
            yield Static("Advanced Settings", classes="title")

            with Horizontal(classes="setting-row"):
                yield Static("API Endpoint:", classes="setting-label")
                yield Input("https://api.example.com", id="api-endpoint")

            with Horizontal(classes="setting-row"):
                yield Static("Timeout (s):", classes="setting-label")
                yield Input("30", id="timeout")

    def on_select_changed(self, event: Select.Changed) -> None:
        """Handle select changes."""
        if event.select.id == "language":
            self.settings["language"] = event.value
        elif event.select.id == "theme":
            self.settings["theme"] = event.value

    def on_switch_changed(self, event: Switch.Changed) -> None:
        """Handle switch changes."""
        if event.switch.id == "notifications":
            self.settings["notifications"] = event.value
        elif event.switch.id == "auto-save":
            self.settings["auto_save"] = event.value

    def on_slider_changed(self, event: Slider.Changed) -> None:
        """Handle slider changes."""
        if event.slider.id == "font-size":
            self.settings["font_size"] = event.value
            # Update display
            display = self.query_one("#font-size-display", Static)
            display.update(f"Current: {event.value}px")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        if event.button.id == "save":
            self.save_settings()
        elif event.button.id == "reset":
            self.reset_settings()

    def save_settings(self):
        """Save settings."""
        # In a real app, save to file/database
        print(f"Settings saved: {self.settings}")
        self.bell()

    def reset_settings(self):
        """Reset settings to defaults."""
        self.settings = {
            "theme": "dark",
            "notifications": True,
            "auto_save": True,
            "font_size": 14,
            "language": "en",
        }
        self.app.reload()  # Reload to refresh UI

if __name__ == "__main__":
    app = SettingsApp()
    app.run()
```

### Wizard/Multi-step Form

```python
from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal, Container
from textual.widgets import Static, Button, Input, Checkbox
from textual.widgets import RadioSet, RadioButton, ProgressBar

class WizardApp(App):
    """Multi-step wizard application."""

    CSS = """
    Container {
        padding: 1;
    }

    #step-container {
        border: solid $primary;
        height: 20;
    }

    .step {
        display: none;
        padding: 2;
    }

    .step.active {
        display: block;
    }

    ProgressBar {
        height: 1;
    }
    """

    def __init__(self):
        super().__init__()
        self.current_step = 0
        self.total_steps = 3
        self.data = {
            "name": "",
            "email": "",
            "username": "",
            "password": "",
            "notifications": False,
        }

    def compose(self) -> ComposeResult:
        yield Static("Account Setup Wizard", classes="title")
        yield ProgressBar(total=self.total_steps, id="progress")

        with Container(id="step-container"):
            self.create_step_1()
            self.create_step_2()
            self.create_step_3()

        with Horizontal():
            yield Button("Previous", id="prev", disabled=True)
            yield Static("", classes="expand")
            yield Button("Next", id="next")
            yield Button("Finish", id="finish", disabled=True)

    def create_step_1(self):
        """Step 1: Personal Information."""
        with Vertical(classes="step active", id="step-1"):
            yield Static("Step 1: Personal Information", classes="title")

            with Horizontal():
                yield Static("Name:", size=(15, 1))
                self.name_input = Input(placeholder="Enter your full name...")
                yield self.name_input

            with Horizontal():
                yield Static("Email:", size=(15, 1))
                self.email_input = Input(placeholder="Enter your email...")
                yield self.email_input

    def create_step_2(self):
        """Step 2: Account Details."""
        with Vertical(classes="step", id="step-2"):
            yield Static("Step 2: Account Details", classes="title")

            with Horizontal():
                yield Static("Username:", size=(15, 1))
                self.username_input = Input(placeholder="Choose a username...")
                yield self.username_input

            with Horizontal():
                yield Static("Password:", size=(15, 1))
                self.password_input = Input(placeholder="Choose a password...", password=True)
                yield self.password_input

            with Horizontal():
                yield Static("Confirm:", size=(15, 1))
                self.confirm_password_input = Input(placeholder="Confirm password...", password=True)
                yield self.confirm_password_input

    def create_step_3(self):
        """Step 3: Preferences."""
        with Vertical(classes="step", id="step-3"):
            yield Static("Step 3: Preferences", classes="title")

            with Vertical():
                yield Static("Email Notifications:")
                self.email_notifications = Checkbox("Receive email notifications", value=True)
                yield self.email_notifications

            yield Static("\nReview Your Information:", classes="title")
            self.review_display = Static("")
            yield self.review_display

    def update_step(self):
        """Update wizard step display."""
        # Hide all steps
        for step in self.query(".step").results():
            step.remove_class("active")

        # Show current step
        current = self.query_one(f"#step-{self.current_step + 1}")
        current.add_class("active")

        # Update progress
        progress = self.query_one("#progress", ProgressBar)
        progress.update(self.current_step + 1)

        # Update buttons
        prev_btn = self.query_one("#prev", Button)
        next_btn = self.query_one("#next", Button)
        finish_btn = self.query_one("#finish", Button)

        prev_btn.disabled = self.current_step == 0
        next_btn.disabled = self.current_step == self.total_steps - 1
        finish_btn.disabled = self.current_step != self.total_steps - 1

        # Update review on final step
        if self.current_step == 2:
            self.update_review()

    def update_review(self):
        """Update review display."""
        review = f"""Name: {self.data['name']}
Email: {self.data['email']}
Username: {self.data['username']}
Notifications: {'Yes' if self.data['notifications'] else 'No'}"""

        self.review_display.update(review)

    def validate_step(self, step: int) -> bool:
        """Validate current step."""
        if step == 0:
            # Validate step 1
            if not self.name_input.value.strip():
                self.bell()
                return False
            if not self.email_input.value.strip() or "@" not in self.email_input.value:
                self.bell()
                return False
            self.data["name"] = self.name_input.value
            self.data["email"] = self.email_input.value

        elif step == 1:
            # Validate step 2
            if not self.username_input.value.strip():
                self.bell()
                return False
            if len(self.password_input.value) < 8:
                self.bell()
                return False
            if self.password_input.value != self.confirm_password_input.value:
                self.bell()
                return False
            self.data["username"] = self.username_input.value
            self.data["password"] = self.password_input.value

        elif step == 2:
            # Validate step 3
            self.data["notifications"] = self.email_notifications.value

        return True

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        if event.button.id == "next":
            if self.validate_step(self.current_step):
                self.current_step = min(self.current_step + 1, self.total_steps - 1)
                self.update_step()

        elif event.button.id == "prev":
            self.current_step = max(self.current_step - 1, 0)
            self.update_step()

        elif event.button.id == "finish":
            self.finish_wizard()

    def finish_wizard(self):
        """Complete the wizard."""
        # In a real app, save data or submit form
        print(f"Account created: {self.data}")
        self.bell()
        self.exit()

    def on_mount(self) -> None:
        """Initialize wizard."""
        self.update_step()

if __name__ == "__main__":
    app = WizardApp()
    app.run()
```

## Dashboard Patterns

### System Monitor Dashboard

```python
import psutil
import time
from datetime import datetime
from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal, Grid
from textual.widgets import Static, ProgressBar, Label
from textual.widgets import DataTable

class SystemMonitorApp(App):
    """System monitoring dashboard."""

    CSS = """
    Grid {
        grid-gutter: 1;
    }

    Container.metric {
        border: solid $panel;
        padding: 1;
        height: 8;
    }

    Container.metric .title {
        text-align: center;
        text-style: bold;
    }

    Container.metric .value {
        text-align: center;
        font-size: 2;
    }

    DataTable {
        height: 15;
        border: solid $panel;
    }
    """

    def __init__(self):
        super().__init__()
        self.processes = []
        self.update_interval = 1.0

    def compose(self) -> ComposeResult:
        yield Static("System Monitor", classes="title")
        yield Static(f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", id="timestamp")

        with Grid():
            # CPU Usage
            with Vertical(classes="metric", id="cpu-metric"):
                yield Static("CPU Usage", classes="title")
                yield Static("--", id="cpu-value", classes="value")
                yield ProgressBar(id="cpu-bar")

            # Memory Usage
            with Vertical(classes="metric", id="mem-metric"):
                yield Static("Memory Usage", classes="title")
                yield Static("--", id="mem-value", classes="value")
                yield ProgressBar(id="mem-bar")

            # Disk Usage
            with Vertical(classes="metric", id="disk-metric"):
                yield Static("Disk Usage", classes="title")
                yield Static("--", id="disk-value", classes="value")
                yield ProgressBar(id="disk-bar")

            # Network
            with Vertical(classes="metric", id="net-metric"):
                yield Static("Network", classes="title")
                yield Static("--", id="net-value", classes="value")
                yield Static("", id="net-details")

        yield Static("\nTop Processes", classes="title")
        self.process_table = DataTable()
        self.process_table.add_columns("PID", "Name", "CPU%", "Memory%", "Status")
        yield self.process_table

    def on_mount(self) -> None:
        """Start monitoring."""
        self.set_interval(self.update_interval, self.update_metrics)

    def update_metrics(self):
        """Update system metrics."""
        # CPU
        cpu_percent = psutil.cpu_percent(interval=None)
        cpu_value = self.query_one("#cpu-value", Static)
        cpu_value.update(f"{cpu_percent:.1f}%")
        cpu_bar = self.query_one("#cpu-bar", ProgressBar)
        cpu_bar.update(cpu_percent / 100.0)

        # Memory
        memory = psutil.virtual_memory()
        mem_percent = memory.percent
        mem_value = self.query_one("#mem-value", Static)
        mem_value.update(f"{mem_percent:.1f}%")
        mem_bar = self.query_one("#mem-bar", ProgressBar)
        mem_bar.update(mem_percent / 100.0)

        # Disk
        disk = psutil.disk_usage('/')
        disk_percent = (disk.used / disk.total) * 100
        disk_value = self.query_one("#disk-value", Static)
        disk_value.update(f"{disk_percent:.1f}%")
        disk_bar = self.query_one("#disk-bar", ProgressBar)
        disk_bar.update(disk_percent / 100.0)

        # Network
        net_io = psutil.net_io_counters()
        net_value = self.query_one("#net-value", Static)
        net_value.update(f"↑ {self.format_bytes(net_io.bytes_sent)} ↓ {self.format_bytes(net_io.bytes_recv)}")

        # Update timestamp
        timestamp = self.query_one("#timestamp", Static)
        timestamp.update(f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        # Update processes
        self.update_processes()

    def update_processes(self):
        """Update process list."""
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent', 'status']):
            try:
                processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass

        # Sort by CPU usage
        processes.sort(key=lambda x: x['cpu_percent'] or 0, reverse=True)

        # Update table
        self.process_table.clear(rows=True)
        for proc in processes[:20]:  # Top 20
            self.process_table.add_row(
                str(proc['pid']),
                proc['name'][:20],
                f"{proc['cpu_percent']:.1f}" if proc['cpu_percent'] else "0.0",
                f"{proc['memory_percent']:.1f}" if proc['memory_percent'] else "0.0",
                proc['status'] or "unknown"
            )

    def format_bytes(self, bytes_val):
        """Format bytes to human readable."""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if bytes_val < 1024.0:
                return f"{bytes_val:.1f} {unit}"
            bytes_val /= 1024.0
        return f"{bytes_val:.1f} PB"

if __name__ == "__main__":
    app = SystemMonitorApp()
    app.run()
```

### Weather Dashboard

```python
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical, Grid
from textual.widgets import Static, Button
from dataclasses import dataclass
from typing import List

@dataclass
class WeatherData:
    city: str
    temperature: float
    condition: str
    humidity: int
    wind_speed: float

class WeatherDashboardApp(App):
    """Weather dashboard."""

    CSS = """
    Grid {
        grid-gutter: 1;
    }

    .weather-card {
        border: solid $primary;
        padding: 1;
        height: 10;
        text-align: center;
    }

    .city-name {
        text-style: bold;
        font-size: 1.5;
        margin-bottom: 1;
    }

    .temperature {
        font-size: 3;
        margin: 1;
    }

    .condition {
        text-style: italic;
        margin: 1;
    }

    .details {
        margin-top: 1;
        font-size: 0.9;
    }
    """

    def __init__(self):
        super().__init__()
        self.weather_data = [
            WeatherData("New York", 22.5, "Partly Cloudy", 65, 15.3),
            WeatherData("London", 18.0, "Rainy", 80, 20.5),
            WeatherData("Tokyo", 28.3, "Sunny", 45, 8.7),
            WeatherData("Paris", 20.1, "Cloudy", 70, 12.2),
            WeatherData("Sydney", 24.7, "Partly Cloudy", 55, 18.9),
            WeatherData("Berlin", 19.2, "Overcast", 75, 14.5),
        ]

    def compose(self) -> ComposeResult:
        yield Static("Weather Dashboard", classes="title")
        yield Static(f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", id="timestamp")

        # Location selector
        with Horizontal():
            yield Button("Add Location", id="add")
            yield Button("Refresh", id="refresh")
            yield Button("°C/°F", id="toggle-temp")

        # Weather cards in grid
        with Grid():
            for weather in self.weather_data:
                yield self.create_weather_card(weather)

    def create_weather_card(self, weather: WeatherData) -> Vertical:
        """Create weather card widget."""
        icon = self.get_weather_icon(weather.condition)

        card = Vertical(classes="weather-card", id=f"card-{weather.city}")
        card.mount(Static(weather.city, classes="city-name"))
        card.mount(Static(icon, classes="icon"))
        card.mount(Static(f"{weather.temperature:.1f}°C", classes="temperature"))
        card.mount(Static(weather.condition, classes="condition"))
        card.mount(Static(f"Humidity: {weather.humidity}%", classes="details"))
        card.mount(Static(f"Wind: {weather.wind_speed} km/h", classes="details"))

        return card

    def get_weather_icon(self, condition: str) -> str:
        """Get icon for weather condition."""
        icons = {
            "Sunny": "☀️",
            "Partly Cloudy": "⛅",
            "Cloudy": "☁️",
            "Overcast": "☁️",
            "Rainy": "🌧️",
            "Stormy": "⛈️",
            "Snowy": "❄️",
            "Foggy": "🌫️",
        }
        return icons.get(condition, "🌤️")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        if event.button.id == "add":
            self.add_location()
        elif event.button.id == "refresh":
            self.refresh_weather()
        elif event.button.id == "toggle-temp":
            self.toggle_temperature()

    def add_location(self):
        """Add new location."""
        # In a real app, prompt for location
        new_weather = WeatherData("Moscow", 15.5, "Cloudy", 60, 10.0)
        self.weather_data.append(new_weather)
        self.app.reload()

    def refresh_weather(self):
        """Refresh weather data."""
        # In a real app, fetch fresh data
        self.bell()
        timestamp = self.query_one("#timestamp", Static)
        timestamp.update(f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    def toggle_temperature(self):
        """Toggle between Celsius and Fahrenheit."""
        button = self.query_one("#toggle-temp", Button)

        if "°C" in button.label:
            # Convert to Fahrenheit
            for weather in self.weather_data:
                weather.temperature = (weather.temperature * 9/5) + 32
            button.label = "°F/°C"
        else:
            # Convert to Celsius
            for weather in self.weather_data:
                weather.temperature = (weather.temperature - 32) * 5/9
            button.label = "°C/°F"

        self.app.reload()

if __name__ == "__main__":
    app = WeatherDashboardApp()
    app.run()
```

## Utility Patterns

### Command Palette

```python
from textual.app import App, ComposeResult
from textual.containers import Vertical, Horizontal
from textual.widgets import Input, Static, Button
from textual.widgets import ListView, ListItem

class CommandPalette(App):
    """Command palette widget."""

    CSS = """
    Vertical {
        width: 80;
        height: 20;
        border: solid $accent;
        padding: 1;
    }

    Input {
        margin-bottom: 1;
    }

    ListView {
        border: solid $panel;
    }

    ListItem {
        padding: 0 1;
    }

    ListItem:hover {
        background: $primary 20%;
    }

    ListItem.selected {
        background: $primary 40%;
    }
    """

    BINDINGS = [
        ("escape", "cancel", "Cancel"),
        ("enter", "select", "Select"),
    ]

    def __init__(self, commands: List[dict]):
        super().__init__()
        self.commands = commands
        self.selected_index = 0

    def compose(self) -> ComposeResult:
        yield Static("Command Palette", classes="title")
        self.search_input = Input(placeholder="Type a command...")
        yield self.search_input

        self.list_view = ListView(id="command-list")
        yield self.list_view

        # Initial commands
        self.filter_commands("")

    def on_input_changed(self, event: Input.Changed) -> None:
        """Filter commands based on search."""
        if event.input == self.search_input:
            self.filter_commands(event.input.value)

    def filter_commands(self, query: str):
        """Filter and display commands."""
        query = query.lower()

        # Clear existing items
        self.list_view.clear()

        # Filter commands
        filtered = [
            cmd for cmd in self.commands
            if query in cmd["name"].lower() or query in cmd["description"].lower()
        ]

        # Add to list
        for cmd in filtered:
            item = ListItem(
                Static(f"{cmd['name']} - {cmd['description']}", id=f"item-{cmd['id']}")
            )
            self.list_view.mount(item)

        self.selected_index = 0
        self.update_selection()

    def update_selection(self):
        """Update selection highlight."""
        items = self.list_view.children

        # Remove previous selection
        for item in items:
            item.remove_class("selected")

        # Add selection to current item
        if items and 0 <= self.selected_index < len(items):
            items[self.selected_index].add_class("selected")

    def on_key(self, event) -> None:
        """Handle key presses."""
        if event.key == "down":
            self.selected_index = min(self.selected_index + 1, len(self.list_view.children) - 1)
            self.update_selection()
        elif event.key == "up":
            self.selected_index = max(self.selected_index - 1, 0)
            self.update_selection()
        elif event.key == "enter":
            self.select_command()
        elif event.key == "escape":
            self.action_cancel()

    def select_command(self):
        """Select current command."""
        items = self.list_view.children
        if items and 0 <= self.selected_index < len(items):
            # Get command ID from selected item
            item = items[self.selected_index]
            item_id = item.query_one("Static").id.replace("item-", "")

            # Find command
            command = next((cmd for cmd in self.commands if cmd["id"] == item_id), None)

            if command:
                # Execute command
                command["action"]()
                self.app.pop_screen()

class MainApp(App):
    """Main app with command palette."""

    CSS = """
    Vertical {
        padding: 1;
    }
    """

    def __init__(self):
        super().__init__()
        self.commands = [
            {
                "id": "new-file",
                "name": "New File",
                "description": "Create a new file",
                "action": self.new_file,
            },
            {
                "id": "open-file",
                "name": "Open File",
                "description": "Open an existing file",
                "action": self.open_file,
            },
            {
                "id": "save",
                "name": "Save",
                "description": "Save current file",
                "action": self.save_file,
            },
            {
                "id": "settings",
                "name": "Settings",
                "description": "Open settings",
                "action": self.open_settings,
            },
        ]

    def compose(self) -> ComposeResult:
        yield Static("Text Editor", classes="title")
        yield Static("Press Ctrl+P to open command palette")

        with Horizontal():
            yield Button("New File", id="new")
            yield Button("Open Command Palette", id="palette")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        if event.button.id == "new":
            self.new_file()
        elif event.button.id == "palette":
            self.open_command_palette()

    def action_palette(self):
        """Open command palette."""
        self.push_screen(CommandPalette(self.commands))

    def new_file(self):
        """Create new file."""
        self.bell()

    def open_file(self):
        """Open file."""
        self.bell()

    def save_file(self):
        """Save file."""
        self.bell()

    def open_settings(self):
        """Open settings."""
        self.bell()

    def open_command_palette(self):
        """Show command palette."""
        self.action_palette()

    BINDINGS = [
        ("ctrl+p", "palette", "Command Palette"),
    ]

if __name__ == "__main__":
    app = MainApp()
    app.run()
```

## Pattern Usage Guide

### Choosing the Right Pattern

1. **Simple Apps**: Use basic patterns (Counter, Todo)
2. **Data-heavy Apps**: Use table patterns (User Management)
3. **Monitoring Apps**: Use dashboard patterns (System Monitor)
4. **Configuration**: Use settings patterns
5. **Multi-step Workflows**: Use wizard patterns

### Common Pattern Elements

```python
# Reactive state management
self.state = reactive(initial_value)

# Event handling
def on_button_pressed(self, event: Button.Pressed) -> None:
    # Handle event

# Data updates
def update_display(self):
    widget = self.query_one("#widget-id", Widget)
    widget.update(new_value)

# Async operations
async def load_data(self):
    data = await self.fetch_data()
    self.update_ui(data)
```

### Pattern Customization Tips

1. **CSS Styling**: Customize the CSS section for your theme
2. **Data Models**: Replace dataclasses with your data models
3. **Event Handlers**: Add your specific event handling logic
4. **Async Operations**: Integrate with your async APIs
5. **Error Handling**: Add proper error handling for production

### Integration Patterns

```python
# Integrate with database
class DatabaseApp(App):
    def __init__(self):
        super().__init__()
        self.db = DatabaseConnection()

# Integrate with API
class ApiApp(App):
    def __init__(self):
        super().__init__()
        self.api = ApiClient()

# Integrate with file system
class FileApp(App):
    def __init__(self):
        super().__init__()
        self.file_handler = FileHandler()
```

## See Also

- [Textual Widgets Reference](textual-widgets-reference.md)
- [Textual Layouts Guide](textual-layouts-guide.md)
- [Textual CSS Styling](textual-css-styling.md)
- [Textual Events Handling](textual-events-handling.md)
- [Textual Data Binding](textual-data-binding.md)
