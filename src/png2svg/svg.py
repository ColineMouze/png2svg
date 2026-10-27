def create_hexagon_svg (points, color):
    
    # Concatenate the points' coordinates, separating each point with a space
    points_text = " ".join(f"{x},{y}" for x, y in points) #Concatenate in a character string the points' coordinates
    
    # Convert the RGB color into a hexadecimal string
    color_hexagon = "#{:02x}{:02x}{:02x}".format(*color) #Convert RGB color into hex
    
    return f'<polygon points="{points_text}" fill="{color_hexagon}"/>'
