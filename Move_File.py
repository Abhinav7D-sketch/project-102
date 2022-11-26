import os
import shutil

from_dir = "C:/Users/ga969/Downloads"
to_dir = "C:/Users/ga969/OneDrive/Documents/Document_Files"
list_of_files = os.listdir(from_dir)
print(list_of_files)

for file in list_of_files:
    name,extension = os.path.splitext(file)
    print(name)
    print(extension)
    if extension == "":
        continue
    if extension in [".txt", ".doc", ".docx", ".pdf"]:
        path1 = from_dir+"/"+file
        path2 = to_dir + '/' + "Document_Files"
        path3 = to_dir + '/' + "Document_Files" + '/' + file

        if os.path.exsits(path2):
            print("Moving " + file + "......")

            shutil.move(path1, path3)

        else:
            os.makdirs(path2)
            print("Moving " + file + "......")
            shutil.movie(path1,path3)