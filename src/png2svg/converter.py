from PIL import Image

from png2svg.geometry import hexagon_points
from png2svg.sampling import average_color
from png2svg.svg import create_hexagon_svg


def point_in_hexagon(x, y, center_x, center_y, size):
    """Return a boolean which determines if a point(x,y) belongs to an hexagon(center_x, center_y, size)"""
    dx = abs(x - center_x)
    dy = abs(y - center_y)

    if dx > size:
        return False

    if dy > (3**0.5) * size / 2:
        return False

    return (3**0.5) * dx + dy <= (3**0.5) * size


def convert_png_to_svg(input_filename, output_filename, hex_size):

    """
    Convert a PNG image into an SVG wallpaper using a hexagonal grid.

    Each hexagon is filled with the average color of the pixels
    located inside it.

    Args:
        input_filename (str): Path to the input PNG image.
        output_filename (str): Path where the generated SVG file will be saved.
        hex_size (float): Size of each hexagon, measured from its center
            to one of its vertices.

    Returns:
        None: The function writes the generated SVG content directly
        to the output file and does not return a value.
    """

    # Open the input PNG image an convert it to RGB
    # Each pixel will have 3 color components : red, green, blue
    image = Image.open(input_filename).convert("RGB")

    # Retrieve the image dimensions in pixels
    width, height = image.size

    # Create a list that will store all the SVG polygons
    svg_elements = []


    # Calculate the horizontal distance between 2 hexagons centers on the same row
    horizontal_spacing = (3**0.5)* hex_size

    # Calculate the vertical distance between 2 rows of hexagons
    vertical_spacing = 1.5 * hex_size


    # Keep track of the row number
    row = 0

    # Set the vertical coordinate of the hexagon centers on the current row
    center_y = 0


    # Iterate over the rows of hexagons until the image height is covered
    while center_y < height + hex_size:

        # By default, the first hexagon in a row has non horizontal offset
        center_x_offset = 0

        # Offset one row in two to create an hexagonal grid pattern
        if row % 2:
            center_x_offset = 0.5 * horizontal_spacing

        # Set the horizontal coordinate of the first hexagon center
        center_x = center_x_offset

        # Iterate over the hexagon centers until the image width is covered
        while center_x < width + hex_size:

            # Calculate the coordinate of the six vertices of the hexagon
            points = hexagon_points(center_x, center_y, hex_size,)

            # Create a list to store the RGB colors of the pixels
            pixels = []

            # Calculate the horizontal boundaries of the area to examine
            # Pixel coordinates must remain between 0 and width - 1
            min_x = max(0, int(center_x - hex_size))
            max_x = min(width - 1, int(center_x + hex_size))

            # Calculate the vertical boundaries of the area to examine (a regular hexagon's height is sqrt(3) multiplied by its size)
            # Pixel coordinates must remain between 0 and height - 1
            min_y = max(0, int(center_y - (3**0.5) * hex_size / 2))
            max_y = min(height - 1, int(center_y + (3**0.5) * hex_size / 2))

            # Iterate over the pixels inside the candidate rectangular area
            for pixel_x in range(min_x, max_x + 1):
                for pixel_y in range(min_y, max_y + 1):

                    # Check whether the current pixel belongs to the hexagon
                    if point_in_hexagon(pixel_x, pixel_y, center_x, center_y, hex_size):
                        # Add its RGB color to the list
                        pixels.append(image.getpixel((pixel_x, pixel_y)))

            # Continue only if at least one pixel was found
            if pixels:

                # Calculate the average RGB color of the sampled pixels
                color = average_color(pixels)

                # Create an SVG polygon using the hexagon's vertices and its average color, then store it in the list
                svg_elements.append(create_hexagon_svg(points, color))
        
            # Move horizontally to the next hexagon center
            center_x = center_x + horizontal_spacing

        # Move to the next row
        row = row + 1
        # Move down to the next row of hexagons
        center_y = center_y + vertical_spacing


    # Build the complete SVG document.
    # - xmlns specifies the SVG namespace.
    # - width and height define the document dimensions.
    # - viewBox defines the SVG coordinate system.
    # - The generated polygons are inserted between the SVG tags.
    svg_content = (
        f'<svg xmlns="http://www.w3.org/2000/svg" '
        f'width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}">\n'
        + "\n".join(svg_elements)
        + "\n</svg>"
    )

    # Open the output file in write mode.
    # If the file does not exist, it will be created.
    # If it already exists, its previous content will be overwritten.
    with open(output_filename, "w") as f:

        # Write the generated SVG content to the output file
        f.write(svg_content)