import os
import shutil

class FileOrganizer:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.file_types = {
            'Images': ['.jpg', '.jpeg', '.png',],
            'Docs': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.pptx'],
            'Videos': ['.mp4', '.mkv'],
            'Music': ['.mp3', '.wav'],
            'Others': []
        }

    def organize_files(self):
        try:
            files = os.listdir(self.folder_path)
        except FileNotFoundError:
            print("The specified folder does not exist.")
            return

        for file_name in files:
            full_path = os.path.join(self.folder_path, file_name)

            # Skip if it's a folder
            if os.path.isdir(full_path):
                continue

            file_extension = os.path.splitext(file_name)[1].lower()
            moved = False

            for folder, extensions in self.file_types.items():
                if file_extension in extensions:
                    self.move_file(file_name, folder)
                    moved = True
                    break

            if not moved:
                self.move_file(file_name, 'Others')

    def move_file(self, file_name, folder_name):
        destination_folder = os.path.join(self.folder_path, folder_name)

        # Create folder if it doesn't exist
        if not os.path.exists(destination_folder):
            try:
                os.makedirs(destination_folder)
                print(f"Created folder: {folder_name}")
            except Exception as e:
                print(f"Failed to create folder {folder_name}: {e}")
                return

        source = os.path.join(self.folder_path, file_name)
        destination = os.path.join(destination_folder, file_name)

        try:
            shutil.move(source, destination)
            print(f"Moved {file_name} to {folder_name}/")
        except Exception as e:
            print(f"Failed to move {file_name}: {e}")

# Example usage:
organizer = FileOrganizer(r"C:\Users\maury\OneDrive\Desktop\holofil report\Snake Report")
organizer.organize_files()
