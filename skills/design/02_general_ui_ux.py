"""
Skill: General UI/UX Design Principles

This skill covers fundamental UI/UX design principles including
visual hierarchy, color theory, typography, layout, accessibility,
and best practices for 2025.
"""


# ============================================================================
# CORE UI/UX PRINCIPLES
# ============================================================================

CORE_UX_PRINCIPLES = """
CORE UI/UX DESIGN PRINCIPLES
============================

## 1. Clarity and Simplicity

The best UX designs prioritize clarity and simplicity.

**Guidelines:**
- Remove unnecessary elements
- Use clear, concise language
- One primary action per screen
- Clear visual hierarchy
- Obvious navigation

**Example:**
```
# Complex
[ Submit ] [ Cancel ] [ Save Draft ] [ Preview ] [ Reset ]

# Simple
[ Save ] [ Cancel ]
(Auto-saves drafts, preview available in menu)
```

## 2. Visual Hierarchy

Guide users' attention through visual hierarchy.

**Techniques:**
- **Size**: Larger elements draw attention
- **Color**: Bright/contrasting colors stand out
- **Position**: Top-left gets attention first (Western UX)
- **Spacing**: White space creates grouping
- **Typography**: Bold, italic, size variations

**Priority Levels:**
1. Primary action (largest, most prominent)
2. Secondary actions (medium prominence)
3. Tertiary actions (smallest, subtle)

## 3. Consistency

Maintain consistency across your interface.

**What to Keep Consistent:**
- Color scheme
- Typography (fonts, sizes, weights)
- Spacing and padding
- Button styles
- Icon style
- Terminology
- Interaction patterns

**Use Design Systems:**
- Create reusable components
- Document patterns
- Maintain component library
- Use design tokens

## 4. Feedback

Always provide feedback for user actions.

**Types of Feedback:**
- **Immediate**: Button press states, hover effects
- **Progress**: Loading indicators, progress bars
- **Completion**: Success messages, confirmations
- **Errors**: Clear error messages with solutions

**Examples:**
```
Loading:  ⏳ Loading data...
Success:  ✅ Changes saved successfully
Error:    ❌ Failed to save. Please check your connection.
```

## 5. User Control

Give users control over their experience.

**Guidelines:**
- Undo/redo functionality
- Confirmation for destructive actions
- Cancel option for operations
- Save drafts automatically
- Customizable preferences

## 6. Error Prevention

Design to prevent errors before they happen.

**Techniques:**
- Input validation
- Helpful constraints (date pickers vs text input)
- Disabled states for unavailable actions
- Clear labels and instructions
- Confirmation dialogs for dangerous actions

## 7. Recognition Over Recall

Make information visible rather than requiring memory.

**Bad (Recall):**
```
Enter the code from email sent on 2025-01-15
```

**Good (Recognition):**
```
We sent a 6-digit code to john@example.com
[ _ _ _ _ _ _ ]
Didn't receive it? Resend code
```

## 8. Flexibility and Efficiency

Support both novice and expert users.

**Techniques:**
- Keyboard shortcuts for power users
- Default workflows for beginners
- Customizable interfaces
- Advanced options hidden but accessible
- Multiple ways to accomplish tasks

## 9. Aesthetic and Minimalist Design

Every element should serve a purpose.

**Guidelines:**
- Remove decorative elements that don't add value
- Use white space effectively
- Limit color palette
- Consistent, clean layouts
- Focus on content

## 10. Help and Documentation

Provide accessible help when needed.

**Best Practices:**
- Contextual help (tooltips, hints)
- Searchable documentation
- Getting started guides
- FAQ sections
- Examples and tutorials
"""


# ============================================================================
# COLOR THEORY FOR UI/UX
# ============================================================================

