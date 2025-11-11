# textual-style

Apply Textual styling, themes, CSS utilities, and design patterns to create beautiful and consistent TUI applications.

## Overview

This command provides comprehensive styling utilities for Textual applications, including theme generation, CSS templates, component library creation, and styling best practices.

## Usage

```
/textual-style <command> [options]
```

## Commands

- `theme <name>` - Create or apply a theme
- `apply <file>` - Apply styles from file
- `generate <type>` - Generate CSS templates
- `component <name>` - Create styled component
- `migrate` - Migrate existing CSS
- `validate <file>` - Validate CSS syntax
- `minify <file>` - Minify CSS file
- `lint <file>` - Lint CSS for best practices

## Examples

### Create a Theme

```
/textual-style theme my-dark-theme --type dark
```

Creates a complete dark theme with:
- Color palette
- Typography scale
- Component styles
- Theme variants

### Generate Component Styles

```
/textual-style component card --variant elevated --interactive
```

Creates:
- Card component CSS
- Hover and focus states
- Multiple variants
- Responsive design

### Generate Full CSS Template

```
/textual-style generate full-app --layout dashboard
```

Generates:
- Complete app stylesheet
- Layout system
- Component library
- Utilities

## Theme Commands

### Create Theme

```
/textual-style theme <name> [options]
```

#### Options

- **--type <type>**: Theme type (dark, light, high-contrast, custom)
- **--primary-color <color>**: Primary brand color
- **--accent-color <color>**: Accent color
- **--font-family <family>**: Font family
- **--font-size <size>**: Base font size
- **--spacing-scale <scale>**: Spacing scale (tight, normal, loose)
- **--border-radius <radius>**: Border radius size
- **--output <dir>**: Output directory

#### Theme Types

**Dark Theme:**
```css
/* dark-theme.tcss */
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
}
```

**Light Theme:**
```css
/* light-theme.tcss */
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
}
```

**High Contrast Theme:**
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
}
```

### Apply Theme

```
/textual-style theme apply <theme-name>
```

**Apply to existing app:**
```bash
# Apply to specific app
textual-style theme apply dark --app app.py

# Apply to entire directory
textual-style theme apply light --dir ./apps
```

**Output:**
```python
# app.py - Theme applied
from textual.app import App

class MyApp(App):
    CSS = """
    /* Theme: dark */
    Screen {
        background: #1e1e1e;
        color: #e0e0e0;
    }

    Button {
        background: #007acc;
        color: white;
    }
    """
```

## Component Commands

### Create Styled Component

```
/textual-style component <name> [options]
```

#### Options

- **--variant <variant>**: Style variant (default, elevated, outlined, filled)
- **--size <size>**: Size (sm, md, lg, xl)
- **--interactive**: Include hover/focus states
- **--responsive**: Include responsive styles
- **--output <file>**: Output CSS file

#### Component Examples

**Button Component:**
```bash
textual-style component button --variant primary --interactive
```

**Generated CSS:**
```css
/* button.tcss */
Button.btn-primary {
    background: var(--primary);
    color: white;
    border: solid var(--primary);
    border-radius: 4;
    padding: 0 2;
    min-height: 3;
}

Button.btn-primary:hover {
    background: var(--primary-hover);
    border-color: var(--primary-hover);
}

Button.btn-primary:pressed {
    background: var(--primary-active);
}

Button.btn-primary:disabled {
    background: var(--surface);
    color: var(--text-muted);
    border-color: var(--surface);
    opacity: 0.5;
}
```

**Card Component:**
```bash
textual-style component card --variant elevated --interactive --responsive
```

**Generated CSS:**
```css
/* card.tcss */
Card {
    background: var(--panel);
    border: solid var(--border-color);
    border-radius: var(--border-radius);
    padding: var(--spacing);
    margin: var(--spacing);
    box-shadow: 0 2 4 rgba(0, 0, 0, 0.1);
}

Card.-elevated {
    box-shadow: 0 4 8 rgba(0, 0, 0, 0.15);
}

Card.-outlined {
    border: solid 2 var(--border-color);
    box-shadow: none;
}

Card.-filled {
    background: var(--surface);
    border: none;
}

Card:hover {
    border-color: var(--primary);
}

