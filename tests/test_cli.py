from PIL import Image

from png2svg.cli import main


def test_cli_requires_arguments():
    try:
        main([])
    except SystemExit as error:
        assert error.code != 0

def test_cli_converts_png_to_svg(tmp_path):
    input_file = tmp_path / "input.png"
    output_file = tmp_path / "output.svg"

    image = Image.new("RGB", (20, 20), (255, 0, 0))
    image.save(input_file)

    main([
        str(input_file),
        str(output_file),
        "--hex-size",
        "5",
    ])

    assert output_file.exists()