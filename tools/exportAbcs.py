# -*- coding: UTF-8 -*-
import sys
sys.path.append("..")
import os
from utils import osUtils
from utils import mayaUtils


def main(assetDir):
    # 根据maya文件的类型，可以更改后缀名ma或者mb
    scenes = osUtils.getFilesOfType(assetDir, "ma")
    for scene in scenes:
        abc = mayaUtils.exportMesh(scene)
        print("exported:", abc)


if __name__ == "__main__":
    main(sys.argv[-1])
