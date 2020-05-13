# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\init_ui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_init_Form(object):
    def __init__(self, area=[], line_class=[], line_num=[], debug = False):
        super().__init__()
        self.r_c = 0
        self.area_list = area
        self.line_class_list = line_class
        self.line_num_list = line_num
        self.r_area = ""
        self.r_line_class = ""
        self.r_line_num = ""
        if(debug):print("area = " + str(area))
        if(debug):print("line_class = " + str(line_class))
        if(debug):print("line_num = " + str(line_num))

    def setupUi(self, init_Form):
        init_Form.setObjectName("init_Form")
        init_Form.resize(400, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(init_Form.sizePolicy().hasHeightForWidth())
        init_Form.setSizePolicy(sizePolicy)
        init_Form.setMinimumSize(QtCore.QSize(400, 800))
        init_Form.setMaximumSize(QtCore.QSize(400, 800))
        self.verticalLayout = QtWidgets.QVBoxLayout(init_Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.sel_Area_GB = QtWidgets.QGroupBox(init_Form)
        self.sel_Area_GB.setObjectName("sel_Area_GB")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.sel_Area_GB)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.sel_Area_RB = QtWidgets.QRadioButton(self.sel_Area_GB)
        self.sel_Area_RB.setChecked(True)
        self.sel_Area_RB.setObjectName("sel_Area_RB")
        self.horizontalLayout_5.addWidget(self.sel_Area_RB)
        self.sel_Area_Q_CB = QtWidgets.QComboBox(self.sel_Area_GB)
        self.sel_Area_Q_CB.addItems(self.area_list)
        self.sel_Area_Q_CB.setObjectName("sel_Area_Q_CB")
        self.horizontalLayout_5.addWidget(self.sel_Area_Q_CB)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.sel_Area_U_RB = QtWidgets.QRadioButton(self.sel_Area_GB)
        self.sel_Area_U_RB.setObjectName("sel_Area_U_RB")
        self.horizontalLayout_6.addWidget(self.sel_Area_U_RB)
        self.sel_Area_LE = QtWidgets.QLineEdit(self.sel_Area_GB)
        self.sel_Area_LE.setMinimumSize(QtCore.QSize(100, 0))
        self.sel_Area_LE.setObjectName("sel_Area_LE")
        self.horizontalLayout_6.addWidget(self.sel_Area_LE)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4.addWidget(self.sel_Area_GB)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.sel_line_class_GB = QtWidgets.QGroupBox(init_Form)
        self.sel_line_class_GB.setObjectName("sel_line_class_GB")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.sel_line_class_GB)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.quickRB_3 = QtWidgets.QRadioButton(self.sel_line_class_GB)
        self.quickRB_3.setChecked(True)
        self.quickRB_3.setObjectName("quickRB_3")
        self.horizontalLayout_8.addWidget(self.quickRB_3)
        self.comboBox_3 = QtWidgets.QComboBox(self.sel_line_class_GB)
        self.comboBox_3.addItems(self.line_class_list)
        self.comboBox_3.setObjectName("comboBox_3")
        self.horizontalLayout_8.addWidget(self.comboBox_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.userRB_3 = QtWidgets.QRadioButton(self.sel_line_class_GB)
        self.userRB_3.setObjectName("userRB_3")
        self.horizontalLayout_9.addWidget(self.userRB_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.sel_line_class_GB)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_9.addWidget(self.lineEdit_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_7.addWidget(self.sel_line_class_GB)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.sel_line_num_GB = QtWidgets.QGroupBox(init_Form)
        self.sel_line_num_GB.setObjectName("sel_line_num_GB")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.sel_line_num_GB)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.quickRB_4 = QtWidgets.QRadioButton(self.sel_line_num_GB)
        self.quickRB_4.setChecked(True)
        self.quickRB_4.setObjectName("quickRB_4")
        self.horizontalLayout_11.addWidget(self.quickRB_4)
        self.comboBox_4 = QtWidgets.QComboBox(self.sel_line_num_GB)
        self.comboBox_4.addItems(self.line_num_list)
        self.comboBox_4.setObjectName("comboBox_4")
        self.horizontalLayout_11.addWidget(self.comboBox_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.userRB_4 = QtWidgets.QRadioButton(self.sel_line_num_GB)
        self.userRB_4.setObjectName("userRB_4")
        self.horizontalLayout_12.addWidget(self.userRB_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.sel_line_num_GB)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_12.addWidget(self.lineEdit_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_10.addWidget(self.sel_line_num_GB)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.pushButton = QtWidgets.QPushButton(init_Form)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.buttonclick)

        self.retranslateUi(init_Form)
        QtCore.QMetaObject.connectSlotsByName(init_Form)

    def retranslateUi(self, init_Form):
        _translate = QtCore.QCoreApplication.translate
        init_Form.setWindowTitle(_translate("init_Form", "初始化設定"))
        self.sel_Area_GB.setTitle(_translate("init_Form", "選擇區間"))
        self.sel_Area_RB.setText(_translate("init_Form", "快速選擇"))
        self.sel_Area_U_RB.setText(_translate("init_Form", "自行輸入"))
        self.sel_line_class_GB.setTitle(_translate("init_Form", "選擇線別"))
        self.quickRB_3.setText(_translate("init_Form", "快速選擇"))
        self.userRB_3.setText(_translate("init_Form", "自行輸入"))
        self.sel_line_num_GB.setTitle(_translate("init_Form", "選擇軌別"))
        self.quickRB_4.setText(_translate("init_Form", "快速選擇"))
        self.userRB_4.setText(_translate("init_Form", "自行輸入"))
        self.pushButton.setText(_translate("init_Form", "確認"))

    def buttonclick(self, init_Form, debug = False):
        self.r_area = self.sel_Area_LE.text()
        self.r_line_class = self.lineEdit_3.text()
        self.r_line_num = self.lineEdit_4.text()
        if(self.sel_Area_RB.isChecked()):
            self.r_area = str(self.sel_Area_Q_CB.currentText())
        if(self.quickRB_3.isChecked()):
            self.r_line_class = str(self.comboBox_3.currentText())
        if(self.quickRB_4.isChecked()):
            self.r_line_num = str(self.comboBox_4.currentText())
        if(debug):print("area = " + str(self.r_area))
        if(debug):print("line_class = " + str(self.r_line_class))
        if(debug):print("line_num = " + str(self.r_line_num))
        self.r_c = 1
        QtCore.QCoreApplication.instance().quit()