Card:disabled {
    opacity: 0.5;
}

/* Responsive */
@media (width < 60) {
    Card {
        margin: 0;
        border-radius: 0;
    }
}
```

**Input Component:**
```bash
textual-style component input --variant filled --interactive
```

**Generated CSS:**
```css
/* input.tcss */
Input.input {
    background: var(--surface);
    border: solid var(--border-color);
    border-radius: var(--border-radius);
    padding: var(--spacing-sm) var(--spacing);
    color: var(--text);
    min-height: 3;
}

Input.input:focus {
    border-color: var(--primary);
    background: var(--panel);
}

Input.input:invalid {
    border-color: var(--error);
}

Input.input:disabled {
    background: var(--surface);
    color: var(--text-muted);
    border-color: var(--surface);
}
```

**DataTable Component:**
```bash
textual-style component datatable --variant striped --interactive
```

**Generated CSS:**
```css
/* datatable.tcss */
DataTable {
    background: var(--panel);
    border: solid var(--border-color);
    border-radius: var(--border-radius);
}

DataTable > .-header {
    background: var(--primary);
    color: white;
    text-style: bold;
}

DataTable > .-row {
    border-bottom: solid var(--border-color);
}

DataTable > .-row:nth-child(even) {
    background: var(--surface);
}

DataTable > .-row:hover {
    background: var(--surface-hover);
}

DataTable > .-row.-selected {
    background: var(--primary-20);
    color: var(--text);
}

DataTable > .-cell {
    padding: var(--spacing-sm) var(--spacing);
}
```

### Create Component Library

```
/textual-style component library --output component-library.tcss
```

**Generates complete CSS library:**
```css
/* component-library.tcss */

/* ==========================================================================
   Design System
   ========================================================================== */

:root {
  /* Colors */
  --primary: #007acc;
  --primary-hover: #005a9e;
  --primary-active: #004578;
  --primary-20: rgba(0, 122, 204, 0.2);

  --secondary: #8b5cf6;
  --accent: #ec4899;

  --success: #22c55e;
  --warning: #f59e0b;
  --error: #ef4444;
  --info: #3b82f6;

  /* Neutral Colors */
  --background: #1e1e1e;
  --surface: #252525;
  --panel: #2d2d2d;
  --border-color: #3a3a3a;

  --text: #e0e0e0;
  --text-muted: #a0a0a0;
  --text-disabled: #6b7280;

  /* Typography */
  --font-family: "Cascadia Mono", monospace;
  --font-size-base: 1rem;
  --font-size-sm: 0.875rem;
  --font-size-lg: 1.125rem;
  --font-size-xl: 1.25rem;
  --font-size-2xl: 1.5rem;
  --font-size-3xl: 1.875rem;

  /* Spacing */
  --spacing-xs: 0.25rem;
  --spacing-sm: 0.5rem;
  --spacing: 1rem;
  --spacing-lg: 1.5rem;
  --spacing-xl: 2rem;

  /* Border Radius */
  --border-radius: 4;
  --border-radius-lg: 8;
  --border-radius-full: 999;

  /* Shadows */
  --shadow-sm: 0 1 2 rgba(0, 0, 0, 0.1);
  --shadow: 0 2 4 rgba(0, 0, 0, 0.1);
  --shadow-lg: 0 4 8 rgba(0, 0, 0, 0.15);
}

/* ==========================================================================
   Buttons
   ========================================================================== */

Button {
    background: var(--surface);
    border: solid var(--border-color);
    border-radius: var(--border-radius);
    padding: var(--spacing-sm) var(--spacing);
    min-height: 3;
    cursor: pointer;
    transition: background 0.2s, border-color 0.2s;
}

Button:hover {
    background: var(--surface-hover);
    border-color: var(--primary);
}

Button:pressed {
    background: var(--surface-active);
}

Button.primary {
    background: var(--primary);
    color: white;
    border-color: var(--primary);
}

Button.primary:hover {
    background: var(--primary-hover);
    border-color: var(--primary-hover);
}

Button.secondary {
    background: var(--secondary);
    color: white;
}

Button.success {
    background: var(--success);
    color: white;
}

Button.warning {
    background: var(--warning);
    color: white;
}

