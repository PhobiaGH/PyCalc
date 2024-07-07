from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        Calculator.setObjectName("Calculator")
        Calculator.resize(380, 588)
        self.centralwidget = QtWidgets.QWidget(Calculator)
        self.centralwidget.setObjectName("centralwidget")
        self.outputlabel = QtWidgets.QLabel(self.centralwidget)
        self.outputlabel.setGeometry(QtCore.QRect(10, 10, 352, 90))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.outputlabel.setFont(font)
        self.outputlabel.setFrameShape(QtWidgets.QFrame.Box)
        self.outputlabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.outputlabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.outputlabel.setObjectName("outputlabel")
        
        self.cButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("C"))
        self.cButton.setGeometry(QtCore.QRect(10, 110, 165, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.cButton.setFont(font)
        self.cButton.setObjectName("cButton")
        
        self.arrowButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.remove())
        self.arrowButton.setGeometry(QtCore.QRect(200, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.arrowButton.setFont(font)
        self.arrowButton.setObjectName("arrowButton")
        
        self.devideButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("/"))
        self.devideButton.setGeometry(QtCore.QRect(290, 110, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.devideButton.setFont(font)
        self.devideButton.setObjectName("devideButton")
        
        self.sevenButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("7"))
        self.sevenButton.setGeometry(QtCore.QRect(10, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sevenButton.setFont(font)
        self.sevenButton.setObjectName("sevenButton")
        
        self.eightButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("8"))
        self.eightButton.setGeometry(QtCore.QRect(100, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.eightButton.setFont(font)
        self.eightButton.setObjectName("eightButton")
        
        self.nineButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("9"))
        self.nineButton.setGeometry(QtCore.QRect(200, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.nineButton.setFont(font)
        self.nineButton.setObjectName("nineButton")
        
        self.multiplyButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("*"))
        self.multiplyButton.setGeometry(QtCore.QRect(290, 200, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.multiplyButton.setFont(font)
        self.multiplyButton.setObjectName("multiplyButton")
        
        self.fourButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("4"))
        self.fourButton.setGeometry(QtCore.QRect(10, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fourButton.setFont(font)
        self.fourButton.setObjectName("fourButton")
        
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("5"))
        self.fiveButton.setGeometry(QtCore.QRect(100, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.fiveButton.setFont(font)
        self.fiveButton.setObjectName("fiveButton")
        
        self.sixButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("6"))
        self.sixButton.setGeometry(QtCore.QRect(200, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.sixButton.setFont(font)
        self.sixButton.setObjectName("sixButton")
        
        self.minusButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("-"))
        self.minusButton.setGeometry(QtCore.QRect(290, 290, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")
        
        self.oneButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("1"))
        self.oneButton.setGeometry(QtCore.QRect(10, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.oneButton.setFont(font)
        self.oneButton.setObjectName("oneButton")
        
        self.twoButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("2"))
        self.twoButton.setGeometry(QtCore.QRect(100, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.twoButton.setFont(font)
        self.twoButton.setObjectName("twoButton")
        
        self.threeButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("3"))
        self.threeButton.setGeometry(QtCore.QRect(200, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.threeButton.setFont(font)
        self.threeButton.setObjectName("threeButton")
        
        self.additionButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("+"))
        self.additionButton.setGeometry(QtCore.QRect(290, 380, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.additionButton.setFont(font)
        self.additionButton.setObjectName("additionButton")
        
        self.plus_minusButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.plus_minus())
        self.plus_minusButton.setGeometry(QtCore.QRect(10, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.plus_minusButton.setFont(font)
        self.plus_minusButton.setObjectName("plus_minusButton")
        
        self.zeroButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.press_it("0"))
        self.zeroButton.setGeometry(QtCore.QRect(100, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.zeroButton.setFont(font)
        self.zeroButton.setObjectName("zeroButton")
        
        self.periodButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.dot())
        self.periodButton.setGeometry(QtCore.QRect(200, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.periodButton.setFont(font)
        self.periodButton.setObjectName("periodButton")
        
        self.equalsButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.math())
        self.equalsButton.setGeometry(QtCore.QRect(290, 470, 75, 75))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.equalsButton.setFont(font)
        self.equalsButton.setObjectName("equalsButton")
        
        Calculator.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Calculator)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 380, 22))
        self.menubar.setObjectName("menubar")
        Calculator.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Calculator)
        self.statusbar.setObjectName("statusbar")
        Calculator.setStatusBar(self.statusbar)

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)
    
    def math(self):
        # Grab what is on screen
        screen = self.outputlabel.text()
        try:
            # Do the math
            answer = eval(screen)
            # Output answer to screen
            self.outputlabel.setText(str(answer))
        except:
            # Output error to screen
            self.outputlabel.setText("ERROR")

    def remove(self):
        # Grab what is on screen
        screen = self.outputlabel.text()
        # Remove last item in list/string
        screen = screen[:-1]
        # Output back to the screen
        self.outputlabel.setText(screen)

    def plus_minus(self):
        # Grab what is on screen
        screen = self.outputlabel.text()
        if "-" in screen:
            self.outputlabel.setText(screen.replace("-", ""))
        else:
            self.outputlabel.setText(f'-{screen}')

    # Add decimal
    def dot(self):
        # Grab what is on screen
        screen = self.outputlabel.text()
        if screen[-1] == ".":
            pass
        else:
            self.outputlabel.setText(f'{screen}.')
    
    # Add pressed button onto screen
    def press_it(self, pressed):
        # Clears screen when C is pressed
        if pressed == "C":
            self.outputlabel.setText("0")
        else:
            # Checks if 0 and deletes 0
            if self.outputlabel.text() == "0":
                self.outputlabel.setText("")
            # Concatenate button presses with previous button press
            self.outputlabel.setText(f'{self.outputlabel.text()}{pressed}')

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Calculator"))
        self.outputlabel.setText(_translate("Calculator", "0"))
        self.cButton.setText(_translate("Calculator", "C"))
        self.arrowButton.setText(_translate("Calculator", "<<"))
        self.devideButton.setText(_translate("Calculator", "/"))
        self.sevenButton.setText(_translate("Calculator", "7"))
        self.eightButton.setText(_translate("Calculator", "8"))
        self.nineButton.setText(_translate("Calculator", "9"))
        self.multiplyButton.setText(_translate("Calculator", "x"))
        self.fourButton.setText(_translate("Calculator", "4"))
        self.fiveButton.setText(_translate("Calculator", "5"))
        self.sixButton.setText(_translate("Calculator", "6"))
        self.minusButton.setText(_translate("Calculator", "-"))
        self.oneButton.setText(_translate("Calculator", "1"))
        self.twoButton.setText(_translate("Calculator", "2"))
        self.threeButton.setText(_translate("Calculator", "3"))
        self.additionButton.setText(_translate("Calculator", "+"))
        self.plus_minusButton.setText(_translate("Calculator", "+/-"))
        self.zeroButton.setText(_translate("Calculator", "0"))
        self.periodButton.setText(_translate("Calculator", "."))
        self.equalsButton.setText(_translate("Calculator", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calculator = QtWidgets.QMainWindow()
    ui = Ui_Calculator()
    ui.setupUi(Calculator)
    Calculator.show()
    sys.exit(app.exec_())