COLOR_THEORY = """
COLOR THEORY FOR UI/UX DESIGN
=============================

## Color Harmonies

**1. Monochromatic**
- Single hue with varying shades/tints
- Creates cohesive, harmonious design
- Safe choice for beginners

Example: #1e3a8a → #3b82f6 → #93c5fd

**2. Analogous**
- Colors next to each other on color wheel
- Creates comfortable, pleasing combinations
- One dominant color, others support

Example: Blue → Blue-Green → Green

**3. Complementary**
- Opposite colors on color wheel
- High contrast, vibrant
- Use one as dominant, other as accent

Example: Blue (#0000ff) ↔ Orange (#ff8800)

**4. Triadic**
- Three colors evenly spaced on wheel
- Bold, vibrant
- Use one as primary, others as accents

Example: Red → Blue → Yellow

## Functional Color Palette

**Primary Color**
- Brand identity
- Main actions (primary buttons)
- Navigation highlights
- 1-2 shades

**Secondary Color**
- Supporting actions
- Variation in interface
- 1-2 shades

**Neutral Colors**
- Text (black, dark gray)
- Backgrounds (white, light gray)
- Borders, dividers
- 5-7 shades from light to dark

**Semantic Colors**
- Success: Green (#10b981)
- Warning: Yellow/Orange (#f59e0b)
- Error: Red (#ef4444)
- Info: Blue (#3b82f6)

## Accessibility: Contrast Ratios

**WCAG Standards:**

**Normal Text (< 18pt):**
- AA: 4.5:1 minimum
- AAA: 7:1 minimum

**Large Text (≥ 18pt or bold ≥ 14pt):**
- AA: 3:1 minimum
- AAA: 4.5:1 minimum

**Non-Text (icons, UI components):**
- AA: 3:1 minimum

**Tools:**
- WebAIM Contrast Checker
- Contrast Ratio Calculator
- Browser DevTools

## Color Usage Guidelines

**1. Never Use Color Alone**
Combine color with icons, text, or patterns.

Bad:  🟢 🔴
Good: ✅ Success    ❌ Error

**2. Limit Your Palette**
- 1-2 primary colors
- 1 secondary color
- 1 accent color
- Neutral scale
- Semantic colors

**3. Consider Color Blindness**
- 8% of men have color blindness
- Test with color blindness simulators
- Don't rely on red/green distinction alone
- Use patterns or icons as alternatives

**Types:**
- Deuteranopia (red-green, most common)
- Protanopia (red-green)
- Tritanopia (blue-yellow, rare)

**4. Dark Mode Considerations**
- Don't just invert colors
- Reduce contrast slightly (pure white on pure black is harsh)
- Use dark gray instead of pure black
- Test semantic colors in both modes

**Light Mode:**
- Background: #ffffff
- Text: #1f2937

**Dark Mode:**
- Background: #1f2937 (not #000000)
- Text: #f9fafb (not #ffffff)

## Color Psychology

**Red:**
- Emotion: Urgency, danger, passion
- Use: Errors, warnings, sales, CTAs
- Avoid: Large backgrounds (can be overwhelming)

**Blue:**
- Emotion: Trust, calm, professional
- Use: Primary actions, corporate brands
- Most universally liked color

**Green:**
- Emotion: Success, growth, nature
- Use: Success messages, eco-friendly, financial
- Safe, positive associations

**Yellow:**
- Emotion: Optimism, warning, energy
- Use: Warnings, highlights
- Hard to read in large amounts

**Orange:**
- Emotion: Friendly, energetic, affordable
- Use: CTAs, warnings, creative brands

**Purple:**
- Emotion: Luxury, creativity, wisdom
- Use: Premium products, creative tools

**Gray:**
- Emotion: Neutral, professional, sophisticated
- Use: Text, backgrounds, disabled states
"""


# ============================================================================
# TYPOGRAPHY PRINCIPLES
# ============================================================================

TYPOGRAPHY = """
TYPOGRAPHY FOR UI/UX
===================

## Type Scale

Create a consistent hierarchy with size.

**Example Scale (1.250 ratio - Major Third):**
- H1: 39px
- H2: 31px
- H3: 25px
- H4: 20px
- Body: 16px (base)
- Small: 13px
- Tiny: 10px

**Guidelines:**
- Base font size: 16px minimum for body text
- Line height: 1.5 for body text, 1.2 for headings
- Increase line height for narrow text
- Limit line length: 50-75 characters ideal

## Font Selection

**Maximum Fonts:**
- 2 font families maximum
- One for headings, one for body
- Or use different weights of same family

**Font Pairings:**
- Serif + Sans-serif (classic)
- Geometric + Humanist (modern)
- Display + Simple (dramatic)

**Web-Safe Fonts:**
- Sans-serif: Arial, Helvetica, Verdana
- Serif: Georgia, Times New Roman
- Monospace: Courier, Consolas

**Modern Web Fonts:**
- Google Fonts: Inter, Roboto, Open Sans
- System fonts: -apple-system, BlinkMacSystemFont

## Readability Guidelines

**1. Contrast**
- Minimum 4.5:1 for body text
- 7:1 for AAA compliance

**2. Font Size**
- Desktop: 16px minimum for body
- Mobile: 16px minimum (prevents zoom on iOS)
- Larger for older audiences

**3. Line Length**
- Desktop: 50-75 characters
- Mobile: 35-50 characters
- Use max-width to constrain

**4. Line Height**
- Body text: 1.5-1.75
- Headings: 1.2-1.3
- Increase for narrow text

**5. Font Weight**
- Body: 400 (regular)
- Emphasis: 600 (semi-bold) or 700 (bold)
- Avoid 300 (light) for small text

**6. Letter Spacing**
- Normal for body text
- Increase slightly for uppercase headings
- Reduce slightly for large headings

## Accessibility

**1. Avoid All Caps**
- Harder to read
- If needed, increase letter-spacing

**2. Sufficient Size**
- Never below 12px
- 16px minimum for body

**3. Adjustable Text**
- Users should be able to zoom 200%
- Design should still work

**4. Dyslexia-Friendly**
- Good line spacing
- Clear fonts (avoid decorative)
- Left-aligned (not justified)
- Adequate contrast
"""


