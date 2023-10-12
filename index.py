from PIL import Image
import os


def convert_png_to_webp(input_folder, output_folder):

    # Create an output folder if it doesn't exist already
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.png'):
            input_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + '.webp'
            output_path = os.path.join(output_folder, output_filename)

            try:
                image = Image.open(input_path)
                image.save(output_path, 'webp')
                print(f'Converted {filename} to WebP')
            except Exception as e:
                print(f'Error converting {filename}: {str(e)}')


if __name__ == "__main__":
    input_folder = 'input_images'
    output_folder = 'output_images'

    convert_png_to_webp(input_folder, output_folder)  # call
