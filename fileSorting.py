import os
import shutil

ORIGIN_PATH = ""
DESTINATION_PATH = ""

unpackFolders = False


def fileSorting(Path):
    directories = os.scandir(Path)

    for directory in directories:
        if directory.is_file():

            dir_name = directory.name.split(".")

            if (len(dir_name) > 1):
                dest_path = DESTINATION_PATH + "\\" + dir_name[-1].lower()
                new_name = dir_name[-2] + "(" + Path.split("\\")[-1] + ")." + dir_name[-1].lower()

                if dir_name[-1].lower() not in os.listdir(DESTINATION_PATH):
                    os.mkdir(dest_path)

                os.rename(Path + "\\" + directory.name, Path + "\\" + new_name)
                
                try:
                    shutil.move(Path + "\\" + new_name, dest_path)
                except os.error:
                    print("Dupa")
                    pass

            else:
                dest_path = DESTINATION_PATH
                try:
                    shutil.move(Path + "\\" + directory.name, dest_path)
                except os.error:
                    print("Dupa")
                    pass

        else:
            new_name = directory.name + "(" + Path.split("\\")[-1] + ")"
            os.rename(Path + "\\" + directory.name, Path + "\\" + new_name)

            if unpackFolders:
                fileSorting(Path + "\\" + new_name)
            else:
                dest_path = DESTINATION_PATH + "\\"

                try:
                    shutil.move(Path + "\\" + new_name, dest_path)
                except os.error:
                    print("Dupa")
                    pass

fileSorting(ORIGIN_PATH)