Button.error {
    background: var(--error);
    color: white;
}

Button.ghost {
    background: transparent;
    border-color: transparent;
}

Button.ghost:hover {
    background: var(--surface);
}

Button:disabled {
    background: var(--surface);
    color: var(--text-disabled);
    border-color: var(--surface);
    cursor: not-allowed;
    opacity: 0.5;
}

/* ==========================================================================
   Forms
   ========================================================================== */

Input {
    background: var(--surface);
    border: solid var(--border-color);
    border-radius: var(--border-radius);
    padding: var(--spacing-sm) var(--spacing);
    color: var(--text);
    min-height: 3;
}

Input:focus {
    border-color: var(--primary);
    background: var(--panel);
}

Input:invalid {
    border-color: var(--error);
}

Input:disabled {
    background: var(--surface);
    color: var(--text-muted);
    border-color: var(--surface);
}

TextArea {
    background: var(--surface);
    border: solid var(--border-color);
    border-radius: var(--border-radius);
    padding: var(--spacing);
    color: var(--text);
}

Checkbox {
    margin: 0 var(--spacing-sm);
}

Switch {
    margin: 0 var(--spacing-sm);
}

/* ==========================================================================
   Navigation
   ========================================================================== */

Tabs {
    height: 3;
    border-bottom: solid var(--border-color);
}

Tabs > TabPane.active {
    background: var(--primary);
    color: white;
}

Tabs > TabPane:hover {
    background: var(--surface);
}

/* ==========================================================================
   Data Display
   ========================================================================== */

DataTable {
    background: var(--panel);
    border: solid var(--border-color);
    border-radius: var(--border-radius);
}

DataTable > .-header {
    background: var(--primary);
    color: white;
    text-style: bold;
}

DataTable > .-row {
    border-bottom: solid var(--border-color);
}

DataTable > .-row:nth-child(even) {
    background: var(--surface);
}

DataTable > .-row:hover {
    background: var(--surface-hover);
}

DataTable > .-row.-selected {
    background: var(--primary-20);
}

Log {
    background: var(--panel);
    border: solid var(--border-color);
    border-radius: var(--border-radius);
    padding: var(--spacing);
}

Tree {
    background: var(--panel);
    border: solid var(--border-color);
}

/* ==========================================================================
   Layout
   ========================================================================== */

Container {
    padding: var(--spacing);
}

Container.panel {
    background: var(--panel);
    border: solid var(--border-color);
    border-radius: var(--border-radius);
    padding: var(--spacing);
}

Container.scrollable {
    overflow: auto;
}

/* ==========================================================================
   Utilities
   ========================================================================== */

.hidden {
    display: none;
}

.sr-only {
    position: absolute;
    width: 1;
    height: 1;
    padding: 0;
    margin: -1;
    overflow: hidden;
    clip: rect(0, 0, 0, 0);
    white-space: nowrap;
    border: 0;
}

.text-left {
    text-align: left;
}

.text-center {
    text-align: center;
}

.text-right {
    text-align: right;
}

.text-primary {
    color: var(--primary);
}

.text-success {
    color: var(--success);
}

.text-warning {
    color: var(--warning);
}

.text-error {
    color: var(--error);
}

.bg-primary {
    background: var(--primary);
}

.bg-surface {
    background: var(--surface);
}

.bg-panel {
    background: var(--panel);
}

.m-0 { margin: 0; }
.m-1 { margin: var(--spacing-sm); }
.m-2 { margin: var(--spacing); }
.m-3 { margin: var(--spacing-lg); }

.mt-0 { margin-top: 0; }
.mt-1 { margin-top: var(--spacing-sm); }
.mt-2 { margin-top: var(--spacing); }
.mt-3 { margin-top: var(--spacing-lg); }

.mb-0 { margin-bottom: 0; }
.mb-1 { margin-bottom: var(--spacing-sm); }
.mb-2 { margin-bottom: var(--spacing); }
.mb-3 { margin-bottom: var(--spacing-lg); }

.p-0 { padding: 0; }
.p-1 { padding: var(--spacing-sm); }
.p-2 { padding: var(--spacing); }
.p-3 { padding: var(--spacing-lg); }

