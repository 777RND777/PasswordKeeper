from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QMessageBox, QPushButton, QVBoxLayout, QWidget
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
        self.addButton.setShortcut("Return")

        self.table = DBTable()

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.websiteLayout)
        self.mainLayout.addLayout(self.loginLayout)
        self.mainLayout.addLayout(self.passwordLayout)
        self.mainLayout.addWidget(self.addButton, alignment=Qt.AlignCenter)
        self.mainLayout.addWidget(self.table, alignment=Qt.AlignBaseline)

        self.setLayout(self.mainLayout)

    def add_info(self):
        if len(self.websiteText.text()) == 0:
            QMessageBox.critical(None, "Error", "Website field is empty.")
        elif len(self.loginText.text()) == 0:
            QMessageBox.critical(None, "Error", "Login field is empty.")
        elif len(self.passwordText.text()) == 0:
            QMessageBox.critical(None, "Error", "Password field is empty.")
        else:
            self.table.add_row(self.websiteText.text(), self.loginText.text(), self.passwordText.text())
            self.empty_fields()

    def empty_fields(self):
        self.websiteText.setText("")
        self.loginText.setText("")
        self.passwordText.setText("")
