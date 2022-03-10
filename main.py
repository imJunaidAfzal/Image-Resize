import sys

from PyQt5.QtWidgets import QApplication, QStyleFactory

from image_resizer import ImageResizer


if __name__ == '__main__':
    login_user = 'Guest'
    app = QApplication(sys.argv)
    app.setStyle(QStyleFactory.create("Fusion"))

    reg_win = ImageResizer()
    reg_win.show()

    sys.exit(app.exec_())
