# textual-data-binding

Textual reactive data binding, MVVM patterns, state management, and data flow architectures for modern TUI applications.

## Overview

Textual provides powerful reactive programming features that enable clean separation between data models and UI views. Understanding data binding patterns is essential for building maintainable, scalable TUI applications.

## Reactive Properties

### Basic Reactive Properties

```python
from textual.reactive import reactive
from textual.app import App

class MyModel(App):
    """Model with reactive properties."""

    # Define reactive properties
    count = reactive(0)
    name = reactive("")
    is_active = reactive(False)

    def __init__(self):
        super().__init__()
        # Watchers are called when properties change
        self.count = 0

    def watch_count(self, value: int) -> None:
        """Called when count changes."""
        self.log(f"Count changed to: {value}")

    def watch_name(self, value: str) -> None:
        """Called when name changes."""
        self.log(f"Name changed to: {value}")

    def watch_is_active(self, value: bool) -> None:
        """Called when is_active changes."""
        status = "active" if value else "inactive"
        self.log(f"Status: {status}")
```

### Reactive Property Types

```python
from textual.reactive import reactive

# Integer
count = reactive(0)

# String
name = reactive("")

# Boolean
is_enabled = reactive(False)

# Float
progress = reactive(0.0)

# List (shallow reactivity)
items = reactive([], always_update=True)

# Dict (shallow reactivity)
config = reactive({}, always_update=True)

# Custom type with watcher
class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

current_user = reactive(None)

def watch_current_user(self, user: User) -> None:
    if user:
        self.log(f"User changed to: {user.name}")
```

### Reactive Options

```python
# Basic reactive (only updates when value changes)
count = reactive(0)

# Always update (even if value is same)
count = reactive(0, always_update=True)

# Use setter/getter
def _get_count(self):
    return self._count

def _set_count(self, value):
    self._count = max(0, value)  # Clamp to 0+

count = reactive(0, setter=_set_count, getter=_get_count)
```

## MVVM Pattern

### Model

```python
from dataclasses import dataclass
from typing import List, Optional
from textual.reactive import reactive

@dataclass
class TodoItem:
    """Data model for todo item."""
    id: str
    title: str
    completed: bool = False
    created_at: str = ""

class TodoModel:
    """Todo model with reactive properties."""

    # Reactive collections
    items = reactive([], always_update=True)
    filter = reactive("all")  # all, active, completed
    is_loading = reactive(False)

    # Computed reactive property
    @reactive(auto=True)
    def filtered_items(self) -> List[TodoItem]:
        """Filter items based on current filter."""
        if self.filter == "active":
            return [item for item in self.items if not item.completed]
        elif self.filter == "completed":
            return [item for item in self.items if item.completed]
        else:
            return self.items

    @reactive(auto=True)
    def stats(self) -> dict:
        """Calculate stats."""
        total = len(self.items)
        completed = sum(1 for item in self.items if item.completed)
        active = total - completed
        return {
            "total": total,
            "active": active,
            "completed": completed,
            "completion_rate": completed / total if total > 0 else 0,
        }

    def add_item(self, title: str):
        """Add new todo item."""
        import uuid
        import datetime

        item = TodoItem(
            id=str(uuid.uuid4()),
            title=title,
            created_at=datetime.datetime.now().isoformat(),
        )
        new_items = self.items.copy()
        new_items.append(item)
        self.items = new_items

    def toggle_item(self, item_id: str):
        """Toggle item completion status."""
        new_items = []
        for item in self.items:
            if item.id == item_id:
                new_item = TodoItem(
                    id=item.id,
                    title=item.title,
                    completed=not item.completed,
                    created_at=item.created_at,
                )
                new_items.append(new_item)
            else:
                new_items.append(item)
        self.items = new_items

    def delete_item(self, item_id: str):
        """Delete todo item."""
        self.items = [item for item in self.items if item.id != item_id]

    def clear_completed(self):
        """Clear all completed items."""
        self.items = [item for item in self.items if not item.completed]
```

### ViewModel

