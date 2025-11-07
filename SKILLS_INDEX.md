# Textual Skills Index

Complete catalog of all available skills organized by category and difficulty.

## 📊 Skills Overview

| Category | Skills | Difficulty | Priority |
|----------|--------|------------|----------|
| Core | 2 | Beginner | Essential |
| Widgets | 2 | Beginner-Intermediate | Essential |
| Layout | 2 | Beginner-Intermediate | Essential |
| Interactivity | 1 | Intermediate | Essential |
| Reactivity | 1 | Intermediate | Recommended |
| Navigation | 1 | Intermediate | Recommended |
| Testing | 1 | Intermediate | Recommended |
| DOM | 0 | Intermediate | Optional |
| Input | 0 | Intermediate | Optional |
| Advanced | 0 | Advanced | Optional |
| Development | 0 | All levels | Optional |

## 🎯 Core Skills (Essential)

### 01. Getting Started with Textual
**File:** `skills/core/01_getting_started.py`
**Difficulty:** Beginner
**Covers:**
- Basic app structure
- Project setup
- Hot reload development
- Async patterns
- Quick start guide

**Key Examples:**
- BasicTextualApp
- DevelopmentApp
- AsyncApp

**When to Use:**
- Starting any new Textual project
- Learning Textual basics
- Setting up development environment

---

### 02. App Lifecycle & Structure
**File:** `skills/core/02_app_lifecycle.py`
**Difficulty:** Beginner
**Covers:**
- Lifecycle events (init, load, mount, unmount)
- App configuration
- Command-line arguments
- Graceful shutdown

**Key Examples:**
- LifecycleApp
- ConfigurableApp
- GracefulShutdownApp
- CLIApp

**When to Use:**
- Need initialization logic
- Require configuration
- Need cleanup on exit
- Building CLI tools

---

## 🎨 Widget Skills

### 03. Built-in Widget Usage
**File:** `skills/widgets/01_builtin_widgets.py`
**Difficulty:** Beginner
**Covers:**
- Button (all variants)
- Input (text, password, validation)
- DataTable, Tree, ListView
- Checkbox, RadioButton, Switch, Select
- ProgressBar, LoadingIndicator
- Tabs, TabbedContent
- Markdown, RichLog

**Key Examples:**
- ButtonDemo
- InputDemo
- SelectionDemo
- DataTableDemo
- TabsDemo

**When to Use:**
- Building any UI
- Need standard controls
- Forms and data entry
- Data display

---

### 04. Custom Widget Development
**File:** `skills/widgets/02_custom_widgets.py`
**Difficulty:** Intermediate
**Covers:**
- Widget class basics
- DEFAULT_CSS
- Compose method
- Custom messages
- Reactive widgets
- Container widgets

**Key Examples:**
- Counter (basic reactive widget)
- UserCard (with messages)
- SearchBox (composable)
- StatusIndicator (reactive state)
- Card (container)
- Badge (render method)

**When to Use:**
- Need reusable components
- Encapsulate functionality
- Share widgets across apps
- Build widget libraries

---

## 📐 Layout & Design Skills

### 05. Layout Systems
**File:** `skills/layout/01_layouts.py`
**Difficulty:** Beginner-Intermediate
**Covers:**
- Vertical layout (default)
- Horizontal layout
- Grid layout
- Dock layout (sticky)
- Scrollable containers
- Nested layouts
- Flexible sizing (fr units)

**Key Examples:**
- VerticalLayoutDemo
- HorizontalLayoutDemo
- GridLayoutDemo
- DockLayoutDemo
- ScrollDemo
- NestedLayoutDemo
- FlexibleLayoutDemo

**When to Use:**
- Positioning widgets
- Creating dashboards
- Sticky headers/footers
- Responsive designs
- Complex UIs

---

### 06. CSS Styling (TCSS)
**File:** `skills/layout/02_css_styling.py`
**Difficulty:** Intermediate
**Covers:**
- Selectors (type, ID, class, pseudo)
- Color system
- Borders and spacing
- Text styling
- Layout with CSS
- External stylesheets
- Responsive design

**Key Examples:**
- BasicCSSDemo
- SelectorsDemo
- ColorsDemo
- BordersSpacingDemo
- TextStylingDemo
- ResponsiveDemo

**When to Use:**
- Styling your app
- Creating themes
- Responsive layouts
- Professional appearance

---

## ⚡ Interactivity Skills

