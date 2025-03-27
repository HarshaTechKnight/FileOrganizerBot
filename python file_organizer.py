import os
import shutil

def organize_files(folder_path):
    """
    Organizes files in the given folder by their extensions.
    Creates subfolders for each file type and moves files accordingly.
    """
    # Dictionary mapping file extensions to folder names
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
        'Documents': ['.pdf', '.docx', '.doc', '.xlsx', '.xls', '.pptx', '.ppt', '.txt', '.rtf'],
        'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv'],
        'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg'],
        'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz'],
        'Executables': ['.exe', '.msi', '.bat', '.sh'],
        'Code': ['.py', '.js', '.html', '.css', '.cpp', '.c', '.java', '.php', '.json'],
        'Data': ['.csv', '.xml', '.sql', '.db']
    }

    # Create folders if they don't exist
    for folder_name in file_types.keys():
        folder = os.path.join(folder_path, folder_name)
        if not os.path.exists(folder):
            os.makedirs(folder)

    # Get all files in the directory
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Move files to their respective folders
    for file in files:
        file_path = os.path.join(folder_path, file)
        file_ext = os.path.splitext(file)[1].lower()

        moved = False
        for folder_name, extensions in file_types.items():
            if file_ext in extensions:
                dest_folder = os.path.join(folder_path, folder_name)
                try:
                    shutil.move(file_path, dest_folder)
                    print(f"Moved {file} to {folder_name}")
                    moved = True
                    break
                except Exception as e:
                    print(f"Error moving {file}: {e}")

        # If file type not in dictionary, move to 'Others' folder
        if not moved:
            others_folder = os.path.join(folder_path, 'Others')
            if not os.path.exists(others_folder):
                os.makedirs(others_folder)
            try:
                shutil.move(file_path, others_folder)
                print(f"Moved {file} to Others")
            except Exception as e:
                print(f"Error moving {file}: {e}")

    print("File organization completed!")

if __name__ == "__main__":
    folder_to_organize = input("Enter the folder path to organize: ")
    if os.path.isdir(folder_to_organize):
        organize_files(folder_to_organize)
    else:
        print("Invalid folder path. Please try again.")