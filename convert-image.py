from PIL import Image
import sys

def convert_png_to_jpg(png_file_path, jpg_file_path):
    with Image.open(png_file_path) as img:
        rgb_img = img.convert('RGB')
        rgb_img.save(jpg_file_path, 'JPEG')

if __name__ == "__main__":
    png_file_path = sys.argv[1]
    jpg_file_path = sys.argv[2]
    convert_png_to_jpg(png_file_path, jpg_file_path)
