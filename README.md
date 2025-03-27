File Organizer Bot
Overview
File Organizer Bot is a Python-based automation tool that organizes files in a specified folder by their file type (e.g., .pdf, .jpg, .mp3). It creates subfolders like "Images", "Documents", etc., and moves files into them, keeping your directories clean and structured.

Features
Automatically sorts files based on their extensions.
Creates categorized subfolders (e.g., "Images", "Docs", "Videos").
Lightweight and easy to use via command line.
Customizable for additional file types.
Tech Stack
Python: Core scripting language.
Modules: os, shutil for file handling and organization.
How to Run
Prerequisites:
Python 3.x installed on your system.
Clone or download this repository:
git clone https://github.com/yourusername/FileOrganizerBot.git
Setup:
Navigate to the project folder:
cd FileOrganizerBot
(Optional) Install dependencies (if any):
pip install -r requirements.txt
Run the Script:
Execute the script in terminal:
python file_organizer.py
Enter the folder path you want to organize when prompted.
Example:
Input folder: C:/Users/Mava/Downloads
Output: Files moved to Images/, Docs/, Videos/, etc.
Sample Output
Before:

text

Collapse

Wrap

Copy
Downloads/
├── photo.jpg
├── report.pdf
├── song.mp3
├── video.mp4
After:

text

Collapse

Wrap

Copy
Downloads/
├── Images/
│   └── photo.jpg
├── Docs/
│   └── report.pdf
├── Audio/
│   └── song.mp3
├── Videos/
│   └── video.mp4
Installation as Executable (Optional)
Convert to .exe for easy sharing:
Install PyInstaller: pip install pyinstaller
Run: pyinstaller --onefile file_organizer.py
Find the .exe in the dist/ folder.
Download the pre-built .exe (add link if you upload it).
Future Enhancements
GUI interface using tkinter.
Support for duplicate file detection.
Cloud integration for remote folder organization.
Why This Project?
Built this to showcase my Python automation skills, leveraging my 2 years of Java experience in logic building and file handling. Quick learner, adapted to Python in a week!

Contact
GitHub: HarshaTechKnight
Email: sriharsha0413@gmail.com
