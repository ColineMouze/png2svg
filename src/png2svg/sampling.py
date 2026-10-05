def average_color (pixels):
    pixels = list(pixels)
    if not pixels :
        raise ValueError ("Cannot average an empty collection")
    number_of_pixels = len(pixels)
    R = sum(pixel[0] for pixel in pixels)//number_of_pixels
    G = sum(pixel[1] for pixel in pixels)//number_of_pixels
    B = sum(pixel[2] for pixel in pixels)//number_of_pixels
    return (R, G, B)