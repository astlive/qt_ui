#local
from monitor import Ui_Form
from init_ui import Ui_init_Form

#pip package
from PyQt5 import QtGui, QtWidgets, QtCore
import sys
from datetime import datetime

class mainwid(QtWidgets.QWidget):
    def __init__(self, line_num=[], line_class=[], area=[], parent=None):
        self.line_num_list = line_num
        self.line_class_list = line_class
        self.area_list = area
        self.translate = QtCore.QCoreApplication.translate

        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.init_ui = Ui_init_Form(area=self.area_list, line_class=self.line_class_list, line_num=self.line_num_list)

        self.clocktimer = QtCore.QTimer(self)
        self.clocktimer.timeout.connect(self.synctime)
        self.clocktimer.start(1000)

        self.open_dialog(self.init_ui)
        self.syncinfo(area=self.init_ui.r_area, line_class=self.init_ui.r_line_class, line_num=self.init_ui.r_line_num)
    def execute_event(self):
        pass

    def execute_all_event(self):
        pass

    def reload_event(self):
        pass

    def showinitdialog(self):
        pass

    def syncinfo(self, area=None, line_class=None, line_num=None, debug=True):
        if(debug):print("area = " + str(area))
        if(debug):print("line_class = " + str(line_class))
        if(debug):print("line_num = " + str(line_num))
        if(area != None):
            self.ui.Area_label.setText(self.translate("Form", "<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\">區間:" + area + "</span></p></body></html>"))
        if(line_class != None):
            self.ui.line_class.setText(self.translate("Form", "<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\">線別:" + line_class + "</span></p></body></html>"))
        if(line_num != None):
            self.ui.line_num.setText(self.translate("Form", "<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\">軌別:" + line_num + "</span></p></body></html>"))

    def open_dialog(self, obj):
        dialog = QtWidgets.QDialog()
        dialog.ui = obj
        dialog.ui.setupUi(dialog)
        dialog.exec_()
        dialog.show()

    def synctime(self):
        self.ui.time_label.setText(self.translate("Form", "<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\">日期:" + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "</span></p></body></html>"))
        
if __name__ == "__main__":
    line_num = ['左側', '右側', '單線']
    line_class = ['東正線', '東副線', '西正線', '西副線']
    area = ['苗栗段', '台中段', '彰化段']
    app = QtWidgets.QApplication(sys.argv)
    myapp = mainwid(line_class= line_class, line_num= line_num, area=area)
    myapp.show()
    sys.exit(app.exec_())