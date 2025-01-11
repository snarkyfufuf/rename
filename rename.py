import os

def rename_folders(directory):
    for root, dirs, _ in os.walk(directory, topdown=False):
        for dir_name in dirs:
            old_path = os.path.join(root, dir_name)
            if 'Blank-' in dir_name and old_path != directory:
                new_name = dir_name.replace('Blank-', '')
                new_path = os.path.join(root, new_name)
                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed folder: {old_path} to {new_path}")
                except PermissionError as e:
                    print(f"Permission error for {old_path}: {e}")
                except Exception as e:
                    print(f"Error renaming {old_path}: {e}")

if __name__ == "__main__":
    directory_path = os.path.expanduser("~/Desktop")
    rename_folders(directory_path)