```python
class TodoViewModel:
    """ViewModel for Todo app."""

    def __init__(self):
        self.model = TodoModel()
        # Watch model changes
        self.model.filtered_items.subscribe(self.on_items_changed)
        self.model.stats.subscribe(self.on_stats_changed)

    def on_items_changed(self, items: List[TodoItem]) -> None:
        """React to filtered items change."""
        pass  # View will update automatically

    def on_stats_changed(self, stats: dict) -> None:
        """React to stats change."""
        pass  # View will update automatically

    # Commands
    def add_todo(self, title: str):
        """Add new todo."""
        if title.strip():
            self.model.add_item(title.strip())

    def toggle_todo(self, item_id: str):
        """Toggle todo completion."""
        self.model.toggle_item(item_id)

    def delete_todo(self, item_id: str):
        """Delete todo."""
        self.model.delete_item(item_id)

    def set_filter(self, filter_value: str):
        """Set filter (all, active, completed)."""
        if filter_value in ["all", "active", "completed"]:
            self.model.filter = filter_value

    def clear_completed(self):
        """Clear all completed todos."""
        self.model.clear_completed()

    # Properties for view
    @property
    def items(self) -> List[TodoItem]:
        return self.model.filtered_items

    @property
    def stats(self) -> dict:
        return self.model.stats

    @property
    def filter(self) -> str:
        return self.model.filter
```

### View

```python
from textual.app import App
from textual.containers import Vertical, Horizontal
from textual.widgets import Button, Input, Label, Static, Checkbox

class TodoItemWidget(Vertical):
    """Widget for individual todo item."""

    def __init__(self, item_id: str, title: str, completed: bool):
        super().__init__()
        self.item_id = item_id
        self._title = title
        self._completed = completed

    def compose(self):
        with Horizontal():
            # Checkbox for completion
            self.checkbox = Checkbox(self._title, value=self._completed)
            yield self.checkbox
            yield Button("Delete", id="delete", variant="error")

    def on_checkbox_changed(self, event: Checkbox.Changed) -> None:
        """Handle checkbox toggle."""
        if event.checkbox.value:
            self.app.viewmodel.toggle_todo(self.item_id)
        else:
            self.app.viewmodel.toggle_todo(self.item_id)

    def on_button_pressed_delete(self, event: Button.Pressed) -> None:
        """Handle delete button."""
        self.app.viewmodel.delete_todo(self.item_id)
        # Remove this widget
        self.remove()

class TodoApp(App):
    """Todo app following MVVM pattern."""

    def __init__(self):
        super().__init__()
        self.viewmodel = TodoViewModel()

    CSS = """
    #stats {
        height: 3;
        background: $panel;
        padding: 1;
    }

    #controls {
        height: 3;
        background: $surface;
        padding: 1;
    }

    #todo-list {
        background: $background;
    }

    TodoItemWidget {
        padding: 0 1;
        border-bottom: solid $surface;
    }
    """

    def compose(self):
        # Header
        yield Label("Todo App", classes="title")
        yield Static("", id="stats")

        # Controls
        with Horizontal(id="controls"):
            self.input = Input(placeholder="Add new todo...")
            yield self.input
            yield Button("Add", id="add", variant="primary")
            yield Button("All", id="filter-all")
            yield Button("Active", id="filter-active")
            yield Button("Completed", id="filter-completed")
            yield Button("Clear Completed", id="clear-completed")

        # Todo list
        with Vertical(id="todo-list"):
            pass  # Items will be added here

    def on_mount(self) -> None:
        """Initialize view."""
        self.render_items()
        self.update_stats()

        # Watch for changes
        self.viewmodel.model.filtered_items.subscribe(self.on_items_changed)
        self.viewmodel.model.stats.subscribe(self.on_stats_changed)

    def on_items_changed(self, items: List[TodoItem]) -> None:
        """React to items change."""
        self.render_items()

    def on_stats_changed(self, stats: dict) -> None:
        """React to stats change."""
        self.update_stats()

    def render_items(self) -> None:
        """Render todo items."""
        list_container = self.query_one("#todo-list", Vertical)

        # Clear existing items
        for widget in list_container.children.copy():
            widget.remove()

        # Render items
        for item in self.viewmodel.items:
            widget = TodoItemWidget(item.id, item.title, item.completed)
            list_container.mount(widget)

    def update_stats(self) -> None:
        """Update stats display."""
        stats = self.viewmodel.stats
        stats_widget = self.query_one("#stats", Static)
        stats_widget.update(
            f"Total: {stats['total']} | "
            f"Active: {stats['active']} | "
            f"Completed: {stats['completed']} | "
            f"Completion Rate: {stats['completion_rate']:.0%}"
        )

    def on_input_submitted(self, event: Input.Submitted) -> None:
        """Handle input submission."""
        if event.input.value.strip():
            self.viewmodel.add_todo(event.input.value)
            self.input.value = ""

    def on_button_pressed_add(self, event: Button.Pressed) -> None:
        """Handle add button."""
        if self.input.value.strip():
            self.viewmodel.add_todo(self.input.value)
            self.input.value = ""

    def on_button_pressed_filter_all(self, event: Button.Pressed) -> None:
        """Filter all items."""
        self.viewmodel.set_filter("all")

    def on_button_pressed_filter_active(self, event: Button.Pressed) -> None:
        """Filter active items."""
        self.viewmodel.set_filter("active")

    def on_button_pressed_filter_completed(self, event: Button.Pressed) -> None:
        """Filter completed items."""
        self.viewmodel.set_filter("completed")

    def on_button_pressed_clear_completed(self, event: Button.Pressed) -> None:
        """Clear completed items."""
        self.viewmodel.clear_completed()
```

