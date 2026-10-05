from png2svg.sampling import average_color


def test_average_color():
    pixels=[(255,0,0), (0,255,0), (0,0,255)]
    assert average_color(pixels)==(85,85,85)
