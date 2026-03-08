# File Automation Script

## Project Description

This project is a Python automation script that performs basic file management tasks.
It automatically sorts files into different folders based on their file type.
The script also records all operations in a log file and handles errors using exception handling.

## Features

* File sorting based on file extensions
* Automatic folder creation
* Logging of operations
* User input for folder path
* Exception handling for errors

## Technologies Used

* Python
* OS Module
* Shutil Module
* Exception Handling

## Project Structure

FileAutomationProject
│
├── automation.py
├── log.txt
└── README.md

## How the Script Works

1. The user enters the folder path.
2. The script scans all files in that folder.
3. It checks each file extension.
4. It creates folders if they do not exist.
5. Files are moved into their respective folders.
6. Each operation is recorded in the log file.

## Example Input

Folder containing files:

photo.png
song.mp3
notes.txt
doc.pdf

## Example Output

After running the script:

Images/photo.png
Audio/song.mp3
Text/notes.txt
PDF/doc.pdf

## How to Run the Project

1. Install Python.
2. Open terminal in the project folder.
3. Run the command:

python automation.py

4. Enter the folder path when prompted.

## Output

* Files sorted into folders
* Log file generated with details of operations

## Author

Abhi Kommisetti