## State Management Patterns

### Simple State Pattern

```python
class AppState:
    """Simple global state."""

    def __init__(self):
        self.state = {
            "user": None,
            "is_authenticated": False,
            "current_view": "dashboard",
            "data": [],
            "loading": False,
            "error": None,
        }
        self.listeners = []

    def set_state(self, key: str, value):
        """Update state and notify listeners."""
        if key in self.state and self.state[key] != value:
            self.state[key] = value
            self.notify_listeners()

    def get_state(self, key: str):
        """Get state value."""
        return self.state[key]

    def subscribe(self, callback):
        """Subscribe to state changes."""
        self.listeners.append(callback)

    def notify_listeners(self):
        """Notify all listeners of state changes."""
        for callback in self.listeners:
            callback(self.state)

class MyApp(App):
    """App using simple state pattern."""

    def __init__(self):
        super().__init__()
        self.state = AppState()
        # Subscribe to state changes
        self.state.subscribe(self.on_state_change)

    def on_state_change(self, new_state):
        """React to global state changes."""
        if new_state["loading"]:
            self.show_loading()
        elif new_state["error"]:
            self.show_error(new_state["error"])
        else:
            self.hide_loading()

    def authenticate(self, username: str, password: str):
        """Authenticate user."""
        self.state.set_state("loading", True)

        # Simulate async auth
        self.set_timer(1.0, lambda: self._auth_complete(True))

    def _auth_complete(self, success: bool):
        """Complete authentication."""
        if success:
            self.state.set_state("user", {"username": "user"})
            self.state.set_state("is_authenticated", True)
        else:
            self.state.set_state("error", "Authentication failed")
        self.state.set_state("loading", False)
```

### Redux-like Pattern