# ============================================================================
# LAYOUT PRINCIPLES
# ============================================================================

LAYOUT_PRINCIPLES = """
LAYOUT DESIGN PRINCIPLES
========================

## The Grid System

**12-Column Grid** (most common)
- Divides page into 12 equal columns
- Flexible for different layouts
- Easy responsive breakpoints

**8-Point Grid**
- All spacing in multiples of 8px
- Creates visual rhythm
- Easier for developers

**Example Spacing Scale:**
- 4px (0.5 units)
- 8px (1 unit)
- 16px (2 units)
- 24px (3 units)
- 32px (4 units)
- 48px (6 units)
- 64px (8 units)

## White Space

**Benefits:**
- Improves readability
- Creates visual hierarchy
- Reduces cognitive load
- Appears more premium

**Guidelines:**
- More space around important elements
- Consistent spacing within groups
- Generous margins and padding
- Don't fear "empty" space

## Visual Weight and Balance

**Symmetrical Balance:**
- Elements evenly distributed
- Formal, stable feeling
- Good for professional interfaces

**Asymmetrical Balance:**
- Uneven but balanced
- More dynamic, interesting
- Good for creative interfaces

**Visual Weight Factors:**
- Size (larger = heavier)
- Color (bright = heavier)
- Position (top = heavier)
- Density (more elements = heavier)

## F and Z Patterns

**F-Pattern** (Content-heavy pages)
```
F F F F F F
F F F F
F F F
```
Users scan:
1. Horizontally across top
2. Down left side
3. Horizontally again (shorter)

**Z-Pattern** (Simple pages)
```
Z Z Z Z Z Z
    Z Z Z
  Z Z Z
Z Z Z Z Z Z
```
Users scan:
1. Top left to top right
2. Diagonal to bottom left
3. Bottom left to bottom right

**Implications:**
- Put important info top-left
- Put CTAs along the scan path
- Support natural reading patterns

## Mobile-First Design

**Process:**
1. Design for smallest screen first
2. Scale up for larger screens
3. Add complexity progressively

**Benefits:**
- Forces focus on essentials
- Better performance
- Easier to scale up than down

**Breakpoints (common):**
- Mobile: 0-639px
- Tablet: 640-1023px
- Desktop: 1024-1279px
- Large: 1280px+

## Responsive Patterns

**1. Column Drop**
- Stacks columns on small screens
- Side-by-side on large screens

**2. Mostly Fluid**
- Columns stay relative until very large
- Then max-width and center

**3. Layout Shifter**
- Different layouts for different sizes
- Most flexible, most work

**4. Off Canvas**
- Less frequent content off-screen
- Slide in when needed (navigation)
"""


# ============================================================================
# ACCESSIBILITY (A11Y) PRINCIPLES
# ============================================================================

