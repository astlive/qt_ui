# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\select_line_num.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_line_num_sel(object):
    def setupUi(self, line_num_sel):
        line_num_sel.setObjectName("line_num_sel")
        line_num_sel.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(line_num_sel.sizePolicy().hasHeightForWidth())
        line_num_sel.setSizePolicy(sizePolicy)
        line_num_sel.setMinimumSize(QtCore.QSize(400, 300))
        line_num_sel.setMaximumSize(QtCore.QSize(400, 300))
        self.verticalLayout = QtWidgets.QVBoxLayout(line_num_sel)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(line_num_sel)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.quickRB = QtWidgets.QRadioButton(self.groupBox)
        self.quickRB.setChecked(True)
        self.quickRB.setObjectName("quickRB")
        self.horizontalLayout_2.addWidget(self.quickRB)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.userRB = QtWidgets.QRadioButton(self.groupBox)
        self.userRB.setObjectName("userRB")
        self.horizontalLayout_3.addWidget(self.userRB)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setMinimumSize(QtCore.QSize(100, 0))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(line_num_sel)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(line_num_sel)
        self.buttonBox.accepted.connect(line_num_sel.accept)
        self.buttonBox.rejected.connect(line_num_sel.reject)
        QtCore.QMetaObject.connectSlotsByName(line_num_sel)

    def retranslateUi(self, line_num_sel):
        _translate = QtCore.QCoreApplication.translate
        line_num_sel.setWindowTitle(_translate("line_num_sel", "選擇軌別"))
        self.quickRB.setText(_translate("line_num_sel", "快速選擇"))
        self.userRB.setText(_translate("line_num_sel", "自行輸入"))