### 07. Events and Messages
**File:** `skills/interactivity/01_events_messages.py`
**Difficulty:** Intermediate
**Covers:**
- Event handlers (on_* methods)
- @on decorator
- Custom messages
- Message bubbling
- Keyboard events
- Mouse events
- Focus events

**Key Examples:**
- BasicEventsApp
- OnDecoratorApp
- CustomMessageApp
- BubblingApp
- KeyEventsApp
- MouseEventsApp
- FocusEventsApp

**When to Use:**
- User interaction
- Button clicks
- Keyboard input
- Custom widget communication
- Event propagation

---

## 🔄 Reactivity Skills

### 08. Reactive Attributes
**File:** `skills/reactivity/01_reactive_attributes.py`
**Difficulty:** Intermediate
**Covers:**
- Basic reactive attributes
- Watch methods
- Compute methods
- Reactive validation
- App-level reactivity
- Init parameter

**Key Examples:**
- Counter (basic)
- StatusWidget (multiple reactives)
- Calculator (computed values)
- ValidatedInput (validation)
- ReactiveApp (app-level)

**When to Use:**
- Dynamic UI updates
- State management
- Computed values
- Input validation
- Auto-updating displays

---

## 🗺️ Navigation Skills

### 09. Screens and Navigation
**File:** `skills/navigation/01_screens.py`
**Difficulty:** Intermediate
**Covers:**
- Screen definition
- Navigation (push/pop/switch)
- Modal screens
- Returning values
- Screen callbacks
- Async screen handling
- Screen stack management

**Key Examples:**
- HomeScreen, SettingsScreen, AboutScreen
- ConfirmModal, InputModal
- DataEntryScreen
- StackScreen

**When to Use:**
- Multi-screen apps
- Wizards and flows
- Dialogs and modals
- Settings screens
- Complex navigation

---

## 🧪 Testing Skills

### 10. Snapshot Testing
**File:** `skills/testing/01_snapshot_testing.py`
**Difficulty:** Intermediate
**Covers:**
- pytest-textual-snapshot
- Basic snapshot tests
- User interaction testing
- Keyboard/mouse simulation
- Form testing
- DataTable testing
- Theme testing

**Key Examples:**
- test_simple_app
- test_interactive_app
- test_keyboard_app
- test_form_app
- test_table_app

**When to Use:**
- Visual regression testing
- UI verification
- Test-driven development
- CI/CD integration
- Catching visual bugs

---

## 📚 Helper Scripts

### textual_generator.py
**Purpose:** Generate Textual code

**Capabilities:**
- Generate complete apps
- Create custom widgets
- Generate screens and modals
- Create test files

**Usage:**
```python
from helpers.textual_generator import TextualGenerator

generator = TextualGenerator()
code = generator.generate_app("MyApp", widgets, css)
```

---

### template_manager.py
**Purpose:** Access code templates

**Templates:**
- Apps (4 variants)
- Widgets (4 variants)
- Screens (2 variants)
- Modals (2 variants)
- Tests (2 variants)
- CSS (3 variants)
- Event handlers (3 variants)
- Reactive attributes (3 variants)

**Usage:**
```python
from helpers.template_manager import TemplateManager, TemplateType

manager = TemplateManager()
code = manager.get_template(TemplateType.APP, "basic", app_name="MyApp")
```

---

### skill_finder.py
**Purpose:** Find relevant skills

**Features:**
- Search by keyword
- Task-based recommendations
- Learning paths
- Skill categorization

**Usage:**
```python
from helpers.skill_finder import SkillFinder

finder = SkillFinder()
skills = finder.find_skills("button")
recommendations = finder.find_by_task("Create a form")
path = finder.get_learning_path("beginner")
```

---

### quick_reference.py
**Purpose:** Quick syntax lookup

**Contains:**
- Widget signatures
- Common patterns
- CSS snippets
- Event handlers
- Best practices

**Usage:**
```python
from helpers.quick_reference import QUICK_REFERENCE, get_pattern

print(QUICK_REFERENCE)
pattern = get_pattern("counter")
```

---

## 🎓 Learning Paths

### Path 1: Beginner (Build Your First TUI)
1. Getting Started (core/01)
2. Built-in Widgets (widgets/01)
3. Layout Systems (layout/01)
4. Events and Messages (interactivity/01)
5. CSS Styling (layout/02)

**Goal:** Create simple, functional TUI apps
**Time:** 2-4 hours

---

