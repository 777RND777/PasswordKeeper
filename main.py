from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import password
import sys
import table


class MainWindow(QMainWindow):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)

        self.setWindowTitle("Password Keeper")

        self.passwordWidget = password.PasswordWidget()
        self.passwordWidget.switch_window.connect(self.switch_window)
        self.setCentralWidget(self.passwordWidget)

    def switch_window(self):
        self.setCentralWidget(table.ProgramWidget())


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
