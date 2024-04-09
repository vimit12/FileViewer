import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QFileDialog, QLineEdit, QTableWidget, QTableWidgetItem, QLabel, QHBoxLayout, QHeaderView
import pandas as pd


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Excel Data Viewer")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.column_search_layout = QHBoxLayout()
        self.layout.addLayout(self.column_search_layout)

        self.lbl_column_name = QLabel("Enter Column Name:")
        self.column_search_layout.addWidget(self.lbl_column_name)

        self.column_input = QLineEdit()
        self.column_search_layout.addWidget(self.column_input)

        self.search_layout = QHBoxLayout()
        self.layout.addLayout(self.search_layout)

        self.lbl_search = QLabel("Enter Search Text:")
        self.search_layout.addWidget(self.lbl_search)

        self.search_input = QLineEdit()
        self.search_layout.addWidget(self.search_input)

        self.button_layout = QHBoxLayout()
        self.layout.addLayout(self.button_layout)

        self.btn_select_file = QPushButton("Select Excel File")
        self.btn_select_file.clicked.connect(self.select_excel_file)
        self.button_layout.addWidget(self.btn_select_file)

        self.btn_search = QPushButton("Search")
        self.btn_search.clicked.connect(self.search_text)
        self.button_layout.addWidget(self.btn_search)

        self.table = QTableWidget()
        self.layout.addWidget(self.table)

    def select_excel_file(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Excel files (*.xlsx *.xls)")
        file_dialog.setViewMode(QFileDialog.Detail)

        if file_dialog.exec_():
            file_paths = file_dialog.selectedFiles()
            if file_paths:
                excel_file_path = file_paths[0]
                self.load_excel_data(excel_file_path)

    def load_excel_data(self, excel_file_path):
        try:
            self.df = pd.read_excel(excel_file_path)
            self.display_data()
        except Exception as e:
            print("Error loading Excel file:", e)

    def display_data(self):
        self.table.clear()

        if hasattr(self, "df"):
            self.table.setRowCount(len(self.df))
            self.table.setColumnCount(len(self.df.columns))
            self.table.setHorizontalHeaderLabels(self.df.columns)

            for i, row in self.df.iterrows():
                for j, value in enumerate(row):
                    item = QTableWidgetItem(str(value))
                    self.table.setItem(i, j, item)

            # Set column width and text wrapping
            for i in range(len(self.df.columns)):
                self.table.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeToContents)
                self.table.horizontalHeaderItem(i).setTextAlignment(0x0001 | 0x0080)
            self.table.setWordWrap(True)

            self.table.setSortingEnabled(True)

    def search_text(self):
        search_text = self.search_input.text()
        column_name = self.column_input.text()

        if hasattr(self, "df"):
            if column_name in self.df.columns:
                search_result = self.df[self.df[column_name].str.contains(search_text, case=False)]

                self.display_search_result(search_result)
            else:
                print(f"Column '{column_name}' not found in Excel file.")

    def display_search_result(self, search_result):
        self.table.clear()
        if not search_result.empty:
            self.table.setRowCount(len(search_result))
            self.table.setColumnCount(len(search_result.columns))
            self.table.setHorizontalHeaderLabels(search_result.columns)
            print(search_result)
            for i, row in search_result.iterrows():
                for j, value in enumerate(row):
                    item = QTableWidgetItem(str(value))
                    self.table.setItem(i, j, item)

            # Set column width and text wrapping
            for i in range(len(self.df.columns)):
                self.table.horizontalHeader().setSectionResizeMode(i, QHeaderView.ResizeToContents)
                self.table.horizontalHeaderItem(i).setTextAlignment(0x0001 | 0x0080)
            self.table.setWordWrap(True)
            self.table.setSortingEnabled(True)

        else:
            print("No matching rows found.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