.pt-0 { padding-top: 0; }
.pt-1 { padding-top: var(--spacing-sm); }
.pt-2 { padding-top: var(--spacing); }
.pt-3 { padding-top: var(--spacing-lg); }

.pb-0 { padding-bottom: 0; }
.pb-1 { padding-bottom: var(--spacing-sm); }
.pb-2 { padding-bottom: var(--spacing); }
.pb-3 { padding-bottom: var(--spacing-lg); }
```

## Generate Commands

### Generate Full App Stylesheet

```
/textual-style generate full-app --layout <layout-type>
```

#### Layout Types

**Dashboard Layout:**
```bash
textual-style generate full-app --layout dashboard
```

**Generated CSS:**
```css
/* app.tcss - Dashboard Layout */

Screen {
    background: var(--background);
    color: var(--text);
}

/* Header */
.header {
    dock: top;
    height: 3;
    background: var(--primary);
    color: white;
    padding: 0 var(--spacing);
}

/* Sidebar */
.sidebar {
    dock: left;
    width: 25;
    background: var(--panel);
    border-right: solid var(--border-color);
    padding: var(--spacing);
}

/* Main Content */
.main {
    background: var(--background);
    padding: var(--spacing);
}

/* Right Panel */
.panel {
    dock: right;
    width: 30;
    background: var(--panel);
    border-left: solid var(--border-color);
    padding: var(--spacing);
}

/* Footer */
.footer {
    dock: bottom;
    height: 3;
    background: var(--surface);
    border-top: solid var(--border-color);
    padding: 0 var(--spacing);
}

/* Widgets */
.widget {
    background: var(--panel);
    border: solid var(--border-color);
    border-radius: var(--border-radius);
    padding: var(--spacing);
    margin-bottom: var(--spacing);
}

.widget-header {
    font-size: var(--font-size-lg);
    font-weight: bold;
    margin-bottom: var(--spacing);
    padding-bottom: var(--spacing-sm);
    border-bottom: solid var(--border-color);
}

.widget-content {
    /* Widget specific content */
}
```

**Form Layout:**
```bash
textual-style generate full-app --layout form
```

**Generated CSS:**
```css
/* app.tcss - Form Layout */

Screen {
    background: var(--background);
    color: var(--text);
}

.form-container {
    width: 80%;
    max-width: 600;
    margin: 0 auto;
    padding: var(--spacing-xl);
}

.form-header {
    text-align: center;
    font-size: var(--font-size-2xl);
    font-weight: bold;
    margin-bottom: var(--spacing-xl);
}

.form-group {
    margin-bottom: var(--spacing-lg);
}

.form-label {
    display: block;
    margin-bottom: var(--spacing-sm);
    font-weight: bold;
}

.form-input {
    width: 100%;
}

.form-help {
    margin-top: var(--spacing-sm);
    font-size: var(--font-size-sm);
    color: var(--text-muted);
}

.form-error {
    color: var(--error);
    font-size: var(--font-size-sm);
    margin-top: var(--spacing-sm);
}

.form-actions {
    margin-top: var(--spacing-xl);
    text-align: right;
}

.form-actions Button {
    margin-left: var(--spacing);
}
```

**List Layout:**
```bash
textual-style generate full-app --layout list
```

### Generate Layout System

```
/textual-style generate layout-system --type <type>
```

#### Layout Types

**CSS Grid System:**
```bash
textual-style generate layout-system --type grid
```

**Generated CSS:**
```css
/* layout-grid.tcss */

.grid {
    display: grid;
    gap: var(--spacing);
}

.grid-cols-1 { grid-template-columns: 1fr; }
.grid-cols-2 { grid-template-columns: repeat(2, 1fr); }
.grid-cols-3 { grid-template-columns: repeat(3, 1fr); }
.grid-cols-4 { grid-template-columns: repeat(4, 1fr); }
.grid-cols-12 { grid-template-columns: repeat(12, 1fr); }

.col-span-1 { grid-column: span 1; }
.col-span-2 { grid-column: span 2; }
.col-span-3 { grid-column: span 3; }
.col-span-4 { grid-column: span 4; }
.col-span-full { grid-column: 1 / -1; }

