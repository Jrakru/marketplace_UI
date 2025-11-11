# textual-css-styling

Textual CSS styling patterns, themes, color schemes, typography, and advanced styling techniques for beautiful TUIs.

## Overview

Textual uses CSS-like styling to create visually appealing terminal user interfaces. Understanding CSS in Textual enables you to create consistent, maintainable, and beautiful TUIs.

## CSS Basics in Textual

### Applying CSS

```python
# Method 1: External CSS file
from textual.app import App

class StyledApp(App):
    CSS = """
    Screen {
        background: $background;
    }
    """

# Method 2: External file
class AppWithCSSFile(App):
    pass

app = AppWithCSSFile()
app.css_file = "styles.tcss"

# Method 3: Import from file
class App(App):
    CSS_PATH = "styles.tcss"

# Method 4: Programmatic styles
button = Button("Styled Button")
button.styles.background = "red"
button.styles.color = "white"
```

### CSS File Structure

```css
/* styles.tcss */
Screen {
    background: #1e1e1e;
}

Container {
    padding: 1;
}

Button {
    margin: 1 2;
}

Button.primary {
    background: #007acc;
    color: white;
}
```

## Color System

### Color Formats

```css
/* Named colors */
Screen {
    background: black;
    color: white;
}

/* Hex colors */
Button {
    background: #ff0000;
    color: #ffffff;
}

/* RGB */
Panel {
    background: rgb(255, 0, 0);
    color: rgb(255, 255, 255);
}

/* RGBA (with transparency) */
Modal {
    background: rgba(0, 0, 0, 0.8);
    color: white;
}

/* HSL */
Accent {
    background: hsl(200, 100%, 50%);
    color: hsl(0, 0%, 100%);
}

/* CSS variables */
:root {
    --primary-color: #007acc;
    --text-color: #ffffff;
}

Button {
    background: var(--primary-color);
    color: var(--text-color);
}
```

### Textual Color Variables

```css
/* Built-in Textual colors */
Screen {
    background: $background;    /* Terminal background */
    color: $text;               /* Terminal foreground */
    /* $surface - Slightly different background */
    /* $panel - Panel background */
    /* $accent - Accent color */
    /* $primary - Primary color */
    /* $secondary - Secondary color */
}

/* Textual semantic colors */
.success { color: $success; }
.warning { color: $warning; }
.error { color: $error; }
.info { color: $info; }
```

### Custom Color Palette

```css
:root {
    /* Brand colors */
    --brand-primary: #6366f1;
    --brand-secondary: #8b5cf6;
    --brand-accent: #ec4899;

    /* Neutral colors */
    --neutral-50: #fafafa;
    --neutral-100: #f5f5f5;
    --neutral-200: #e5e5e5;
    --neutral-300: #d4d4d4;
    --neutral-400: #a3a3a3;
    --neutral-500: #737373;
    --neutral-600: #525252;
    --neutral-700: #404040;
    --neutral-800: #262626;
    --neutral-900: #171717;

    /* Text colors */
    --text-primary: var(--neutral-900);
    --text-secondary: var(--neutral-600);
    --text-muted: var(--neutral-500);
}
```

## Typography

### Font Families

```css
/* Monospace (default) */
.monospace {
    font-family: "Cascadia Mono", "Fira Code", monospace;
}

/* Sans-serif */
.sans-serif {
    font-family: "Inter", "Helvetica", sans-serif;
}

/* Specific font */
.code {
    font-family: "Cascadia Code", monospace;
}
```

### Font Size

```css
/* Text size classes */
.text-xs { font-size: 0.75rem; }
.text-sm { font-size: 0.875rem; }
.text-base { font-size: 1rem; }
.text-lg { font-size: 1.125rem; }
.text-xl { font-size: 1.25rem; }
.text-2xl { font-size: 1.5rem; }
.text-3xl { font-size: 1.875rem; }

/* Custom sizes */
.large-text {
    font-size: 2rem;
}
```

### Font Weight

```css
.bold { font-weight: bold; }
.bolder { font-weight: bolder; }
.lighter { font-weight: lighter; }

.text-normal { font-weight: normal; }
.text-medium { font-weight: 500; }
.text-semibold { font-weight: 600; }
.text-bold { font-weight: 700; }
```

### Text Alignment

```css
.left { text-align: left; }
.center { text-align: center; }
.right { text-align: right; }
.justify { text-align: justify; }
```

### Text Styling

