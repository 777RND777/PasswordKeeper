from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from table import DBTable


class ProgramWidget(QWidget):
    def __init__(self):
        super(ProgramWidget, self).__init__()

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
        self.addButton.clicked.connect(self.add_info)

        self.table = DBTable()

        self.dbLayout = QVBoxLayout()
        self.dbLayout.addLayout(self.websiteLayout)
        self.dbLayout.addLayout(self.loginLayout)
        self.dbLayout.addLayout(self.passwordLayout)
        self.dbLayout.addWidget(self.addButton, alignment=Qt.AlignCenter)
        self.dbLayout.addWidget(self.table, alignment=Qt.AlignBaseline)

        self.setLayout(self.dbLayout)

    def add_info(self):
        self.table.add_row(self.websiteText.text(), self.loginText.text(), self.passwordText.text())
        self.empty_fields()

    def empty_fields(self):
        self.websiteText.setText("")
        self.loginText.setText("")
        self.passwordText.setText("")
