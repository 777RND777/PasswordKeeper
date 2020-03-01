from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QMessageBox, QPlainTextEdit, QPushButton, QTableView
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

        self.enterPasswordInput = QPlainTextEdit(self)
        self.enterPasswordInput.setPlaceholderText("Password...")
        self.enterPasswordInput.resize(180, 40)
        self.enterPasswordInput.move(70, 120)

        self.passwordButton = QPushButton(self)
        self.passwordButton.setText("Submit")
        self.passwordButton.resize(150, 40)
        self.passwordButton.move(85, 190)
        self.passwordButton.clicked.connect(self.check_password)

        self.websiteText = QLabel(self)
        self.websiteText.hide()
        self.websiteInput = QPlainTextEdit(self)
        self.websiteInput.hide()
        self.loginText = QLabel(self)
        self.loginText.hide()
        self.loginInput = QPlainTextEdit(self)
        self.loginInput.hide()
        self.passwordText = QLabel(self)
        self.passwordText.hide()
        self.passwordInput = QPlainTextEdit(self)
        self.passwordInput.hide()
        self.addButton = QPushButton(self)
        self.addButton.hide()

    def check_password(self):
        if self.enterPasswordInput.toPlainText() == "qqq":
            self.change_menu()
        else:
            self.infoText.setText("WRONG!")

    def change_menu(self):
        self.resize(320, 480)
        self.infoText.hide()
        self.enterPasswordInput.hide()
        self.passwordButton.hide()

        self.websiteText.show()
        self.websiteText.setText("Website:")
        self.websiteText.move(20, 20)
        self.websiteInput.show()
        self.websiteInput.resize(180, 40)
        self.websiteInput.move(120, 20)

        self.loginText.show()
        self.loginText.setText("Login:")
        self.loginText.move(20, 70)
        self.loginInput.show()
        self.loginInput.resize(180, 40)
        self.loginInput.move(120, 70)

        self.passwordText.show()
        self.passwordText.setText("Password:")
        self.passwordText.move(20, 120)
        self.passwordInput.show()
        self.passwordInput.resize(180, 40)
        self.passwordInput.move(120, 120)

        self.addButton.show()
        self.addButton.setText("Add")
        self.addButton.resize(180, 40)
        self.addButton.move(70, 170)


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