ACCESSIBILITY = """
ACCESSIBILITY (A11Y) BEST PRACTICES 2025
========================================

## Legal Requirements

**United States:**
- ADA applies to websites/apps
- WCAG 2.1 AA is legal standard
- Lawsuits increased 14% in 2024

**Europe:**
- European Accessibility Act (2025)
- WCAG 2.1 AA compliance required

**International:**
- WCAG 2.1 (World Wide Web Consortium)
- Levels: A (minimum), AA (recommended), AAA (enhanced)

## WCAG Principles: POUR

**1. Perceivable**
Users must be able to perceive information.

- Text alternatives for images
- Captions for videos
- Sufficient color contrast
- Resizable text

**2. Operable**
Users must be able to operate interface.

- Keyboard navigation
- Sufficient time to complete tasks
- No seizure-inducing content
- Clear focus indicators

**3. Understandable**
Information must be understandable.

- Readable text
- Predictable behavior
- Input assistance and error prevention
- Consistent navigation

**4. Robust**
Content works with assistive technologies.

- Valid HTML
- Semantic markup
- ARIA attributes where needed
- Compatible with screen readers

## Color Contrast

**Requirements:**
- Normal text: 4.5:1 (AA), 7:1 (AAA)
- Large text: 3:1 (AA), 4.5:1 (AAA)
- UI components: 3:1

**Tools:**
- WebAIM Contrast Checker
- Chrome DevTools
- axe DevTools

**Examples:**
✅ Black (#000) on white (#fff) = 21:1
✅ Dark gray (#555) on white (#fff) = 8.6:1
❌ Light gray (#999) on white (#fff) = 2.8:1

## Keyboard Navigation

**Essential Shortcuts:**
- Tab: Move forward
- Shift+Tab: Move backward
- Enter/Space: Activate
- Esc: Close/cancel
- Arrow keys: Within component

**Requirements:**
- All interactive elements keyboard accessible
- Visible focus indicators
- Logical tab order
- Skip navigation links
- No keyboard traps

## Screen Readers

**Best Practices:**
- Semantic HTML (use correct elements)
- Alt text for images (describe function, not just content)
- ARIA labels for custom components
- Heading hierarchy (h1, h2, h3)
- Link text describes destination

**Bad:**
```html
<div onclick="submit()">Click here</div>
<img src="icon.png">
```

**Good:**
```html
<button type="submit">Submit form</button>
<img src="icon.png" alt="User profile icon">
```

## Forms Accessibility

**Guidelines:**
- Every input has a label
- Use label element (not just placeholder)
- Group related inputs with fieldset
- Provide clear error messages
- Indicate required fields
- Support autocomplete

**Example:**
```html
<label for="email">Email address *</label>
<input
  type="email"
  id="email"
  name="email"
  required
  aria-describedby="email-error"
  autocomplete="email"
>
<span id="email-error" role="alert">
  Please enter a valid email address
</span>
```

## ARIA (Accessible Rich Internet Applications)

**Common Attributes:**

**aria-label**: Label for element
```html
<button aria-label="Close dialog">×</button>
```

**aria-labelledby**: Reference to label
```html
<h2 id="dialog-title">Confirm Delete</h2>
<div role="dialog" aria-labelledby="dialog-title">
```

**aria-describedby**: Additional description
```html
<input aria-describedby="password-requirements">
<p id="password-requirements">Must be 8+ characters</p>
```

**role**: Define element type
```html
<div role="button" tabindex="0">Click me</div>
```

**aria-live**: Announce changes
```html
<div aria-live="polite" aria-atomic="true">
  3 new messages
</div>
```

## Touch Targets (Mobile)

**Minimum Size:**
- 44x44 pixels (iOS guideline)
- 48x48 pixels (Android guideline)
- Larger for users with motor impairments

**Spacing:**
- Minimum 8px between targets
- 16px+ recommended

## Motion and Animation

**Guidelines:**
- Respect prefers-reduced-motion
- No auto-playing videos with sound
- Pause/stop controls for moving content
- No flashing > 3 times per second

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}
```

## Testing Tools

**Automated:**
- axe DevTools
- WAVE
- Lighthouse
- Pa11y

**Manual:**
- Keyboard navigation test
- Screen reader test (NVDA, JAWS, VoiceOver)
- Zoom to 200%
- Color contrast check

**Note:** Automated tools catch only ~30% of issues.
Manual testing is essential.
"""


# ============================================================================
# NOTEBOOK INTERFACE DESIGN
# ============================================================================

