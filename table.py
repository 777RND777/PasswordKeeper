from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


class DBTable(QTableWidget):
    def __init__(self):
        super(DBTable, self).__init__()

        self.setColumnCount(3)
        self.setHorizontalHeaderLabels(["Website", "Login", "Password"])

    def add_row(self, website, login, password):
        row_position = self.rowCount()
        self.insertRow(row_position)
        self.setItem(row_position, 0, QTableWidgetItem(website))
        self.setItem(row_position, 1, QTableWidgetItem(login))
        self.setItem(row_position, 2, QTableWidgetItem(password))
