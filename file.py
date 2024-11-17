import os
import shutil

path=input("Enter path: ")
files=os.listdir(path)

for files in files:
    filename,extension=os.path.splitext(files)
    extension=extension[1:]

    if os.path.exists(path+'/'+extension):
        shutil.move(path+'/'+files,path+'/'+extension+'/'+files)

    else:
        os.makedirs(path+'/'+extension)
        shutil.move(path+'/'+files , path+'/'+extension+'/'+files)
