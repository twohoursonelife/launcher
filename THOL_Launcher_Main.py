from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import QApplication, QMainWindow
#from PyQt5 import QtCore, QtGui, QtWidgets, uic
#from PyQt5.QtWidgets import QApplication, QWidget, Q
from THOL_Launcher_GUI import Ui_MainWindow
import sys

#print(Ui_MainWindow.Btn_2HOL_Website.setObjectName)
#Ui_MainWindow.Btn_SaveSettings.clicked()

#qtCreatorFile = "THOL_Launcher_GUI.ui"
#Ui_MainWindow, QtBaseClass = uic.loadUi(qtCreatorFile)

'''
class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.Btn_SaveSettings.clicked.connect(self.changeBtnText)
        print("mööööp")

    def changeBtnText(self):
        buttontext = "Burger"
        print("fuckin shit")
        #self.Btn_SaveSettings.setText
'''
def home(self):
    btn = Ui_MainWindow.Btn_SaveSettings()
    #btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
    Ui_MainWindow.Btn_SaveSettings.clicked.connect(QtCore.QCoreApplication.instance().quit)

#theText = Ui_MainWindow.Btn_SaveSettings.setText()
#print(Ui_MainWindow.retranslateUi())

class Ui(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('THOL_Launcher_GUI.ui', self)
        self.button = self.findChild(QtWidgets.QPushButton, 'Btn_SaveSettings')
        self.Btn_SaveSettings.clicked.connect(self.stuff)
        self.show()

    def stuff(self):
        print("stuffy")
        


'''
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = QMainWindow
    #win.setGeometry(200,200,300,300)
    #win.setWin
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    app.exec_()
    

    #app = QtWidgets.QApplication(sys.argv)
'''


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
