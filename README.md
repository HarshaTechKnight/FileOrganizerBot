# File Organizer Bot

A Python script that automatically organizes files in a folder by their file types (extensions). 
Creates subfolders and moves files into appropriate categories. Includes both CLI and GUI versions.

## Features
- Organizes files into categories: Images, Documents, Videos, Audio, Archives, etc.
- Handles unknown file types in "Others" folder
- GUI version with progress tracking (tkinter)
- Optional duplicate file remover (MD5 hash based)
- Cross-platform (Windows/macOS/Linux)

## Requirements
- Python 3.x
- No additional packages required for basic version
- Tkinter (usually comes with Python) for GUI version

## How to Use

### Basic Version (Command Line)
1. Run `file_organizer.py`
2. Enter the folder path you want to organize when prompted
3. Files will be sorted into subfolders automatically

### GUI Version
1. Run `file_organizer_gui.py`
2. Click "Browse" to select a folder
3. Click "Organize Files"
4. View progress in the status bar

### Duplicate File Remover
The script includes an optional function to remove duplicate files based on content.

## File Categories
- Images: .jpg, .png, .gif, etc.
- Documents: .pdf, .docx, .xlsx, etc.
- Videos: .mp4, .mov, .avi, etc.
- Audio: .mp3, .wav, etc.
- Archives: .zip, .rar, etc.
- Executables: .exe, .msi, etc.
- Code: .py, .js, .html, etc.
- Data: .csv, .xml, etc.
- Others: All other file types

## Notes
- Always back up important files before running
- The script won't modify system folders or hidden files
- Tested on Windows 10/11 and macOS

## Author
Sri Harsha M
