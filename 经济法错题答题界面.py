# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '答题界面.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QTextCursor
import 数据库操作
import 经济法错题选择
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self,tiku,ti_bao):

        super(Ui_MainWindow, self).__init__()
        # 图标
        self.setWindowIcon(QIcon('会计.jpg'))
        self.tiku = tiku
        self.ti_bao = ti_bao
        self.num_1 = 1
        self.id, self.question, self.answer, self.parsing = 数据库操作.createDB(self.tiku,self.num_1,self.ti_bao)
        # 题数
        self.total_tishu = 数据库操作.getTotalRecordCount(self.tiku,self.ti_bao)

        # 行数
        if self.total_tishu <=4:
            self.hang_shu = 1

        elif self.total_tishu % 4 == 0:
            self.hang_shu = self.total_tishu // 4
        else:
            self.hang_shu = self.total_tishu // 4 + 1

        self.font = QtGui.QFont()
        # 字体
        self.font.setFamily('微软雅黑')
        # 加粗
        self.font.setBold(False)
        # # 大小
        self.font.setPointSize(13)

        self.bu_ju()


    def bu_ju(self):
        self.setObjectName("self")
        self.resize(1079, 720)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(450, 10, 621, 251))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(450, 260, 621, 81))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.horizontalLayout.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.horizontalLayout.addWidget(self.checkBox_4)
        self.pushButton_next = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_next.setObjectName("pushButton_next")
        self.horizontalLayout.addWidget(self.pushButton_next)
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close.setGeometry(QtCore.QRect(980, 510, 93, 28))
        self.pushButton_close.setObjectName("pushButton_close")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(840, 350, 231, 151))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_3.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(450, 350, 391, 301))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(3, 11, 441, 651))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        num_3 = 1
        for i in range(self.hang_shu):

            for j in range(4):
                self.pushButton_num3 = QtWidgets.QPushButton(self.layoutWidget_2)
                self.pushButton_num3.setObjectName("pushButton_{}".format(num_3))
                self.gridLayout.addWidget(self.pushButton_num3, i, j, 1, 1)
                _translate = QtCore.QCoreApplication.translate
                self.pushButton_num3.setText(_translate("self", "{}".format(num_3)))
                if num_3 == self.total_tishu:
                    break
                num_3 += 1

        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1079, 25))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)


        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "会计实务错题答题界面"))
        self.plainTextEdit.setPlainText(_translate("self", self.question))
        self.checkBox.setText(_translate("self", "A"))
        self.checkBox_2.setText(_translate("self", "B"))
        self.checkBox_3.setText(_translate("self", "C"))
        self.checkBox_4.setText(_translate("self", "D"))
        self.pushButton_next.setText(_translate("self", "下一题"))
        self.pushButton_close.setText(_translate("self", "退出"))
        self.label.setText(_translate("self", "你的答案:"))
        self.lineEdit.setText(_translate("self", ""))
        self.label_2.setText(_translate("self", "正确答案:"))
        self.lineEdit_2.setText(_translate("self", ""))
        self.plainTextEdit_2.setPlainText(_translate("self", ""))



        self.zi_ti_yang_shi(self.font)
        self.bang_ding_xin_hao_cao()

    def bang_ding_xin_hao_cao(self):

        self.pushButton_next.clicked.connect(self.xia_yi_ti)
        self.pushButton_close.clicked.connect(self.tui_chu)

    def zi_ti_yang_shi(self,font):
        #设置字体样式
        self.plainTextEdit.setFont(font)
        self.plainTextEdit_2.setFont(font)
        #设置为不可编辑
        #self.lineEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plainTextEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.plainTextEdit_2.setFocusPolicy(QtCore.Qt.NoFocus)
    def tui_chu(self):
        self.close()
        self.open_ti_bao_xuan_ze = 经济法错题选择.Ui_MainWindow()
        self.open_ti_bao_xuan_ze.show()




    def qing_li(self):
        #先将文本框清理

        self.lineEdit_2.clear()
        self.plainTextEdit_2.clear()
        #如果有选项选中执行
        if self.checkBox.isChecked() == True or self.checkBox_2.isChecked() == True or self.checkBox_3.isChecked() == True or self.checkBox_4.isChecked() == True:
            self.lineEdit.clear()

        if self.checkBox.isChecked() == True:
            self.checkBox.click()
            self.lineEdit.insert("A")
        if self.checkBox_2.isChecked() == True:
            self.lineEdit.insert('B')
            self.checkBox_2.click()
        if self.checkBox_3.isChecked() == True:
            self.lineEdit.insert('C')
            self.checkBox_3.click()
        if self.checkBox_4.isChecked() == True:
            self.lineEdit.insert('D')
            self.checkBox_4.click()
        self.lineEdit_2.insert(self.answer)



        #正确
        if self.lineEdit.text() == self.lineEdit_2.text():
            if self.num_1 < self.total_tishu:
                self.num_1+=1
                self.id,self.question,self.answer,self.parsing = 数据库操作.createDB(self.tiku,self.num_1,self.ti_bao)
                self.bu_ju()
            else:
                QMessageBox.information(self, "提示", "已经为最后一题")


        else:
            pass
            #写入错题库
            # self.xie_ru_cuo_ti_ku()

            #解析
            # self.plainTextEdit_2.appendPlainText(self.parsing)
        # else:#没有选中的直接跳过该题
        #     pass


    def xie_ru_cuo_ti_ku(self):
        数据库操作.xie_ru(self.tiku,'错题'+str(self.ti_bao[-1]),self.id,str(self.question),str(self.answer),str(self.parsing))



    def xia_yi_ti(self):

        self.qing_li()