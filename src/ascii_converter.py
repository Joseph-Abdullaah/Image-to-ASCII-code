import src.image_processor as image_processor

def pixels_to_ascii(pixel_value, ascii_chars):
    ascii_art = []

    for row in pixel_value:
        ascii_row = []
        for pixel in row:
            normalized_value = pixel / 255
            char_index = int(normalized_value * (len(ascii_chars)- 1))
            ascii_char = ascii_chars[char_index]
            ascii_row.append(ascii_char)
        ascii_art.append(ascii_row)
    return ascii_art



def assemble_ascii_string(ascii_grid):
    ascii_lines = []

    for row in ascii_grid:
        line = " ".join(row)
        ascii_lines.append(line)

    ascii_art_string = "\n".join(ascii_lines)
    return ascii_art_string