from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtWidgets import QTableView


class DBTable(QTableView):
    def __init__(self):
        super(DBTable, self).__init__()

        info = fill_table()
        self.setModel(info)


def fill_table():
    info = QStandardItemModel()
    for program in get_saved_info():
        first = QStandardItem(program)
        second = QStandardItem(program)
        third = QStandardItem(program)
        info.appendRow([first, second, third])
    info.setHorizontalHeaderLabels(["Website", "Login", "Password"])
    return info


def get_saved_info():
    return ["AAA", "BBB"]
