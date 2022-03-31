from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QLineEdit
from PyQt5.QtGui import QIcon
equation = []


def pushed(eq):
    equation.append(eq)


app = QApplication([])
window = QWidget()
window.setWindowIcon(QIcon('icon/icon1.jpg'))
window.setStyleSheet(
    "background-color: rgb(50, 100, 170);"
    "background-image: url('/backgrounds/colored.png');"
    "background-repeat: no-repeat;"
    "background-position: center;"
)

window.setWindowTitle('Calculator')
'window.setFixedSize(325, 400)'
window.move(60, 15)
zero_point = ['.', 0, '=']
for i in range(12):
    numbers = QPushButton(window)
    if i < 9:
        numbers.clicked.connect(lambda: equation.append(i))
        numbers.setText(str(i+1))
    else:
        numbers.setText(str(zero_point[i - 9]))
        numbers.clicked.connect(lambda: equation.append(zero_point[i - 9]))

    numbers.setGeometry(60 * (i % 3) + 10, 42 * (i // 3 + 3) + 8, 61, 41)
    numbers.setStyleSheet("background-color: rgba(10, 180, 255, 150); "
                          "border-style: outset; "
                          "border-width: 2px; "
                          "border-radius: 15px; "
                          "border-color: rgba(150, 150, 255, 50); "
                          "font-family: Times;"
                          "font-size: 17px;")
    if i == 11:
        numbers.setGeometry(60 * (i % 3) + 10, 42 * (i // 3 + 3) + 8, 63, 43)
        numbers.setStyleSheet("background-color: rgba(50, 160, 230); "
                              "border-style: outset; "
                              "border-width: 2px; "
                              "border-radius: 12px; "
                              "border-color: rgba(100, 250, 255);"
                              "font-family: Times;"
                              "font-size: 15px;")

operators_1 = ['^', '+', '-', '*', 'asin', 'acos', 'atan', 'π', '⌫']
for i in range(4):
    operators = QPushButton(window)
    operators.setText(operators_1[i])
    operators.clicked.connect(lambda: equation.append(i))
    operators.setGeometry(194, 43 * (i + 1) + 88, 60, 42)
    operators.setStyleSheet("background-color: rgba(50, 160, 230); "
                            "border-style: outset; "
                            "border-width: 2px; "
                            "border-radius: 10px; "
                            "border-color: rgba(100, 250, 255);"
                            "font-family: Times;"
                            "font-size: 15px;")
for i in range(5):
    operators = QPushButton(window)
    operators.setText(operators_1[i + 4])
    operators.clicked.connect(lambda: equation.append(operators_1[i + 4]))
    operators.setGeometry(61 * (i % 5) + 10, 50, 60, 40)
    operators.setStyleSheet("background-color: rgba(50, 160, 230); "
                            "border-style: outset; "
                            "border-width: 2px; "
                            "border-radius: 10px; "
                            "border-color: rgba(100, 250, 255);"
                            "font-family: Times;"
                            "font-size: 14px; ")

operators_2 = ['sin', 'cos', 'tan', 'x', '∫f(x) dx']
for i in range(5):
    operators = QPushButton(window)
    operators.setText(operators_2[i])
    operators.clicked.connect(lambda: equation.append(operators_2[i]))
    operators.setGeometry(61 * (i % 5) + 10, 90, 60, 40)
    operators.setStyleSheet("background-color: rgba(50, 160, 230); "
                            "border-style: outset; "
                            "border-width: 2px; "
                            "border-radius: 10px; "
                            "border-color: rgba(100, 250, 255); "
                            "font-family: Times;"
                            "font-size: 14px;")

operators_3 = ['√', 'd/dx', 'x!', '÷']
for i in range(4):
    operators = QPushButton(window)
    operators.setText(operators_3[i])
    operators.clicked.connect(lambda: equation.append(operators_3[i]))
    operators.setGeometry(254, 43 * (i + 1) + 88, 60, 42)
    operators.setStyleSheet("background-color: rgba(50, 160, 230); "
                            "border-style: outset; "
                            "border-width: 2px; "
                            "border-radius: 10px; "
                            "border-color: rgba(100, 250, 255); "
                            "font-family: Times;"
                            "font-size: 14px;")

inputs = QLineEdit(window)
inputs.setGeometry(12, 5, 300, 40)
inputs.setStyleSheet(
    "font-size: 16px;"
    "font: bold;"
    "border-width: 2px;"
    "border-radius: 10px;"
    "border-color: rgba(10, 250, 255);"
    "background-color: rgba(220, 220, 220);"
)


window.show()
app.exec()
window.close()
print(equation)
