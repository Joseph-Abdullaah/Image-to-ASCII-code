import os
from PIL import Image, UnidentifiedImageError


def checkFileExists(filePath):
    return os.path.exists(filePath)

def permissionCheck(filePath):
    try:
        with open(filePath, 'r'):
            pass
        return True
    except PermissionError:
        return False
    

def checkFileSupported(filePath):
    try:
        with Image.open(filePath) as img:
            img.verify() 

        img = Image.open(filePath)
        grayscale_img = img.convert("L")
        
        # Close the original image
        img.close()

        return grayscale_img
            
    except UnidentifiedImageError:
        return False
    except Exception as e:
        print(f"An error occurred: {e}") # Good to print the error for debugging
        return False


def resizeImage(image, targetWidth):
    if image is None:
        return None
    
    width, height = image.size
    # print(width, height)
    aspectRatio = height / width
    new_height = int(targetWidth * aspectRatio)

    resized_img = image.resize((targetWidth, new_height))

    return resized_img


def loadAndProcessImage(imagePath, target_width=100):
    """
    Main function to load, validate, and process image
    """
    # Step 1: Check if file exists
    if not checkFileExists(imagePath):
        print("Error: File does not exist.")
        return None
        
    # Step 2: Check read permission
    if not permissionCheck(imagePath):
        print("Error: Permission denied to read the file.")
        return None
    
    # Step 3: Check if supported and get grayscale image
    grayscale_image = checkFileSupported(imagePath)
    if grayscale_image is None:
        print("Error: Unsupported image format or corrupted file.")
        return None
    
    # Step 4: Resize the image for ASCII conversion
    processed_image = resizeImage(grayscale_image, target_width)
    
    return processed_image

def get_pixel_data(image):
    width = image.width
    height = image.height
    all_pixels = []
    for y in range(height):
        row = []
        for x in range(width):
            brightness = image.getpixel((x, y))
            row.append(brightness)
        all_pixels.append(row)
    return all_pixels



    