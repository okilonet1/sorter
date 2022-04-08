import os
import shutil

dirName = input("Enter the directory name: ")

li = os.listdir(dirName)

for i in li:
    fileName, fileExt = os.path.splitext(i)

    fileExt = fileExt[1:]

    if fileExt == "":
        continue

    if os.path.exists(dirName + "/" + fileExt):
        shutil.move(dirName + "/" + i, dirName + "/" + fileExt + "/" + i)

    else:
        os.mkdir(dirName + "/" + fileExt)
        shutil.move(dirName + "/" + i, dirName + "/" + fileExt + "/" + i)
