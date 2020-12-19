import hou
import osUtils
import os

def reduceAsset(assetPath, amount=50):
    """ PolyReduce asset and export a new version
    """
    fileNode = hou.node("/obj/geo/FILE_IN")
    fileNode.parm("file").set(assetPath)
    fileNode.parm("reload").pressButton()

    polyReduceNode = hou.node("/obj/geo/polyreduce1")
    polyReduceNode.parm("percentage").set(amount)

    newAsset = assetPath.replace(".obj", "_reduced.obj")

    ropNode = hou.node("/obj/geo/FILE_OUT")
    ropNode.parm("sopoutput").set(newAsset)
    ropNode.parm("execute").pressButton()

    print(newAsset)


# test in houdini, houdini中路径里的\必须要全部改为/
# assetPath = "E:/test/2.obj"
# reduceAsset(assetPath, amount=5)
def runReduction(assetDir, amount):
    hou.hipFile.load("E:/test/reduce.hip", ignore_load_warnings=True)
    for asset in osUtils.getFilesOfType(assetDir, "obj"):
        print(asset.replace("\\", "/"))
        reduceAsset(asset.replace("\\", "/"), amount)


def captureFbx(fbxPath, cameraDistance=350):
    """
    Gather fbx and create camera to follow it
    """
    # import fbx
    subnet = hou.hipFile.importFBX(file_name=fbxPath, import_geometry=True)
    subnet = subnet[0]

    # Turn off joint viz
    for node in subnet.children():
        if "bone" in node.name():
            node.setDisplayFlag(0)

    # Get main joint (usually Hips whendownload from mixamo.com)
    rootJntNode = ""
    rootJntPath = ""
    for node in subnet.children():
        if "Hips" in node.name():
            rootJntNode = node
            rootJntPath = node.path()
            break

    # 找出起始帧和最后一帧
    print(rootJntPath)
    range = []
    for x in hou.node(rootJntPath).parm("tx").keyframes():
        range.append(x.frame())

    range.sort()
    print(range)

    # Create camera and constrain to fbx
    if rootJntNode:
        mainJntTxPath = rootJntNode.parm("tx").path()
        mainJntTyHeight = rootJntNode.parm("ty").eval()
        mainJntTzPath = rootJntNode.parm("tz").path()

        cam = hou.node("/obj").createNode("cam")
        cam.parm("tx").setExpression('ch("%s") + %d' % (mainJntTxPath, int(cameraDistance)))
        cam.parm("ty").set(mainJntTyHeight)
        cam.parm("tz").setExpression('ch("%s") + %d' % (mainJntTzPath, int(cameraDistance)))
        cam.parm("ry").set(45)

    # Add openGL
    openGl = hou.node("/out").createNode("opengl")
    # set frame range
    openGl.parm("trange").set(1)
    # frameRange = hou.playbar.playbackRange()
    # openGl.parm("/out/opengl1/f1").set(frameRange[0])
    # openGl.parm("/out/opengl1/f2").set(frameRange[1])
    openGl.parm("/out/opengl1/f1").set(range[0]+1)
    openGl.parm("/out/opengl1/f2").set(range[-1]+1)

    # set fbx path  as comment
    openGl.parm("/out/opengl1/vpcomment").set(fbxPath)
    openGl.parm("/out/opengl1/tres").set(1)
    openGl.parmTuple("/out/opengl1/res").set((720, 720))

    # make imgaes path
    outputPath = os.path.dirname(fbxPath) + "/tmp.$F4.jpeg"
    openGl.parm("/out/opengl1/picture").set(outputPath)

    openGl.parm("aamode").set(3)
    openGl.parm("/out/opengl1/shadingmode").set(6)
    openGl.parm("/out/opengl1/execute").pressButton()
