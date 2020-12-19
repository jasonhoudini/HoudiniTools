from PIL import Image
import os
import osUtils


def convertImages(images, convertFrom, convertTo):
    """ convert one image type to another at the same place
        return a converted images list to put them together
    """
    newImages = []
    for image in images:
        newImage = image.replace(convertFrom, convertTo)
        img = Image.open(image)
        img.save(newImage)
        newImages.append(newImage)
    return newImages


def convertToTex(images):
    """ convert to tex
    """
    for image in images:
        txMakeStr = "txmake"
        txMakeStr += " %s %s" % (image, image.replace(".tif", ".tex"))
        os.system(txMakeStr)


def createProxy(inDir, destDir, fileType):
    """ create proxy images
    """
    for dr in os.listdir(inDir):
        currentDir = os.path.join(inDir, dr).replace("\\", "/")

        if os.path.isdir(currentDir):
            newDir = os.path.join(destDir, os.path.basename(currentDir) + "_proxy").replace("\\", "/")
            if not os.path.exists(newDir):
                os.mkdir(newDir)

            for img in osUtils.getFilesOfType(currentDir, fileType,):
                image = Image.open(img)
                size = image.size
                image.thumbnail((size[0]/2, size[1]/2))
                print(img.replace(currentDir, newDir))
                image.save(img.replace(currentDir, newDir))

