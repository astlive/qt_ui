from datetime import datetime
from PyQt5 import QtGui, QtWidgets, QtCore

translate = QtCore.QCoreApplication.translate

def transtext(txt1, txt2 = "", mode = 0):
    #mode 0 
    if(mode == 0):
        return translate("Form", "<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\">" + txt1 + " " + txt2 + "</span></p></body></html>")
    #mode 1 for linkable label
    elif(mode == 1):
        return translate("Form", "<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\">" + txt1 + " </span><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\"> " + txt2 + " </span></p></body></html>")
