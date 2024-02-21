from PIL import Image
import sys
import logging

logging.basicConfig(level=logging.INFO)

def convert_png_to_jpg(png_file_path, jpg_file_path):
    try:
        with Image.open(png_file_path) as img:
            rgb_img = img.convert('RGB')
            rgb_img.save(jpg_file_path, 'JPEG')
        logging.info("Image saved successfully!")
    except Exception as e:
        logging.error(f"Failed to convert the image: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        logging.error("Not enough command line arguments. Please provide both PNG and JPG file paths.")
    else:
        png_file_path = sys.argv[1]
        jpg_file_path = sys.argv[2]
        convert_png_to_jpg(png_file_path, jpg_file_path)
