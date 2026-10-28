import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import tempfile
    from pathlib import Path

    import marimo as mo

    from png2svg.converter import convert_png_to_svg

    return Path, convert_png_to_svg, mo, tempfile


@app.cell
def _(mo):
    # Display the notebook title and instructions

    mo.md("""
    # PNG to SVG Converter

    Convert a PNG image into an SVG image composed of colored hexagons.

    ## How to use this application

    1. **Select a PNG image** from your computer.
    2. **Choose the hexagon size** using the slider.
    3. **Click Convert image** to start the conversion.
    4. **Download the generated SVG file**.

    ---
    *Adjust the hexagon size to change the level of detail in the result.*
    """)
    return


@app.cell
def _(mo):
    # Create a file selector restricted to PNG images
    image_file = mo.ui.file(
        filetypes=[".png"],
        label="Select a PNG image",
        multiple=False,
    )

    # Display the file selector
    mo.vstack([
        mo.md("### 1. Select a PNG image"),
        image_file,
    ])
    return (image_file,)


@app.cell
def _(mo):
    # Create a slider to control the hexagon size
    hex_size = mo.ui.slider(
        start=1,
        stop=30,
        step=1,
        value=5,
        label="Hexagon size",
    )

    # Display the slider
    mo.vstack([
        mo.md("### 2. Choose the hexagon size"),
        hex_size,
    ])
    return (hex_size,)


@app.cell
def _(mo):
    # Create a button to start the conversion
    convert_button = mo.ui.run_button(
        label="Convert image",
    )

    # Display the conversion button
    mo.vstack([
        mo.md("### 3. Convert the image"),
        convert_button,
    ])
    return (convert_button,)


@app.cell
def _(
    Path,
    convert_button,
    convert_png_to_svg,
    hex_size,
    image_file,
    mo,
    tempfile,
):
    # Convert the selected PNG image into an SVG file

    result = mo.md("Select a PNG image and click **Convert image** to begin.")

    if convert_button.value and image_file.value:

        # Get the uploaded image
        uploaded_file = image_file.value[0]

        # Create temporary paths for the input and output files
        with tempfile.TemporaryDirectory() as temporary_directory:
            input_path = Path(temporary_directory) / uploaded_file.name
            output_path = Path(temporary_directory) / "converted.svg"

            # Save the uploaded PNG image
            input_path.write_bytes(uploaded_file.contents)

            # Convert the PNG image into SVG
            convert_png_to_svg(
                str(input_path),
                str(output_path),
                hex_size=hex_size.value,
            )

            # Read the generated SVG before the temporary directory is deleted
            svg_bytes = output_path.read_bytes()

        # Create a download button for the SVG file
        result = mo.download(
            data=svg_bytes,
            filename="converted.svg",
            mimetype="image/svg+xml",
            label="Download SVG",
        )

    # Display the instructions or the download button
    result
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
