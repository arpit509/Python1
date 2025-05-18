import os
import shutil

class FileOrganizer:
    def __init__(self, directory):  # <-- corrected __init_
        self.directory = directory
        self.file_types = {
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
            'Docs': ['.pdf', '.docx', '.doc', '.txt', '.xls', '.xlsx'],
            'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
            'Music': ['.mp3', '.wav', '.aac'],
        }

    def organize_files(self):
        try:
            for filename in os.listdir(self.directory):
                file_path = os.path.join(self.directory, filename)
                
                # Only process files, skip folders
                if os.path.isfile(file_path):
                    moved = False
                    for folder_name, extensions in self.file_types.items():
                        if any(filename.lower().endswith(ext) for ext in extensions):
                            self.move_file(file_path, folder_name, filename)
                            moved = True
                            break
                    if not moved:
                        self.move_file(file_path, 'Others', filename)
        except Exception as e:
            print(f"ERROR OCCURRED: {e}")

    def move_file(self, file_path, folder_name, filename):
        try:
            folder_path = os.path.join(self.directory, folder_name)
            
            # Create folder if it doesn't exist
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            shutil.move(file_path, os.path.join(folder_path, filename))
        except Exception as e:
            print(f"FAILED TO MOVE FILE {filename}: {e}")

organizer = FileOrganizer(r"D:\Projects\Wisper api")
organizer.organize_files()