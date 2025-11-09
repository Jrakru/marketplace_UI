"""
Marimo Notebook Generator

Helper script for AI agents to generate marimo notebooks programmatically.
Follows Anthropic's agent skill best practices.
"""

from typing import List, Dict, Any, Optional
from dataclasses import dataclass


@dataclass
class MarimoCell:
    """Represents a marimo cell with code and optional dependencies."""
    code: str
    dependencies: List[str] = None
    returns: List[str] = None

    def __post_init__(self):
        if self.dependencies is None:
            self.dependencies = []
        if self.returns is None:
            self.returns = []


class MarimoNotebookGenerator:
    """Generate marimo notebooks programmatically."""

    def __init__(self, version: str = "0.10.11"):
        self.version = version
        self.cells: List[MarimoCell] = []

    def add_imports_cell(self, imports: List[str]) -> 'MarimoNotebookGenerator':
        """Add a cell with imports (typically the first cell)."""
        import_code = "\n".join(imports)
        # Extract module names for returns
        returns = []
        for imp in imports:
            if "import" in imp:
                if " as " in imp:
                    # import marimo as mo
                    returns.append(imp.split(" as ")[-1].strip())
                else:
                    # import pandas
                    parts = imp.split()
                    if "from" in parts:
                        # from X import Y
                        idx = parts.index("import") + 1
                        returns.extend([p.strip(",") for p in parts[idx:]])
                    else:
                        # import X
                        idx = parts.index("import") + 1
                        returns.append(parts[idx].split(".")[0])

        self.cells.append(MarimoCell(
            code=import_code,
            dependencies=[],
            returns=returns
        ))
        return self

    def add_cell(self, code: str, dependencies: List[str] = None,
                 returns: List[str] = None) -> 'MarimoNotebookGenerator':
        """Add a custom cell."""
        self.cells.append(MarimoCell(
            code=code,
            dependencies=dependencies or [],
            returns=returns or []
        ))
        return self

    def add_markdown_cell(self, markdown: str, dependencies: List[str] = None) -> 'MarimoNotebookGenerator':
        """Add a markdown cell."""
        # Escape quotes in markdown
        markdown_escaped = markdown.replace('"""', '\\"\\"\\"')
        code = f'mo.md(\n    """\n{markdown}\n    """\n)'
        self.cells.append(MarimoCell(
            code=code,
            dependencies=dependencies or ["mo"],
            returns=[]
        ))
        return self

    def add_widget_cell(self, widget_name: str, widget_type: str,
                       **widget_params) -> 'MarimoNotebookGenerator':
        """Add a UI widget cell."""
        params = ", ".join([f"{k}={repr(v)}" for k, v in widget_params.items()])
        code = f'{widget_name} = mo.ui.{widget_type}({params})\n{widget_name}'
        self.cells.append(MarimoCell(
            code=code,
            dependencies=["mo"],
            returns=[widget_name]
        ))
        return self

    def add_layout_cell(self, layout_type: str, items: List[str],
                       **layout_params) -> 'MarimoNotebookGenerator':
        """Add a layout cell (hstack, vstack, etc.)."""
        params = ", ".join([f"{k}={repr(v)}" for k, v in layout_params.items()])
        items_str = ", ".join(items)
        if params:
            code = f'mo.{layout_type}([{items_str}], {params})'
        else:
            code = f'mo.{layout_type}([{items_str}])'

        self.cells.append(MarimoCell(
            code=code,
            dependencies=["mo"] + items,
            returns=[]
        ))
        return self

    def generate(self) -> str:
        """Generate the complete marimo notebook code."""
        lines = [
            'import marimo',
            '',
            f'__generated_with = "{self.version}"',
            'app = marimo.App()',
            ''
        ]

        for cell in self.cells:
            lines.append('@app.cell')

            # Generate function signature
            if cell.dependencies:
                deps = ", ".join(cell.dependencies)
                lines.append(f'def __({deps}):')
            else:
                lines.append('def __():')

            # Add cell code (indented)
            for code_line in cell.code.split('\n'):
                lines.append(f'    {code_line}')

            # Add return statement
            if cell.returns:
                returns = ", ".join(cell.returns)
                lines.append(f'    return {returns},')
            else:
                lines.append('    return')

            lines.append('')

        # Add main block
        lines.extend([
            '',
            'if __name__ == "__main__":',
            '    app.run()'
        ])

        return '\n'.join(lines)

    def save(self, filename: str) -> None:
        """Save the notebook to a file."""
        with open(filename, 'w') as f:
            f.write(self.generate())


# ============================================================================
# TEMPLATE GENERATORS
# ============================================================================

