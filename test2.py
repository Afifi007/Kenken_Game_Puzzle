from PyQt5 import uic, QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import sys

class board_3(QMainWindow):
  def __init__(self):
    super(board_3, self).__init__()
    self.setGeometry(300,100,800,800)
    self.setWindowTitle("Test Kenken")
    self.initUi()

  def initUi(self):
    self.label = QtWidgets.QLabel(self)
    self.label.setText("my 1st label")
    self.label.move(50,50)

    self.b1 = QtWidgets.QPushButton(self)
    self.b1.setText("click Me")
    # self.b1.clicked.connect(lambda: gen_line_edit(80,80))
    self.b1.clicked.connect(self.clicked)

    # creating a QLineEdit object
    self.line_edit_1 = QtWidgets.QLineEdit(self)
    # setting geometry
    self.line_edit_1.setGeometry(80, 80, 80, 80)
    # adding action to the line edit when enter key is pressed
    self.line_edit_1.returnPressed.connect(lambda: do_action())
    self.label_1 = QtWidgets.QLabel(self)
    self.label_1.setText("+4")
    self.label_1.move(85,85)

    # creating a QLineEdit object
    self.line_edit_2 = QtWidgets.QLineEdit(self)
    # setting geometry
    self.line_edit_2.setGeometry(80*2, 80, 80, 80)
    # adding action to the line edit when enter key is pressed
    self.line_edit_2.returnPressed.connect(lambda: do_action())
    self.label_2 = QtWidgets.QLabel(self)
    self.label_2.setText("+10")
    self.label_2.move(80*2+5,85)

    # creating a QLineEdit object
    self.line_edit_3 = QtWidgets.QLineEdit(self)
    # setting geometry
    self.line_edit_3.setGeometry(80*3, 80, 80, 80)
    # adding action to the line edit when enter key is pressed
    self.line_edit_3.returnPressed.connect(lambda: do_action())
    self.label_3 = QtWidgets.QLabel(self)
    self.label_3.setText("+5")
    self.label_3.move(80*3+5,85)

    # creating a QLineEdit object
    self.line_edit_4 = QtWidgets.QLineEdit(self)
    # setting geometry
    self.line_edit_4.setGeometry(80, 80*2, 80, 80)
    # adding action to the line edit when enter key is pressed
    self.line_edit_4.returnPressed.connect(lambda: do_action())

    # creating a QLineEdit object
    self.line_edit_5 = QtWidgets.QLineEdit(self)
    # setting geometry
    self.line_edit_5.setGeometry(80*2, 80*2, 80, 80)
    # adding action to the line edit when enter key is pressed
    self.line_edit_5.returnPressed.connect(lambda: do_action())

    # creating a QLineEdit object
    self.line_edit_6 = QtWidgets.QLineEdit(self)
    # setting geometry
    self.line_edit_6.setGeometry(80*3, 80*2, 80, 80)
    # adding action to the line edit when enter key is pressed
    self.line_edit_6.returnPressed.connect(lambda: do_action())

    # creating a QLineEdit object
    self.line_edit_7 = QtWidgets.QLineEdit(self)
    # setting geometry
    self.line_edit_7.setGeometry(80, 80*3, 80, 80)
    # adding action to the line edit when enter key is pressed
    self.line_edit_7.returnPressed.connect(lambda: do_action())
    # creating a QLineEdit object
    self.line_edit_8 = QtWidgets.QLineEdit(self)
    # setting geometry
    self.line_edit_8.setGeometry(80*2, 80*3, 80, 80)
    # adding action to the line edit when enter key is pressed
    self.line_edit_8.returnPressed.connect(lambda: do_action())
    # creating a QLineEdit object
    self.line_edit_9 = QtWidgets.QLineEdit(self)
    # setting geometry
    self.line_edit_9.setGeometry(80*3, 80*3, 80, 80)
    # adding action to the line edit when enter key is pressed
    self.line_edit_9.returnPressed.connect(lambda: do_action())

    # self.line_edit_1.setText("1")
    

    # method to do action
    def do_action():

        # getting text from the line edit
        value = self.line_edit.text()

        # setting text to the label
        self.label.setText(value)

    # def gen_line_edit(x,y):
    #   print("gen_line_edit")
    #   le1 = QtWidgets.QLineEdit(self)
    #   le1.setGeometry(x,y, 80, 80)


    # To generate board
    # def generate_board(rows, cols):
    #   print("Generating board")
    #   xPos = 80
    #   yPos = 80
    #   for row in range(rows):
    #     # for col in range(cols):
    #       # creating a QLineEdit object
    #       self.le1 = QtWidgets.QLineEdit(self)
    #       # setting geometry
    #       # self.le1.setGeometry(xPos*(col+1), yPos, 80, 80)
    #       self.le1.setGeometry(80,80, 80, 80)
    #       break
    #     # yPos = yPos + 80
    #   print(xPos, yPos)

  def clicked(self):
    self.label.setText("You pressed b1")


def window():
  app = QApplication(sys.argv);
  win = board_3()

  win.show()
  app.exec_() #to make work without closing
  # win.exit(app.exec_())

window()