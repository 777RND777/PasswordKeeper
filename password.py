from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget


class PasswordWidget(QWidget):
    switch_window = pyqtSignal()

    def __init__(self):
        super(PasswordWidget, self).__init__()

        self.infoText = QLabel()
        self.infoText.setText("Type password")

        self.enterText = QLineEdit()

        self.submitButton = QPushButton()
        self.submitButton.setText("Submit")
        self.submitButton.clicked.connect(self.check_password)

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.infoText, alignment=Qt.AlignCenter)
        self.mainLayout.addWidget(self.enterText, alignment=Qt.AlignBaseline)
        self.mainLayout.addWidget(self.submitButton, alignment=Qt.AlignBaseline)

        self.setLayout(self.mainLayout)

    def check_password(self):
        if self.enterText.text() == "qqq":
            self.switch_window.emit()
        else:
            self.infoText.setText("WRONG!")
            self.enterText.setText("")
