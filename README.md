# PNG to SVG Converter

A Python application that converts PNG images into SVG images composed of colored hexagons.

The application samples the colors of an input image and represents them as a hexagonal grid, creating a geometric mosaic effect.

## Features

- Convert PNG images into SVG files.
- Represent the image using a hexagonal grid.
- Sample pixel colors and calculate representative colors for the hexagons.
- Adjust the hexagon size using command-line parameters.
- Use an interactive Marimo notebook to convert images.
- Run automated tests with pytest.
- Check code quality with Ruff.

## Requirements

- Python (compatible with the version specified in `pyproject.toml`)
- [uv](https://docs.astral.sh/uv/)
- A PNG image to convert

## Installation

Clone the repository and navigate to the project directory:

```bash
git clone <YOUR_REPOSITORY_URL>
cd png2svg
```

Install the project dependencies:

```bash
uv sync
```

Replace `<YOUR_REPOSITORY_URL>` with the URL of your GitHub repository.

## Command-line usage

Convert a PNG image into an SVG file:

```bash
uv run png2svg input.png output.svg
```

Adjust the hexagon size:

```bash
uv run png2svg input.png output.svg --hex-size 15
```

Replace `input.png` with the path to your input image and `output.svg` with the desired output path.

The available options depend on the arguments implemented by the CLI. Run the following command to inspect them:

```bash
uv run png2svg --help
```

## Interactive notebook

The project includes an interactive notebook built with Marimo.

Launch the notebook from the project root:

```bash
uv run marimo edit notebooks/png2svg_app.py
```

The notebook opens in your browser.

### How to use the notebook

1. Select a PNG image from your computer.
2. Choose the hexagon size.
3. Click **Convert image**.
4. Click **Download SVG** to save the generated file.

The notebook uses the existing `png2svg` conversion library.

## Tests

Run the automated test suite:

```bash
uv run pytest
```

## Code quality

Check the code with Ruff:

```bash
uv run ruff check .
```

## Project structure

```text
png2svg/
├── .github/
│   └── workflows/
├── notebooks/
│   └── png2svg_app.py
├── src/
│   └── png2svg/
│       ├── __init__.py
│       ├── geometry.py
│       ├── sampling.py
│       ├── svg.py
│       ├── converter.py
│       └── cli.py
├── tests/
├── README.md
├── pyproject.toml
└── uv.lock
```

## Technologies

- Python
- Pillow (PIL)
- uv
- pytest
- Ruff
- Marimo

## License

Add the project's license information here if a license has been chosen.
