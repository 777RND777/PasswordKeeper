from PyQt5.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget


class ProgramWidget(QWidget):
    def __init__(self):
        super(ProgramWidget, self).__init__()

        self.websiteLabel = QLabel("Website")
        self.websiteText = QLineEdit()
        self.websiteLayout = QHBoxLayout()
        self.websiteLayout.addWidget(self.websiteLabel)
        self.websiteLayout.addWidget(self.websiteText)

        self.loginLabel = QLabel("Login")
        self.loginText = QLineEdit()
        self.loginLayout = QHBoxLayout()
        self.loginLayout.addWidget(self.loginLabel)
        self.loginLayout.addWidget(self.loginText)

        self.passwordLabel = QLabel("Password")
        self.passwordText = QLineEdit()
        self.passwordLayout = QHBoxLayout()
        self.passwordLayout.addWidget(self.passwordLabel)
        self.passwordLayout.addWidget(self.passwordText)

        self.addButton = QPushButton("Add")

        self.addLayout = QVBoxLayout()
        self.addLayout.addLayout(self.websiteLayout)
        self.addLayout.addLayout(self.loginLayout)
        self.addLayout.addLayout(self.passwordLayout)
