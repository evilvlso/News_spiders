# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'xiugaidaxiao.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt,QCoreApplication
import Trans
class Ui_MainWindow(object):
    def __init__(self):
        self.index=0
        self.labellist=[('toutiaonews','今日头条热点'),('baidunews','百度热点新闻'),('weibonews','微博热点新闻'),('jiupainews','九派热点新闻')]
        self.channel=Trans.News()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(331, 463)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        #背景
        MainWindow.setAutoFillBackground(True)
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(QtGui.QPixmap("b.jpg")))
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("迷你简行楷")
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setMouseTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("bitbug_favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.preButton = QtWidgets.QToolButton(self.centralwidget)
        self.preButton.setGeometry(QtCore.QRect(20, 20, 51, 41))
        self.preButton.setArrowType(QtCore.Qt.LeftArrow)
        self.preButton.setObjectName("preButton")
        self.preButton.clicked.connect(self.left_clicked)
        self.newslabel = QtWidgets.QLabel(self.centralwidget)
        self.newslabel.setGeometry(QtCore.QRect(80, 20, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.newslabel.setFont(font)
        self.newslabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.newslabel.setWordWrap(True)
        self.newslabel.setObjectName("newslabel")
        #设置字体颜色
        self.newslabel.setStyleSheet("color:white;")
        
        self.nextButton = QtWidgets.QToolButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(260, 20, 51, 41))
        self.nextButton.setArrowType(QtCore.Qt.RightArrow)
        self.nextButton.setObjectName("nextButton")
        self.nextButton.clicked.connect(self.right_clicked)
        
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 70, 291, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        #设置textbrowser
        self.textBrowser.setWordWrapMode(0)
        self.textBrowser.setOpenExternalLinks(True)
        font1 = QtGui.QFont()
        font1.setPointSize(13)
        self.textBrowser.setFont(font1)
        self.textBrowser.setText(u'''<html>
        <body>
        <style type="text/css">
        a:link,a:visited{
         text-decoration:none;  /*超链接无下划线*/
         color : 230,230,255 ;
        font-family: "楷体";
        font-weight:bold;
        }
        p{
        font-size:20px}
        </style>
        <br/>
        <p align="center">点击左右箭头即可获取今日<br/>百度热点，<br/>微博热点，<br/>今日头条，<br/>九派新闻！<br/>~~~///(^v^)\\\~~~</p>
        </body>
        </html>''')
        self.verticalLayout.addWidget(self.textBrowser)
        self.date = QtWidgets.QLCDNumber(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(10, 370, 71, 41))
        self.date.setObjectName("date")
        self.date.setSmallDecimalPoint(True)
        #self.date.setStyleSheet("border: 2px solid black; color: red; background: silver;")
        self.date.display(time.strftime('%H:%M'))
        
        self.pic = QtWidgets.QLabel(self.centralwidget)
        self.pic.setGeometry(QtCore.QRect(90, 368, 128, 41))
        self.pic.setText("")
        self.pic.setPixmap(QtGui.QPixmap("Dossier_Luffy_128px_1108222_easyicon.net.ico"))
        
        self.pic.setObjectName("pic")
        self.shutdown = QtWidgets.QPushButton(self.centralwidget)
        self.shutdown.setGeometry(QtCore.QRect(230, 370, 81, 41))
        font = QtGui.QFont()
        font.setFamily("迷你简黑咪")
        font.setPointSize(16)
        self.shutdown.setFont(font)
        self.shutdown.setObjectName("shutdown")
        #关闭按钮
        self.shutdown.clicked.connect(QCoreApplication.quit)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 331, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setObjectName("menubar")
        self.meunhelp = QtWidgets.QMenu(self.menubar)
        self.meunhelp.setGeometry(QtCore.QRect(339, 104, 155, 62))
        #
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(14)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.meunhelp.setFont(font)
        self.meunhelp.setObjectName("meunhelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        #self.statusbar.showMessage('Are U Ready!')
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.meunhelp.menuAction())
        #定时器
        self.testTimer = QtCore.QTimer()
        self.testTimer.timeout.connect(self.show_time)
        self.testTimer.start(60000)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #实例化Trans
        
    def show_time(self):
        self.date.display(time.strftime("%H:%M"))
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "News"))
        self.preButton.setText(_translate("MainWindow", "..."))
        self.newslabel.setText(_translate("MainWindow", "今日热点"))
        self.nextButton.setText(_translate("MainWindow", "..."))
        self.shutdown.setText(_translate("MainWindow", "Close"))
        self.meunhelp.setTitle(_translate("MainWindow", "Help"))
    def right_clicked(self):
        global index
        self.index=(self.index+5)%4
        self.refresh()
    def left_clicked(self):
        global index
        self.index = (self.index +3) % 4
        self.refresh()
    def refresh(self):
        #设置newslabel
        self.newslabel.setText(self.labellist[self.index][1])
        #获取新闻
        if len(self.channel.global_news[self.labellist[self.index][0]]) == 0:
            self.channel.query(self.labellist[self.index][0])
        info=self.channel.global_news.get(self.labellist[self.index][0])
        tmp = '''<html>
        <body>
        <style type="text/css">
        a:link,a:visited{{
         text-decoration:none;
         color : 230,230,255 ;
        font-family: "楷体";
        font-weight:bold;
        }}

        </style>
        <ul>
        <li><a target="_blank" href="{0}">{1}</a></li>
        <li><a target="_blank" href="{2}">{3}</a></li>
        <li><a target="_blank" href="{4}">{5}</a></li>
        <li><a target="_blank" href="{6}">{7}</a></li>
        <li><a target="_blank" href="{8}">{9}</a></li>
        <li><a target="_blank" href="{10}">{11}</a></li>
        <li><a target="_blank" href="{12}">{13}</a></li>
        <li><a target="_blank" href="{14}">{15}</a></li>
        <li><a target="_blank" href="{16}">{17}</a></li>
        <li><a target="_blank" href="{18}">{19}</a></li></ul>
        </body>
        </html>'''.format(info[0][1], info[0][0], info[1][1], info[1][0], info[2][1], info[2][0], info[3][1],
                          info[3][0], info[4][1], info[4][0], info[5][1], info[5][0], info[6][1], info[6][0],
                          info[7][1], info[7][0], info[8][1], info[8][0], info[9][1], info[9][0], )
        self.textBrowser.setText(tmp)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

