import os
import osUtils
import imageUtils
from shutil import move


def main(imageDir, fileType , convertTo):
    """ search for the specified type of files and convert them to another
        collect all of the converted files and put them together
    """
    images = osUtils.getFilesOfType(imageDir, fileType)
    newImages = imageUtils.convertImages(images, fileType, convertTo)

    # create collection directory
    newDir = imageDir + "/NewGatherOf%s" % convertTo.capitalize() + "/"
    if not os.path.exists(newDir):
        os.makedirs(newDir)
    # move file into newDir
    for file in newImages:
        move(file, os.path.join(newDir + file.split("\\")[-1]))


if __name__ == "__main__":
    main("E:/test", "png", "tif")

