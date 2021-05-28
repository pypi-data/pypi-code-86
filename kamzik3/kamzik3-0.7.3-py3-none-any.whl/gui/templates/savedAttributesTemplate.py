# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'savedAttributesTemplate.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1060, 502)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setEnabled(True)
        self.frame.setStyleSheet("QFrame {background-color:#d5d5d5}\n"
"QLabel {padding:3px;padding-left:7px;padding-right:7px}")
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMaximumSize(QtCore.QSize(9999999, 16777215))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setStyleSheet("")
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addWidget(self.frame, 3, 0, 1, 1)
        self.groups_frame = QtWidgets.QFrame(Form)
        self.groups_frame.setStyleSheet("QFrame#groups_frame {background-color:#f6b442}")
        self.groups_frame.setObjectName("groups_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groups_frame)
        self.horizontalLayout_3.setContentsMargins(6, 2, 6, 2)
        self.horizontalLayout_3.setSpacing(3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_saved_groups = QtWidgets.QLabel(self.groups_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_saved_groups.sizePolicy().hasHeightForWidth())
        self.label_saved_groups.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_saved_groups.setFont(font)
        self.label_saved_groups.setObjectName("label_saved_groups")
        self.horizontalLayout_3.addWidget(self.label_saved_groups)
        self.combo_preset = QtWidgets.QComboBox(self.groups_frame)
        self.combo_preset.setMinimumSize(QtCore.QSize(200, 0))
        self.combo_preset.setObjectName("combo_preset")
        self.horizontalLayout_3.addWidget(self.combo_preset)
        self.button_remove_preset_group = QtWidgets.QPushButton(self.groups_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_remove_preset_group.sizePolicy().hasHeightForWidth())
        self.button_remove_preset_group.setSizePolicy(sizePolicy)
        self.button_remove_preset_group.setMinimumSize(QtCore.QSize(100, 0))
        self.button_remove_preset_group.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.button_remove_preset_group.setFont(font)
        self.button_remove_preset_group.setStyleSheet("QPushButton {color:red}")
        self.button_remove_preset_group.setIconSize(QtCore.QSize(0, 0))
        self.button_remove_preset_group.setObjectName("button_remove_preset_group")
        self.horizontalLayout_3.addWidget(self.button_remove_preset_group)
        self.button_add_preset_group = QtWidgets.QPushButton(self.groups_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_add_preset_group.sizePolicy().hasHeightForWidth())
        self.button_add_preset_group.setSizePolicy(sizePolicy)
        self.button_add_preset_group.setMinimumSize(QtCore.QSize(100, 0))
        self.button_add_preset_group.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.button_add_preset_group.setFont(font)
        self.button_add_preset_group.setStyleSheet("QPushButton {color:green}")
        self.button_add_preset_group.setIconSize(QtCore.QSize(0, 0))
        self.button_add_preset_group.setObjectName("button_add_preset_group")
        self.horizontalLayout_3.addWidget(self.button_add_preset_group)
        self.label_saved_groups_2 = QtWidgets.QLabel(self.groups_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_saved_groups_2.sizePolicy().hasHeightForWidth())
        self.label_saved_groups_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_saved_groups_2.setFont(font)
        self.label_saved_groups_2.setObjectName("label_saved_groups_2")
        self.horizontalLayout_3.addWidget(self.label_saved_groups_2)
        self.button_first_page = QtWidgets.QPushButton(self.groups_frame)
        self.button_first_page.setMaximumSize(QtCore.QSize(25, 16777215))
        self.button_first_page.setObjectName("button_first_page")
        self.horizontalLayout_3.addWidget(self.button_first_page)
        self.button_previous_page = QtWidgets.QPushButton(self.groups_frame)
        self.button_previous_page.setMaximumSize(QtCore.QSize(25, 16777215))
        self.button_previous_page.setObjectName("button_previous_page")
        self.horizontalLayout_3.addWidget(self.button_previous_page)
        self.input_page = QtWidgets.QSpinBox(self.groups_frame)
        self.input_page.setMinimum(1)
        self.input_page.setMaximum(10000)
        self.input_page.setObjectName("input_page")
        self.horizontalLayout_3.addWidget(self.input_page)
        self.button_next_page = QtWidgets.QPushButton(self.groups_frame)
        self.button_next_page.setMaximumSize(QtCore.QSize(25, 16777215))
        self.button_next_page.setObjectName("button_next_page")
        self.horizontalLayout_3.addWidget(self.button_next_page)
        self.button_last_page = QtWidgets.QPushButton(self.groups_frame)
        self.button_last_page.setMaximumSize(QtCore.QSize(25, 16777215))
        self.button_last_page.setObjectName("button_last_page")
        self.horizontalLayout_3.addWidget(self.button_last_page)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.checkbox_allow_double_click = QtWidgets.QCheckBox(self.groups_frame)
        self.checkbox_allow_double_click.setObjectName("checkbox_allow_double_click")
        self.horizontalLayout_3.addWidget(self.checkbox_allow_double_click)
        self.gridLayout.addWidget(self.groups_frame, 2, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_set_value = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_set_value.sizePolicy().hasHeightForWidth())
        self.button_set_value.setSizePolicy(sizePolicy)
        self.button_set_value.setMinimumSize(QtCore.QSize(35, 35))
        self.button_set_value.setMaximumSize(QtCore.QSize(40, 40))
        self.button_set_value.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/target.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_set_value.setIcon(icon)
        self.button_set_value.setIconSize(QtCore.QSize(25, 25))
        self.button_set_value.setObjectName("button_set_value")
        self.verticalLayout.addWidget(self.button_set_value)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.button_change_color = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_change_color.sizePolicy().hasHeightForWidth())
        self.button_change_color.setSizePolicy(sizePolicy)
        self.button_change_color.setMinimumSize(QtCore.QSize(35, 35))
        self.button_change_color.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_change_color.setFont(font)
        self.button_change_color.setStyleSheet("QPushButton {color:red}")
        self.button_change_color.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/color_picker.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_change_color.setIcon(icon1)
        self.button_change_color.setIconSize(QtCore.QSize(25, 25))
        self.button_change_color.setObjectName("button_change_color")
        self.verticalLayout.addWidget(self.button_change_color)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.button_remove = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_remove.sizePolicy().hasHeightForWidth())
        self.button_remove.setSizePolicy(sizePolicy)
        self.button_remove.setMinimumSize(QtCore.QSize(35, 35))
        self.button_remove.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_remove.setFont(font)
        self.button_remove.setStyleSheet("QPushButton {color:red}")
        self.button_remove.setIconSize(QtCore.QSize(0, 0))
        self.button_remove.setObjectName("button_remove")
        self.verticalLayout.addWidget(self.button_remove)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.button_add = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_add.sizePolicy().hasHeightForWidth())
        self.button_add.setSizePolicy(sizePolicy)
        self.button_add.setMinimumSize(QtCore.QSize(35, 35))
        self.button_add.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.button_add.setFont(font)
        self.button_add.setStyleSheet("QPushButton {color:green}")
        self.button_add.setIconSize(QtCore.QSize(0, 0))
        self.button_add.setObjectName("button_add")
        self.verticalLayout.addWidget(self.button_add)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout.addItem(spacerItem5)
        self.gridLayout.addLayout(self.verticalLayout, 1, 2, 1, 1)
        self.table_attributes = QtWidgets.QTableView(Form)
        self.table_attributes.setObjectName("table_attributes")
        self.gridLayout.addWidget(self.table_attributes, 1, 0, 1, 1)
        self.layout_subgroups_select = QtWidgets.QHBoxLayout()
        self.layout_subgroups_select.setObjectName("layout_subgroups_select")
        self.gridLayout.addLayout(self.layout_subgroups_select, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.button_remove.clicked.connect(Form.remove_rows)
        self.button_add.clicked.connect(Form.add_row)
        self.button_change_color.clicked.connect(Form.select_color)
        self.button_set_value.clicked.connect(Form.set_attribute_value)
        self.button_add_preset_group.clicked.connect(Form.add_preset_group)
        self.button_remove_preset_group.clicked.connect(Form.remove_preset_group)
        self.combo_preset.currentTextChanged['QString'].connect(Form.slot_refresh_group_tables)
        self.input_page.valueChanged['int'].connect(Form.slot_jump_to_page)
        self.button_next_page.clicked.connect(self.input_page.stepUp)
        self.button_previous_page.clicked.connect(self.input_page.stepDown)
        self.button_first_page.clicked.connect(Form.slot_jump_to_first_page)
        self.button_last_page.clicked.connect(Form.slot_jump_to_last_page)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "ALT+A   [ add row ]"))
        self.label_2.setText(_translate("Form", "ALT+D   [ remove row ]"))
        self.label_3.setText(_translate("Form", "ALT+X   [ set value ]"))
        self.label_4.setText(_translate("Form", "ALT+C   [ set row color ]"))
        self.label_saved_groups.setText(_translate("Form", "Group:"))
        self.button_remove_preset_group.setToolTip(_translate("Form", "Remove selected group"))
        self.button_remove_preset_group.setText(_translate("Form", "- Remove group"))
        self.button_add_preset_group.setToolTip(_translate("Form", "Add new save group"))
        self.button_add_preset_group.setText(_translate("Form", "+ Empty group"))
        self.label_saved_groups_2.setText(_translate("Form", "Paging:"))
        self.button_first_page.setToolTip(_translate("Form", "Jump to first page"))
        self.button_first_page.setText(_translate("Form", "<|"))
        self.button_previous_page.setToolTip(_translate("Form", "Jump to previous page"))
        self.button_previous_page.setText(_translate("Form", "<"))
        self.button_next_page.setToolTip(_translate("Form", "Jump to next page"))
        self.button_next_page.setText(_translate("Form", ">"))
        self.button_last_page.setToolTip(_translate("Form", "Jump to last page"))
        self.button_last_page.setText(_translate("Form", "|>"))
        self.checkbox_allow_double_click.setText(_translate("Form", "Allow set on double click"))
        self.button_set_value.setToolTip(_translate("Form", "Set attribute to saved value (ALT+x)"))
        self.button_change_color.setToolTip(_translate("Form", "Change row color (ALT+C)"))
        self.button_remove.setToolTip(_translate("Form", "Remove row (ALT+D)"))
        self.button_remove.setText(_translate("Form", "-"))
        self.button_add.setToolTip(_translate("Form", "Add row (ALT+A)"))
        self.button_add.setText(_translate("Form", "+"))
from kamzik3 import resource_kamzik3_rc
