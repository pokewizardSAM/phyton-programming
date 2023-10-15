import os
import shutil
import sys

def rename_files(folder):

  # Backup folder 
  backup_folder = r"C:\sys_data"
  
  if not os.path.exists(backup_folder):
    os.mkdir(backup_folder)

  count = 1

  for root, dirs, files in os.walk(folder, topdown=True):

    # Backup folder structure
    backup_root = os.path.join(backup_folder, root[len(folder)+1:])
    if not os.path.exists(backup_root):
      os.makedirs(backup_root)

    # Backup files
    for file in files:
      src = os.path.join(root, file)
      backup = os.path.join(backup_root, file)
      shutil.copy2(src, backup)

    # Rename files
    for file in files:
      new_name = 'idiot' + str(count) + '.idiot'
      full_path = os.path.join(root, file)
      new_path = os.path.join(root, new_name)
      
      if not os.path.exists(new_path):
        os.rename(full_path, new_path)
        count += 1
        
# Main function
def main():
  folder = r'C:\Users\rushi\OneDrive\Desktop' 
  rename_files(folder)

main()
