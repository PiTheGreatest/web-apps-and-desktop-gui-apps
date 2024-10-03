from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton 
from PyQt6.QtWidgets import QLineEdit, QComboBox, QHBoxLayout
from PyQt6.QtCore import Qt
from bs4 import BeautifulSoup
import requests

def get_currency_rate(in_currency, out_currency):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1#google_vignette"
    source_code_content = requests.get(url).text
    soup_object = BeautifulSoup(source_code_content, "html.parser")
    currency_rate = soup_object.find("span", class_ = "ccOutputRslt").get_text()
    rate_string_list = currency_rate.split(" ")
    float_from_string_list = float(rate_string_list[0])
    return float_from_string_list

def make_currency():
    input_text = float(text.text())
    in_cur = in_combo.currentText()
    target_cur = target_combo.currentText()
    rate = get_currency_rate(in_cur, target_cur)
    output = round(input_text * rate, 2)
    msg = f"{input_text} {in_cur} is equal to {output} {target_cur}"
    output_label.setText(msg)

app = QApplication([])
window = QWidget()
window.setWindowTitle("Currency Converter")

layout = QVBoxLayout()

layout1 = QHBoxLayout()
layout.addLayout(layout1)

output_label = QLabel("")
layout.addWidget(output_label)

layout2 = QVBoxLayout()
layout1.addLayout(layout2)

layout3 = QVBoxLayout()
layout1.addLayout(layout3)

in_combo = QComboBox()
currencies = ["USD", "EUR", "GBP", "INR", "CAD", "SGD", "AED", "BGN", "ARS", "BND", "BHD", "BRL", "CHF", "BWP", "CZK", "CLP", "CHY"]
in_combo.addItems(currencies)
layout2.addWidget(in_combo)

target_combo = QComboBox()
target_combo.addItems(currencies)
layout2.addWidget(target_combo)

text = QLineEdit()
layout3.addWidget(text)

btn = QPushButton("Convert")
layout3.addWidget(btn, Qt.AlignmentFlag.AlignRight, Qt.AlignmentFlag.AlignBottom)
btn.clicked.connect(make_currency)

window.setLayout(layout)
window.show()
app.exec()