```python
from typing import Callable, Any, Dict
from dataclasses import asdict
from textual.reactive import reactive

class Action:
    """Action base class."""

    def __init__(self, type: str, payload: Dict[str, Any] = None):
        self.type = type
        self.payload = payload or {}

class UserAction(Action):
    """User-related actions."""
    pass

class DataAction(Action):
    """Data-related actions."""
    pass

class Store:
    """Redux-like store."""

    def __init__(self, reducer: Callable, initial_state: Dict[str, Any]):
        self.reducer = reducer
        self.state = initial_state
        self.listeners = []

    def dispatch(self, action: Action):
        """Dispatch action to reducer."""
        self.state = self.reducer(self.state, action)
        self.notify_listeners()

    def subscribe(self, listener: Callable):
        """Subscribe to state changes."""
        self.listeners.append(listener)

    def notify_listeners(self):
        """Notify all listeners."""
        for listener in self.listeners:
            listener(self.state)

    def get_state(self) -> Dict[str, Any]:
        """Get current state."""
        return self.state

# Reducer function
def todo_reducer(state: Dict[str, Any], action: Action) -> Dict[str, Any]:
    """Reducer for todo actions."""
    new_state = state.copy()

    if action.type == "ADD_TODO":
        new_state["todos"].append({
            "id": action.payload["id"],
            "title": action.payload["title"],
            "completed": False,
        })

    elif action.type == "TOGGLE_TODO":
        for todo in new_state["todos"]:
            if todo["id"] == action.payload["id"]:
                todo["completed"] = not todo["completed"]

    elif action.type == "DELETE_TODO":
        new_state["todos"] = [
            todo for todo in new_state["todos"]
            if todo["id"] != action.payload["id"]
        ]

    elif action.type == "SET_FILTER":
        new_state["filter"] = action.payload["filter"]

    return new_state

# Middleware
def logging_middleware(store):
    """Logging middleware."""
    def next_(action):
        print(f"Action: {action.type}")
        result = store.reducer(store.get_state(), action)
        print(f"State updated")
        return result
    return next_

class TodoApp(App):
    """Todo app using Redux pattern."""

    def __init__(self):
        super().__init__()
        initial_state = {
            "todos": [],
            "filter": "all",
        }
        self.store = Store(todo_reducer, initial_state)
        # Subscribe to store
        self.store.subscribe(self.on_state_change)

    def on_state_change(self, state):
        """React to state changes."""
        self.render_todos()
        self.update_filter_display()

    def add_todo(self, title: str):
        """Add todo via action."""
        action = Action("ADD_TODO", {
            "id": str(uuid.uuid4()),
            "title": title,
        })
        self.store.dispatch(action)

    def toggle_todo(self, item_id: str):
        """Toggle todo via action."""
        action = Action("TOGGLE_TODO", {"id": item_id})
        self.store.dispatch(action)

    def delete_todo(self, item_id: str):
        """Delete todo via action."""
        action = Action("DELETE_TODO", {"id": item_id})
        self.store.dispatch(action)

    def set_filter(self, filter_value: str):
        """Set filter via action."""
        action = Action("SET_FILTER", {"filter": filter_value})
        self.store.dispatch(action)
```

## Observable Collections

### Observable List

```python
from typing import List, Callable, Any

class ObservableList(List):
    """Observable list that notifies on changes."""

    def __init__(self, items=None):
        super().__init__(items or [])
        self._listeners: List[Callable] = []

    def subscribe(self, listener: Callable):
        """Subscribe to list changes."""
        self._listeners.append(listener)

    def notify(self, action: str, item: Any = None, index: int = -1):
        """Notify listeners of changes."""
        for listener in self._listeners:
            listener(action, item, index)

    def append(self, item) -> None:
        """Append item and notify."""
        super().append(item)
        self.notify("append", item, len(self) - 1)

    def remove(self, item) -> None:
        """Remove item and notify."""
        super().remove(item)
        self.notify("remove", item)

    def __setitem__(self, index, value) -> None:
        """Set item and notify."""
        old_value = self[index]
        super().__setitem__(index, value)
        self.notify("setitem", value, index)

    def __delitem__(self, index) -> None:
        """Delete item and notify."""
        item = self[index]
        super().__delitem__(index)
        self.notify("delitem", item, index)

class DataSource:
    """Observable data source."""

    def __init__(self):
        self.items = ObservableList()
        # Subscribe to changes
        self.items.subscribe(self.on_items_changed)

    def on_items_changed(self, action: str, item: Any, index: int):
        """React to data changes."""
        print(f"Data changed: {action} - {item} at {index}")

class ListView(Vertical):
    """Observable list view."""

    def __init__(self, data_source: DataSource):
        super().__init__()
        self.data_source = data_source

    def compose(self):
        """Create list items."""
        for item in self.data_source.items:
            yield Static(str(item))

    def on_mount(self) -> None:
        """Subscribe to data changes."""
        # Re-render when data changes
        self.data_source.items.subscribe(self.on_data_changed)

    def on_data_changed(self, action: str, item: Any, index: int):
        """React to data changes."""
        # Re-render the list
        self.render()

    def render(self) -> None:
        """Re-render the list."""
        # Clear existing items
        for widget in self.children.copy():
            widget.remove()

        # Re-mount items
        for item in self.data_source.items:
            self.mount(Static(str(item)))
```

