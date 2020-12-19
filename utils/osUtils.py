import os
import tarfile
import glob


def getFilesOfType(destinationDir, fileType):
    """ return files of given type in a location"""
    files=[]
    for x in os.walk(destinationDir):
        for y in glob.glob(os.path.join(x[0], "*.%s" % fileType)):
            files.append(y.replace("\\", "/"))
    return files


def rename(dirName, text, mode, replaceText=""):
    for file in os.listdir(dirName):
        file = os.path.join(dirName, file).replace("\\", "/")
        fileName = os.path.basename(file)

        if mode == "prepend":
            newName = os.path.join(dirNmae, fileName.replace(fileName, text + fileName))
        elif mode == "replace":
            newName = os.path.join(dirName, fileName.replace(text, replaceText))

        os.rename(file, newName)

def rename_bilibili(dirName, nameFile):
    for file in os.listdir


if __name__ == "__main__":
    rename(1,1,1)
