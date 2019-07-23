import sys,fine,os
from PyQt5.QtWidgets import (QApplication, QPushButton, QMessageBox, QLabel, QLineEdit, QFileDialog,QWidget )
from PyQt5.QtGui import QCursor,QFont,QMovie,QPalette,QColor,QPixmap
from PyQt5.QtCore import Qt,QObject,QThread, pyqtSignal
class ui(QWidget):
    ##########      界面初始化   ################

    def __init__(self):
        super(ui, self).__init__(None,Qt.FramelessWindowHint)
        self.cinit()
        self.winit()
        self.fileName=0
        self.bu5.setEnabled(False)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()

    def mouseMoveEvent(self, e):
        if Qt.LeftButton and self.m_flag:
            self.move(e.globalPos() - self.m_Position)  # 更改窗口位置

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def mouseDoubleClickEvent(self, QMouseEvent):
        return None

    def winit(self):
        self.window2 = MyWindow2()  # 自定义窗口
        self.window2.before_close_signal.connect(self.echo)

    def cinit(self):
        lbl1 = QLabel('GIF图片转字符', self)
        lbl1.move(114, 20)
        lbl1.setFont(QFont("Microsoft YaHei", 13))

        lbl2 = QLabel('Made by SWW', self)
        lbl2.move(270, 230)

        lbl3 = QLabel('2018/12/4', self)
        lbl3.move(180, 230)

        self.lbl4 =QLabel("正在转换中...",self)
        self.lbl4.move(124, 189)
        self.lbl4.hide()

        self.label = QLabel('', self)
        self.label.move(146, 140)
        self.movie = QMovie('pic/waiting2.gif')
        self.label.setMovie(self.movie)
        self.movie.start()
        self.label.hide()


        self.bu1 = QPushButton('选择图片', self)
        self.bu1.move(282, 86)
        self.bu1.resize(90, 30)
        self.bu1.clicked.connect(self.showDialog)


        self.bu2 = QPushButton('开始转换', self)
        self.bu2.move(282, 132)
        self.bu2.resize(90, 30)
        self.bu2.clicked.connect(self.bu2_clicked)

        self.bu3 = QPushButton(self)
        self.bu3.move(373, 0)
        self.bu3.resize(14, 14)
        self.bu3.setWindowOpacity(0.9)
        # self.bu3.setIcon(QIcon("bu3.png"))
        self.bu3.setStyleSheet(
            "QPushButton{background-image: url(pic/bu3.png)}"
            "QPushButton{border:5px}"
            "QPushButton:hover{background-image: url(pic/bu3_1.png)}")
        self.bu3.clicked.connect(self.bu3_clicked)

        self.bu4 = QPushButton(self)
        self.bu4.move(350, 0)
        self.bu4.resize(14, 14)
        self.bu4.setWindowOpacity(0.9)
        # self.bu3.setIcon(QIcon("bu4.png"))
        self.bu4.setStyleSheet(
            "QPushButton{background-image: url(pic/bu4.png)}"
            "QPushButton{border:5px}"
            "QPushButton:hover{background-image: url(pic/bu4_1.png)}")
        self.bu4.clicked.connect(self.bu4_clicked)

        self.bu5 =  QPushButton("终止转换",self)
        self.bu5.move(282, 182)
        self.bu5.resize(90, 30)
        self.bu5.clicked.connect(self.bu5_clicked)

        self.setGeometry(800, 300, 400, 250)
        self.setWindowOpacity(0.90)
        self.setWindowFlags(Qt.CustomizeWindowHint|
                            Qt.WindowStaysOnTopHint)
        self.tex = QLineEdit("", self)
        self.tex.move(76, 89)
        self.tex.resize(200, 25)
        palette1 = QPalette()
        palette1.setColor(self.backgroundRole(), QColor(255, 255, 255))
        self.setPalette(palette1)

    def bu5_clicked(self):
        fine.isgoingon = 0
        self.lbl4.setText("正在取消操作")
    def bu3_clicked(self):
        self.close()

    def bu4_clicked(self):
        self.showMinimized()

    def bu2_clicked(self):
        fine.isgoingon = 1

        if os.path.exists(self.tex.text()):
            self.tinit()
            self.bu5.setEnabled(True)
        else:
            self.window2.show()


    def showDialog(self):
        fileName1, filetype = QFileDialog.getOpenFileName(self,
                                                          "选取文件",
                                                          "C:\\Users\\10698\PycharmProjects\\untitled1\\test",
                                                          "(*.gif)")  # 设置文件扩展名过滤,注意用双分号间隔
        self.fileName=fileName1
        print(fileName1, filetype)
        self.tex.setText(fileName1)

    def action_shift(self):

        self.a = self.tex.text()
        fine.action(self.a)


    def thread_exit(self):
        self.thread.quit()
        self.label.hide()
        self.lbl4.hide()
        self.lbl4.setText("正在转换中...")
        self.bu1.setEnabled(True)
        self.bu2.setEnabled(True)
        self.bu5.setEnabled(False)

    '''
    def closeEvent(self, event):
        try:
            customMsgBox = QMessageBox(self)

            yesButton = customMsgBox.addButton(self.tr("确定"), QMessageBox.ActionRole)
            noButton = customMsgBox.addButton(self.tr("取消"), QMessageBox.ActionRole)
            customMsgBox.setText(self.tr("你确定要退出吗？"))
            customMsgBox.setWindowTitle(self.tr("通批警告"))
            customMsgBox.exec_()
            button = customMsgBox.clickedButton()
            if button == yesButton:
                event.accept()
            else:
                event.ignore()
        except Exception as e:
            print(e)
    '''
    def tinit(self):
        # 创建线程
        self.label.show()
        self.lbl4.show()
        self.bu1.setEnabled(False)
        self.bu2.setEnabled(False)
        self.backend = BackendThread()
        self.backend.update_date.connect(self.handleDisplay)
        self.thread = QThread()
        self.backend.moveToThread(self.thread)
        self.thread.started.connect(self.backend.run)
        self.backend.finished.connect(self.thread_exit)
        self.thread.start()


    def handleDisplay(self):
        print("sss")

    def echo(self, value):
        '''显示对话框返回值'''
        QMessageBox.information(self, "返回值", "得到",
                                QMessageBox.Yes | QMessageBox.No)

