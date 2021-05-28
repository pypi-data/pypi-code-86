# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'customOpenDialogTemplate.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(930, 541)
        Dialog.setStyleSheet("QSplitter::handle:horizontal {\n"
"  image: url(:/icons/icons/splitter.png);\n"
"  width:13px;\n"
"  height:13px;\n"
"  background: #f6b442;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setHandleWidth(11)
        self.splitter.setObjectName("splitter")
        self.input_category = QtWidgets.QListView(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_category.sizePolicy().hasHeightForWidth())
        self.input_category.setSizePolicy(sizePolicy)
        self.input_category.setMinimumSize(QtCore.QSize(150, 0))
        self.input_category.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.input_category.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.input_category.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.input_category.setResizeMode(QtWidgets.QListView.Adjust)
        self.input_category.setViewMode(QtWidgets.QListView.ListMode)
        self.input_category.setObjectName("input_category")
        self.table_directory_content = QtWidgets.QTableView(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.table_directory_content.sizePolicy().hasHeightForWidth())
        self.table_directory_content.setSizePolicy(sizePolicy)
        self.table_directory_content.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_directory_content.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_directory_content.setShowGrid(False)
        self.table_directory_content.setSortingEnabled(True)
        self.table_directory_content.setObjectName("table_directory_content")
        self.table_directory_content.horizontalHeader().setDefaultSectionSize(150)
        self.table_directory_content.horizontalHeader().setMinimumSectionSize(150)
        self.table_directory_content.horizontalHeader().setStretchLastSection(False)
        self.table_directory_content.verticalHeader().setVisible(False)
        self.table_directory_content.verticalHeader().setHighlightSections(False)
        self.gridLayout.addWidget(self.splitter, 1, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.input_directory = QtWidgets.QComboBox(Dialog)
        self.input_directory.setObjectName("input_directory")
        self.gridLayout_2.addWidget(self.input_directory, 0, 1, 1, 1)
        self.button_up = QtWidgets.QPushButton(Dialog)
        self.button_up.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_up.sizePolicy().hasHeightForWidth())
        self.button_up.setSizePolicy(sizePolicy)
        self.button_up.setObjectName("button_up")
        self.gridLayout_2.addWidget(self.button_up, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.input_file_name = QtWidgets.QLineEdit(Dialog)
        self.input_file_name.setObjectName("input_file_name")
        self.gridLayout_2.addWidget(self.input_file_name, 1, 1, 1, 1)
        self.button_filter = QtWidgets.QPushButton(Dialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.button_filter.setIcon(icon)
        self.button_filter.setObjectName("button_filter")
        self.gridLayout_2.addWidget(self.button_filter, 1, 2, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Open)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        self.table_directory_content.doubleClicked['QModelIndex'].connect(Dialog.slot_file_selected)
        self.button_up.clicked.connect(Dialog.slot_dir_up)
        self.input_directory.currentIndexChanged['QString'].connect(Dialog.slot_change_path)
        self.button_filter.clicked.connect(Dialog.slot_file_filter)
        self.input_category.clicked['QModelIndex'].connect(Dialog.slot_drive_changed)
        self.input_file_name.returnPressed.connect(self.button_filter.click)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.input_file_name, self.button_filter)
        Dialog.setTabOrder(self.button_filter, self.button_up)
        Dialog.setTabOrder(self.button_up, self.input_directory)
        Dialog.setTabOrder(self.input_directory, self.input_category)
        Dialog.setTabOrder(self.input_category, self.table_directory_content)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.button_up.setText(_translate("Dialog", "^ Up"))
        self.label.setText(_translate("Dialog", "Current directory:"))
        self.label_2.setText(_translate("Dialog", "File name:"))
        self.button_filter.setText(_translate("Dialog", "Filter"))
from kamzik3 import resource_kamzik3_rc
