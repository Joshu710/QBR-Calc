from logging import PlaceHolder
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Passer Rating Calculator")
        self.setGeometry(50, 50, 320, 500)


        self.compLabel = QLabel(self)
        self.compLabel.setText("Enter # of Completions")
        self.compLabel.adjustSize()
        self.compLabel.move(20,20)
        self.compBox = QLineEdit(self)
        self.compBox.move(20,40)
        self.compBox.resize(280,40)


        self.attLabel = QLabel(self)
        self.attLabel.setText("Enter # of Attempts")
        self.attLabel.adjustSize()
        self.attLabel.move(20,100)
        self.attBox = QLineEdit(self)
        self.attBox.move(20,120)
        self.attBox.resize(280,40)
        
        self.ydLabel = QLabel(self)
        self.ydLabel.setText("Enter # of Yards")
        self.ydLabel.adjustSize()
        self.ydLabel.move(20,180)
        self.ydBox = QLineEdit(self)
        self.ydBox.move(20,200)
        self.ydBox.resize(280,40)

        self.tdLabel = QLabel(self)
        self.tdLabel.setText("Enter # of Touchdowns")
        self.tdLabel.adjustSize()
        self.tdLabel.move(20,260)
        self.tdBox = QLineEdit(self)
        self.tdBox.move(20,280)
        self.tdBox.resize(280,40)

        self.intLabel = QLabel(self)
        self.intLabel.setText("Enter # of Interceptions")
        self.intLabel.adjustSize()
        self.intLabel.move(20,340)
        self.intBox = QLineEdit(self)
        self.intBox.move(20,360)
        self.intBox.resize(280,40)



        self.button = QPushButton("Calculate Passer Rating", self)
        self.button.adjustSize()
        self.button.move(20,420)

        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        completions = int(self.compBox.text())
        attempts = int(self.attBox.text())
        yards = int(self.ydBox.text())
        touchdowns = int(self.tdBox.text())
        interceptions = int(self.intBox.text())

        a = ((completions/attempts) - .3) * 5
        if a > 2.375: a = 2.375
        b = ((yards/attempts) - 3) * .25
        if b > 2.375: b = 2.375
        c = ((touchdowns/attempts) * 20)
        if c > 2.375: c = 2.375
        d = 2.375 - ((interceptions/attempts) * 25)
        if d > 2.375: d = 2.375

        myData = ((a + b + c + d)/6) * 100

        if myData < 0:
            myData = 0

        myData = "%.1f"%myData
        
        QMessageBox.question(self, "Result", "Passer rating is: " + str(myData), QMessageBox.Ok, QMessageBox.Ok)
        self.compBox.setText("")
        self.attBox.setText("")
        self.ydBox.setText("")
        self.tdBox.setText("")
        self.intBox.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())