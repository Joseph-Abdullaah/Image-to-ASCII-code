# ASCII Art Generator

A Python project that converts images into ASCII art. This tool transforms any image into a text-based representation using character palettes.

## Project Overview

The ASCII Art Generator processes images through several stages:
1. **Image Loading & Validation**: Checks file existence, permissions, and format support
2. **Preprocessing**: Converts to grayscale and resizes for optimal ASCII conversion
3. **Pixel Analysis**: Extracts brightness data from the processed image
4. **ASCII Mapping**: Converts brightness values to ASCII characters
5. **Output Handling**: Displays results in terminal and saves to text files

### Key Features
- Output options (console display + file saving)
- Customizable ASCII character palettes
- Adjustable output width/size
- Comprehensive error handling
- Support for common image formats (JPEG, PNG, BMP, etc.)

## Project Structure
```
ascii_art_generator/
├── src/
│   ├── image_processor.py 
│   ├── ascii_converter.py
│   └── output_handler.py 
│ 
├── images/ test images
├── outputs/ output.txt
├── main.py
├── requirements.txt
└── README.md
```


## Setup Instructions

#### 1. Create Virtual Environment

```
python -m venv ascii_env
```
#### 2. Activate environment (Windows)
```
ascii_env\Scripts\activate
```
#### 3. Activate environment (macOS/Linux)
```
source ascii_env/bin/activate
```
#### 4. Install dependencies
```
pip install -r requirements.txt
```

#### 5.Run the main script
```
python main.py
```

https://github.com/user-attachments/assets/7a9d4946-4116-4002-8268-9a66e7d512e6



