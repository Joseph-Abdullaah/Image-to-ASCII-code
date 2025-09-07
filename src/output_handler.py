import os

def print_ascii(ascii_string):
    print(ascii_string)

def save_ascii_to_file(ascii_string, file_path="outputs/ascii_art.txt"):

    try:
        # Create the outputs directory if it doesn't exist
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Write to file with UTF-8 encoding to handle all characters
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(ascii_string)
        print(f"ASCII art successfully saved to: {file_path}")
        
    except Exception as e:
        print(f"Error saving file: {e}")

# Optional: Combined function that does both
def handle_output(ascii_string, save_to_file=False, file_path="outputs/ascii_art.txt"):
    
    print_ascii(ascii_string)
    
    if save_to_file:
        save_ascii_to_file(ascii_string, file_path)