/* Responsive grid */
@media (width < 80) {
    .grid-cols-3 { grid-template-columns: repeat(2, 1fr); }
    .grid-cols-4 { grid-template-columns: repeat(2, 1fr); }
}

@media (width < 60) {
    .grid-cols-2,
    .grid-cols-3,
    .grid-cols-4 { grid-template-columns: 1fr; }
}
```

**Flexbox System:**
```bash
textual-style generate layout-system --type flex
```

**Generated CSS:**
```css
/* layout-flex.tcss */

.flex {
    display: flex;
    gap: var(--spacing);
}

.flex-col {
    flex-direction: column;
}

.flex-row {
    flex-direction: row;
}

.flex-wrap {
    flex-wrap: wrap;
}

.flex-nowrap {
    flex-wrap: nowrap;
}

.justify-start { justify-content: flex-start; }
.justify-center { justify-content: center; }
.justify-end { justify-content: flex-end; }
.justify-between { justify-content: space-between; }
.justify-around { justify-content: space-around; }

.align-start { align-items: flex-start; }
.align-center { align-items: center; }
.align-end { align-items: flex-end; }
.align-stretch { align-items: stretch; }

.flex-1 { flex: 1; }
.flex-auto { flex: auto; }
.flex-none { flex: none; }

.gap-0 { gap: 0; }
.gap-1 { gap: var(--spacing-sm); }
.gap-2 { gap: var(--spacing); }
.gap-3 { gap: var(--spacing-lg); }
.gap-4 { gap: var(--spacing-xl); }
```

### Generate Utilities

```
/textual-style generate utilities --type <type>
```

#### Utility Types

**Spacing Utilities:**
```bash
textual-style generate utilities --type spacing
```

**Generated CSS:**
```css
/* utilities-spacing.tcss */

/* Margin */
.m-0 { margin: 0; }
.m-1 { margin: var(--spacing-xs); }
.m-2 { margin: var(--spacing-sm); }
.m-3 { margin: var(--spacing); }
.m-4 { margin: var(--spacing-lg); }
.m-5 { margin: var(--spacing-xl); }

.mt-0 { margin-top: 0; }
.mt-1 { margin-top: var(--spacing-xs); }
.mt-2 { margin-top: var(--spacing-sm); }
.mt-3 { margin-top: var(--spacing); }
.mt-4 { margin-top: var(--spacing-lg); }
.mt-5 { margin-top: var(--spacing-xl); }

.mr-0 { margin-right: 0; }
.mr-1 { margin-right: var(--spacing-xs); }
.mr-2 { margin-right: var(--spacing-sm); }
.mr-3 { margin-right: var(--spacing); }
.mr-4 { margin-right: var(--spacing-lg); }
.mr-5 { margin-right: var(--spacing-xl); }

.mb-0 { margin-bottom: 0; }
.mb-1 { margin-bottom: var(--spacing-xs); }
.mb-2 { margin-bottom: var(--spacing-sm); }
.mb-3 { margin-bottom: var(--spacing); }
.mb-4 { margin-bottom: var(--spacing-lg); }
.mb-5 { margin-bottom: var(--spacing-xl); }

.ml-0 { margin-left: 0; }
.ml-1 { margin-left: var(--spacing-xs); }
.ml-2 { margin-left: var(--spacing-sm); }
.ml-3 { margin-left: var(--spacing); }
.ml-4 { margin-left: var(--spacing-lg); }
.ml-5 { margin-left: var(--spacing-xl); }

/* Negative margins */
.-m-1 { margin: calc(var(--spacing-xs) * -1); }
.-m-2 { margin: calc(var(--spacing-sm) * -1); }
.-m-3 { margin: calc(var(--spacing) * -1); }
.-m-4 { margin: calc(var(--spacing-lg) * -1); }
.-m-5 { margin: calc(var(--spacing-xl) * -1); }

/* Padding */
.p-0 { padding: 0; }
.p-1 { padding: var(--spacing-xs); }
.p-2 { padding: var(--spacing-sm); }
.p-3 { padding: var(--spacing); }
.p-4 { padding: var(--spacing-lg); }
.p-5 { padding: var(--spacing-xl); }