### Path 2: Intermediate (Interactive Apps)
1. Custom Widgets (widgets/02)
2. Reactive Attributes (reactivity/01)
3. Screens and Navigation (navigation/01)
4. Snapshot Testing (testing/01)

**Goal:** Build multi-screen, reactive applications
**Time:** 4-6 hours

---

### Path 3: Advanced (Professional TUIs)
1. App Lifecycle (core/02)
2. Advanced Testing
3. Performance Optimization
4. Complex State Management
5. Accessibility

**Goal:** Production-ready applications
**Time:** 6-10 hours

---

## 🔍 Quick Skill Finder

### I Want To...

**Create a button that does something**
→ widgets/01_builtin_widgets.py → ButtonDemo

**Build a form with inputs**
→ widgets/01_builtin_widgets.py → InputDemo
→ interactivity/01_events_messages.py → FormApp

**Display data in a table**
→ widgets/01_builtin_widgets.py → DataTableDemo

**Make a counter**
→ reactivity/01_reactive_attributes.py → Counter

**Create a multi-screen app**
→ navigation/01_screens.py → BasicScreenApp

**Show a confirmation dialog**
→ navigation/01_screens.py → ConfirmModal

**Style my app**
→ layout/02_css_styling.py → All examples

**Arrange widgets in a grid**
→ layout/01_layouts.py → GridLayoutDemo

**Handle button clicks**
→ interactivity/01_events_messages.py → BasicEventsApp

**Auto-update UI when data changes**
→ reactivity/01_reactive_attributes.py → All examples

**Test my app**
→ testing/01_snapshot_testing.py → All tests

**Create a reusable widget**
→ widgets/02_custom_widgets.py → All examples

---

## 📊 Skill Matrix

| Feature | Skill File | Example | Difficulty |
|---------|-----------|---------|------------|
| Basic App | core/01 | BasicTextualApp | ⭐ |
| Lifecycle | core/02 | LifecycleApp | ⭐⭐ |
| Buttons | widgets/01 | ButtonDemo | ⭐ |
| Inputs | widgets/01 | InputDemo | ⭐ |
| Tables | widgets/01 | DataTableDemo | ⭐⭐ |
| Custom Widget | widgets/02 | Counter | ⭐⭐⭐ |
| Layouts | layout/01 | GridLayoutDemo | ⭐⭐ |
| CSS | layout/02 | ColorsDemo | ⭐⭐ |
| Events | interactivity/01 | OnDecoratorApp | ⭐⭐ |
| Reactive | reactivity/01 | ReactiveApp | ⭐⭐⭐ |
| Screens | navigation/01 | BasicScreenApp | ⭐⭐⭐ |
| Modals | navigation/01 | ModalApp | ⭐⭐⭐ |
| Testing | testing/01 | All tests | ⭐⭐ |

**Legend:**
- ⭐ Beginner
- ⭐⭐ Intermediate
- ⭐⭐⭐ Advanced

---

## 🎯 Common Use Cases

### Use Case: Dashboard App
**Skills Needed:**
1. layout/01 (Grid layout)
2. widgets/01 (DataTable, ProgressBar)
3. reactivity/01 (Auto-updates)
4. layout/02 (Styling)

### Use Case: Form Application
**Skills Needed:**
1. widgets/01 (Input, Button, Checkbox)
2. interactivity/01 (Events)
3. reactivity/01 (Validation)
4. navigation/01 (Confirmation modals)

### Use Case: File Manager
**Skills Needed:**
1. widgets/01 (Tree, ListView)
2. navigation/01 (Screens)
3. interactivity/01 (Keyboard events)
4. layout/01 (Dock layout)

### Use Case: Chat Application
**Skills Needed:**
1. widgets/01 (RichLog, Input)
2. reactivity/01 (Message updates)
3. layout/01 (Dock layout)
4. interactivity/01 (Input events)

### Use Case: Settings Panel
**Skills Needed:**
1. widgets/01 (Checkbox, Select, Input)
2. navigation/01 (Settings screen)
3. core/02 (Configuration)
4. layout/02 (Styling)

---

## 📖 Next Steps

1. **Browse Skills** - Explore the skills/ directory
2. **Run Examples** - Execute skill files directly
3. **Use Helpers** - Leverage generator and templates
4. **Read Guides** - Check guide sections in skills
5. **Build Projects** - Apply skills to real apps
6. **Test Everything** - Use snapshot testing

---

**Pro Tip:** Start with the quick reference (helpers/quick_reference.py) for instant syntax lookups!
