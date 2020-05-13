#local
from monitor import Ui_Form
from init_ui import Ui_init_Form
from sel_dialog_2inputs import Ui_sel_dialog
from textfont import transtext

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
        self.sel_dialog_ui = Ui_sel_dialog() 

        self.ui.setupUi(self)
        # self.ui.Area_label.clicked.connect(self.open_dialog(obj=self.sel_area_ui))
        self.ui.Area_label.mousePressEvent = functools.partial(self.open_sel_dig, id="area")
        self.ui.line_class.mousePressEvent = functools.partial(self.open_sel_dig, id="line_class")
        self.ui.line_num.mousePressEvent = functools.partial(self.open_sel_dig, id="line_num")
        
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
                self.sel_dialog_ui.resetui(n_title="區間", n_list=self.area_list)
                resp = self.open_dialog(obj=self.sel_dialog_ui)
                if(resp == QtWidgets.QDialog.Accepted):
                    if(debug):print("r.value = " + str(self.sel_dialog_ui.r_value))
                    self.syncinfo(area=self.sel_dialog_ui.r_value)
            elif(id == "line_class"):
                self.sel_dialog_ui.resetui(n_title="線別", n_list=self.line_class_list)
                resp = self.open_dialog(obj=self.sel_dialog_ui)
                if(resp == QtWidgets.QDialog.Accepted):
                    if(debug):print("r.value = " + str(self.sel_dialog_ui.r_value))
                    self.syncinfo(line_class=self.sel_dialog_ui.r_value)
            elif(id == "line_num"):
                self.sel_dialog_ui.resetui(n_title="軌別", n_list=self.line_num_list)
                resp = self.open_dialog(obj=self.sel_dialog_ui)
                if(resp == QtWidgets.QDialog.Accepted):
                    if(debug):print("r.value = " + str(self.sel_dialog_ui.r_value))
                    self.syncinfo(line_num=self.sel_dialog_ui.r_value)

    def syncinfo(self, area=None, line_class=None, line_num=None, debug=False):
        if(debug):print("change from syncinfo()")
        if(debug):print("area = " + str(area))
        if(debug):print("line_class = " + str(line_class))
        if(debug):print("line_num = " + str(line_num))
        if(area != None):
            self.ui.Area_label.setText(transtext("區間:", area, mode=1))
        if(line_class != None):
            self.ui.line_class.setText(transtext("線別:", line_class, mode=1))
        if(line_num != None):
            self.ui.line_num.setText(transtext("軌別:", line_num, mode=1))

    def open_dialog(self, obj):
        dialog = QtWidgets.QDialog()
        dialog.ui = obj
        dialog.ui.setupUi(dialog)
        rr = dialog.exec_()
        dialog.show()
        return rr

    def synctime(self):
        self.ui.time_label.setText(transtext("日期:", datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 0))
        
if __name__ == "__main__":
    line_num = ['左側', '右側', '單線']
    line_class = ['東正線', '東副線', '西正線', '西副線']
    area = ['苗栗段', '台中段', '彰化段']
    app = QtWidgets.QApplication(sys.argv)
    myapp = mainwid(line_class= line_class, line_num= line_num, area=area)
    myapp.show()
    sys.exit(app.exec_())