```css
.italic { font-style: italic; }
.oblique { font-style: oblique; }

.underline { text-decoration: underline; }
.line-through { text-decoration: line-through; }
.no-decoration { text-decoration: none; }

/* Combined */
.title {
    font-size: 2rem;
    font-weight: bold;
    text-align: center;
}
```

## Layout Properties

### Padding and Margin

```css
/* Padding */
.no-padding { padding: 0; }
.padding-1 { padding: 1; }
.padding-2 { padding: 2; }
.padding-3 { padding: 3; }

/* Specific sides */
.padding-top-1 { padding-top: 1; }
.padding-right-2 { padding-right: 2; }
.padding-bottom-1 { padding-bottom: 1; }
.padding-left-2 { padding-left: 2; }

/* Margin */
.no-margin { margin: 0; }
.margin-1 { margin: 1; }
.margin-2 { margin: 2; }

/* Auto margin (centering) */
.centered {
    margin-left: auto;
    margin-right: auto;
}
```

### Width and Height

```css
/* Width */
.w-full { width: 100%; }
.w-auto { width: auto; }
.w-half { width: 50%; }
.w-quarter { width: 25%; }

/* Fixed width */
.width-20 { width: 20; }
.width-30 { width: 30; }

/* Height */
.h-full { height: 100%; }
.h-auto { height: auto; }
.h-half { height: 50%; }

/* Fixed height */
.height-10 { height: 10; }
.height-20 { height: 20; }

/* Min/max */
.min-width-10 { min-width: 10; }
.max-width-30 { max-width: 30; }
.min-height-5 { min-height: 5; }
.max-height-20 { max-height: 20; }
```

### Border

```css
/* Border width */
.no-border { border: none; }
.border { border: solid; }
.border-1 { border: solid; }
.border-2 { border: solid; }

/* Border sides */
.border-top { border-top: solid; }
.border-right { border-right: solid; }
.border-bottom { border-bottom: solid; }
.border-left { border-left: solid; }

/* Border colors */
.border-primary { border: solid $primary; }
.border-success { border: solid $success; }
.border-error { border: solid $error; }

/* Border styles */
.border-dashed { border: dashed; }
.border-dotted { border: dotted; }

/* Combined border */
.panel {
    border: solid $panel;
    border-radius: 2;
}
```

## Layout Systems

### Display Types

```css
/* Block (default) */
.block { display: block; }

/* Inline */
.inline { display: inline; }

/* Flex */
.flex { display: flex; }

/* Grid */
.grid { display: grid; }

/* None (hidden) */
.hidden { display: none; }
```

### Flexbox

```css
.flex-container {
    display: flex;
    flex-direction: row;      /* row, column, row-reverse, column-reverse */
    flex-wrap: nowrap;        /* nowrap, wrap, wrap-reverse */
    justify-content: start;   /* start, end, center, space-between, space-around */
    align-items: stretch;     /* stretch, start, end, center */
    gap: 1;                   /* spacing between items */
}

/* Flex items */
.flex-1 { flex: 1; }
.flex-2 { flex: 2; }
.flex-grow { flex-grow: 1; }
.flex-shrink { flex-shrink: 1; }

/* Align self */
.self-start { align-self: start; }
.self-center { align-self: center; }
.self-end { align-self: end; }
```

### Grid

```css
.grid-container {
    display: grid;
    grid-columns: 1fr 2fr 1fr;    /* Column sizes */
    grid-rows: auto 1fr auto;     /* Row sizes */
    grid-gutter: 1;               /* Gap between cells */
}

/* Grid areas */
.header { grid-area: header; }
.sidebar { grid-area: sidebar; }
.content { grid-area: content; }
.footer { grid-area: footer; }
```

### Docking

```css
.docked-top {
    dock: top;
    height: 1;
}

.docked-bottom {
    dock: bottom;
    height: 1;
}

.docked-left {
    dock: left;
    width: 20;
}

.docked-right {
    dock: right;
    width: 20;
}
```

## Background and Borders

### Background Colors

```css
/* Solid colors */
.bg-primary { background: $primary; }
.bg-secondary { background: $secondary; }
.bg-success { background: $success; }
.bg-warning { background: $warning; }
.bg-error { background: $error; }
.bg-info { background: $info; }

/* Custom backgrounds */
.bg-dark { background: #1e1e1e; }
.bg-light { background: #f5f5f5; }

/* Semi-transparent */
.bg-overlay { background: rgba(0, 0, 0, 0.5); }
```

### Background Gradients