.pt-0 { padding-top: 0; }
.pt-1 { padding-top: var(--spacing-xs); }
.pt-2 { padding-top: var(--spacing-sm); }
.pt-3 { padding-top: var(--spacing); }
.pt-4 { padding-top: var(--spacing-lg); }
.pt-5 { padding-top: var(--spacing-xl); }

.pr-0 { padding-right: 0; }
.pr-1 { padding-right: var(--spacing-xs); }
.pr-2 { padding-right: var(--spacing-sm); }
.pr-3 { padding-right: var(--spacing); }
.pr-4 { padding-right: var(--spacing-lg); }
.pr-5 { padding-right: var(--spacing-xl); }

.pb-0 { padding-bottom: 0; }
.pb-1 { padding-bottom: var(--spacing-xs); }
.pb-2 { padding-bottom: var(--spacing-sm); }
.pb-3 { padding-bottom: var(--spacing); }
.pb-4 { padding-bottom: var(--spacing-lg); }
.pb-5 { padding-bottom: var(--spacing-xl); }

.pl-0 { padding-left: 0; }
.pl-1 { padding-left: var(--spacing-xs); }
.pl-2 { padding-left: var(--spacing-sm); }
.pl-3 { padding-left: var(--spacing); }
.pl-4 { padding-left: var(--spacing-lg); }
.pl-5 { padding-left: var(--spacing-xl); }
```

**Typography Utilities:**
```bash
textual-style generate utilities --type typography
```

**Generated CSS:**
```css
/* utilities-typography.tcss */

/* Font families */
.font-mono { font-family: var(--font-family); }
.font-sans { font-family: "Inter", sans-serif; }

/* Font sizes */
.text-xs { font-size: var(--font-size-sm); }
.text-sm { font-size: var(--font-size-sm); }
.text-base { font-size: var(--font-size-base); }
.text-lg { font-size: var(--font-size-lg); }
.text-xl { font-size: var(--font-size-xl); }
.text-2xl { font-size: var(--font-size-2xl); }
.text-3xl { font-size: var(--font-size-3xl); }

/* Font weights */
.font-normal { font-weight: normal; }
.font-medium { font-weight: 500; }
.font-semibold { font-weight: 600; }
.font-bold { font-weight: bold; }

/* Text alignment */
.text-left { text-align: left; }
.text-center { text-align: center; }
.text-right { text-align: right; }

/* Text decoration */
.underline { text-decoration: underline; }
.line-through { text-decoration: line-through; }
.no-underline { text-decoration: none; }

/* Text transform */
.uppercase { text-transform: uppercase; }
.lowercase { text-transform: lowercase; }
.capitalize { text-transform: capitalize; }

/* Text colors */
.text-primary { color: var(--primary); }
.text-secondary { color: var(--secondary); }
.text-muted { color: var(--text-muted); }
.text-success { color: var(--success); }
.text-warning { color: var(--warning); }
.text-error { color: var(--error); }
```

## Migration Commands

### Migrate Existing CSS

```
/textual-style migrate <file> [options]
```

**Convert old Textual CSS to new format:**
```bash
# Migrate single file
textual-style migrate old-styles.tcss --output new-styles.tcss

# Migrate and modernize
textual-style migrate styles.tcss --modernize

# Migrate with theme conversion
textual-style migrate styles.tcss --to-theme modern-dark
```

**Migration Features:**
- Convert hardcoded colors to CSS variables
- Update syntax to latest Textual CSS
- Add responsive design
- Modernize selectors
- Optimize specificity

**Before Migration:**
```css
/* old-styles.tcss */
Screen {
    background-color: #1e1e1e;
}

Container {
    padding: 10px;
}

Button {
    background-color: #007acc;
    color: white;
}
```

**After Migration:**
```css
/* new-styles.tcss */
:root {
    --background: #1e1e1e;
    --primary: #007acc;
    --text: #ffffff;
    --spacing: 1;
}

Screen {
    background: var(--background);
}

Container {
    padding: var(--spacing);
}

Button {
    background: var(--primary);
    color: var(--text);
}
```

## Validation Commands

### Validate CSS

```
/textual-style validate <file> [options]
```

**Check for errors:**
```bash
textual-style validate styles.tcss --strict
```

**Output:**
```
✓ Valid CSS syntax
✓ No deprecated properties
✓ Consistent naming
✓ Proper specificity

