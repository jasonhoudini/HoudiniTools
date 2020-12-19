# -*- coding: UTF-8 -*-
# mayapy 是Python2的解释器
import os
# 注意一下maya的相关模块在用mayapy.exe解释器的时候可以自动检索，所以只需要在环境变量中加上mayapy的PATH即可
import maya.standalone
maya.standalone.initialize()
import maya.cmds as cmds


def validateMesh(scene):
    """ Validate meshes
    """
    if os.path.isfile(scene):
        cmds.file(scene, open=True, force=True)

        for obj in cmds.listRelatives(cmds.ls(type="mesh", v=True), p=True, fullPath=True):

            validityFlags = "    scene: %s\n" % scene
            validityFlags = "    mesh: %s\n" % obj

            if not cmds.polyInfo(obj, invalidEdges=True):
                validityFlags += "        invalid edges found\n"
            if not cmds.polyInfo(obj, invalidVertices=True):
                validityFlags += "        invalid vertices found\n"
            if not cmds.polyInfo(obj, laminaFaces=True):
                validityFlags += "        lamina faces found\n"
            if not cmds.polyInfo(obj, nonManifoldEdges=True):
                validityFlags += "        non-Manifold faces found\n"
            if not cmds.polyInfo(obj, nonManifoldUVEdges=True):
                validityFlags += "        non-Manifold UV edges found\n"
            if not cmds.polyInfo(obj, nonManifoldUVs=True):
                validityFlags += "        non-Manifold UVs found\n"
            if not cmds.polyInfo(obj, nonManifoldVertices=True):
                validityFlags += "        non-Manifold vertices found\n"

            return validityFlags

def exportMesh(scene):
    """ Export mesh
    """
    if os.path.isfile(scene):
        cmds.file(scene, open=True, force= True)

        meshes = cmds.listRelatives(cmds.ls(type="mesh", v=True), p=True, fullPath=True)
        cmds.select(meshes)

        abcStr = ""
        for obj in cmds.ls(sl=True, l=True):
            abcStr += " -root" + obj

        cmds.loadPlugin("AbcExport.so")
        # 导出整个frame range
        start, end = cmds.playbackOptions(q=True, minTime=True), cmds.playbackOptions(q=True, maxTime=True)
        # 导出一帧
        # start, end = 1, 1

        export = scene.replace(".ma", ".abc")
        abcStr += "%s -frameRange %s %s -uvWrite -file %s" % (abcStr, start, end, export)
        # 不能导出abc文件，不知道为什么
        cmds.AbcExport(j=abcStr)
        return export
