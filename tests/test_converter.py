from PIL import Image

from png2svg.converter import convert_png_to_svg, point_in_hexagon


def test_point_in_hexagon():
    assert point_in_hexagon(10, 10, 10, 10, 5)


def test_point_outside_hexagon():
    assert not point_in_hexagon(20, 20, 10, 10, 5)


def test_convert_png_to_svg(tmp_path):
    input_file = tmp_path / "input.png"
    output_file = tmp_path / "output.svg"

    image = Image.new("RGB", (20, 20), (255, 0, 0))
    image.save(input_file)

    convert_png_to_svg(input_file, output_file, hex_size=5)

    assert output_file.exists()