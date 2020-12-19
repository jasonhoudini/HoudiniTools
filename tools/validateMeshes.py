# -*- coding: UTF-8 -*-
import sys
sys.path.append("..")
import os
from utils import osUtils
from utils import mayaUtils


def main(assetDir):
    fileObj = open(os.path.join(assetDir, "report.txt"), "a")
    # 根据maya文件的类型，可以更改后缀名ma或者mb
    scenes = osUtils.getFilesOfType(assetDir, "mb")
    for scene in scenes:
        validate = mayaUtils.validateMesh(scene)
        # 打印出来本身没有意义，只是为了在cmd中显示运行正确
        # print(validate)
        fileObj.write(validate)
        fileObj.write("\n")
    fileObj.close()


if __name__ == "__main__":
    main(sys.argv[-1])