Found 5 warnings:
  Line 25: Consider using CSS variables for color
  Line 42: Unused class '.old-style'
  Line 58: Duplicate property 'padding'
  Line 73: Consider consolidating margin rules
  Line 89: Missing hover state for interactive elements
```

### Lint CSS

```
/textual-style lint <file> [options]
```

**Lint for best practices:**
```bash
textual-style lint styles.tcss --fix
```

**Checks:**
- Property order
- Selector naming
- Specificity issues
- Redundant code
- Accessibility concerns
- Performance optimization

## Apply Commands

### Apply Styles

```
/textual-style apply <file> [options]
```

**Apply to app:**
```bash
# Apply to specific app
textual-style apply component-library.tcss --app app.py

# Apply and merge
textual-style apply styles.tcss --app app.py --merge

# Apply with specific target
textual-style apply button-styles.tcss --target Button --app app.py
```

**Update app.py:**
```python
# Before
class MyApp(App):
    pass

# After
class MyApp(App):
    CSS = """
    /* Component Library Applied */
    Button {
        background: var(--primary);
        color: white;
        border-radius: var(--border-radius);
    }
    """
```

## Best Practices

### CSS Organization

```css
/* 1. Variables at the top */
:root {
    --primary: #007acc;
    --spacing: 1rem;
}

/* 2. Base styles */
Screen {
    background: var(--background);
    color: var(--text);
}

/* 3. Component styles */
Button {
    background: var(--primary);
}

Input {
    border: solid var(--border-color);
}

/* 4. Utility classes */
.text-center { text-align: center; }
.mt-2 { margin-top: var(--spacing); }
```

### Naming Conventions

```css
/* Use kebab-case for classes */
.my-component {
    background: var(--primary);
}

/* Use consistent naming */
.button-primary { }
.button-secondary { }
.button-error { }

/* Use semantic names */
.nav-menu { }
.content-area { }
.sidebar-panel { }
```

### Performance Tips

```css
/* Avoid deep nesting */
Container Container Container Button { }

/* Use efficient selectors */
Button.primary { }

/* Minimize specificity */
.my-component { }

/* Group related properties */
Button {
    background: var(--primary);
    color: white;  /* Grouped */
    border: none;  /* Grouped */
}
```

### Responsive Design

```css
/* Mobile first */
.my-component {
    width: 100%;
    padding: var(--spacing-sm);
}

/* Tablet */
@media (width >= 60) {
    .my-component {
        width: 50%;
        padding: var(--spacing);
    }
}

/* Desktop */
@media (width >= 100) {
    .my-component {
        width: 33%;
        padding: var(--spacing-lg);
    }
}
```

## Troubleshooting

### Common Issues

**Issue: Styles not applying**
```python
# Check CSS_PATH is set
class MyApp(App):
    CSS_PATH = "styles/main.tcss"

# Or use DEFAULT_CSS
class MyWidget(Widget):
    DEFAULT_CSS = """
    MyWidget {
        background: red;
    }
    """
```

**Issue: Specificity conflicts**
```css
/* Use more specific selectors */
Button.button-primary {
    background: blue;  /* Wins over generic Button */
}

/* Or use !important (avoid when possible) */
Button {
    background: blue !important;
}
```

**Issue: Responsive design breaks**
```css
/* Test at different sizes */
@media (width < 60) {
    .sidebar {
        /* Styles for narrow screens */
    }
}

/* Verify media query syntax */
@media (width < 60) {  /* Correct */
    @media (max-width: 60px) {  /* Wrong */
```

**Issue: Color contrast issues**
```css
/* Check contrast ratios */
.high-contrast {
    background: black;   /* Dark background */
    color: white;        /* Light text */
}

/* Test readability */
.text-muted {
    color: var(--text-muted);  /* Ensure sufficient contrast */
}
```

## See Also

- [Textual CSS Styling](../helpers/textual-css-styling.md)
- [Textual Layouts Guide](../helpers/textual-layouts-guide.md)
- [Textual Widgets Reference](../helpers/textual-widgets-reference.md)
- [Textual Performance](../helpers/textual-performance.md)
