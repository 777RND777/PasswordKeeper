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

        self.passwordText = QPlainTextEdit(self)
        self.passwordText.resize(180, 40)
        self.passwordText.move(70, 120)

        self.passwordButton = QPushButton(self)
        self.passwordButton.setText("Submit")
        self.passwordButton.resize(150, 40)
        self.passwordButton.move(85, 190)
        self.passwordButton.clicked.connect(self.check_password)

    def check_password(self):
        if self.passwordText.toPlainText() == "qqq":
            self.infoText.setText("Correct!")
        else:
            self.infoText.setText("WRONG!")


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
