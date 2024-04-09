import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QVBoxLayout, QWidget, QTextEdit, QMessageBox
import pytesseract
from PIL import Image


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Text Extractor")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.text_edit = QTextEdit()
        self.layout.addWidget(self.text_edit)

        self.btn_open_image = QPushButton("Open Image")
        self.btn_open_image.clicked.connect(self.open_image)
        self.layout.addWidget(self.btn_open_image)

        self.btn_save_text = QPushButton("Save Text")
        self.btn_save_text.clicked.connect(self.save_text)
        self.layout.addWidget(self.btn_save_text)

        self.extracted_text = ""

    def open_image(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Images (*.png *.jpg *.bmp *.jpeg)")
        file_dialog.setViewMode(QFileDialog.Detail)

        if file_dialog.exec_():
            file_paths = file_dialog.selectedFiles()
            if file_paths:
                image_path = file_paths[0]
                self.extract_text(image_path)

    def extract_text(self, image_path):
        try:
            with Image.open(image_path) as img:
                text = pytesseract.image_to_string(img)
                self.extracted_text = text
                self.text_edit.setText(text)
        except Exception as e:
            self.extracted_text = ""
            self.text_edit.setText("Error: " + str(e))
            QMessageBox.warning(self, "Extraction Error", "Failed to extract text from the image.")

    def save_text(self):
        if self.extracted_text:
            file_dialog = QFileDialog()
            file_dialog.setFileMode(QFileDialog.AnyFile)
            file_dialog.setAcceptMode(QFileDialog.AcceptSave)
            file_dialog.setNameFilter("Text files (*.txt)")

            if file_dialog.exec_():
                file_path = file_dialog.selectedFiles()[0]
                with open(file_path, "w") as f:
                    f.write(self.extracted_text)
        else:
            QMessageBox.warning(self, "No Text to Save", "There is no text to save.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
