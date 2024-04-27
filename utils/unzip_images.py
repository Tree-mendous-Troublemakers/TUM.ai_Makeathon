import os
import shutil
import zipfile

def unzip_all_folders(directory, output_directory):
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)
    
    # Iterate through each file in the directory
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        
        # Check if the file is a zip folder
        if zipfile.is_zipfile(filepath):
            print(f"Extracting {filename}...")
            
            # Create a folder to extract the contents
            folder_name = os.path.splitext(filename)[0]  # Use the zip file name as the folder name
            folder_path = os.path.join(output_directory, folder_name)
            os.makedirs(folder_path, exist_ok=True)
            
            # Extract the contents of the zip folder
            with zipfile.ZipFile(filepath, 'r') as zip_ref:
                zip_ref.extractall(folder_path)
            
            print(f"{filename} extracted to {folder_path}")
        else:
            print(f"{filename} is not a zip folder. Skipping...")

# Specify the directory containing the zip folders
input_directory = "/Users/jamisonproctor/Documents/dev/TUM.ai_Makeathon/data/bronze_layer/SEN4AMA"

# Specify the directory where you want to save the unzipped folders
output_directory = "/Users/jamisonproctor/Documents/dev/TUM.ai_Makeathon/data/silver_layer/SEN4AMA"

# Unzip all folders in the specified directory
unzip_all_folders(input_directory, output_directory)
