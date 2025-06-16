from PIL import Image, ImageEnhance
import os

def gray_images(input_folder, output_folder):
    for filename in os.listdir(input_folder):
         if filename.endswith(".jpg") or filename.endswith(".png"):
            img = Image.open(os.path.join(input_folder, filename))
            gray_image = img.convert('L')
            enhancer = ImageEnhance.Contrast(gray_image)
            equalized_image = enhancer.enhance(1.5)
            equalized_image.save(os.path.join(output_folder, filename))

input_folder = "/path/to/your/input_folder"
output_folder = "/path/to/your/output_folder"
gray_images(input_folder, output_folder)


