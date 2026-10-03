from png2svg.geometry import hexagon_points


def test_hexagon_has_six_points():
    points = hexagon_points(10, 10, 5)

    assert len(points) == 6
