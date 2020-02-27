from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QMessageBox
import sys


class MainWindow(QMainWindow):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.setWindowTitle("Password Keeper")
        self.resize(320, 240)

        self.passwordButton = QPushButton(self)
        self.passwordButton.setText("Submit")
        self.passwordButton.resize(150, 40)
        self.passwordButton.move(85, 190)


def catch_exceptions(t, val, tb):
    QMessageBox.critical(None, 'An exception was raised', 'Exception type: {}'.format(t))
    old_hook(t, val, tb)


if __name__ == '__main__':
    old_hook = sys.excepthook
    sys.excepthook = catch_exceptions

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
