import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

import 主界面

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainwindow = 主界面.Ui_MainWindow()

    mainwindow.show()
    sys.exit(app.exec_())