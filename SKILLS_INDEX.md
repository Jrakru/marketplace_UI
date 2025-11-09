# Skills Index - UI Development Marketplace

Complete catalog of all available skills organized by category and difficulty.

## 📊 Skills Overview

| Category | Skills | Difficulty | Priority |
|----------|--------|------------|----------|
| Core (Textual) | 2 | Beginner | Essential |
| Widgets (Textual) | 2 | Beginner-Intermediate | Essential |
| Layout (Textual) | 2 | Beginner-Intermediate | Essential |
| Interactivity (Textual) | 1 | Intermediate | Essential |
| Reactivity (Textual) | 1 | Intermediate | Recommended |
| Navigation (Textual) | 1 | Intermediate | Recommended |
| Testing (Textual) | 1 | Intermediate | Recommended |
| **Marimo (Notebooks)** | **3** | **Beginner-Intermediate** | **Recommended** |
| **Design (UI/UX)** | **2** | **All Levels** | **Essential** |
| DOM | 0 | Intermediate | Optional |
| Input | 0 | Intermediate | Optional |
| Advanced | 0 | Advanced | Optional |
| Development | 0 | All levels | Optional |

## 🎯 Textual Skills (TUI Framework)

### 01. Getting Started with Textual
**File:** `skills/textual/core/01_getting_started.py`
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
**File:** `skills/textual/core/02_app_lifecycle.py`
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
**File:** `skills/textual/widgets/01_builtin_widgets.py`
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
**File:** `skills/textual/widgets/02_custom_widgets.py`
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
**File:** `skills/textual/layout/01_layouts.py`
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
**File:** `skills/textual/layout/02_css_styling.py`
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
**File:** `skills/textual/interactivity/01_events_messages.py`
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
**File:** `skills/textual/reactivity/01_reactive_attributes.py`
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
**File:** `skills/textual/navigation/01_screens.py`
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
**File:** `skills/textual/testing/01_snapshot_testing.py`
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
1. Getting Started (textual/core/01)
2. Built-in Widgets (textual/widgets/01)
3. Layout Systems (textual/layout/01)
4. Events and Messages (textual/interactivity/01)
5. CSS Styling (textual/layout/02)

**Goal:** Create simple, functional TUI apps
**Time:** 2-4 hours

---

### Path 2: Intermediate (Interactive Apps)
1. Custom Widgets (textual/widgets/02)
2. Reactive Attributes (textual/reactivity/01)
3. Screens and Navigation (textual/navigation/01)
4. Snapshot Testing (textual/testing/01)

**Goal:** Build multi-screen, reactive applications
**Time:** 4-6 hours

---

### Path 3: Advanced (Professional TUIs)
1. App Lifecycle (textual/core/02)
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
→ textual/widgets/01_builtin_widgets.py → ButtonDemo

**Build a form with inputs**
→ textual/widgets/01_builtin_widgets.py → InputDemo
→ textual/interactivity/01_events_messages.py → FormApp

**Display data in a table**
→ textual/widgets/01_builtin_widgets.py → DataTableDemo

**Make a counter**
→ textual/reactivity/01_reactive_attributes.py → Counter

**Create a multi-screen app**
→ textual/navigation/01_screens.py → BasicScreenApp

**Show a confirmation dialog**
→ textual/navigation/01_screens.py → ConfirmModal

**Style my app**
→ textual/layout/02_css_styling.py → All examples

**Arrange widgets in a grid**
→ textual/layout/01_layouts.py → GridLayoutDemo

**Handle button clicks**
→ textual/interactivity/01_events_messages.py → BasicEventsApp

**Auto-update UI when data changes**
→ textual/reactivity/01_reactive_attributes.py → All examples

**Test my app**
→ textual/testing/01_snapshot_testing.py → All tests

**Create a reusable widget**
→ textual/widgets/02_custom_widgets.py → All examples

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

## 📓 Marimo Skills (Reactive Notebooks)

### 11. Getting Started with Marimo
**File:** `skills/marimo/01_getting_started.py`
**Difficulty:** Beginner
**Covers:**
- Installation and setup
- Basic notebook structure
- Reactive execution model
- Creating cells
- Import patterns
- Running notebooks

**Key Examples:**
- BasicMarimoNotebook
- ReactiveCounter
- InteractiveDataVisualization

**When to Use:**
- Building reactive Python notebooks
- Data exploration and analysis
- Creating interactive dashboards
- Reproducible research
- Educational content

---

### 12. Marimo Widgets and UI Components
**File:** `skills/marimo/02_widgets_ui.py`
**Difficulty:** Beginner-Intermediate
**Covers:**
- Input widgets (text, number, slider)
- Selection widgets (dropdown, checkbox, radio)
- Data widgets (table, dataframe)
- File upload widgets
- Code editor widget
- Composite widgets (form, array, dictionary)
- Button actions
- Widget reactivity

**Key Examples:**
- TextInputDemo
- DataTableExplorer
- FormSubmission
- InteractiveControls

