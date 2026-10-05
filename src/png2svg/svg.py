def create_hexagon_svg (points, color):
    points_text = "".join(f"{x},{y}" for x, y in points) #Concatenate in a character string the points' coordinates
    color_hexagon = "#{:02x}{:02x}{:02x}".format(*color) #Convert RGB color into hex
    return f'<polygon points="{points_text}" fill="{color_hexagon}"/>'
