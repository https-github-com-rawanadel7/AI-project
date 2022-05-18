from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import loadUiType
import random

open,_ = loadUiType('First.ui')
one,_=loadUiType('one.ui')
two,_=loadUiType('two.ui')

class Open(QWidget,open):
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("X&O Game")
        self.Handel_Buttons()



    def Handel_Buttons(self):
        self.pushButton.clicked.connect(self.Computer)
        self.pushButton_2.clicked.connect(self.Two_players)

    def Computer(self):
        self.window2 = One()
        self.close()
        self.window2.show()

    def Two_players(self):
        self.window2 = Two()
        self.close()
        self.window2.show()


class One(QWidget,one):
    turn = 0
    winner = 0
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("X&O Game-Computer")
        self.Handel_Buttons()
        self.label_3.setVisible(False)



    def Handel_Buttons(self):
        self.b1.clicked.connect(self.Click)
        self.b2.clicked.connect(self.Click)
        self.b3.clicked.connect(self.Click)
        self.b4.clicked.connect(self.Click)
        self.b5.clicked.connect(self.Click)
        self.b6.clicked.connect(self.Click)
        self.b7.clicked.connect(self.Click)
        self.b8.clicked.connect(self.Click)
        self.b9.clicked.connect(self.Click)

        self.pushButton_10.clicked.connect(self.Back)

    def Back(self):
        self.window2 = Open()
        self.close()
        self.window2.show()

    def Click(self):
        sender = self.sender()
        if (self.turn % 2 == 0):
            sender.setText('X')
            self.turn += 1
            self.check_winner()
            self.check_draw()

    def ai_win(self):
        if ((self.b1.text()=="")and(self.b2.text()=="O")and(self.b3.text()=="O")):
            return self.b1
        elif ((self.b1.text()=="O")and(self.b2.text()=="")and(self.b3.text()=="O")):
            return self.b2
        elif ((self.b1.text()=="O")and(self.b2.text()=="O")and(self.b3.text()=="")):
            return self.b3

        elif ((self.b4.text()=="")and(self.b5.text()=="O")and(self.b6.text()=="O")):
            return self.b4
        elif ((self.b4.text()=="O")and(self.b5.text()=="")and(self.b6.text()=="O")):
            return self.b5
        elif ((self.b4.text()=="O")and(self.b5.text()=="O")and(self.b6.text()=="")):
            return self.b6

        elif ((self.b7.text()=="")and(self.b8.text()=="O")and(self.b9.text()=="O")):
            return self.b7
        elif ((self.b7.text()=="O")and(self.b8.text()=="")and(self.b9.text()=="O")):
            return self.b8
        elif ((self.b7.text()=="O")and(self.b8.text()=="O")and(self.b9.text()=="")):
            return self.b9

        elif ((self.b1.text() == "") and (self.b4.text() == "O") and (self.b7.text() == "O")):
            return self.b1
        elif ((self.b1.text() == "O") and (self.b4.text() == "") and (self.b7.text() == "O")):
            return self.b4
        elif ((self.b1.text() == "O") and (self.b4.text() == "O") and (self.b7.text() == "")):
            return self.b7

        elif ((self.b2.text() == "") and (self.b5.text() == "O") and (self.b8.text() == "O")):
            return self.b2
        elif ((self.b2.text() == "O") and (self.b5.text() == "") and (self.b8.text() == "O")):
            return self.b5
        elif ((self.b2.text() == "O") and (self.b5.text() == "O") and (self.b8.text() == "")):
            return self.b8

        elif ((self.b3.text() == "") and (self.b6.text() == "O") and (self.b9.text() == "O")):
            return self.b3
        elif ((self.b3.text() == "O") and (self.b6.text() == "") and (self.b9.text() == "O")):
            return self.b6
        elif ((self.b3.text() == "O") and (self.b6.text() == "O") and (self.b9.text() == "")):
            return self.b9

        elif ((self.b1.text() == "") and (self.b5.text() == "O") and (self.b9.text() == "O")):
            return self.b1
        elif ((self.b1.text() == "O") and (self.b5.text() == "") and (self.b9.text() == "O")):
            return self.b5
        elif ((self.b1.text() == "O") and (self.b5.text() == "O") and (self.b9.text() == "")):
            return self.b9

        elif ((self.b3.text() == "") and (self.b5.text() == "O") and (self.b7.text() == "O")):
            return self.b3
        elif ((self.b3.text() == "O") and (self.b5.text() == "") and (self.b7.text() == "O")):
            return self.b5
        elif ((self.b3.text() == "O") and (self.b5.text() == "O") and (self.b7.text() == "")):
            return self.b7

        else:
            return None

    def ai_block_win(self):
        if ((self.b1.text()=="")and(self.b2.text()=="X")and(self.b3.text()=="X")):
            return self.b1
        elif ((self.b1.text()=="X")and(self.b2.text()=="")and(self.b3.text()=="X")):
            return self.b2
        elif ((self.b1.text()=="X")and(self.b2.text()=="X")and(self.b3.text()=="")):
            return self.b3

        elif ((self.b4.text()=="")and(self.b5.text()=="X")and(self.b6.text()=="X")):
            return self.b4
        elif ((self.b4.text()=="X")and(self.b5.text()=="")and(self.b6.text()=="X")):
            return self.b5
        elif ((self.b4.text()=="X")and(self.b5.text()=="X")and(self.b6.text()=="")):
            return self.b6

        elif ((self.b7.text()=="")and(self.b8.text()=="X")and(self.b9.text()=="X")):
            return self.b7
        elif ((self.b7.text()=="X")and(self.b8.text()=="")and(self.b9.text()=="X")):
            return self.b8
        elif ((self.b7.text()=="X")and(self.b8.text()=="X")and(self.b9.text()=="")):
            return self.b9

        elif ((self.b1.text() == "") and (self.b4.text() == "X") and (self.b7.text() == "X")):
            return self.b1
        elif ((self.b1.text() == "X") and (self.b4.text() == "") and (self.b7.text() == "X")):
            return self.b4
        elif ((self.b1.text() == "X") and (self.b4.text() == "X") and (self.b7.text() == "")):
            return self.b7

        elif ((self.b2.text() == "") and (self.b5.text() == "X") and (self.b8.text() == "X")):
            return self.b2
        elif ((self.b2.text() == "X") and (self.b5.text() == "") and (self.b8.text() == "X")):
            return self.b5
        elif ((self.b2.text() == "X") and (self.b5.text() == "X") and (self.b8.text() == "")):
            return self.b8

        elif ((self.b3.text() == "") and (self.b6.text() == "X") and (self.b9.text() == "O")):
            return self.b3
        elif ((self.b3.text() == "X") and (self.b6.text() == "") and (self.b9.text() == "X")):
            return self.b6
        elif ((self.b3.text() == "X") and (self.b6.text() == "X") and (self.b9.text() == "")):
            return self.b9

        elif ((self.b1.text() == "") and (self.b5.text() == "X") and (self.b9.text() == "X")):
            return self.b1
        elif ((self.b1.text() == "X") and (self.b5.text() == "") and (self.b9.text() == "X")):
            return self.b5
        elif ((self.b1.text() == "X") and (self.b5.text() == "X") and (self.b9.text() == "")):
            return self.b9

        elif ((self.b3.text() == "") and (self.b5.text() == "X") and (self.b7.text() == "X")):
            return self.b3
        elif ((self.b3.text() == "X") and (self.b5.text() == "") and (self.b7.text() == "X")):
            return self.b5
        elif ((self.b3.text() == "X") and (self.b5.text() == "X") and (self.b7.text() == "")):
            return self.b7

        else:
            return None
        
    def ai_logic(self):
        if (self.b5.text()==''):
            return self.b5
        card=random.randint(0,3)
        match card:
            case'0':
                if (self.b1.text()==""):
                    return self.b1
            case '1':
                if (self.b3.text() == ""):
                    return self.b3
            case '2':
                if (self.b7.text() == ""):
                    return self.b7
            case '3':
                if (self.b9.text() == ""):
                    return self.b9

        if(self.b2.text()==""):
            return self.b2
        elif (self.b4.text() == ""):
            return self.b4
        elif (self.b5.text() == ""):
            return self.b5
        elif (self.b6.text() == ""):
            return self.b6
        elif (self.b8.text() == ""):
            return self.b8
        else:
            return None

    def ai_bestMove(self):
        move=None
        if (self.turn%2==1 and move==None):
            move=self.ai_win()
        if (self.turn%2==1 and move==None):
            move=self.ai_block_win()
        if (self.turn%2==1 and move==None):
            move=self.ai_logic()
        if(self.turn%2==1 and move!=None):
            move.setText('O')
            self.turn += 1
            self.check_winner()


    def check_winner(self):
        ######Horizontal######
        if (self.b1.text() == self.b2.text() and self.b2.text() == self.b3.text() and self.b3.text() == 'X'):
            self.label_3.setVisible(True)
            self.label_4.setText('X')
        if (self.b1.text() == self.b2.text() and self.b2.text() == self.b3.text() and self.b3.text() == 'O'):
            self.label_3.setVisible(True)
            self.label_4.setText('O')

        if (self.b4.text() == self.b5.text() and self.b5.text() == self.b6.text() and self.b6.text() == 'X'):
            self.label_3.setVisible(True)
            self.label_4.setText('X')
        if (self.b4.text() == self.b5.text() and self.b5.text() == self.b6.text() and self.b6.text() == 'O'):
            self.label_3.setVisible(True)
            self.label_4.setText('O')

        if (self.b7.text() == self.b8.text() and self.b8.text() == self.b9.text() and self.b9.text() == 'X'):
            self.label_3.setVisible(True)
            self.label_4.setText('X')
        if (self.b7.text() == self.b8.text() and self.b8.text() == self.b9.text() and self.b9.text() == 'O'):
            self.label_3.setVisible(True)
            self.label_4.setText('O')
        ######Vertical######
        if (self.b1.text() == self.b4.text() and self.b4.text() == self.b7.text() and self.b7.text() == 'X'):
            self.label_3.setVisible(True)
            self.label_4.setText('X')
        if (self.b1.text() == self.b4.text() and self.b4.text() == self.b7.text() and self.b7.text() == 'O'):
            self.label_3.setVisible(True)
            self.label_4.setText('O')

        if (self.b2.text() == self.b5.text() and self.b5.text() == self.b8.text() and self.b8.text() == 'X'):
            self.label_3.setVisible(True)
            self.label_4.setText('X')
        if (self.b2.text() == self.b5.text() and self.b5.text() == self.b8.text() and self.b8.text() == 'O'):
            self.label_3.setVisible(True)
            self.label_4.setText('O')

        if (self.b3.text() == self.b6.text() and self.b6.text() == self.b9.text() and self.b9.text() == 'X'):
            self.label_3.setVisible(True)
            self.label_4.setText('X')
        if (self.b3.text() == self.b6.text() and self.b6.text() == self.b9.text() and self.b9.text() == 'O'):
            self.label_3.setVisible(True)
            self.label_4.setText('O')

        ######Cross######
        if (self.b1.text() == self.b5.text() and self.b5.text() == self.b9.text() and self.b9.text() == 'X'):
            self.label_3.setVisible(True)
            self.label_4.setText('X')
        if (self.b1.text() == self.b5.text() and self.b5.text() == self.b9.text() and self.b9.text() == 'O'):
            self.label_3.setVisible(True)
            self.label_4.setText('O')

        if (self.b3.text() == self.b5.text() and self.b5.text() == self.b7.text() and self.b7.text() == 'X'):
            self.label_3.setVisible(True)
            self.label_4.setText('X')
        if (self.b3.text() == self.b5.text() and self.b5.text() == self.b7.text() and self.b7.text() == 'O'):
            self.label_3.setVisible(True)
            self.label_4.setText('O')
        self.ai_bestMove()

    def check_draw(self):
        if(self.turn==9):
            self.label_4.setText('draw')


