from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit, QToolButton
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtWidgets import QLayout, QGridLayout

from keypad import numPadList, operatorList, constantList, functionList
import calcFunctions

class Button(QToolButton):

    def __init__(self, text, callback):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        self.setText(text)
        self.clicked.connect(callback)

    def sizeHint(self):
        size = super(Button, self).sizeHint()
        size.setHeight(size.height() + 20)
        size.setWidth(max(size.width(), size.height()))
        return size


class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        # Button Creation and Placement
        numLayout = QGridLayout()
        opLayout = QGridLayout()
        constLayout = QGridLayout()
        funcLayout = QGridLayout()

        buttonGroups = {
            'num': {'buttons': numPadList, 'layout': numLayout, 'columns': 3},
            'op': {'buttons': operatorList, 'layout': opLayout, 'columns': 2},
            'constants': {'buttons': constantList, 'layout': constLayout, 'columns': 1},
            'functions': {'buttons': functionList, 'layout': funcLayout, 'columns': 1},
        }

        for label in buttonGroups.keys():
            r = 0; c = 0
            buttonPad = buttonGroups[label]
            for btnText in buttonPad['buttons']:
                button = Button(btnText, self.buttonClicked)
                buttonPad['layout'].addWidget(button, r, c)
                c += 1
                if c >= buttonPad['columns']:
                    c = 0; r += 1

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)
        mainLayout.addLayout(numLayout, 1, 0)
        mainLayout.addLayout(opLayout, 1, 1)
        mainLayout.addLayout(constLayout, 2, 0)
        mainLayout.addLayout(funcLayout, 2, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")


    def buttonClicked(self):
        if 'clear' in init:
            self.display.clear()
            init.clear()

        button = self.sender()
        key = button.text()

        ## 06 + 3처럼 앞에 0이 있을 경우 에러처리가 나던 것을 처리하기 위해
        ## 맨앞에 0이 나타나지 않을때까지 0을 지우고 연산기호 뒤의 문자도 0이면 없애는 식으로 하려했으나
        ## 연산기호를 여러번 쓰는부분을 어떻게 코딩해야할지 몰라 남겼습니다.
        '''idx = 0
        if key == '=':
            if '+' or '-' or '*' or '/' in self.display.text():
                del0 = ''
                for i in range(1, len(self.display.text())):
                # 연산기호가 몇번째에 있는 지 확인
                    if self.display.text()[i] == '+':
                        idx = i
                    if self.display.text()[i] == '-':
                        idx = i
                    if self.display.text()[i] == '*':
                        idx = i
                    if self.display.text()[i] == '/':
                        idx = i

                del1 = ''
                ## 첫째 인자에 0이 있는 경우
                count = 1
                print(idx)
                while self.display.text()[0] == '0':
                    count += 1
                    # 첫째 인자 0제거
                    for i in range(1, len(self.display.text())):
                        del0 += self.display.text()[i]
                    self.display.setText(del0)
                    # 둘째 인자 0 유무 확인
                    while del0[idx + 1] == '0':
                    # 0이 있네?
                        for i in range(1, len(del0)):
                            if i == idx:
                                continue
                            else:
                                del1 += del0[i]
                        self.display.setText(del1)
                    # 둘째 인자에 0이 없는 경우
                    else:
                        self.display.setText(str(eval(del0)))

                ## 첫재 인자에 0이 없는우 경우
                else:
                    ## 둘째 인자에 0이 있는 경우
                    if self.display.text()[idx + 1] == 0:
                        print('22')

                    ## 둘째 인장에 0이 없는 경우
                    else:
                        try:
                            result = str(eval(self.display.text()))
                        except:
                            result = 'Error!'
                        self.display.setText(result)'''
        if key == '=':

            ## 계산 입력 후 값 초기화를 위해 init라는 리스트를 생성
            ## ZeroDivisionErro 처리
            if '/' in self.display.text():
                try:
                    result = str(eval(self.display.text()))
                except ZeroDivisionError:
                    result = 'ZeroDivisionError'
                    init.append('clear')
                self.display.setText(result)


            else:
                try:
                    result = str(eval(self.display.text()))
                except:
                    result = 'Error!'
                    init.append('clear')

                self.display.setText(result)


        elif key == 'C':
            self.display.clear()
        elif key == constantList[0]:
           self.display.setText(self.display.text() + '3.141592')
        elif key == constantList[1]:
            self.display.setText(self.display.text() + '3E+8')
        elif key == constantList[2]:
            self.display.setText(self.display.text() + '340')
        elif key == constantList[3]:
            self.display.setText(self.display.text() + '1.5E+8')
        elif key == functionList[0]:
            n = self.display.text()
            value = calcFunctions.factorial(n)
            self.display.setText(str(value))
            init.append('clear')
        elif key == functionList[1]:
            n = self.display.text()
            value = calcFunctions.decToBin(n)
            self.display.setText(str(value))
        elif key == functionList[2]:
            n = self.display.text()
            value = calcFunctions.binToDec(n)
            self.display.setText(str(value))
        elif key == functionList[3]:
            n = self.display.text()
            value = calcFunctions.decToRoman(n)
            self.display.setText(str(value))
        else:
            self.display.setText(self.display.text() + key)  ## 계산 입력


if __name__ == '__main__':

    import sys
    init = []
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())


'''elif '('  or ')' in self.display.text():
                result = ''
                while self.display.text()[0] == '(' or ')':
                    for i in range(0, len(self.display.text()) - 1):
                        self.display.text()[i] = self.display.text()[i+1]
                    self.display.setText(self.display.text())
                while self.display.text()[-1] == '(' or ')':
                    for i in range(0, len(self.display.text()) - 1):
                        result += self.display.text()[i] '''