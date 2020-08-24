from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget


class ProgramWidget(QWidget):
    def __init__(self, parent=None):
        super(ProgramWidget, self).__init__(parent)

        self.websiteLabel = QLabel("Website")
        self.websiteText = QLineEdit()
        self.websiteLayout = QHBoxLayout()
        self.websiteLayout.addWidget(self.websiteLabel, alignment=Qt.AlignCenter)
        self.websiteLayout.addWidget(self.websiteText, alignment=Qt.AlignCenter)

        self.loginLabel = QLabel("Login")
        self.loginText = QLineEdit()
        self.loginLayout = QHBoxLayout()
        self.loginLayout.addWidget(self.loginLabel, alignment=Qt.AlignCenter)
        self.loginLayout.addWidget(self.loginText, alignment=Qt.AlignCenter)

        self.passwordLabel = QLabel("Password")
        self.passwordText = QLineEdit()
        self.passwordLayout = QHBoxLayout()
        self.passwordLayout.addWidget(self.passwordLabel, alignment=Qt.AlignCenter)
        self.passwordLayout.addWidget(self.passwordText, alignment=Qt.AlignCenter)

        self.addButton = QPushButton("Add")

        self.dbLayout = QVBoxLayout()
        self.dbLayout.addLayout(self.websiteLayout)
        self.dbLayout.addLayout(self.loginLayout)
        self.dbLayout.addLayout(self.passwordLayout)

        self.setLayout(self.dbLayout)