```css
.gradient-primary {
    background: $primary 0%, $secondary 100%;
}

.gradient-vertical {
    background: linear-gradient(#000, #333);
}

.gradient-horizontal {
    background: linear-gradient(90deg, #000, #333);
}
```

### Borders and Rounding

```css
.rounded { border-radius: 2; }
.rounded-lg { border-radius: 4; }
.rounded-full { border-radius: 999; }

.border-primary { border: solid $primary; }
.border-2 { border: solid 2; }

.outline { border: solid $accent; }
```

## Widget-Specific Styling

### Button Styling

```css
Button {
    background: $panel;
    color: $text;
    border: solid $accent;
    margin: 1;
}

Button:hover {
    background: $accent;
    color: $text;
}

Button:pressed {
    background: $secondary;
}

Button.primary {
    background: $primary;
    color: white;
}

Button.success {
    background: $success;
    color: white;
}

Button.warning {
    background: $warning;
    color: white;
}

Button.error {
    background: $error;
    color: white;
}

Button:disabled {
    background: $surface;
    color: $text-disabled;
    opacity: 0.5;
}
```

### Input Styling

```css
Input {
    background: $surface;
    color: $text;
    border: solid $accent;
    padding: 0 1;
}

Input:focus {
    border: solid $primary;
    background: $panel;
}

Input:invalid {
    border: solid $error;
}

Input#search {
    background: $primary 10%;
}
```

### Panel Styling

```css
Panel {
    background: $panel;
    border: solid $accent;
    padding: 1;
}

Panel.title {
    background: $primary;
    color: white;
    text-align: center;
}

Panel.header {
    background: $surface;
    border: solid $accent;
    border-bottom: none;
}

Panel.footer {
    background: $surface;
    border: solid $accent;
    border-top: none;
}
```

### Table Styling

```css
DataTable {
    background: $panel;
    border: solid $accent;
}

DataTable > .datatable--header {
    background: $primary;
    color: white;
}

DataTable > .datatable--cursor {
    background: $accent;
    color: $text;
}

DataTable > .datatable--hover {
    background: $surface;
}
```

### Log Styling

```css
Log {
    background: $panel;
    border: solid $accent;
    color: $text;
}

Log .log-level-debug {
    color: $text-muted;
}

Log .log-level-info {
    color: $info;
}

Log .log-level-warning {
    color: $warning;
}

Log .log-level-error {
    color: $error;
}
```

## Theme System

### Dark Theme

```css
/* dark.tcss */
:root {
    --background: #1e1e1e;
    --surface: #252525;
    --panel: #2d2d2d;
    --text: #e0e0e0;
    --text-muted: #a0a0a0;
    --primary: #007acc;
    --secondary: #8b5cf6;
    --accent: #ec4899;
    --success: #22c55e;
    --warning: #f59e0b;
    --error: #ef4444;
    --info: #3b82f6;
}

Screen {
    background: $background;
    color: $text;
}
```

### Light Theme

```css
/* light.tcss */
:root {
    --background: #ffffff;
    --surface: #f5f5f5;
    --panel: #ffffff;
    --text: #1a1a1a;
    --text-muted: #666666;
    --primary: #007acc;
    --secondary: #8b5cf6;
    --accent: #ec4899;
    --success: #22c55e;
    --warning: #f59e0b;
    --error: #ef4444;
    --info: #3b82f6;
}

Screen {
    background: $background;
    color: $text;
}
```

### High Contrast Theme

```css
/* high-contrast.tcss */
:root {
    --background: #000000;
    --surface: #000000;
    --panel: #000000;
    --text: #ffffff;
    --text-muted: #ffffff;
    --primary: #ffffff;
    --secondary: #ffffff;
    --accent: #ffffff;
    --success: #00ff00;
    --warning: #ffff00;
    --error: #ff0000;
    --info: #00ffff;
}

Screen {
    background: $background;
    color: $text;
}

Button, Input, DataTable {
    border: solid white;
}
```

### Theme Switching

```python
class ThemedApp(App):
    """App with theme switching."""

    CSS = """
    Screen {
        background: $background;
        color: $text;
    }
    """

    def compose(self):
        yield Button("Toggle Theme", id="toggle-theme")
        yield Static("Sample content", classes="content")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "toggle-theme":
            self.toggle_theme()

    def toggle_theme(self):
        """Toggle between light and dark themes."""
        current_theme = self.get_attribute("data-theme", "dark")
        new_theme = "light" if current_theme == "dark" else "dark"

        # Clear existing CSS
        self.clear_css()

        # Load new theme
        theme_file = f"{new_theme}.tcss"
        self.css_file = theme_file

        self.set_attribute("data-theme", new_theme)

    def get_attribute(self, name, default=None):
        """Get temporary attribute."""
        return getattr(self, f"_{name}", default)

    def set_attribute(self, name, value):
        """Set temporary attribute."""
        setattr(self, f"_{name}", value)
```

