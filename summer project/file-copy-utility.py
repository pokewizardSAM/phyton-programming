import os
import shutil

# Specify the path of the master directory
master_dir_path = "D:\Preset"

# Get the list of all folders inside the master directory
folders = [f.path for f in os.scandir(master_dir_path) if f.is_dir()]

# Iterate through each folder
for folder_path in folders:

    # Get the name of the folder
    folder_name = os.path.basename(folder_path)

    # Get the path of the file inside the folder
    file_path = os.path.join(folder_path, os.listdir(folder_path)[0])

    # Rename the file with the folder name
    new_file_name = folder_name + os.path.splitext(file_path)[1]
    new_file_path = os.path.join(master_dir_path, new_file_name)

    # Copy the file to the master directory with the new name
    shutil.copy(file_path, new_file_path)
