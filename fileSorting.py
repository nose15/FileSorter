import os
import shutil

FOLDERPATH = "C:\\Users\\lukol\\OneDrive\\Pulpit\\webdev"
DESTINATIONDIR = "C:\\Users\\lukol\\OneDrive\\Pulpit\\webdev"

unpackFolders = False

def fileSorting(Path):
    dirs = os.scandir(Path)

    for directory in dirs:
        if directory.is_file():
            dirName = directory.name.split(".")
            if (len(dirName) > 1):
                destPath = DESTINATIONDIR + "\\" + dirName[-1].lower()
                newName = dirName[0] + "(" + Path.split("\\")[-1] + ")." + dirName[-1].lower()

                if dirName[-1].lower() not in os.listdir(DESTINATIONDIR):
                    os.mkdir(destPath)

                os.rename(Path + "\\" + directory.name, Path + "\\" + newName)
                try:
                    shutil.move(Path + "\\" + newName, destPath)
                except os.error:
                    print("Dupa")
                    pass

            else:
                destPath = DESTINATIONDIR
                try:
                    shutil.move(Path + "\\" + directory.name, destPath)
                except os.error:
                    print("Dupa")
                    pass

        else:
            newName = directory.name + "(" + Path.split("\\")[-1] + ")"
            os.rename(Path + "\\" + directory.name, Path + "\\" + newName)

            if unpackFolders:
                fileSorting(Path + "\\" + newName)
            else:
                destPath = DESTINATIONDIR + "\\"

                try:
                    shutil.move(Path + "\\" + newName, destPath)
                except os.error:
                    print("Dupa")
                    pass

fileSorting(FOLDERPATH)

