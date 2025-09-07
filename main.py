# main.py
import os
from src.image_processor import loadAndProcessImage, get_pixel_data
from src.ascii_converter import pixels_to_ascii, assemble_ascii_string
from src.output_handler import print_ascii, save_ascii_to_file

def main():
    # Configuration
    # Prompt user for image path (use default if blank)
    image_path = input("Enter the path to the image file (press Enter for default 'images/friends.jpg'): ").strip()
    if not image_path:
        image_path = "images/friends.jpg"
    elif not os.path.isfile(image_path):
        print("File does not exist. Using default image path.")
        image_path = "images/friends.jpg"

    # Prompt user for target width (use default if blank)
    target_width_input = input("Enter the target width for ASCII conversion (press Enter for default 900): ").strip()
    if not target_width_input:
        target_width = 900
    else:
        try:
            target_width = int(target_width_input)
            if target_width <= 0:
                print("Width must be a positive integer. Using default 900.")
                target_width = 900
        except ValueError:
            print("Invalid input. Using default width 900.")
            target_width = 900

    output_path = "outputs/ascii_art.txt"
    # ascii paltette from darkest to lightest
    ascii_palette = "@%#*+=-:. " 
    
    # Process the image
    print("Processing image...")
    processed_image = loadAndProcessImage(image_path, target_width=target_width)

    if not processed_image:
        print("Failed to process image. Exiting.")
        return
    
    # Convert to ASCII
    print("Converting to ASCII...")
    pixel_data = get_pixel_data(processed_image)
    ascii_grid = pixels_to_ascii(pixel_data, ascii_palette)
    ascii_art = assemble_ascii_string(ascii_grid)
    
    # Output the result
    print("\n" + "="*50)
    print_ascii(ascii_art)
    print("="*50)
    
    # Save to file
    try:
        save_ascii_to_file(ascii_art, output_path)
    except Exception as e:
        print(f"Warning: Could not save file: {e}")

if __name__ == "__main__":
    main()