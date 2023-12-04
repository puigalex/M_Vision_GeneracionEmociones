import os
import shutil

# Path to the file with image names and labels
file_path = "RAF-DB_basic_emotions/EmoLabel/list_partition_label.txt"
# Path to the folder containing the images
image_folder = "RAF-DB_basic_emotions_Image"

# Path to the folder where you want to move the images
destination_folder = "./new_folder"

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Read the file and move the images
with open(file_path, "r") as file:
    for line in file:
        # Split the line into image name and label (assuming they are separated by a space)
        image_name, label = line.strip().split()

        # Construct the source and destination paths
        source_path = os.path.join(image_folder, image_name)
        destination_path = os.path.join(destination_folder, image_name)

        # Move the image to the destination folder
        shutil.move(source_path, destination_path)

print("Images moved successfully.")