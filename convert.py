__author__ = 'jefftsai'

# positive info.dat need to convert by this script

from PyQt5 import QtWidgets
import sys


windowSize = 120

app = QtWidgets.QApplication(sys.argv)
inFileName,_ = QtWidgets.QFileDialog.getOpenFileName(None,"Open Dat File","","Dat Files(*.dat)")
outFileName,_ = QtWidgets.QFileDialog.getSaveFileName(None,"Save Dat File","","Dat Files(*.dat)")

if inFileName=="" or outFileName=="":
    print("File Name Empty!")

else:
    inFile = open(inFileName,"r")
    outFile = open(outFileName,"w")
    sum = 0
    while 1:
        text = inFile.readline()
        if text == "":
            break
        else:
            data = text.split(" ")
            data = data[2:-1]
            outFile.write("  ".join(text.split(" ")[0:2])+" ")
            for i in range(0,int(len(data)/4)):
                x,y = data[i*4],data[i*4+1]
                outFile.write("".join(x)+" ")
                outFile.write("".join(y)+" ")
                outFile.write("".join(str(windowSize))+" ")
                outFile.write("".join(str(windowSize))+"   ")
            outFile.write("\n")

inFile.close()
outFile.close()