## Computed Properties

### Auto-updating Computed Properties

```python
from textual.reactive import reactive

class DataModel:
    """Model with computed properties."""

    # Source properties
    price = reactive(0.0)
    quantity = reactive(1)
    tax_rate = reactive(0.1)

    # Computed properties (auto-update when dependencies change)
    @reactive(auto=True)
    def subtotal(self) -> float:
        """Calculate subtotal."""
        return self.price * self.quantity

    @reactive(auto=True)
    def tax_amount(self) -> float:
        """Calculate tax amount."""
        return self.subtotal * self.tax_rate

    @reactive(auto=True)
    def total(self) -> float:
        """Calculate total."""
        return self.subtotal + self.tax_amount

    @reactive(auto=True)
    def formatted_total(self) -> str:
        """Format total for display."""
        return f"${self.total:.2f}"

class Calculator(App):
    """Calculator with computed properties."""

    def compose(self):
        yield Input(value="0", id="price")
        yield Input(value="1", id="quantity")
        yield Input(value="0.1", id="tax-rate")
        yield Static("", id="total-display")

    def on_mount(self) -> None:
        self.model = DataModel()
        # Watch model for changes
        self.model.total.subscribe(self.update_display)
        self.update_display(self.model.total)

    def update_display(self, total: float):
        """Update display with computed total."""
        display = self.query_one("#total-display", Static)
        display.update(f"Total: ${total:.2f}")

    def on_input_changed(self, event: Input.Changed) -> None:
        """Update model when inputs change."""
        try:
            if event.input.id == "price":
                self.model.price = float(event.input.value)
            elif event.input.id == "quantity":
                self.model.quantity = int(event.input.value)
            elif event.input.id == "tax-rate":
                self.model.tax_rate = float(event.input.value)
        except ValueError:
            pass
```

## Data Flow Patterns

### Unidirectional Data Flow

```python
class UserManager:
    """User management service."""

    def __init__(self):
        self.users = []
        self.current_user = None

    def load_users(self, callback):
        """Load users asynchronously."""
        # Simulate async loading
        self.set_timer(1.0, lambda: self._load_complete([
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"},
            {"id": 3, "name": "Charlie"},
        ], callback))

    def _load_complete(self, users, callback):
        """Complete user loading."""
        self.users = users
        callback(self.users)

    def set_current_user(self, user_id: int):
        """Set current user."""
        for user in self.users:
            if user["id"] == user_id:
                self.current_user = user
                break

class UserListView(Vertical):
    """View for displaying user list."""

    def __init__(self, user_manager: UserManager):
        super().__init__()
        self.user_manager = user_manager

    def compose(self):
        """Render user list."""
        for user in self.user_manager.users:
            yield Button(user["name"], id=f"user-{user['id']}")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle user selection."""
        if event.button.id.startswith("user-"):
            user_id = int(event.button.id.split("-")[1])
            self.user_manager.set_current_user(user_id)

class UserDetailView(Vertical):
    """View for displaying user details."""

    def __init__(self, user_manager: UserManager):
        super().__init__()
        self.user_manager = user_manager
        self.detail_display = Static("No user selected")

    def compose(self):
        yield Static("User Details:")
        yield self.detail_display

    def on_mount(self) -> None:
        """Watch for current user changes."""
        self.user_manager.current_user = None  # Trigger watcher
        # Would need reactive property for real implementation

class UserApp(App):
    """App demonstrating unidirectional data flow."""

    def compose(self):
        self.user_manager = UserManager()
        yield UserListView(self.user_manager)
        yield UserDetailView(self.user_manager)

    def on_mount(self) -> None:
        """Load users on mount."""
        self.user_manager.load_users(self.on_users_loaded)

    def on_users_loaded(self, users):
        """Handle loaded users."""
        # Re-render user list
        list_view = self.query_one(UserListView)
        list_view.render()
```

