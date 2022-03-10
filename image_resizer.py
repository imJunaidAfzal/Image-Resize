from PyQt5.QtGui import QPixmap
import PyQt5
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QLabel

import resources
from image_resize import resize_profile
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QWidget
from PyQt5 import QtCore, QtGui, QtWidgets


class ImageResizer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.window = uic.loadUi("image_resizer.ui", self)
        self.select_img_button.clicked.connect(self.handle_open_image)
        self.resize_btn.clicked.connect(self.handle_resize_button)
        self.filenames = None

    def handle_open_image(self):
        try:
            dlg = QFileDialog()
            dlg.setFileMode(QFileDialog.AnyFile)

            # dlg.setFilter("(*.jpg)")


            if dlg.exec_():
                self.filenames = dlg.selectedFiles()

                self.image_show_label.setPixmap(QPixmap(self.filenames[0]))
                self.image_show_label.setScaledContents(True)
                self.image_show_label.setMaximumSize(1024, 2000)
                self.image_show_label.show()

                print(filenames)
        except Exception as ex:
            dia = QDialog()
            dia.setParent(self)
            dia.show()

    def handle_resize_button(self):
        if self.filenames:

            try:
                location = str(QFileDialog.getExistingDirectory(self, "Select Directory to Save File"))
                print(location)
                location = location + '/'
                res = resize_profile(self.filenames[0],
                                     dim=(self.height_input.value(), self.width_input.value()),
                                     save_path=location
                                     )
                dia = QDialog(self)
                dia.setWindowTitle('File Saved Successfully')
                dia.setModal(True)
                lbl = QLabel(dia)
                lbl.setWordWrap(True)
                lbl.setText(f'Image Saved at : {str(res[1])}')
                font = QtGui.QFont()
                font.setPointSize(24)
                lbl.setFont(font)
                lbl.setStyleSheet("""
                            border : 1px solid ;
                            border-color : rgb(78, 154, 6);
                            background-color: rgba(52, 214, 22, 133);
                            """)
                lbl.show()
                dia.show()
            except Exception as ex:

                dia = QDialog(self)
                dia.setWindowTitle('Zero Size Error')
                dia.setModal(True)
                lbl = QLabel(dia)
                lbl.setText(f'Error: {str(ex)}')
                font = QtGui.QFont()
                font.setPointSize(24)
                lbl.setFont(font)
                lbl.setStyleSheet("""
            border : 1px solid ;
            border-color : red;
            background-color: rgba(204, 0, 0, 0.2);
            """)
                lbl.show()
                dia.show()


