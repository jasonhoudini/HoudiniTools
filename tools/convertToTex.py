import sys
sys.path.append("..")
from utils import osUtils
from utils import imageUtils

def main(imageDir):
    """convert to tex
    """
    if len(sys.argv) !=2:
        print("no directory provided")
        return
    # 只能把tif转换为tex，之后相加更改此处和convertToTex即可
    images = osUtils.getFilesOfType(imageDir, "tif")
    imageUtils.convertToTex(images)


if __name__ == "__main__":
    main(sys.argv[-1])
