#local
from monitor import Ui_Form
from init_ui import Ui_init_Form
from sel_area import Ui_area_sel
from sel_line_cls import Ui_line_class_sel
from sel_line_num import Ui_line_num_sel

#pip package
from PyQt5 import QtGui, QtWidgets, QtCore
import sys
import functools
from datetime import datetime

class mainwid(QtWidgets.QWidget):
    def __init__(self, line_num=[], line_class=[], area=[], parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.line_num_list = line_num
        self.line_class_list = line_class
        self.area_list = area
        self.translate = QtCore.QCoreApplication.translate

        self.ui = Ui_Form()
        self.init_ui = Ui_init_Form(area=self.area_list, line_class=self.line_class_list, line_num=self.line_num_list)
        self.sel_area_ui = Ui_area_sel(area= self.area_list)

        self.ui.setupUi(self)
        # self.ui.Area_label.clicked.connect(self.open_dialog(obj=self.sel_area_ui))
        self.ui.Area_label.mousePressEvent = functools.partial(self.open_sel_dig, id="area")
        
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

    def open_sel_dig(self, event, id="", debug = False):
        if(debug):print("id = " + str(id))
        if(debug):print("event.button() = " + str(event.button()))
        if(event.button() == QtCore.Qt.LeftButton):
            if(id == "area"):
                resp = self.open_dialog(obj=self.sel_area_ui)
                if(resp == QtWidgets.QDialog.Accepted):
                    if(debug):print("r.value = " + str(self.sel_area_ui.r_value))
                    self.ui.Area_label.setText(self.transtext(txt1="區間",txt2=self.sel_area_ui.r_value,mode=1))

    def transtext(self, txt1, txt2 = "", mode = 0):
        #mode 0 
        if(mode == 0):
            return self.translate("Form", "<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\">" + txt1 + ":" + txt2 + "</span></p></body></html>")
        #mode 1 for linkable label
        elif(mode == 1):
            return self.translate("Form", "<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\">" + txt1 + ":</span><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\"> " + txt2 + " </span></p></body></html>")
    
    def syncinfo(self, area=None, line_class=None, line_num=None, debug=False):
        if(debug):print("change from syncinfo()")
        if(debug):print("area = " + str(area))
        if(debug):print("line_class = " + str(line_class))
        if(debug):print("line_num = " + str(line_num))
        if(area != None):
            self.ui.Area_label.setText(self.translate("Form", "<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\">區間:</span><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\"> " + area + " </span></p></body></html>"))
        if(line_class != None):
            self.ui.line_class.setText(self.translate("Form", "<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\">線別:</span><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">" + line_class + "</span></p></body></html>"))
        if(line_num != None):
            self.ui.line_num.setText(self.translate("Form", "<html><head/><body><p align=\"justify\"><span style=\" font-size:12pt;\">軌別:</span><span style=\" font-size:12pt; text-decoration: underline; color:#0000ff;\">" + line_num + "</span></p></body></html>"))

    def open_dialog(self, obj):
        dialog = QtWidgets.QDialog()
        dialog.ui = obj
        dialog.ui.setupUi(dialog)
        rr = dialog.exec_()
        dialog.show()
        return rr

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