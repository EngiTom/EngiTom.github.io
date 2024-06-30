from PIL import Image
import os

def resize_images(input_folder, target_width=500):
    # Loop through all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            # Load the image
            input_path = os.path.join(input_folder, filename)
            img = Image.open(input_path)

            # Calculate the new height while maintaining aspect ratio
            ratio = target_width / float(img.size[0])
            target_height = int(float(img.size[1]) * float(ratio))

            # Resize the image
            resized_img = img.resize((target_width, target_height), Image.ANTIALIAS)

            # Save the resized image to the original file
            resized_img.save(input_path)
            
            print(f"Resized {filename} and replaced the original file")

if __name__ == "__main__":
    current_directory = "/Users/7zh/blogEngitom/EngiTom.github.io/assets/images/teasers"
    input_folder = current_directory  # Use the current directory as the input folder

    resize_images(input_folder)
