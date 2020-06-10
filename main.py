from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMessageBox,
                             QPlainTextEdit, QPushButton, QVBoxLayout, QWidget)
import sys


class MainWindow(QWidget):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.setWindowTitle("Password Keeper")

        self.infoText = QLabel()
        self.infoText.setText("Type password")

        self.enterPasswordText = QPlainTextEdit()

        self.passwordButton = QPushButton()
        self.passwordButton.setText("Submit")
        self.passwordButton.clicked.connect(self.check_password)

        self.passwordLayout = QVBoxLayout()
        self.passwordLayout.addWidget(self.infoText, alignment=Qt.AlignCenter)
        self.passwordLayout.addWidget(self.enterPasswordText, alignment=Qt.AlignBaseline)
        self.passwordLayout.addWidget(self.passwordButton, alignment=Qt.AlignBaseline)

        self.setLayout(self.passwordLayout)

        self.websiteLabel = QLabel()
        self.websiteText = QPlainTextEdit()
        self.loginLabel = QLabel()
        self.loginText = QPlainTextEdit()
        self.passwordLabel = QLabel()
        self.passwordText = QPlainTextEdit()
        self.addButton = QPushButton()

    def check_password(self):
        if self.enterPasswordText.toPlainText() == "qqq":
            self.change_menu()
        else:
            self.infoText.setText("WRONG!")

    def change_menu(self):

        self.websiteLabel.setText("Website")
        self.websiteLabel.show()
        self.websiteText.show()

        self.loginLabel.setText("Login")
        self.loginLabel.show()
        self.loginText.show()

        self.passwordLabel.setText("Password")
        self.passwordLabel.show()
        self.passwordText.show()

        self.addButton.setText("Add")
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
