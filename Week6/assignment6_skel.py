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
        # define variable
        name = QLabel('Name:', self)
        self.namelabel = QLineEdit(self)
        age = QLabel('Age:', self)
        self.agelabel = QLineEdit(self)
        score = QLabel('Score:', self)
        self.scorelabel = QLineEdit(self)
        amount = QLabel('Amount:', self)
        self.amountlabel = QLineEdit(self)
        result = QLabel('Result:', self)
        self.resultlabel = QTextEdit(self)

        Key = QLabel('Key', self)
        combo = QComboBox(self)
        combo.addItem('Name')
        combo.addItem('Age')
        combo.addItem('Score')
        combo.activated[str].connect(self.Del)
        combo.activated[str].connect(self.Find)

        addButton = QPushButton('Add',self)
        delbutton = QPushButton('Del',self)
        findbutton = QPushButton('Find',self)
        incbutton = QPushButton('Inc',self)
        showbutton = QPushButton('Show', self)

        #set layout
        hbox1 = QHBoxLayout()
        hbox1.addWidget(name)
        hbox1.addWidget(self.namelabel)
        hbox1.addWidget(age)
        hbox1.addWidget(self.agelabel)
        hbox1.addWidget(score)
        hbox1.addWidget(self.scorelabel)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(amount)
        hbox2.addWidget(self.amountlabel)
        hbox2.addWidget(Key)
        hbox2.addWidget(combo)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(addButton)
        hbox3.addWidget(delbutton)
        hbox3.addWidget(findbutton)
        hbox3.addWidget(incbutton)
        hbox3.addWidget(showbutton)

        hbox4 = QHBoxLayout()
        hbox4.addWidget(result)

        hbox5 = QHBoxLayout()
        hbox5.addWidget(self.resultlabel)


        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)
        self.setLayout(vbox)

        addButton.clicked.connect(self.Add)
        showbutton.clicked.connect(self.Show)
        delbutton.clicked.connect(self.Del)
        findbutton.clicked.connect(self.Find)
        incbutton.clicked.connect(self.Inc)

        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()


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
            print("Empty DB",self.dbfilename)
        else:
            # convert Age,Score to int type
            print("Open DB", self.dbfilename)
            for integer in self.scoredb:
                integer['Age'] = int(integer['Age'])
                integer['Score'] = int(integer['Score'])

            return self.scoredb
        fH.close()


    # convert Age,Score to int type
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        for integer in self.scoredb:
            integer['Age'] = int(integer['Age'])
            integer['Score'] = int(integer['Score'])

        pickle.dump(self.scoredb, fH)
        fH.close()

    # convert Age,Score to int type for make msg string
    def showScoreDB(self):
        fh = self.readScoreDB()
        msg = ''
        for person in sorted(fh, key = lambda person : person['Name']):
            for k , v in person.items():
                    person[k] = str(person[k])
                    k = str(k)
                    msg += k + '=' + person[k] + '\t'

            msg += '\n'
        self.resultlabel.setText(msg)

    def Add(self):
        name = self.namelabel.text()
        age = self.agelabel.text()
        score = self.scorelabel.text()

        addinfo = {'Name':name, 'Age':age, 'Score':score }
        self.scoredb.append(addinfo)
        self.writeScoreDB()
        self.showScoreDB()
    # make new list to del Del Name
    def Del(self, text):
        name = self.namelabel.text()
        new_db = []

        for i in self.scoredb:
            if['Name'] != name:
                new_db.append(i)

        self.scoredb = new_db
        self.writeScoreDB()
        self.showScoreDB()
    # Find same name and show infomation
    def Find(self, text):
        findname = self.namelabel.text()
        msg = ''
        new_db = []

        for i in self.scoredb:
            if i['Name'] == findname:
                new_db.append(i)

        for p in new_db:
            for Key in p:
                if Key == 'Score' or Key == 'Age':
                    p[Key] = str(p[Key])
                    msg += Key + '=' + p[Key] + '\t'

            msg += '\n'
        self.resultlabel.setText(msg)
    # convert age, score to str type for make msg String
    def Show(self):
        info = self.combo.currentText()
        msg = ''
        for i in sorted(self.readScoreDB(), key=lambda person: person[info]):
            for Key in sorted(i):
                if Key == 'Age' or Key == 'Score':
                    i[Key] = str(i[Key])
                    Key = str(Key)
                msg += Key + '=' + i[Key] + '\t'
            msg += '\n'
        self.resultlabel.setText(msg)
    # Find same name and amount
    def Inc(self):
        name = self.namelabel.text()
        amount = self.amountlabel.text()

        for i in self.scoredb:
            if i['Name'] == name:
                i['Score'] += int(amount)
        self.writeScoreDB()
        self.showScoreDB()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())





