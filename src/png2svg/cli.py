import argparse

from png2svg.converter import convert_png_to_svg


def main(args=None):
    parser = argparse.ArgumentParser(description="Convert a PNG image into an SVG wallpaper.")

    parser.add_argument("input", help="Input PNG file")

    parser.add_argument("output", help="Output SVG file")

    parser.add_argument("--hex-size", type=int, default=10, help="Size of the hexagons")

    parsed_args = parser.parse_args(args)

    convert_png_to_svg(
        parsed_args.input,
        parsed_args.output,
        hex_size=parsed_args.hex_size,
    )
