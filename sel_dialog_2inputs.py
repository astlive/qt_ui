# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\select_area.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sel_dialog(object):
    def __init__(self, items=[], debug = False):
        super().__init__()
        self.lists = items
        self.title = ""
        if(debug):print("self.lists = " + str(self.lists))

    def setupUi(self, sel_dialog):
        sel_dialog.setObjectName("sel_dialog")
        sel_dialog.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(sel_dialog.sizePolicy().hasHeightForWidth())
        sel_dialog.setSizePolicy(sizePolicy)
        sel_dialog.setMinimumSize(QtCore.QSize(400, 300))
        sel_dialog.setMaximumSize(QtCore.QSize(400, 300))
        self.verticalLayout = QtWidgets.QVBoxLayout(sel_dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(sel_dialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.quickRB = QtWidgets.QRadioButton(self.groupBox)
        self.quickRB.setChecked(True)
        self.quickRB.clicked.connect(self.refocus)
        self.quickRB.setObjectName("quickRB")
        self.horizontalLayout_2.addWidget(self.quickRB)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.addItems(self.lists)
        self.comboBox.currentTextChanged.connect(self.valueUpdate)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.userRB = QtWidgets.QRadioButton(self.groupBox)
        self.userRB.clicked.connect(self.refocus)
        self.userRB.setObjectName("userRB")
        self.horizontalLayout_3.addWidget(self.userRB)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit.setEnabled(False)
        self.lineEdit.textChanged.connect(self.valueUpdate)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(sel_dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(sel_dialog)
        self.buttonBox.accepted.connect(sel_dialog.accept)
        self.buttonBox.rejected.connect(sel_dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(sel_dialog)

        self.valueUpdate()

    def retranslateUi(self, sel_dialog):
        _translate = QtCore.QCoreApplication.translate
        sel_dialog.setWindowTitle(_translate("sel_dialog", self.title))
        self.quickRB.setText(_translate("sel_dialog", "快速選擇"))
        self.userRB.setText(_translate("sel_dialog", "自行輸入"))

    def resetui(self, n_title="", n_list=[]):
        self.title = n_title
        self.lists = n_list

    def refocus(self):
        self.comboBox.setEnabled(not self.comboBox.isEnabled())
        self.lineEdit.setEnabled(not self.lineEdit.isEnabled())
        self.valueUpdate

    def valueUpdate(self, debug = False):
        self.r_value = self.lineEdit.text()
        if(self.quickRB.isChecked()):
            self.r_value = self.comboBox.currentText()
        if(debug == True):
            print("quickRB is " + str(self.quickRB.isChecked()))
            print("userRB is " + str(self.userRB.isChecked()))
            print("r_value = " + self.r_value)