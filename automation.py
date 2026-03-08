import os
import shutil
from datetime import datetime

# Ask user for folder path
path = input("Enter folder path: ")

# File types and their folders
folders = {
    ".txt": "Text",
    ".pdf": "PDF",
    ".png": "Images",
    ".jpg": "Images",
    ".mp3": "Audio",
    ".mp4": "Videos"
}

# Open log file
log = open("log.txt", "a")

try:
    files = os.listdir(path)

    for file in files:

        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):

            extension = os.path.splitext(file)[1]

            if extension in folders:

                folder_name = folders[extension]

                destination = os.path.join(path, folder_name)

                if not os.path.exists(destination):
                    os.mkdir(destination)

                shutil.move(file_path, destination)

                time = datetime.now()

                log.write(str(time) + " moved " + file + " to " + folder_name + "\n")

    print("File sorting completed!")

except Exception as e:

    print("Error:", e)

    log.write("Error: " + str(e) + "\n")

log.close()