class MyWindow2(QWidget):

    before_close_signal = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        lbl6 = QLabel('', self)
        lbl6.move(0, 0)
        lbl6.resize(300, 250)

        pixmap=QPixmap("pic/loginfail.jpg")
        lbl6.setPixmap(pixmap)
        lbl6.move(0,18)
        lbl7 = QLabel('图片路径不对哦O(∩_∩)O', self)
        lbl7.setFont(QFont("Microsoft YaHei", 12))
        lbl7.move(15, 272)

        self.bu3 = QPushButton(self)
        self.bu3.move(228, 0)
        self.bu3.resize(14, 14)
        self.bu3.setWindowOpacity(0.9)
        # self.bu3.setIcon(QIcon("bu3.png"))
        self.bu3.setStyleSheet(
            "QPushButton{background-image: url(pic/bu3.png)}"
            "QPushButton{border:5px}"
            "QPushButton:hover{background-image: url(pic/bu3_1.png)}"
        )
        self.bu3.clicked.connect(self.bu3_clicked)
        self.setWindowTitle('无法开始')
        self.resize(250, 300)
        self.setWindowFlags(Qt.CustomizeWindowHint|
                            Qt.WindowStaysOnTopHint)
        palette1 = QPalette()
        palette1.setColor(self.backgroundRole(), QColor(255, 255, 255))
        self.setPalette(palette1)
    def bu3_clicked(self):
        self.close()
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()

    def mouseMoveEvent(self, e):
        if Qt.LeftButton and self.m_flag:
            self.move(e.globalPos() - self.m_Position)  # 更改窗口位置

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def mouseDoubleClickEvent(self, QMouseEvent):
        return None



class BackendThread(QObject):
    finished = pyqtSignal()
    update_date = pyqtSignal(str)
    stopped = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.ex = ui
    # 处理业务逻辑
    def run(self):
        ex.action_shift()
        self.finished.emit()

if __name__ == '__main__':
    # 创建应用程序和对象

    app = QApplication(sys.argv)
    ex = ui()
    ex.show()
    sys.exit(app.exec_())

