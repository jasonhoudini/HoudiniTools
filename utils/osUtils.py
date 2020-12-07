import os
import tarfile
import glob


def getFilesOfType(destinationDir, fileType):
    """return files of given type in a location"""
    files=[]
    for x in os.walk(destinationDir):
        for y in glob.glob(os.path.join(x[0], "*.%s" % fileType)):
            files.append(y.replace("\\", "/"))
    return files
