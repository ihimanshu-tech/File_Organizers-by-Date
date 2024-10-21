import os
import shutil
from datetime import datetime

# Use raw strings or double backslashes to avoid escape sequence issues
source_directory = r'E:\PAPERS'  # Replace with the actual path to your files
destination_directory = r'E:\New_one'  # Replace with the actual destination path

# Ensure destination directory exists
os.makedirs(destination_directory, exist_ok=True)

# Iterate over files in the source directory
for filename in os.listdir(source_directory):
    file_path = os.path.join(source_directory, filename)
    
    # Skip if it's a directory
    if os.path.isdir(file_path):
        continue
    
    # Get the modification time of the file
    mod_time = os.path.getmtime(file_path)
    
    # Convert modification time to a date string (e.g., '2024-10-21')
    file_date = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d')
    
    # Create a folder with the file date if it doesn't exist
    date_folder = os.path.join(destination_directory, file_date)
    os.makedirs(date_folder, exist_ok=True)
    
    # Move the file to the date folder
    shutil.move(file_path, os.path.join(date_folder, filename))

print("Files have been organized by date.")
