import osUtils
import OpenEXR


exrDir = "E:/test"

exrs = osUtils.getFilesOfType(exrDir, "exr")

exrObj = OpenEXR.InputFile(exrs[0])
# 查看存在的metadata，用来做为之后查询的模板
# for k, v in exrObj.header().items():
#     print(k, v)
plateData = {"Filename": exrObj.header()["Filename"],
             "channels": exrObj.header()["channels"],
             "compression": exrObj.header()["compression"],
             "dataWindow": exrObj.header()["dataWindow"],
             "displayWindow": exrObj.header()["displayWindow"],
             "lineOrder": exrObj.header()["lineOrder"],
             "pixelAspectRatio": exrObj.header()["pixelAspectRatio"],
             "screenWindowCenter": exrObj.header()["screenWindowCenter"],
             "screenWindowWidth": exrObj.header()["screenWindowWidth"]}
print(plateData)

import yaml
with open("E:/test/exr/jasonPlateInfo.yaml", "w") as f:
    yaml.dump(plateData, f, default_flow_style=False)