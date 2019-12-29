#!/usr/bin/env python3
import os
import re

def addZeros(imgN):
    if len(str(imgN)) == 1:
        imgN = "00" + str(imgN)
    elif len(str(imgN)) == 2:
        imgN = "0" + str(imgN)
    return imgN

for root, dirs, files in os.walk("Lifecake_Folders", topdown=False):
    #print(root)
    for name in files:
        namestr = str(name)
        if name.endswith(".jpg")==True or name.endswith(".mp4")==True:
            rootList = root.split("\\")
            nameList = name.split(".")
            lastRootItem = len(rootList)-1
            imgName = rootList[lastRootItem]

            lastNameItem = len(nameList)-1
            fileType = nameList[lastNameItem]
            objPath = os.path.join(root, name)
            Num = 1
            imgNum = addZeros(Num)
            newObjPath = "Sorted_Pictures\\" + imgName + "-" + imgNum + "." + fileType
            while os.path.isfile(newObjPath) == True:
                Num += 1
                imgNum = addZeros(Num)
                newObjPath = "Sorted_Pictures\\" + imgName + "-" + str(imgNum) + "." + fileType 
            os.rename(objPath, newObjPath)