class Two(QWidget,two):
    turn = 0
    winner=0
    def __init__(self):
        QWidget.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("X&O Game-2Players")
        self.Handel_Buttons()
        self.label_3.setVisible(False)


    def Handel_Buttons(self):
        self.b1.clicked.connect(self.Click)
        self.b2.clicked.connect(self.Click)
        self.b3.clicked.connect(self.Click)
        self.b4.clicked.connect(self.Click)
        self.b5.clicked.connect(self.Click)
        self.b6.clicked.connect(self.Click)
        self.b7.clicked.connect(self.Click)
        self.b8.clicked.connect(self.Click)
        self.b9.clicked.connect(self.Click)

        self.pushButton_10.clicked.connect(self.Back)


    def Back(self):
        self.window2 = Open()
        self.close()
        self.window2.show()


    def Free(self):
        sender = self.sender()
        text=sender.text()
        if (text==''):
            return True
        else:
            return False

    def Click(self):
        sender=self.sender()
        free=self.Free()
        if (free):
            if (self.turn%2==0):
                sender.setText('X')
            else:
                sender.setText('O')
            self.turn+=1
        self.check_winner()
        self.check_draw()

    def check_winner(self):
        ######Horizontal######
        if (self.b1.text() == self.b2.text() and self.b2.text() == self.b3.text() and self.b3.text()=='X'):
            self.label_3.setVisible(True)
            self.label_4.setText('X')
        if (self.b1.text() == self.b2.text() and self.b2.text() == self.b3.text()and self.b3.text()=='O'):
            self.label_3.setVisible(True)
            self.label_4.setText('O')

        if (self.b4.text() == self.b5.text() and self.b5.text() == self.b6.text() and self.b6.text()=='X'):
            self.label_3.setVisible(True)
            self.label_4.setText('X')
        if (self.b4.text() == self.b5.text() and self.b5.text() == self.b6.text()and self.b6.text()=='O'):
            self.label_3.setVisible(True)
            self.label_4.setText('O')

        if (self.b7.text() == self.b8.text() and self.b8.text() == self.b9.text() and self.b9.text()=='X'):
            self.label_3.setVisible(True)
            self.label_4.setText('X')
        if (self.b7.text() == self.b8.text() and self.b8.text() == self.b9.text() and self.b9.text()=='O'):
            self.label_3.setVisible(True)
            self.label_4.setText('O')
        ######Vertical######
        if (self.b1.text() == self.b4.text() and self.b4.text() == self.b7.text() and self.b7.text()=='X'):
            self.label_3.setVisible(True)
            self.label_4.setText('X')
        if (self.b1.text() == self.b4.text() and self.b4.text() == self.b7.text() and self.b7.text()=='O'):
            self.label_3.setVisible(True)
            self.label_4.setText('O')

        if (self.b2.text() == self.b5.text() and self.b5.text() == self.b8.text() and self.b8.text()=='X'):
            self.label_3.setVisible(True)
            self.label_4.setText('X')
        if (self.b2.text() == self.b5.text() and self.b5.text() == self.b8.text() and self.b8.text()=='O'):
            self.label_3.setVisible(True)
            self.label_4.setText('O')

        if (self.b3.text() == self.b6.text() and self.b6.text() == self.b9.text() and self.b9.text()=='X'):
            self.label_3.setVisible(True)
            self.label_4.setText('X')
        if (self.b3.text() == self.b6.text() and self.b6.text() == self.b9.text() and self.b9.text()=='O'):
            self.label_3.setVisible(True)
            self.label_4.setText('O')


        ######Cross######
        if (self.b1.text() == self.b5.text() and self.b5.text() == self.b9.text() and self.b9.text()=='X'):
            self.label_3.setVisible(True)
            self.label_4.setText('X')
        if (self.b1.text() == self.b5.text() and self.b5.text() == self.b9.text() and self.b9.text()=='O'):
            self.label_3.setVisible(True)
            self.label_4.setText('O')

        if (self.b3.text() == self.b5.text() and self.b5.text() == self.b7.text() and self.b7.text()=='X'):
            self.label_3.setVisible(True)
            self.label_4.setText('X')
        if (self.b3.text() == self.b5.text() and self.b5.text() == self.b7.text() and self.b7.text()=='O'):
            self.label_3.setVisible(True)
            self.label_4.setText('O')

    def check_draw(self):
        if(self.turn==9):
            self.label_4.setText('draw')


def main():
    app = QApplication(sys.argv)
    window = Open()
    window.show()
    app.exec_()



if __name__ == '__main__':
    main()