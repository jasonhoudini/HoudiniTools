import sys
sys.path.append("..")
import os
from utils import osUtils
import argparse

def main():
    """ 利用fbx文件导入hython，利用主骨骼创建相机，然后自动计算出起始和结束的帧数并导出mov浏览
    """
    parser = argparse.ArgumentParser(description="find assets and create preview movs")
    parser.add_argument("-d", "--dir", metavar="", default="", help="a dir for find assets")
    parser.add_argument("-a", "--amount", metavar="", default="50", help="set camera distance")
    args = parser.parse_args()

    assetDir = args.dir
    amount = args.amount

    if not assetDir and amount:
        print("you need to supply dir and camera disrance")
        return

    for fbx in osUtils.getFilesOfType(assetDir, "fbx"):
        command = "D:/Adobe/Houdini18.5.351/bin/"
        command += 'hython -c \"import sys; sys.path.append(\'E:/HoudiniTools/utils\');'
        command += 'import houUtils; houUtils.captureFbx(\'%s\', \'%s\')\"' % (fbx, amount)
        os.system(command)

        dirName = os.path.dirname(fbx)

        # jpeg path
        outputImages = dirName + "/tmp.%04d.jpeg"

        # gen mov
        outputMov = fbx.replace(".FBX", ".mov")
        os.system("ffmpeg -r 24 -s 720x720 -i %s %s" % (outputImages, outputMov))

        # del images
        contents = os.listdir(dirName)
        for item in contents:
            if item.endswith(".jpeg"):
                os.remove(os.path.join(dirName, item).replace("\\", "/"))

        outputThumbnail = fbx.replace(".FBX", ".jpeg")
        os.system("ffmpeg -i %s -vframes 1 -s 360x360 -ss 0.1 %s" % (outputMov, outputThumbnail))

    print("fbx movs exported！")


if __name__ == "__main__":
    main()
