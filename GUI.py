from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QWidget

app = QApplication([])
window = QWidget()
window.setWindowTitle('Calculator')
window.setGeometry(100, 100, 280, 80)
window.move(60, 15)
helloMsg = QLabel('<h1>CALCULATOR!</h1>', parent=window)
helloMsg.move(60, 15)
window.show()
app.exec()
