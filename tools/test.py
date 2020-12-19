import os

dirName = "F:/b"
dirList = []
for file in os.listdir(dirName):
    file = file[0:9]
    dirList.append(file)
    file = os.path.join(dirName, file).replace("\\", "/")

dirList.sort()
for file in dirList:

print(dirList)