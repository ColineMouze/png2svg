import math


def pointy_hex_corner(center_x, center_y, size, i):
    angle_deg = 60 * i - 30 
    angle_rad = math.pi / 180 * angle_deg

    return (
        center_x + size * math.cos(angle_rad),
        center_y + size * math.sin(angle_rad),
    )


def hexagon_points(center_x, center_y, size):
    return [
        pointy_hex_corner(center_x, center_y, size, i)
        for i in range(6)
    ]