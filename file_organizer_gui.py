import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class FileOrganizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Organizer Bot")
        self.root.geometry("500x400")
        
        # Create GUI elements
        self.create_widgets()
        
    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="File Organizer Bot", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)
        
        # Description
        desc_label = tk.Label(self.root, text="Organize files by type into subfolders", font=("Arial", 10))
        desc_label.pack(pady=5)
        
        # Folder selection
        folder_frame = tk.Frame(self.root)
        folder_frame.pack(pady=20, padx=20, fill=tk.X)
        
        self.folder_path = tk.StringVar()
        folder_entry = tk.Entry(folder_frame, textvariable=self.folder_path, width=40)
        folder_entry.pack(side=tk.LEFT, padx=5)
        
        browse_btn = tk.Button(folder_frame, text="Browse", command=self.browse_folder)
        browse_btn.pack(side=tk.LEFT)
        
        # Progress bar
        self.progress = ttk.Progressbar(self.root, orient=tk.HORIZONTAL, length=300, mode='determinate')
        self.progress.pack(pady=20)
        
        # Organize button
        organize_btn = tk.Button(self.root, text="Organize Files", command=self.organize_files, height=2, width=20)
        organize_btn.pack(pady=10)
        
        # Status label
        self.status_label = tk.Label(self.root, text="", fg="blue")
        self.status_label.pack(pady=10)
        
    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.folder_path.set(folder_selected)
    
    def organize_files(self):
        folder_path = self.folder_path.get()
        if not folder_path or not os.path.isdir(folder_path):
            messagebox.showerror("Error", "Please select a valid folder")
            return
            
        self.status_label.config(text="Organizing files...", fg="blue")
        self.root.update_idletasks()
        
        try:
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
            total_files = len(files)
            
            if total_files == 0:
                self.status_label.config(text="No files found to organize", fg="orange")
                return
                
            # Move files to their respective folders
            for i, file in enumerate(files):
                file_path = os.path.join(folder_path, file)
                file_ext = os.path.splitext(file)[1].lower()

                moved = False
                for folder_name, extensions in file_types.items():
                    if file_ext in extensions:
                        dest_folder = os.path.join(folder_path, folder_name)
                        try:
                            shutil.move(file_path, dest_folder)
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
                    except Exception as e:
                        print(f"Error moving {file}: {e}")
                
                # Update progress
                progress = (i + 1) / total_files * 100
                self.progress['value'] = progress
                self.root.update_idletasks()
            
            self.status_label.config(text=f"Organized {total_files} files successfully!", fg="green")
            messagebox.showinfo("Success", "Files organized successfully!")
            
        except Exception as e:
            self.status_label.config(text="Error occurred during organization", fg="red")
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileOrganizerApp(root)
    root.mainloop()