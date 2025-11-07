"""
Skill: CSS Styling (TCSS)

Master Textual CSS for beautiful TUI styling.
"""

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Button, Label
from textual.containers import Container, Horizontal, Vertical


# ============================================================================
# BASIC CSS EXAMPLE
# ============================================================================

class BasicCSSDemo(App):
    """Demonstrates basic CSS styling."""

    CSS = """
    Screen {
        background: $surface;
    }

    .box {
        width: 40;
        height: 10;
        background: $primary;
        color: $text;
        border: solid $accent;
        padding: 2;
        margin: 1;
        content-align: center middle;
    }

    .box:hover {
        background: $primary-lighten-2;
        border: solid $accent-lighten-1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Hover over me!", classes="box")
        yield Footer()


# ============================================================================
# SELECTORS
# ============================================================================

class SelectorsDemo(App):
    """Demonstrates CSS selectors."""

    CSS = """
    /* Type selector */
    Button {
        margin: 1;
    }

    /* ID selector */
    #special {
        background: $success;
        color: white;
    }

    /* Class selector */
    .highlighted {
        border: thick $warning;
        background: $warning 20%;
    }

    /* Descendant selector */
    Container Button {
        width: 100%;
    }

    /* Child selector */
    Container > .direct-child {
        background: $accent 10%;
    }

    /* Pseudo-classes */
    Button:hover {
        background: $primary-lighten-1;
    }

    Button:focus {
        border: thick $accent;
    }

    Button:disabled {
        opacity: 50%;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        with Container():
            yield Button("Normal Button")
            yield Button("Special Button", id="special")
            yield Button("Highlighted", classes="highlighted")
            yield Static("Direct Child", classes="direct-child")
        yield Footer()


# ============================================================================
# COLORS AND THEMES
# ============================================================================

class ColorsDemo(App):
    """Demonstrates color system."""

    CSS = """
    .color-panel {
        height: 5;
        content-align: center middle;
        margin: 1;
        border: solid white;
    }

    /* Theme colors */
    .primary { background: $primary; }
    .secondary { background: $secondary; }
    .accent { background: $accent; }
    .success { background: $success; }
    .warning { background: $warning; }
    .error { background: $error; }

    /* Shades */
    .primary-dark { background: $primary-darken-3; }
    .primary-light { background: $primary-lighten-3; }

    /* RGB */
    .rgb { background: rgb(255, 100, 50); }

    /* Hex */
    .hex { background: #FF6347; }

    /* HSL */
    .hsl { background: hsl(120, 100%, 50%); }

    /* Transparency */
    .transparent { background: $primary 50%; }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("Theme Colors:")
        yield Static("Primary", classes="color-panel primary")
        yield Static("Accent", classes="color-panel accent")
        yield Static("Success", classes="color-panel success")
        yield Static("Warning", classes="color-panel warning")
        yield Static("Error", classes="color-panel error")

        yield Label("Shades:")
        yield Static("Dark", classes="color-panel primary-dark")
        yield Static("Light", classes="color-panel primary-light")
        yield Footer()


# ============================================================================
# BORDERS AND SPACING
# ============================================================================

class BordersSpacingDemo(App):
    """Demonstrates borders, padding, and margins."""

    CSS = """
    .box {
        width: 50%;
        height: auto;
        margin: 2;
    }

    /* Border styles */
    .solid { border: solid green; }
    .thick { border: thick blue; }
    .dashed { border: dashed red; }
    .double { border: double yellow; }
    .round { border: round magenta; }
    .heavy { border: heavy cyan; }

    /* Individual borders */
    .custom-borders {
        border-top: thick red;
        border-right: dashed blue;
        border-bottom: solid green;
        border-left: double yellow;
    }

    /* Padding and margin */
    .spaced {
        padding: 2 4;  /* vertical horizontal */
        margin: 1 2;
        border: solid $accent;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Solid Border", classes="box solid")
        yield Static("Thick Border", classes="box thick")
        yield Static("Round Border", classes="box round")
        yield Static("Custom Borders", classes="box custom-borders")
        yield Static("Padding & Margin", classes="box spaced")
        yield Footer()


# ============================================================================
# TEXT STYLING
# ============================================================================

class TextStylingDemo(App):
    """Demonstrates text styling."""

    CSS = """
    .text-box {
        width: 100%;
        height: auto;
        padding: 1;
        margin: 1;
        border: solid $primary;
    }

    .bold { text-style: bold; }
    .italic { text-style: italic; }
    .underline { text-style: underline; }
    .strike { text-style: strike; }

    .left { text-align: left; }
    .center { text-align: center; }
    .right { text-align: right; }
    .justify { text-align: justify; }

    .large {
        text-style: bold;
        color: $accent;
    }

    .muted {
        color: $text-muted;
        text-style: italic;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Bold Text", classes="text-box bold")
        yield Static("Italic Text", classes="text-box italic")
        yield Static("Center Aligned", classes="text-box center")
        yield Static("Large Accent Text", classes="text-box large")
        yield Static("Muted Text", classes="text-box muted")
        yield Footer()


# ============================================================================
# LAYOUT WITH CSS
# ============================================================================

class CSSLayoutDemo(App):
    """Demonstrates layout via CSS."""

    CSS = """
    .container {
        layout: horizontal;  /* or vertical, grid */
        background: $panel;
        padding: 1;
        height: auto;
    }

    .grid-container {
        layout: grid;
        grid-size: 3;
        grid-gutter: 1;
        padding: 1;
    }

    .item {
        background: $primary 20%;
        border: solid $primary;
        height: 5;
        content-align: center middle;
    }

    /* Alignment */
    .align-center {
        align: center middle;
    }

    .align-right {
        align: right top;
    }

    /* Sizing */
    .half-width { width: 50%; }
    .full-height { height: 100%; }
    .auto-height { height: auto; }
    """

    def compose(self) -> ComposeResult:
        yield Header()

        with Container(classes="container"):
            yield Static("1", classes="item")
            yield Static("2", classes="item")
            yield Static("3", classes="item")

        with Container(classes="grid-container"):
            for i in range(6):
                yield Static(str(i+1), classes="item")

        yield Footer()


# ============================================================================
# EXTERNAL STYLESHEET
# ============================================================================

class ExternalCSSDemo(App):
    """Demonstrates external stylesheet."""

    # Load CSS from external file
    CSS_PATH = "styles.tcss"  # Create this file separately

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Styles loaded from external file")
        yield Footer()


# ============================================================================
# RESPONSIVE DESIGN
# ============================================================================

class ResponsiveDemo(App):
    """Demonstrates responsive design patterns."""

    CSS = """
    .container {
        layout: grid;
        grid-size: 3;  /* 3 columns by default */
        grid-gutter: 1;
        padding: 1;
    }

    .card {
        background: $panel;
        border: round $primary;
        height: 10;
        padding: 1;
        content-align: center middle;
    }

    /* Adjust for narrow screens */
    @media (max-width: 80) {
        .container {
            grid-size: 2;  /* 2 columns */
        }
    }

    @media (max-width: 50) {
        .container {
            grid-size: 1;  /* 1 column */
        }
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        with Container(classes="container"):
            for i in range(6):
                yield Static(f"Card {i+1}", classes="card")
        yield Footer()


# ============================================================================
# HELPER FUNCTIONS AND REFERENCE
# ============================================================================

CSS_REFERENCE = """
TEXTUAL CSS (TCSS) REFERENCE
============================

SELECTORS:
  Type:        Button { }
  ID:          #my-button { }
  Class:       .my-class { }
  Descendant:  Container Button { }
  Child:       Container > Button { }
  Pseudo:      :hover, :focus, :disabled

COLORS:
  Theme:       $primary, $secondary, $accent
               $success, $warning, $error
               $surface, $panel, $background
  Shades:      $primary-lighten-1 to -3
               $primary-darken-1 to -3
  Formats:     #FF0000 (hex)
               rgb(255, 0, 0)
               hsl(0, 100%, 50%)
  Alpha:       $primary 50% (transparency)

BORDERS:
  Styles:      solid, thick, dashed, double
               round, heavy, none
  Sides:       border-top, border-right,
               border-bottom, border-left
  Syntax:      border: STYLE COLOR;

SPACING:
  Padding:     padding: 1;
               padding: 1 2; (v h)
               padding: 1 2 3 4; (t r b l)
  Margin:      margin: 1;
               margin: 1 2; (v h)

SIZING:
  Width:       width: 50; (cells)
               width: 50%; (percentage)
               width: 1fr; (fraction)
               width: auto;
  Height:      height: 10;
               height: auto;
  Min/Max:     min-width, max-width
               min-height, max-height

LAYOUT:
  Type:        layout: vertical | horizontal | grid;
  Grid:        grid-size: 3; (cols)
               grid-size: 3 2; (cols rows)
               grid-gutter: 1; (spacing)
  Dock:        dock: top | right | bottom | left;

TEXT:
  Style:       text-style: bold | italic | underline | strike
  Align:       text-align: left | center | right | justify
  Color:       color: $accent;

ALIGNMENT:
  Container:   align: horizontal vertical;
               align: center middle;
               align: right top;
  Content:     content-align: center middle;

DISPLAY:
  Visibility:  display: none; (hide)
               display: block; (show)
  Opacity:     opacity: 50%;

PSEUDO-CLASSES:
  :hover       Mouse over
  :focus       Has focus
  :disabled    Is disabled
  :enabled     Is enabled

BEST PRACTICES:
1. Use theme colors for consistency
2. External CSS for hot reload
3. Use classes for reusability
4. Keep specificity low
5. Use fr units for flexibility
6. Test on different terminal sizes
7. Use pseudo-classes for interactivity
"""


def create_stylesheet_template() -> str:
    """Create a template TCSS file."""
    return """/* Application Stylesheet */

/* Screen and containers */
Screen {
    background: $surface;
}

Container {
    background: $panel;
    padding: 1;
}

/* Buttons */
Button {
    margin: 1;
}

Button:hover {
    background: $primary-lighten-1;
}

Button.primary {
    background: $primary;
}

Button.danger {
    background: $error;
}

/* Cards */
.card {
    background: $panel;
    border: round $primary;
    padding: 2;
    margin: 1;
}

.card .title {
    text-style: bold;
    color: $accent;
}

/* Layouts */
.horizontal-layout {
    layout: horizontal;
    height: auto;
}

.grid-layout {
    layout: grid;
    grid-size: 3;
    grid-gutter: 1;
}

/* Utilities */
.hidden {
    display: none;
}

.text-center {
    text-align: center;
}

.text-muted {
    color: $text-muted;
}
"""


if __name__ == "__main__":
    app = ColorsDemo()
    app.run()
