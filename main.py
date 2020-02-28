from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QMessageBox, QPlainTextEdit, QPushButton
import sys


class MainWindow(QMainWindow):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.setWindowTitle("Password Keeper")
        self.resize(320, 240)

        self.infoText = QLabel(self)
        self.infoText.setText("Type password:")
        self.infoText.resize(180, 40)
        self.infoText.move(70, 50)

        self.enterPasswordText = QPlainTextEdit(self)
        self.enterPasswordText.resize(180, 40)
        self.enterPasswordText.move(70, 120)

        self.passwordButton = QPushButton(self)
        self.passwordButton.setText("Submit")
        self.passwordButton.resize(150, 40)
        self.passwordButton.move(85, 190)
        self.passwordButton.clicked.connect(self.check_password)

        self.loginText = QPlainTextEdit(self)
        self.loginText.hide()
        self.passwordText = QPlainTextEdit(self)
        self.passwordText.hide()
        self.websiteText = QPlainTextEdit(self)
        self.websiteText.hide()
        self.addButton = QPushButton(self)
        self.addButton.setText("Add")
        self.addButton.hide()

    def check_password(self):
        if self.enterPasswordText.toPlainText() == "qqq":
            self.change_menu()
        else:
            self.infoText.setText("WRONG!")

    def change_menu(self):
        self.infoText.hide()
        self.enterPasswordText.hide()
        self.passwordButton.hide()
        self.loginText.show()
        self.passwordText.show()
        self.websiteText.show()
        self.addButton.show()


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
