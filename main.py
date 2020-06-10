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

        self.websiteLabel = QLabel("Website")
        self.websiteText = QPlainTextEdit()
        self.websiteLayout = QHBoxLayout()
        self.websiteLayout.addWidget(self.websiteLabel)
        self.websiteLayout.addWidget(self.websiteText)

        self.loginLabel = QLabel("Login")
        self.loginText = QPlainTextEdit()
        self.loginLayout = QHBoxLayout()
        self.loginLayout.addWidget(self.loginLabel)
        self.loginLayout.addWidget(self.loginText)

        self.passwordLabel = QLabel("Password")
        self.passwordText = QPlainTextEdit()
        self.passwordLayout = QHBoxLayout()
        self.passwordLayout.addWidget(self.passwordLabel)
        self.passwordLayout.addWidget(self.passwordText)

        self.addButton = QPushButton("Add")

        self.addLayout = QVBoxLayout()
        self.addLayout.addLayout(self.websiteLayout)
        self.addLayout.addLayout(self.loginLayout)
        self.addLayout.addLayout(self.passwordLayout)

    def check_password(self):
        if self.enterPasswordText.toPlainText() == "qqq":
            self.change_menu()
        else:
            self.infoText.setText("WRONG!")

    def change_menu(self):
        self.setLayout(self.addLayout)


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
