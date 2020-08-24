from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget


class PasswordWidget(QWidget):
    switch_window = pyqtSignal()

    # TODO parent ???
    def __init__(self, parent=None):
        super(PasswordWidget, self).__init__(parent)

        self.infoText = QLabel()
        self.infoText.setText("Type password")

        self.enterPasswordText = QLineEdit()

        self.passwordButton = QPushButton()
        self.passwordButton.setText("Submit")
        self.passwordButton.clicked.connect(self.check_password)

        self.passwordLayout = QVBoxLayout()
        self.passwordLayout.addWidget(self.infoText, alignment=Qt.AlignCenter)
        self.passwordLayout.addWidget(self.enterPasswordText, alignment=Qt.AlignBaseline)
        self.passwordLayout.addWidget(self.passwordButton, alignment=Qt.AlignBaseline)

        self.setLayout(self.passwordLayout)

    def check_password(self):
        if self.enterPasswordText.text() == "qqq":
            self.switch_window.emit()
        else:
            self.infoText.setText("WRONG!")
            self.enterPasswordText.setText("")
