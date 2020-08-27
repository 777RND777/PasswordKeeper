from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import password
import sys
import menu


class MainWindow(QMainWindow):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)

        self.setWindowTitle("Password Keeper")

        self.passwordWidget = password.PasswordWidget()
        self.passwordWidget.switch_window.connect(self.pass_check)
        self.setCentralWidget(self.passwordWidget)
        self.pass_check()

    def pass_check(self):
        self.setCentralWidget(menu.ProgramWidget())


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
