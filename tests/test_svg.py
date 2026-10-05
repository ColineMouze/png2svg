from png2svg.svg import create_hexagon_svg


def test_create_hexagon_svg():
    points = [(10,5), (15,10), (15,20), (10,25), (5,20), (5,10)]
    svg = create_hexagon_svg (points, (255,0,0))
    assert '<polygon' in svg
    assert 'fill="#ff0000"' in svg

def test_create_hexagon_svg_with_green():
    points=[(0,0), (10,0), (15,10), (10,20), (0,20), (-5,10)]
    svg = create_hexagon_svg(points, (0,255,0))
    assert 'fill="#00ff00"' in svg
    
