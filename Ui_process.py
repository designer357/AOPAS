# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'process.ui'
#
# Created: Tue Jun 17 00:13:48 2014
#      by: PyQt4 UI code generator 4.11
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Process(object):
    def setupUi(self, Process):
        Process.setObjectName(_fromUtf8("Process"))
        Process.resize(405, 390)
        Process.setMinimumSize(QtCore.QSize(405, 390))
        Process.setMaximumSize(QtCore.QSize(405, 390))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(10)
        Process.setFont(font)
        self.line = QtGui.QFrame(Process)
        self.line.setGeometry(QtCore.QRect(0, 10, 411, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_3 = QtGui.QFrame(Process)
        self.line_3.setGeometry(QtCore.QRect(0, 120, 401, 61))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.pcomboBox1 = QtGui.QComboBox(Process)
        self.pcomboBox1.setGeometry(QtCore.QRect(40, 60, 111, 21))
        self.pcomboBox1.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.pcomboBox1.setAutoFillBackground(False)
        self.pcomboBox1.setStyleSheet(_fromUtf8("font: 75 9pt \"宋体\";"))
        self.pcomboBox1.setFrame(True)
        self.pcomboBox1.setObjectName(_fromUtf8("pcomboBox1"))
        self.pcomboBox1.addItem(_fromUtf8(""))
        self.pcomboBox1.addItem(_fromUtf8(""))
        self.pcomboBox1.addItem(_fromUtf8(""))
        self.pcomboBox1.addItem(_fromUtf8(""))
        self.pcomboBox1.addItem(_fromUtf8(""))
        self.pcomboBox1.addItem(_fromUtf8(""))
        self.pcomboBox1.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(Process)
        self.label.setGeometry(QtCore.QRect(10, 100, 81, 16))
        self.label.setStyleSheet(_fromUtf8("font: 75 12pt \"宋体\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.line_2 = QtGui.QFrame(Process)
        self.line_2.setGeometry(QtCore.QRect(150, 20, 21, 131))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_2 = QtGui.QLabel(Process)
        self.label_2.setGeometry(QtCore.QRect(180, 30, 101, 16))
        self.label_2.setStyleSheet(_fromUtf8("font: 75 9pt \"宋体\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.textEdit = QtGui.QTextEdit(Process)
        self.textEdit.setGeometry(QtCore.QRect(180, 50, 211, 91))
        self.textEdit.setStyleSheet(_fromUtf8("font: 75 12pt \"宋体\";"))
        self.textEdit.setUndoRedoEnabled(False)
        self.textEdit.setLineWrapMode(QtGui.QTextEdit.WidgetWidth)
        self.textEdit.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.pushButton = QtGui.QPushButton(Process)
        self.pushButton.setGeometry(QtCore.QRect(310, 200, 75, 25))
        self.pushButton.setStyleSheet(_fromUtf8("font: 75 9pt \"宋体\";"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Process)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 240, 75, 25))
        self.pushButton_2.setStyleSheet(_fromUtf8("font: 75 9pt \"宋体\";"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.textEdit_2 = QtGui.QTextEdit(Process)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 190, 281, 91))
        self.textEdit_2.setStyleSheet(_fromUtf8("font: 75 12pt \"宋体\";"))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.line_4 = QtGui.QFrame(Process)
        self.line_4.setGeometry(QtCore.QRect(0, 280, 431, 16))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.lineEdit = QtGui.QLineEdit(Process)
        self.lineEdit.setGeometry(QtCore.QRect(230, 160, 91, 21))
        self.lineEdit.setStyleSheet(_fromUtf8("font: 75 12pt \"宋体\";"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pcomboBox3 = QtGui.QComboBox(Process)
        self.pcomboBox3.setGeometry(QtCore.QRect(120, 160, 91, 22))
        self.pcomboBox3.setObjectName(_fromUtf8("pcomboBox3"))
        self.line_5 = QtGui.QFrame(Process)
        self.line_5.setGeometry(QtCore.QRect(-10, 150, 51, 138))
        self.line_5.setFrameShape(QtGui.QFrame.VLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.label1 = QtGui.QLabel(Process)
        self.label1.setGeometry(QtCore.QRect(10, 30, 101, 16))
        self.label1.setStyleSheet(_fromUtf8("font: 75 12pt \"宋体\";"))
        self.label1.setObjectName(_fromUtf8("label1"))
        self.pcomboBox2 = QtGui.QComboBox(Process)
        self.pcomboBox2.setGeometry(QtCore.QRect(40, 120, 111, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("宋体"))
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.pcomboBox2.setFont(font)
        self.pcomboBox2.setStyleSheet(_fromUtf8("font: 75 9pt \"宋体\";"))
        self.pcomboBox2.setObjectName(_fromUtf8("pcomboBox2"))
        self.pcheckBox = QtGui.QCheckBox(Process)
        self.pcheckBox.setGeometry(QtCore.QRect(20, 160, 91, 21))
        self.pcheckBox.setStyleSheet(_fromUtf8("font: 75 9pt \"宋体\";"))
        self.pcheckBox.setObjectName(_fromUtf8("pcheckBox"))
        self.pbuttonOK = QtGui.QPushButton(Process)
        self.pbuttonOK.setGeometry(QtCore.QRect(70, 320, 75, 25))
        self.pbuttonOK.setStyleSheet(_fromUtf8("font: 75 9pt \"宋体\";"))
        self.pbuttonOK.setObjectName(_fromUtf8("pbuttonOK"))
        self.pbuttonCancel = QtGui.QPushButton(Process)
        self.pbuttonCancel.setGeometry(QtCore.QRect(220, 320, 75, 25))
        self.pbuttonCancel.setStyleSheet(_fromUtf8("font: 75 9pt \"宋体\";"))
        self.pbuttonCancel.setObjectName(_fromUtf8("pbuttonCancel"))

        self.retranslateUi(Process)
        QtCore.QMetaObject.connectSlotsByName(Process)

    def retranslateUi(self, Process):
        Process.setWindowTitle(_translate("Process", "数据处理", None))
        self.pcomboBox1.setItemText(0, _translate("Process", "求平均", None))
        self.pcomboBox1.setItemText(1, _translate("Process", "求方差", None))
        self.pcomboBox1.setItemText(2, _translate("Process", "排序", None))
        self.pcomboBox1.setItemText(3, _translate("Process", "滑动平均", None))
        self.pcomboBox1.setItemText(4, _translate("Process", "中值滤波", None))
        self.pcomboBox1.setItemText(5, _translate("Process", "高斯滤波", None))
        self.pcomboBox1.setItemText(6, _translate("Process", "统计信息", None))
        self.label.setText(_translate("Process", "方法函数", None))
        self.label_2.setText(_translate("Process", "Introduction", None))
        self.pushButton.setText(_translate("Process", "Add", None))
        self.pushButton_2.setText(_translate("Process", "Clear", None))
        self.label1.setText(_translate("Process", "操作选择", None))
        self.pcheckBox.setText(_translate("Process", "输入参数", None))
        self.pbuttonOK.setText(_translate("Process", "Confirm", None))
        self.pbuttonCancel.setText(_translate("Process", "Cancel", None))