## Data Validation

### Reactive Validation

```python
from typing import Any, Callable, List
from dataclasses import dataclass

@dataclass
class ValidationError:
    """Validation error."""
    field: str
    message: str

class ValidatedField:
    """Validated reactive field."""

    def __init__(self, initial_value: Any, validators: List[Callable] = None):
        self._value = initial_value
        self.validators = validators or []
        self.errors: List[ValidationError] = []
        self.listeners: List[Callable] = []

    @property
    def value(self) -> Any:
        return self._value

    @value.setter
    def value(self, new_value: Any):
        if self._value != new_value:
            self._value = new_value
            self.validate()
            self.notify_listeners()

    def validate(self):
        """Validate field."""
        self.errors = []
        for validator in self.validators:
            error = validator(self._value)
            if error:
                self.errors.append(error)

    def is_valid(self) -> bool:
        """Check if field is valid."""
        return len(self.errors) == 0

    def subscribe(self, listener: Callable):
        """Subscribe to changes."""
        self.listeners.append(listener)

    def notify_listeners(self):
        """Notify listeners of changes."""
        for listener in self.listeners:
            listener(self._value, self.errors)

# Validators
def required(value: Any) -> ValidationError:
    """Required field validator."""
    if not value or str(value).strip() == "":
        return ValidationError("field", "This field is required")
    return None

def min_length(min_len: int) -> Callable:
    """Minimum length validator."""
    def validator(value: Any) -> ValidationError:
        if value and len(str(value)) < min_len:
            return ValidationError("field", f"Minimum length is {min_len}")
        return None
    return validator

def email_format(value: Any) -> ValidationError:
    """Email format validator."""
    if value and "@" not in str(value):
        return ValidationError("field", "Invalid email format")
    return None

class FormModel:
    """Form model with validation."""

    def __init__(self):
        self.fields = {
            "username": ValidatedField("", [required, min_length(3)]),
            "email": ValidatedField("", [required, email_format]),
            "password": ValidatedField("", [required, min_length(8)]),
        }

        # Subscribe to field changes
        for field in self.fields.values():
            field.subscribe(self.on_field_changed)

    def on_field_changed(self, value, errors):
        """React to field changes."""
        print(f"Field changed: value={value}, errors={errors}")

    def is_valid(self) -> bool:
        """Check if entire form is valid."""
        return all(field.is_valid() for field in self.fields.values())

    def get_data(self) -> dict:
        """Get form data."""
        return {name: field.value for name, field in self.fields.items()}

class FormView(Vertical):
    """Form view with validation."""

    def __init__(self, form_model: FormModel):
        super().__init__()
        self.form_model = form_model

    def compose(self):
        """Render form fields."""
        for name, field in self.form_model.fields.items():
            yield Input(
                placeholder=name.title(),
                id=name,
            )
            yield Static("", id=f"{name}-error", classes="error")

    def on_input_changed(self, event: Input.Changed) -> None:
        """Handle input changes."""
        field = self.form_model.fields[event.input.id]
        field.value = event.input.value

        # Update error display
        error_widget = self.query_one(f"#{event.input.id}-error", Static)
        if field.errors:
            error_widget.update(field.errors[0].message)
        else:
            error_widget.update("")
```

## Best Practices

### 1. Separate Data and View Logic

```python
# Good: Clear separation
class UserModel:
    """Data model - no UI logic."""
    name = reactive("")
    email = reactive("")

class UserViewModel:
    """View model - UI logic only."""
    def __init__(self, model):
        self.model = model

    @property
    def display_name(self):
        return self.model.name or "Anonymous"

    def save(self):
        # Save logic here
        pass

class UserView:
    """View - UI rendering only."""
    def compose(self):
        yield Input(id="name")
        yield Button("Save")
```

### 2. Use Computed Properties for Derived Data

