import os

def has_jfif_header(file_path):
    # Read the first 11 bytes of the file to check for JFIF header markers
    try:
        with open(file_path, 'rb') as f:
            header = f.read(11)
            return header.startswith(b'\xFF\xD8\xFF\xE0\x00\x10JFIF')
    except IOError:
        return False

def delete_corrupt_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if not has_jfif_header(file_path):
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except OSError as e:
                    print(f"Error deleting: {file_path}, Error: {e}")

if __name__ == "__main__":
    directory_to_check = "PetImages"

    # List of subdirectories to check
    subdirectories = ["Cat", "Dog"]

    for subdir in subdirectories:
        full_subdir_path = os.path.join(directory_to_check, subdir)
        if os.path.exists(full_subdir_path):
            print(f"Checking {subdir} directory...")
            delete_corrupt_files(full_subdir_path)
        else:
            print(f"{subdir} directory not found.")