NOTEBOOK_DESIGN = """
NOTEBOOK INTERFACE DESIGN PRINCIPLES
====================================

## Lessons from Jupyter vs Marimo

### Jupyter Notebooks Issues

**1. Hidden State Problem**
- Cells can execute in arbitrary order
- Variables can exist without visible code
- Deleting cell doesn't remove variables
- **Result:** 36% of notebooks non-reproducible

**2. Reproducibility Issues**
- No guaranteed execution order
- Dependency tracking manual
- State gets out of sync with code
- Hard to version control (JSON format)

**3. UI/UX Problems**
- Output/code can be far apart
- Unclear which cells have been run
- Difficult to navigate large notebooks
- Limited interactivity

### Marimo Solutions

**1. Reactive Execution**
- Automatic dependency tracking
- Cells run in deterministic order
- Deleting cell removes variables
- Always synchronized state

**2. Pure Python**
- Stored as .py files
- Git-friendly
- Can run as scripts
- Can import as modules

**3. Better UX**
- Interactive widgets auto-update
- Clear execution flow
- Built-in reactivity
- No hidden state

## Notebook Design Best Practices

**1. Code Organization**
```python
# Cell 1: Imports (always first)
import pandas as pd
import numpy as np

# Cell 2: Load data
df = pd.read_csv('data.csv')

# Cell 3: Process data
processed = df.groupby('category').sum()

# Cell 4: Visualize
plot = processed.plot()
```

**2. Visual Structure**
- Use markdown for sections
- Clear headings hierarchy
- Separate concerns into cells
- One logical operation per cell

**3. Interactivity**
- Widgets for parameters
- Reactive updates
- Clear input/output relationship
- Immediate feedback

**4. Documentation**
- Markdown cells for explanations
- Code comments for complex logic
- Examples for usage
- Clear variable names

**5. Data Exploration Flow**
```
1. Import data →
2. Explore (head, describe, info) →
3. Visualize distributions →
4. Clean/transform →
5. Analyze →
6. Export results
```

## Progressive Disclosure

**Start Simple, Add Complexity:**

**Level 1: Basic View**
```
# Simple controls
value = mo.ui.slider(0, 100, 50)
```

**Level 2: Additional Options**
```
# Show advanced button
if show_advanced:
    - Step size
    - Custom range
    - Multiple sliders
```

**Level 3: Expert Mode**
```
# Full customization
- Custom styling
- Complex interactions
- Programmatic control
```

## Error Handling in Notebooks

**1. Graceful Failures**
```python
try:
    data = load_data(url)
except Exception as e:
    mo.callout(
        mo.md(f"Failed to load data: {e}"),
        kind="danger"
    )
    data = None
```

**2. Validation**
```python
if file_upload.value:
    if file_upload.name().endswith('.csv'):
        # Process CSV
    else:
        mo.callout(
            mo.md("Please upload a CSV file"),
            kind="warn"
        )
```

**3. Helpful Messages**
```python
if df.empty:
    mo.callout(
        mo.md("""
        No data to display.

        Try:
        1. Upload a file above
        2. Check your filters
        3. Verify data source connection
        """),
        kind="info"
    )
```
"""


# ============================================================================
# UI/UX CHECKLIST
# ============================================================================

UX_CHECKLIST = """
UI/UX DESIGN CHECKLIST
=====================

## Visual Design
□ Consistent color palette
□ Sufficient contrast (4.5:1 minimum)
□ Clear visual hierarchy
□ Appropriate typography
□ Adequate white space
□ Aligned elements
□ Consistent spacing (8px grid)

## Usability
□ Clear navigation
□ Obvious primary actions
□ Helpful error messages
□ Loading indicators
□ Success confirmations
□ Undo functionality
□ Keyboard shortcuts

## Content
□ Clear, concise copy
□ Proper heading hierarchy
□ Scannable text (bullets, short paragraphs)
□ Descriptive link text
□ Alt text for images
□ Readable font size (16px+)

## Accessibility
□ WCAG 2.1 AA compliance
□ Keyboard navigation works
□ Screen reader tested
□ Color is not sole indicator
□ Focus indicators visible
□ Forms properly labeled
□ ARIA attributes where needed

## Responsive Design
□ Mobile-first approach
□ Tested on multiple screen sizes
□ Touch targets 44x44px minimum
□ Readable without zooming
□ No horizontal scrolling
□ Appropriate breakpoints

## Performance
□ Fast load times
□ Optimized images
□ Lazy loading where appropriate
□ Responsive feedback
□ No janky animations
□ Efficient rendering

## Forms
□ Clear labels
□ Inline validation
□ Helpful error messages
□ Logical tab order
□ Submit button clearly labeled
□ Required fields indicated
□ Autocomplete enabled

## Buttons & CTAs
□ Primary action is obvious
□ Descriptive button text
□ Appropriate size/spacing
□ Clear disabled state
□ Hover/focus states
□ Loading state during action

## Consistency
□ Design system in use
□ Reusable components
□ Consistent terminology
□ Predictable behavior
□ Standard patterns
□ Documented guidelines
"""

if __name__ == "__main__":
    print(CORE_UX_PRINCIPLES)
