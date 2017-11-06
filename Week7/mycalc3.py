from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout


class Button(QToolButton):

    def __init__(self, text):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size

class Function_Button_Left(QToolButton):
    def __init__(self, text):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Function_Button_Left, self).sizeHint()
        size.setHeight(size.height() + 40 )
        size.setWidth(max(size.width(), size.height()))
        return size

class Function_Button_Right(QToolButton):
    def __init__(self, text):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)

    def sizeHint(self):
        size = super(Function_Button_Right, self).sizeHint()
        size.setHeight(size.height() + 30 )
        size.setWidth(max(size.width(), size.height()))
        return size

class Calculator(QWidget):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Display Window
        self.display = QLineEdit('0')
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)
        
        # Digit Buttons
        self.digitButton = [x for x in range(0, 10)]

        # make for loop ################################################
        for num in range(10):
            self.digitButton[num] = Button('%d' %(num))
        ################################################################
        
        # . and = Buttons
        self.decButton = Button('.')
        self.eqButton = Button('=')

        # Operator Buttons
        self.mulButton = Button('*')
        self.divButton = Button('/')
        self.addButton = Button('+')
        self.subButton = Button('-')

        # Parentheses Buttons
        self.lparButton = Button('(')
        self.rparButton = Button(')')

        # Clear Button
        self.clearButton = Button('C')

        ############################################################################################
        # Function Button - Left
        self.piButton = Function_Button_Left('pi')
        self.lightspeedButton = Function_Button_Left('빛의 이동 속도 (m/s)')
        self.soundspeedButton = Function_Button_Left('소리의 이동 속도 (m/s')
        self.sundistanceButton = Function_Button_Left('태양과의 평군 거리 (km)')

        # Function Button - Right
        self.factoriButton = Function_Button_Right('factorial (!)')
        self.binaryButton = Function_Button_Right('-> binary')
        self.binaryconvertdecButton = Function_Button_Right('binary -> dec')
        self.romanButton = Function_Button_Right('-> roman')
        self.romanconvertdecButton = Function_Button_Right('roman -> dec')
        ############################################################################################
        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)

        numLayout = QGridLayout()

        # make for loop ###########################################################
        num = 0
        for i in range(3, -1, -1):
            if i == 3:
                numLayout.addWidget(self.digitButton[num], i, 0)
                num += 1
            else:
                for j in range(0, 3):
                    numLayout.addWidget(self.digitButton[num], i ,j)
                    num += 1
        ############################################################################
        numLayout.addWidget(self.decButton, 3, 1)
        numLayout.addWidget(self.eqButton, 3, 2)

        mainLayout.addLayout(numLayout, 1, 0)

        opLayout = QGridLayout()

        opLayout.addWidget(self.mulButton, 0, 0)
        opLayout.addWidget(self.divButton, 0, 1)
        opLayout.addWidget(self.addButton, 1, 0)
        opLayout.addWidget(self.subButton, 1, 1)

        opLayout.addWidget(self.lparButton, 2, 0)
        opLayout.addWidget(self.rparButton, 2, 1)
        
        opLayout.addWidget(self.clearButton, 3, 0)
        
        mainLayout.addLayout(opLayout, 1, 1)

        ##############################################################################################
        #Layout

        funcleftLayout = QGridLayout()

        funcleftLayout.addWidget(self.piButton , 0, 0)
        funcleftLayout.addWidget(self.lightspeedButton, 1, 0)
        funcleftLayout.addWidget(self.soundspeedButton, 2, 0)
        funcleftLayout.addWidget(self.sundistanceButton, 3, 0)
        mainLayout.addLayout(funcleftLayout, 2, 0)

        funcrightLayout = QGridLayout()

        funcrightLayout.addWidget(self.factoriButton, 0, 0)
        funcrightLayout.addWidget(self.binaryButton, 1, 0)
        funcrightLayout.addWidget(self.binaryconvertdecButton, 2, 0)
        funcrightLayout.addWidget(self.romanButton, 3, 0)
        funcrightLayout.addWidget(self.romanconvertdecButton, 4, 0)

        mainLayout.addLayout(funcrightLayout, 2, 1)

        ##############################################################################################

        self.setLayout(mainLayout)
        
        self.setWindowTitle("My Calculator")


if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())
