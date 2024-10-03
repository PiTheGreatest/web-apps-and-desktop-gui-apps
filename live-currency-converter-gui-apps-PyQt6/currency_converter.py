from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit
from bs4 import BeautifulSoup
import requests

def get_currency_rate(in_currency = 'EUR', out_currency = "USD"):
    url = f"https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1#google_vignette"
    source_code_content = requests.get(url).text
    soup_object = BeautifulSoup(source_code_content, "html.parser")
    currency_rate = soup_object.find("span", class_ = "ccOutputRslt").get_text()
    rate_string_list = currency_rate.split(" ")
    float_from_string_list = float(rate_string_list[0])
    return float_from_string_list

def make_currency():
    input_text = float(text.text())
    rate = get_currency_rate()
    output = round(input_text * rate, 2)
    output_label.setText(str(output))

app = QApplication([])
window = QWidget()
window.setWindowTitle("Currency Converter")

layout = QVBoxLayout()

text = QLineEdit()
layout.addWidget(text)

btn = QPushButton("Convert")
layout.addWidget(btn)
btn.clicked.connect(make_currency)

output_label = QLabel("")
layout.addWidget(output_label)

window.setLayout(layout)
window.show()
app.exec()