```python
# Good: Computed property
@reactive(auto=True)
def full_name(self) -> str:
    return f"{self.first_name} {self.last_name}"

# Avoid: Manual calculation
def get_full_name(self):
    return f"{self.first_name} {self.last_name}"
```

### 3. Keep Reactive Scope Small

```python
# Good: Reactive properties on small models
class Item:
    name = reactive("")
    completed = reactive(False)

# Avoid: Making entire app reactive
class App:
    # Don't do this
    all_data = reactive({})
```

### 4. Use Immutable Updates

```python
# Good: Create new list
def add_item(self, item):
    new_items = self.items.copy()
    new_items.append(item)
    self.items = new_items

# Avoid: Mutating list in place
def add_item(self, item):
    self.items.append(item)  # Won't trigger reactivity
```

### 5. Subscribe to Specific Changes

```python
# Good: Specific subscriptions
self.model.items.subscribe(self.on_items_changed)
self.model.selected_item.subscribe(self.on_selection_changed)

# Avoid: Global subscriptions
self.model.subscribe(self.on_any_change)
```

### 6. Test Data Binding

```python
async def test_data_binding():
    """Test reactive data binding."""
    model = TestModel()
    model.count = 0

    updates = []
    model.count.subscribe(lambda v: updates.append(v))

    model.count = 1
    model.count = 2

    assert updates == [1, 2]
```

## Integration Patterns

### API Integration

```python
class ApiService:
    """API service with reactive results."""

    def __init__(self):
        self.loading = reactive(False)
        self.data = reactive(None)
        self.error = reactive(None)

    async def fetch_data(self, url: str):
        """Fetch data from API."""
        self.loading = True
        self.error = None

        try:
            # Simulate API call
            await asyncio.sleep(1)
            result = {"data": "example"}
            self.data = result
        except Exception as e:
            self.error = str(e)
        finally:
            self.loading = False

class ApiView(App):
    """View for API integration."""

    def compose(self):
        self.api = ApiService()
        yield Button("Fetch Data", id="fetch")
        yield Static("", id="status")
        yield Static("", id="data")

    def on_mount(self) -> None:
        """Subscribe to API changes."""
        self.api.loading.subscribe(self.on_loading_changed)
        self.api.data.subscribe(self.on_data_changed)
        self.api.error.subscribe(self.on_error_changed)

    def on_button_pressed_fetch(self, event: Button.Pressed) -> None:
        """Trigger data fetch."""
        import asyncio
        asyncio.create_task(self.api.fetch_data("https://api.example.com"))

    def on_loading_changed(self, loading: bool):
        """Update loading state."""
        status = self.query_one("#status", Static)
        if loading:
            status.update("Loading...")
        else:
            status.update("")

    def on_data_changed(self, data):
        """Update data display."""
        if data:
            display = self.query_one("#data", Static)
            display.update(str(data))

    def on_error_changed(self, error):
        """Update error display."""
        if error:
            status = self.query_one("#status", Static)
            status.update(f"Error: {error}")
```

### Database Integration

```python
class DatabaseModel:
    """Reactive database model."""

    def __init__(self, db_connection):
        self.db = db_connection
        self.users = reactive([], always_update=True)
        self.load_users()

    def load_users(self):
        """Load users from database."""
        # Would load from real database
        users = [{"id": 1, "name": "Alice"}]
        self.users = users

    def create_user(self, name: str):
        """Create new user."""
        # Would insert into database
        new_user = {"id": 2, "name": name}
        new_users = self.users.copy()
        new_users.append(new_user)
        self.users = new_users

    def update_user(self, user_id: int, name: str):
        """Update user."""
        new_users = []
        for user in self.users:
            if user["id"] == user_id:
                new_users.append({"id": user_id, "name": name})
            else:
                new_users.append(user)
        self.users = new_users

    def delete_user(self, user_id: int):
        """Delete user."""
        self.users = [u for u in self.users if u["id"] != user_id]
```

## See Also

- [Textual Widgets Reference](textual-widgets-reference.md)
- [Textual Events Handling](textual-events-handling.md)
- [Textual Layouts Guide](textual-layouts-guide.md)
- [Textual CSS Styling](textual-css-styling.md)
