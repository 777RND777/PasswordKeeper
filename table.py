from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem


class DBTable(QTableWidget):
    def __init__(self):
        super(DBTable, self).__init__()

        self.setColumnCount(3)

        self.setHorizontalHeaderLabels(["Website", "Login", "Password"])
        self.get_saved_info()

    def get_saved_info(self):
        with open("db", "r") as f:
            data = f.readlines()
        for line in data:
            line = line.split("|")
            if len(line) == 3:
                self.add_row(line[0], line[1], line[2][:-1])

    def add_row(self, website, login, password):
        row_position = self.rowCount()
        self.insertRow(row_position)
        self.setItem(row_position, 0, QTableWidgetItem(website))
        self.setItem(row_position, 1, QTableWidgetItem(login))
        self.setItem(row_position, 2, QTableWidgetItem(password))

    def save_info(self):
        with open("db", "w") as f:
            for i in range(self.rowCount()):
                f.write(self.item(i, 0).text() + "|" + self.item(i, 1).text() + "|" + self.item(i, 2).text() + "\n")