**When to Use:**
- Creating interactive notebooks
- Building data exploration tools
- Form-based data entry
- Parameter tuning interfaces
- Dashboard controls

---

### 13. Marimo Layouts and UI Organization
**File:** `skills/marimo/03_layouts.py`
**Difficulty:** Intermediate
**Covers:**
- Horizontal stacks (mo.hstack)
- Vertical stacks (mo.vstack)
- Grid layouts
- Tabs (mo.ui.tabs)
- Accordions (mo.accordion)
- Sidebar (mo.sidebar)
- Navigation menus
- Callouts and alerts

**Key Examples:**
- DashboardLayout
- TabbedInterface
- GridLayout
- SidebarNavigation

**When to Use:**
- Organizing complex notebooks
- Creating dashboard-style layouts
- Building multi-section interfaces
- Navigation in large notebooks
- Highlighting important information

---

## 🎨 UI/UX Design Skills

### 14. CLI UX Design Principles
**File:** `skills/design/01_cli_ux_principles.py`
**Difficulty:** All Levels
**Covers:**
- Human-first design
- Progressive discovery
- Helpful error messages
- Arguments vs flags
- Consistency patterns
- Colors and formatting
- Output modes (human/machine)
- CLI accessibility
- Common CLI patterns

**Key Concepts:**
- Feedback and progress indicators
- Interactive prompts
- Documentation in tools
- Composability and pipes
- Testing CLI UX

**When to Use:**
- Building command-line tools
- Creating developer tools
- Designing TUI applications
- Improving CLI user experience
- Writing helpful error messages

---

### 15. General UI/UX Design Principles
**File:** `skills/design/02_general_ui_ux.py`
**Difficulty:** All Levels
**Covers:**
- Core UX principles (clarity, consistency, feedback)
- Color theory and harmonies
- Typography principles
- Layout and grid systems
- Accessibility (WCAG 2.1)
- Notebook interface design
- Visual hierarchy
- Responsive design
- Mobile-first approach

**Key Concepts:**
- POUR principles (Perceivable, Operable, Understandable, Robust)
- Contrast ratios and color accessibility
- F and Z reading patterns
- White space and visual balance
- Progressive disclosure

**When to Use:**
- Designing any user interface
- Creating accessible applications
- Building notebook interfaces
- Improving existing UX
- Ensuring WCAG compliance
- Color scheme selection

---

## 🎓 Updated Learning Paths

### Path 1: Textual TUI Development (Beginner)
1. Getting Started with Textual (textual/core/01)
2. Built-in Widgets (textual/widgets/01)
3. Layout Systems (textual/layout/01)
4. Events and Messages (textual/interactivity/01)
5. CSS Styling (textual/layout/02)

**Goal:** Create functional TUI applications
**Time:** 2-4 hours

---

### Path 2: Marimo Reactive Notebooks (Beginner)
1. Getting Started with Marimo (marimo/01)
2. Widgets and UI Components (marimo/02)
3. Layouts and Organization (marimo/03)
4. General UI/UX Principles (design/02)

**Goal:** Build interactive, reactive notebooks
**Time:** 3-5 hours

---

### Path 3: UI/UX Excellence (All Levels)
1. CLI UX Design Principles (design/01)
2. General UI/UX Design (design/02)
3. Apply to Textual apps (textual/layout/02, textual/widgets/01)
4. Apply to Marimo notebooks (marimo/02, marimo/03)

**Goal:** Master UI/UX design principles across platforms
**Time:** 4-6 hours

---

## 🆕 Updated Use Cases

### Use Case: Interactive Data Dashboard (Marimo)
**Skills Needed:**
1. marimo/01 (Getting Started)
2. marimo/02 (Widgets for controls)
3. marimo/03 (Dashboard layouts)
4. design/02 (Color theory, accessibility)

### Use Case: CLI Tool with Great UX
**Skills Needed:**
1. design/01 (CLI UX principles)
2. core/01 (If using Textual for TUI)
3. design/02 (General UX principles)

### Use Case: Accessible Notebook Interface
**Skills Needed:**
1. marimo/01 (Notebook basics)
2. marimo/02 (UI components)
3. design/02 (Accessibility, color contrast)
4. marimo/03 (Layouts)

---

## 📖 Next Steps

1. **Browse Skills** - Explore the skills/ directory
2. **Run Examples** - Execute skill files directly
3. **Use Helpers** - Leverage generator and templates
4. **Read Guides** - Check guide sections in skills
5. **Build Projects** - Apply skills to real apps
6. **Test Everything** - Use snapshot testing

---

**Pro Tip:**
- For Textual TUIs: Start with the quick reference (helpers/quick_reference.py) for instant syntax lookups!
- For Marimo notebooks: Run `marimo tutorial intro` to get started interactively
- For UI/UX design: Review accessibility guidelines (skills/design/02_general_ui_ux.py) before starting any project
