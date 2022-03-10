# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'image_resizer.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_image_resizer_mainwin(object):
    def setupUi(self, image_resizer_mainwin):
        image_resizer_mainwin.setObjectName("image_resizer_mainwin")
        image_resizer_mainwin.resize(986, 768)
        image_resizer_mainwin.setMaximumSize(QtCore.QSize(1024, 768))
        image_resizer_mainwin.setWindowOpacity(0.98)
        image_resizer_mainwin.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(image_resizer_mainwin)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.hadder_frame = QtWidgets.QFrame(self.frame_2)
        self.hadder_frame.setMaximumSize(QtCore.QSize(9999999, 80))
        self.hadder_frame.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.hadder_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.hadder_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hadder_frame.setObjectName("hadder_frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.hadder_frame)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.left_header_frame = QtWidgets.QFrame(self.hadder_frame)
        self.left_header_frame.setMaximumSize(QtCore.QSize(200, 16777215))
        self.left_header_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.left_header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_header_frame.setObjectName("left_header_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.left_header_frame)
        self.horizontalLayout_4.setContentsMargins(14, -1, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.select_img_button = QtWidgets.QPushButton(self.left_header_frame)
        self.select_img_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.select_img_button.setIcon(icon)
        self.select_img_button.setIconSize(QtCore.QSize(32, 32))
        self.select_img_button.setDefault(True)
        self.select_img_button.setFlat(False)
        self.select_img_button.setObjectName("select_img_button")
        self.horizontalLayout_4.addWidget(self.select_img_button)
        self.horizontalLayout_2.addWidget(self.left_header_frame, 0, QtCore.Qt.AlignLeft)
        self.right_hadder_frame = QtWidgets.QFrame(self.hadder_frame)
        self.right_hadder_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.right_hadder_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_hadder_frame.setObjectName("right_hadder_frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.right_hadder_frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logo_label = QtWidgets.QLabel(self.right_hadder_frame)
        self.logo_label.setMaximumSize(QtCore.QSize(50, 16777215))
        self.logo_label.setText("")
        self.logo_label.setPixmap(QtGui.QPixmap(":/icons/logo.png"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setObjectName("logo_label")
        self.horizontalLayout_3.addWidget(self.logo_label)
        self.main_title_label = QtWidgets.QLabel(self.right_hadder_frame)
        font = QtGui.QFont()
        font.setFamily("Nakula")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.main_title_label.setFont(font)
        self.main_title_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.main_title_label.setObjectName("main_title_label")
        self.horizontalLayout_3.addWidget(self.main_title_label, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.right_hadder_frame, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout.addWidget(self.hadder_frame)
        self.verticalLayout.addWidget(self.frame_2, 0, QtCore.Qt.AlignTop)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 500))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.image_show_frame = QtWidgets.QFrame(self.frame)
        self.image_show_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.image_show_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.image_show_frame.setObjectName("image_show_frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.image_show_frame)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.image_show_label = QtWidgets.QLabel(self.image_show_frame)
        self.image_show_label.setStyleSheet("")
        self.image_show_label.setText("")
        self.image_show_label.setObjectName("image_show_label")
        self.horizontalLayout_7.addWidget(self.image_show_label)
        self.verticalLayout_2.addWidget(self.image_show_frame)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMinimumSize(QtCore.QSize(784, 70))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 70))
        self.frame_4.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setGeometry(QtCore.QRect(10, 10, 764, 50))
        self.frame_5.setMinimumSize(QtCore.QSize(764, 50))
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_5.setStyleSheet("background-color: rgb(46, 52, 54);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_3 = QtWidgets.QFrame(self.frame_5)
        self.frame_3.setGeometry(QtCore.QRect(138, 0, 387, 63))
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.height_input = QtWidgets.QSpinBox(self.frame_6)
        self.height_input.setStyleSheet("color: rgb(255, 255, 255);")
        self.height_input.setMaximum(1000)
        self.height_input.setObjectName("height_input")
        self.horizontalLayout_5.addWidget(self.height_input)
        self.horizontalLayout_10.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_3)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_4 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_9.addWidget(self.label_4)
        self.width_input = QtWidgets.QSpinBox(self.frame_7)
        self.width_input.setStyleSheet("color: rgb(255, 255, 255);")
        self.width_input.setMaximum(1000)
        self.width_input.setObjectName("width_input")
        self.horizontalLayout_9.addWidget(self.width_input)
        self.horizontalLayout_10.addWidget(self.frame_7)
        self.resize_btn = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.resize_btn.setFont(font)
        self.resize_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.resize_btn.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/resize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.resize_btn.setIcon(icon1)
        self.resize_btn.setIconSize(QtCore.QSize(32, 32))
        self.resize_btn.setAutoDefault(False)
        self.resize_btn.setDefault(True)
        self.resize_btn.setFlat(False)
        self.resize_btn.setObjectName("resize_btn")
        self.horizontalLayout_10.addWidget(self.resize_btn)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame)
        image_resizer_mainwin.setCentralWidget(self.centralwidget)

        self.retranslateUi(image_resizer_mainwin)
        QtCore.QMetaObject.connectSlotsByName(image_resizer_mainwin)

    def retranslateUi(self, image_resizer_mainwin):
        _translate = QtCore.QCoreApplication.translate
        image_resizer_mainwin.setWindowTitle(_translate("image_resizer_mainwin", "J. Image Resizer"))
        self.select_img_button.setText(_translate("image_resizer_mainwin", "Select Image"))
        self.main_title_label.setText(_translate("image_resizer_mainwin", "J. Image Resizer(JIS)"))
        self.label_2.setText(_translate("image_resizer_mainwin", "Height"))
        self.label_4.setText(_translate("image_resizer_mainwin", "Width"))
        self.resize_btn.setText(_translate("image_resizer_mainwin", "Resize"))
import image_resize_resources_rc
import resources_rc