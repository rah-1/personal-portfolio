import os
import sys

def rename_files_to_jpg(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)

    # Rename each file to have a .jpg extension
    for index, file_name in enumerate(files):
        # Construct the new file name with .jpg extension
        new_name = f"{os.path.splitext(file_name)[0]}.jpg"

        # Construct the full file paths
        old_file_path = os.path.join(folder_path, file_name)
        new_file_path = os.path.join(folder_path, new_name)

        # Rename the file
        os.rename(old_file_path, new_file_path)
        print(f'Renamed: {file_name} -> {new_name}')

if __name__ == "__main__":
    # Ensure the script is run with the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: python rename_files_to_jpg.py <folder_path>")
        sys.exit(1)

    # Get the folder path from the command-line argument
    folder_path = sys.argv[1]

    # Rename the files in the specified folder
    rename_files_to_jpg(folder_path)
