import os
import json

# Define the base directory for events
BASE_DIR = 'imgs/events'
OUTPUT_FILE = 'event-images.json'
IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.gif')

def generate_event_images_json():
    event_images = {}

    # Loop through each event directory
    if not os.path.exists(BASE_DIR):
        print(f"Error: Directory '{BASE_DIR}' does not exist.")
        return

    for event in os.listdir(BASE_DIR):
        event_path = os.path.join(BASE_DIR, event)

        if os.path.isdir(event_path):
            images = [
                img for img in os.listdir(event_path)
                if img.lower().endswith(IMAGE_EXTENSIONS)
            ]
            if images:
                event_images[event] = images

    # Write to JSON file
    with open(OUTPUT_FILE, 'w') as json_file:
        json.dump(event_images, json_file, indent=4)
    
    print(f"JSON file generated successfully: {OUTPUT_FILE}")

if __name__ == '__main__':
    generate_event_images_json()