## Component Library

### Card Component

```css
/* card.tcss */
.card {
    background: $panel;
    border: solid $accent;
    border-radius: 2;
    padding: 1;
    margin: 1;
}

.card-title {
    background: $primary;
    color: white;
    text-align: center;
    padding: 1;
    margin: -1 -1 1 -1;
}

.card-body {
    padding: 1;
}

.card-actions {
    background: $surface;
    padding: 1;
    margin: 1 -1 -1 -1;
}
```

```python
# card.py
from textual.containers import Container, Vertical

class Card(Container):
    """Card container widget."""

    DEFAULT_CSS = """
    Card {
        background: $panel;
        border: solid $accent;
        border-radius: 2;
        padding: 1;
        margin: 1;
    }
    """

    def compose(self):
        yield Vertical()
```

### Button Group

```css
/* button-group.tcss */
.button-group {
    layout: horizontal;
    gap: 0;
}

.button-group > Button {
    margin: 0;
    border-radius: 0;
}

.button-group > Button:first-child {
    border-top-left-radius: 2;
    border-bottom-left-radius: 2;
}

.button-group > Button:last-child {
    border-top-right-radius: 2;
    border-bottom-right-radius: 2;
}

.button-group > Button:only-child {
    border-radius: 2;
}
```

### Navigation Menu

```css
/* nav-menu.tcss */
.nav-menu {
    background: $panel;
    border: solid $accent;
    padding: 1;
}

.nav-item {
    background: $surface;
    border: none;
    margin: 0 0 1 0;
    padding: 1 2;
    text-align: left;
}

.nav-item:hover {
    background: $accent;
    color: $text;
}

.nav-item.active {
    background: $primary;
    color: white;
}
```

## Responsive Design

### Media Queries

```css
/* Small screens */
@media (width < 60) {
    .sidebar {
        display: none;
    }

    .main {
        width: 100%;
    }
}

/* Medium screens */
@media (width >= 60) and (width < 100) {
    .sidebar {
        width: 20;
    }

    .main {
        width: auto;
    }
}

/* Large screens */
@media (width >= 100) {
    .sidebar {
        width: 25;
    }

    .main {
        width: auto;
    }
}
```

### Adaptive Layouts

```css
/* Stack vertically on small screens */
@media (width < 80) {
    .horizontal-layout {
        layout: vertical;
    }
}

/* Compact spacing on small screens */
@media (width < 60) {
    .compact {
        padding: 0;
        margin: 0;
        gap: 0;
    }
}

/* Hide labels on small screens */
@media (width < 50) {
    .label {
        display: none;
    }
}
```

## Animation and Transitions

### CSS Animations

```css
@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.5; }
}

.loading {
    animation: pulse 2s infinite;
}

@keyframes slide-in {
    from { transform: translate-y(-100%); }
    to { transform: translate-y(0%); }
}

.modal {
    animation: slide-in 0.3s;
}
```

### Hover Effects

```css
Button {
    transition: background 0.3s;
}

Button:hover {
    background: $accent;
}

Input {
    transition: border 0.2s;
}

Input:focus {
    border: solid $primary;
}
```

## Utility Classes

### Spacing Utilities

```css
.m-0 { margin: 0; }
.m-1 { margin: 1; }
.m-2 { margin: 2; }
.m-3 { margin: 3; }

.mt-0 { margin-top: 0; }
.mt-1 { margin-top: 1; }
.mr-1 { margin-right: 1; }
.mb-1 { margin-bottom: 1; }
.ml-1 { margin-left: 1; }

.p-0 { padding: 0; }
.p-1 { padding: 1; }
.p-2 { padding: 2; }
.p-3 { padding: 3; }

.pt-1 { padding-top: 1; }
.pr-1 { padding-right: 1; }
.pb-1 { padding-bottom: 1; }
.pl-1 { padding-left: 1; }
```

### Color Utilities

```css
.text-primary { color: $primary; }
.text-secondary { color: $secondary; }
.text-success { color: $success; }
.text-warning { color: $warning; }
.text-error { color: $error; }
.text-info { color: $info; }
.text-muted { color: $text-muted; }

.bg-primary { background: $primary; }
.bg-secondary { background: $secondary; }
.bg-success { background: $success; }
.bg-warning { background: $warning; }
.bg-error { background: $error; }
.bg-info { background: $info; }
```

