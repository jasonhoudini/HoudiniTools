from PIL import Image
import os
# import osUtils


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

