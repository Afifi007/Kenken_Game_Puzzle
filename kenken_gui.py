# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kenken.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import kenken_board

class Ui_Form(object):
    size = 3
    def clicked(self):
        if self.radioButton.isChecked():
            self.size = 3
        if self.radioButton_2.isChecked():
            self.size = 4 
        if self.radioButton_4.isChecked():
            self.size = 5
        if self.radioButton_6.isChecked():
            self.size = 6
        if self.radioButton_3.isChecked():
            self.size = 7
        if self.radioButton_5.isChecked():
            self.size = 8
        if self.radioButton_7.isChecked():
            self.size = 9
        kenken_board.game_loop(self.size)
    
    def take_n(self):
        return self.size
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(678, 511)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(50, 10, 541, 461))
        self.widget.setObjectName("widget")
        self.radioButton_5 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_5.setGeometry(QtCore.QRect(372, 290, 95, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_7 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_7.setGeometry(QtCore.QRect(222, 340, 95, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_7.setFont(font)
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2.setGeometry(QtCore.QRect(222, 240, 95, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_4 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_4.setGeometry(QtCore.QRect(372, 240, 95, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(142, 120, 261, 61))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setGeometry(QtCore.QRect(72, 240, 95, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_3.setGeometry(QtCore.QRect(222, 290, 95, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(72, 30, 431, 101))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.radioButton_6 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_6.setGeometry(QtCore.QRect(70, 290, 95, 20))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setObjectName("radioButton_6")
        self.next_btn = QtWidgets.QPushButton(self.widget)
        self.next_btn.setGeometry(QtCore.QRect(360, 410, 101, 41))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.next_btn.setFont(font)
        self.next_btn.setObjectName("next_btn")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Kenken"))
        self.radioButton_5.setText(_translate("Form", "8 x 8"))
        self.radioButton_7.setText(_translate("Form", "9 x 9"))
        self.radioButton_2.setText(_translate("Form", "4 x 4"))
        self.radioButton_4.setText(_translate("Form", "5 x 5"))
        self.label_2.setText(_translate("Form", "Choose your board"))
        self.radioButton.setText(_translate("Form", "3 x 3"))
        self.radioButton_3.setText(_translate("Form", "7 x 7"))
        self.label.setText(_translate("Form", "Welcom To Kenken Game"))
        self.radioButton_6.setText(_translate("Form", "6 x 6"))
        self.next_btn.setText(_translate("Form", "Next"))
        self.next_btn.clicked.connect(self.clicked)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
