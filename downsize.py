import os
from PIL import Image

def downsize_images_in_directory(directory_path, new_width, quality=30):
    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        
        if filename.lower().endswith(('jpg', 'jpeg', 'png', 'bmp', 'gif')):
            try:
                img = Image.open(file_path)
                width_percent = (new_width / float(img.size[0]))
                new_height = int((float(img.size[1]) * float(width_percent)))

                img = img.resize((new_width, new_height), Image.LANCZOS)

                img.save(file_path, quality=quality)
                print(f"Downsized image: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

directory_path = 'imgs/events/event3'
downsize_images_in_directory(directory_path, new_width=800, quality=80)
