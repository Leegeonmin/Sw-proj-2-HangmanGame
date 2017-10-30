import pickle
import sys
from PyQt5.QtWidgets import *
'''(QWidget, QPushButton, 
    QHBoxLayout, QVBoxLayout, QApplication, QLabel, 
    QComboBox, QTextEdit, QLineEdit)'''
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

        
    def initUI(self):
        name = QLabel('Name:', self)
        namelabel = QLineEdit(self)
        age = QLabel('Age:', self)
        agelabel = QLineEdit(self)
        score = QLabel('Score:', self)
        scorelabel = QLineEdit(self)
        amount = QLabel('Amount:', self)
        amountlabel = QLineEdit(self)
        result = QLabel('Result:', self)
        resultlabel = QTextEdit(self)


        resultlabel.setGeometry(10,120,470,120)
        namelabel.move(50,10)
        agelabel.move(200, 10)
        scorelabel.move(380, 10)
        amountlabel.move(230, 50)
        name.move(10, 10)
        age.move(170, 10)
        score.move(340, 10)
        amount.move(170, 50)
        result.move(10, 100)


        addButton = QPushButton('Add',self)
        addButton.move(100, 75)
        delbutton = QPushButton('Del',self)
        delbutton.move(180, 75)
        findbutton = QPushButton('Find',self)
        findbutton.move(260, 75)
        incbutton = QPushButton('Inc',self)
        incbutton.move(340, 75)
        showbutton = QPushButton('Show', self)
        showbutton.move(420, 75)

        self.Key = QLabel('Key', self)
        combo = QComboBox(self)
        combo.addItem('Name')
        combo.addItem('Age')
        combo.addItem('Score')
        combo.move(390, 50)
        self.Key.move(350,50)
        combo.activated[str].connect(self.onActivated)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')    
        self.show()

        showbutton.clicked.connect(self.showScoreDB)

    def onActivated(self, text):
        self.Key.setText(text)
        self.Key.adjustSize()

    def closeEvent(self, event):

        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()


    def showScoreDB(self):
        sortkey = self.Key
        print(sortkey)
        print(self.Key.text)

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())





