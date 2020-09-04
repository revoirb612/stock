import sys
sys.path.append("C:/Users/revoi/PycharmProjects/week1")


from kiwoom.kiwoom import *
from PyQt5.QtWidgets import *


class Main:
    def __init__(self):
        print("Main() Start")

        self.app = QApplication(sys.argv)
        self.kiwoom = Kiwoom()
        self.app.exec_()

if __name__ == "__main__":
    Main()