### Layout Utilities

```css
.flex { display: flex; }
.grid { display: grid; }
.hidden { display: none; }
.block { display: block; }
.inline { display: inline; }

.flex-row { flex-direction: row; }
.flex-col { flex-direction: column; }

.items-center { align-items: center; }
.items-start { align-items: start; }
.items-end { align-items: end; }

.justify-center { justify-content: center; }
.justify-between { justify-content: space-between; }
.justify-around { justify-content: space-around; }

.gap-1 { gap: 1; }
.gap-2 { gap: 2; }
.gap-3 { gap: 3; }
```

### Text Utilities

```css
.text-left { text-align: left; }
.text-center { text-align: center; }
.text-right { text-align: right; }

.text-xs { font-size: 0.75rem; }
.text-sm { font-size: 0.875rem; }
.text-base { font-size: 1rem; }
.text-lg { font-size: 1.125rem; }
.text-xl { font-size: 1.25rem; }

.font-bold { font-weight: bold; }
.font-normal { font-weight: normal; }

.italic { font-style: italic; }

.underline { text-decoration: underline; }
.no-underline { text-decoration: none; }
```

## Best Practices

### 1. Use CSS Variables

```css
/* Good: Uses variables */
:root {
    --primary-color: #007acc;
}

Button.primary {
    background: var(--primary-color);
}

/* Avoid: Hard-coded colors */
Button {
    background: #007acc;
}
```

### 2. Organize by Component

```css
/* Card styles */
.card { /* ... */ }
.card-title { /* ... */ }
.card-body { /* ... */ }

/* Button styles */
.button { /* ... */ }
.button-primary { /* ... */ }
.button-secondary { /* ... */ }

/* Layout styles */
.container { /* ... */ }
.sidebar { /* ... */ }
.main { /* ... */ }
```

### 3. Use Semantic Class Names

```css
/* Good */
.button-primary { }
.status-success { }
.nav-menu { }

/* Avoid */
.button-1 { }
.status-2 { }
.menu-3 { }
```

### 4. Keep CSS DRY

```css
/* Good: Use variables and classes */
:root {
    --card-padding: 1;
    --card-radius: 2;
}

.card {
    padding: var(--card-padding);
    border-radius: var(--card-radius);
}

/* Avoid: Repetition */
.card1 { padding: 1; border-radius: 2; }
.card2 { padding: 1; border-radius: 2; }
.card3 { padding: 1; border-radius: 2; }
```

### 5. Responsive-First Approach

```css
/* Start with mobile/base styles */
.container {
    layout: vertical;
    gap: 1;
}

/* Enhance for larger screens */
@media (width >= 60) {
    .container {
        layout: horizontal;
        gap: 2;
    }
}
```

### 6. Performance Considerations

```css
/* Avoid complex selectors */
Screen Button:hover .icon { }

/* Use simple, direct selectors */
.button:hover { }
.icon { }
```

### 7. Accessibility

```css
/* Ensure sufficient contrast */
.high-contrast {
    background: black;
    color: white;
}

/* Focus indicators */
Button:focus {
    border: solid $primary;
}

Input:focus {
    outline: solid $primary;
}
```

## CSS Patterns

### Split Layout Pattern

```css
.app {
    layout: horizontal;
}

.sidebar {
    width: 25;
    background: $panel;
}

.main {
    background: $background;
}
```

### Header-Content-Footer Pattern

```css
.app {
    layout: vertical;
}

.header {
    height: 1;
    background: $primary;
}

.content {
    background: $background;
}

.footer {
    height: 1;
    background: $surface;
}
```

### Modal Pattern

```css
.modal-overlay {
    background: rgba(0, 0, 0, 0.8);
}

.modal {
    width: 50;
    height: auto;
    background: $panel;
    border: solid $accent;
    padding: 2;
}
```

### Dashboard Grid Pattern

```css
.dashboard {
    layout: grid;
    grid-columns: 1fr 1fr;
    grid-rows: auto;
    gap: 1;
}

.widget {
    background: $panel;
    border: solid $accent;
    padding: 1;
}
```

## See Also

- [Textual Widgets Reference](textual-widgets-reference.md)
- [Textual Layouts Guide](textual-layouts-guide.md)
- [Textual Events Handling](textual-events-handling.md)
- [Textual Data Binding](textual-data-binding.md)
