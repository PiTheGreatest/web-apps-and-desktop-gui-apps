from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtWidgets import QPushButton, QFileDialog
from PyQt6.QtCore import Qt
from pathlib import Path

app = QApplication([])
window = QWidget()
window.setWindowTitle("File Destroyer")
layout = QVBoxLayout()

def open_files():
    global filenames
    filenames, _ = QFileDialog.getOpenFileNames(window, "Select Files")
    message.setText("\n".join(filenames))

def destroy_files():
    for filename in filenames:
        path = Path(filename)
        with open(path, "wb") as file:
            file.write(b"")
        path.unlink()
    message.setText("Files successfully destroyed!")

description = QLabel('Select the files you want to destroy. The files would be <font color = "red">permanently</font> deleted.')
layout.addWidget(description)

open_btn = QPushButton("Open files")
open_btn.setToolTip("Select the files you want to destroy")
open_btn.setFixedWidth(100)
layout.addWidget(open_btn, alignment= Qt.AlignmentFlag.AlignCenter)
open_btn.clicked.connect(open_files)

destroy_btn = QPushButton("Destroy files")
destroy_btn.setFixedWidth(100)
layout.addWidget(destroy_btn, alignment= Qt.AlignmentFlag.AlignCenter)
destroy_btn.clicked.connect(destroy_files)

message = QLabel("")
layout.addWidget(message, alignment= Qt.AlignmentFlag.AlignCenter)

window.setLayout(layout)
window.show()
app.exec()
