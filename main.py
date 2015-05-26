__author__ = 'jefftsai'

# This for train cascade model use
# Data notation and get sub image

import cv2 as cv
import numpy as np
from PyQt5 import QtWidgets
import sys
import math

windowSize = 120
resizeScale = 2
resizeWindowSize = int(windowSize/resizeScale/2)

img = np.array
Mark = []
def mouseCallBack(event,x,y,flag,para):
    if event ==1:
        Mark.append([x,y])
        draw = drawRectangle(img,Mark)
        cv.imshow("img",draw)

    elif event == 2:
        for i in range(0,len(Mark)):
            if math.fabs(x-Mark[i][0]) < resizeWindowSize and math.fabs(y-Mark[i][1]) < resizeWindowSize:
                print("remove")
                Mark.remove(Mark[i])
                break
        draw = drawRectangle(img,Mark)
        cv.imshow("img",draw)

def drawRectangle(img,Mark):
    draw = np.copy(img)
    for i in range(0,len(Mark)):
        draw = cv.rectangle(draw,(Mark[i][0]-resizeWindowSize,Mark[i][1]-resizeWindowSize),(Mark[i][0]+resizeWindowSize,Mark[i][1]+resizeWindowSize),(0,0,255))
    return draw





app = QtWidgets.QApplication(sys.argv)
fileName,_ = QtWidgets.QFileDialog.getOpenFileName(None,"Open Video","","Video Files(*.avi)")
outFileName,_ = QtWidgets.QFileDialog.getSaveFileName(None,"Save Info File","","Dat Files(*.dat)")

cap = cv.VideoCapture(fileName)
outFile = open(outFileName,"w")


cv.namedWindow("img")
cv.setMouseCallback("img",mouseCallBack)



if cap.isOpened():

    count = 0
    while 1:
        ret,frame = cap.read()
        img =np.copy(frame)
        smallSizeX = np.shape(img)[0]
        smallSizeY = np.shape(img)[1]
        img = cv.resize(img,(int(smallSizeY/resizeScale),int(smallSizeX/resizeScale)))
        cv.imshow("img",img)

        key = cv.waitKey(0)
        if key == 27:
            break
        elif key == 32:
            count = count+1
            msg = ""
            for i in range(0,len(Mark)):


                for j in range(0,len(Mark[i])):
                    Mark[i][j] = Mark[i][j]*resizeScale
                    msg = msg+str(Mark[i][j])+" "

                subImg = cv.getRectSubPix(frame,(windowSize,windowSize),(Mark[i][0],Mark[i][1]))
                cv.imwrite("images/img_"+str(count)+"_"+str(i)+".jpg",subImg)

                msg = msg[:-1]+"   "
            frameFileName = "frame_"+str(count)+".jpg"
            cv.imwrite(frameFileName,frame)

            # for neg
            outFile.write("neg_images/"+frameFileName+"\n")


            # for pos
            # outFile.write(frameFileName+" "+str(len(Mark))+" ")
            # outFile.write(msg+"\n")
            Mark.clear()

del cap
outFile.close()


