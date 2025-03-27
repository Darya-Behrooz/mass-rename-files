import os

# Folder path
folder_path = r"" # EDIT: DIRECTORY

# Select all files
files = os.listdir(folder_path)

# Filter file type
file_type = [f for f in files if f.endswith(".mkv")] # EDIT: EXTENSION

# Rename files loop
for i , file_type in enumerate(sorted(file_type) , start = 1):
    
    # Define new name format
    new_name = f"Episode {i}.mkv" # EDIT: NEW NAME
    
    # Rename files
    old_file = os.path.join(folder_path , file_type)
    new_file = os.path.join(folder_path , new_name)
    
    os.rename(old_file , new_file)

print("Renaming completed!")