def create_basic_notebook(title: str = "My Notebook") -> str:
    """Create a basic marimo notebook template."""
    gen = MarimoNotebookGenerator()
    gen.add_imports_cell(["import marimo as mo"])
    gen.add_markdown_cell(f"# {title}\n\nYour reactive notebook starts here.")
    gen.add_markdown_cell("Add your code below:")
    return gen.generate()


def create_data_analysis_notebook(dataset_name: str = "data") -> str:
    """Create a data analysis notebook template."""
    gen = MarimoNotebookGenerator()
    gen.add_imports_cell([
        "import marimo as mo",
        "import pandas as pd",
        "import numpy as np",
        "import matplotlib.pyplot as plt"
    ])
    gen.add_markdown_cell("# Data Analysis\n\nAnalyzing dataset: " + dataset_name)

    # Data loading cell
    gen.add_cell(
        f"# Load your data\ndf = pd.read_csv('{dataset_name}.csv')\ndf.head()",
        dependencies=["pd"],
        returns=["df"]
    )

    # Data exploration widget
    gen.add_widget_cell(
        "column_selector",
        "dropdown",
        options=["col1", "col2", "col3"],
        value="col1",
        label="Select column to visualize"
    )

    # Visualization cell
    gen.add_cell(
        """fig, ax = plt.subplots()
ax.hist(df[column_selector.value], bins=30)
ax.set_title(f'Distribution of {column_selector.value}')
mo.mpl.interactive(fig)""",
        dependencies=["df", "column_selector", "plt", "mo"],
        returns=["fig", "ax"]
    )

    return gen.generate()


def create_dashboard_notebook(title: str = "Dashboard") -> str:
    """Create an interactive dashboard template."""
    gen = MarimoNotebookGenerator()
    gen.add_imports_cell([
        "import marimo as mo",
        "import pandas as pd",
        "import plotly.express as px"
    ])
    gen.add_markdown_cell(f"# {title}\n\nInteractive dashboard with controls")

    # Controls
    gen.add_markdown_cell("## Controls")
    gen.add_widget_cell(
        "date_range",
        "date",
        value="2025-01-01",
        label="Start Date"
    )
    gen.add_widget_cell(
        "refresh_btn",
        "button",
        label="Refresh Data",
        kind="success"
    )

    # Layout controls
    gen.add_layout_cell(
        "hstack",
        ["date_range", "refresh_btn"],
        gap=2
    )

    # Data display
    gen.add_markdown_cell("## Data", dependencies=["mo"])

    return gen.generate()


# ============================================================================
# COMMON PATTERNS
# ============================================================================

PATTERNS = {
    "reactive_counter": """
@app.cell
def __(mo):
    increment = mo.ui.button(label="+", value=0)
    decrement = mo.ui.button(label="-", value=0)
    mo.hstack([decrement, increment])
    return increment, decrement

@app.cell
def __(increment, decrement):
    count = increment.value - decrement.value
    return count,

@app.cell
def __(mo, count):
    mo.md(f"## Count: {count}")
    return
""",

    "data_explorer": """
@app.cell
def __(mo):
    file_upload = mo.ui.file(filetypes=[".csv"], label="Upload CSV")
    file_upload
    return file_upload,

@app.cell
def __(pd, file_upload):
    if file_upload.value:
        df = pd.read_csv(file_upload.contents())
    else:
        df = None
    return df,

@app.cell
def __(mo, df):
    if df is not None:
        explorer = mo.ui.dataframe(df)
        explorer
    else:
        mo.md("Upload a CSV file to explore")
    return
""",

    "form_with_validation": """
@app.cell
def __(mo):
    form = mo.ui.form({
        "name": mo.ui.text(placeholder="Your name", required=True),
        "email": mo.ui.text(placeholder="Email", required=True),
        "age": mo.ui.number(start=0, stop=120, value=25),
        "subscribe": mo.ui.checkbox(label="Subscribe to updates")
    })
    form
    return form,

@app.cell
def __(mo, form):
    if form.value:
        # Validation
        if "@" not in form.value.get("email", ""):
            mo.callout(mo.md("Invalid email address"), kind="danger")
        else:
            mo.callout(
                mo.md(f"✅ Form submitted for {form.value['name']}"),
                kind="success"
            )
    return
"""
}


def get_pattern(pattern_name: str) -> str:
    """Get a code pattern by name."""
    return PATTERNS.get(pattern_name, "")


if __name__ == "__main__":
    # Example usage
    print("=== Basic Notebook ===")
    print(create_basic_notebook("Test Notebook"))
    print("\n=== Data Analysis Notebook ===")
    print(create_data_analysis_notebook("my_data"))
