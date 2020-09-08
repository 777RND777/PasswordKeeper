from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
import base64


class DBTable(QTableWidget):
    def __init__(self):
        super(DBTable, self).__init__()

        self.setColumnCount(3)

        self.setHorizontalHeaderLabels(["Website", "Login", "Password"])
        self.get_saved_info()

    def get_saved_info(self):
        try:
            with open("db", "r") as f:
                data = f.readlines()
            for line in data:
                line = base64.b64decode(line[2:-2].encode()).decode()
                line = line.split("|")
                if len(line) == 3:
                    self.add_row(line[0], line[1], line[2].replace("\n", ""))
        except FileNotFoundError:
            pass

    def add_row(self, website, login, password):
        row_position = self.rowCount()
        self.insertRow(row_position)
        self.setItem(row_position, 0, QTableWidgetItem(website))
        self.setItem(row_position, 1, QTableWidgetItem(login))
        self.setItem(row_position, 2, QTableWidgetItem(password))

    def save_info(self):
        with open("db", "w") as f:
            for i in range(self.rowCount()):
                row = self.item(i, 0).text() + "|" + self.item(i, 1).text() + "|" + self.item(i, 2).text()
                f.write(str(base64.b64encode(row.encode())) + "\n")
