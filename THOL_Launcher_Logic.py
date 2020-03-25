'''
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from THOL_Launcher_GUI import Ui_MainWindow
'''

import sys
import PyQt5.QtCore as core
import PyQt5.QtWidgets as widgets
import PyQt5.QtGui as gui
import PyQt5.uic as uic
from THOL_Launcher_GUI import Ui_MainWindow

app = widgets.QApplication(sys.argv)
MainWindow = uic.loadUi("THOL_Launcher_GUI.ui")

#----------------------------------------------

iniEmail = "settings/email.ini"
iniKey = "settings/accountKey.ini"
iniBorderless = "settings/borderless.ini"

class widgetUseIni:
    def __init__(self, iniFilePath, widget):
        super().__init__()
        self.iniFilePath = iniFilePath
        self.widget = widget

    def ReadIniLineEdit(self):
        self.varLERead = open(self.iniFilePath, "r")
        self.iniLEContent = self.varLERead.read()
        self.widget.setText(self.iniLEContent)
        print("LineEdit Content: ", self.iniLEContent)

    def ReadIniCheckbox(self):
        self.varCB = open(self.iniFilePath, "r")
        self.iniCBContent = self.bool(int(varCB.read()))
        self.widget.setText(self.iniCBContent)
        print(self.iniCBContent)

    def WriteIniLineEdit(self):
        self.varLEWrite = open(self.iniFilePath, "w+")
        self.varLEWrite.write(self.widget.text())
        print("Writing:", self.widget.text(), "\nto:", self.iniFilePath)

UsernameClass = widgetUseIni(iniEmail, MainWindow.LE_Username)
KeyClass = widgetUseIni(iniKey, MainWindow.LE_Key)

UsernameClass.ReadIniLineEdit()
KeyClass.ReadIniLineEdit()

MainWindow.LE_Username.editingFinished.connect(UsernameClass.WriteIniLineEdit)
MainWindow.LE_Key.editingFinished.connect(KeyClass.WriteIniLineEdit)

class widgetReset:
    def __init__(self, Checkbox, ResetButton, CheckState):
        super().__init__()
        self.Checkbox = Checkbox
        self.ResetButton = ResetButton
        self.CheckState = CheckState

    def ResetCheckbox(self):
        self.Checkbox.setCheckState(CheckState)
        self.ResetButton.setVisible(False)

borderlessClass = widgetReset(MainWindow.cBx_Borderless, MainWindow.Btn_Borderless_Reset, 2)

'''
username = open(iniEmail, "r")
usernameContents = username.read()
MainWindow.LE_Username.setText(usernameContents)

f = open(iniKey, "r")
accountKeyContents = f.read()
#MainWindow.LE_Key.setText(accountKeyContents)
'''

borderless = open(iniBorderless, "r")
borderlessContents = bool(int(borderless.read()))
print("borderless Contents =", borderlessContents)
if borderlessContents == "":
    borderlessContents = True

MainWindow.cBx_Borderless.setChecked(borderlessContents)

#----------------------------------------------

if borderlessContents == False:
    MainWindow.Btn_Borderless_Reset.setVisible(True)
else:
    MainWindow.Btn_Borderless_Reset.setVisible(False)


def BorderlessChangeState():
    global borderlessContents
    borderlessContents = MainWindow.cBx_Borderless.isChecked()
    print("BorderlessValue =", borderlessContents)
    if borderlessContents == True:
        MainWindow.Btn_Borderless_Reset.setVisible(False)
    else:
        MainWindow.Btn_Borderless_Reset.setVisible(True)
    Borderless = open("settings/borderless.ini", "w+")
    Borderless.write(str(int(borderlessContents)))
    print("Uncorrected State =", str(MainWindow.cBx_Borderless.checkState()))
    borderlessContents = MainWindow.cBx_Borderless.isChecked()
    print("Borderless Check State: ", borderlessContents)
    return borderlessContents

# Integrated in class widget Interaction
#def BorderlessReset():
#    MainWindow.cBx_Borderless.setCheckState(2)
#    MainWindow.Btn_Borderless_Reset.setVisible(False)

'''
def changeUsername():
    username = open("settings/email.ini", "w+")
    username.write(MainWindow.LE_Username.text())
    #UNTextContent = MainWindow.LE_Username.text()
    print(MainWindow.LE_Username.text())
'''

MainWindow.Btn_Borderless_Reset.clicked.connect(borderlessClass.ResetCheckbox)
MainWindow.cBx_Borderless.stateChanged.connect(BorderlessChangeState)


#class widgetReadFromIni:
#    def __init__(self, iniFilePath, widget):
#        super().__init__()

#MainWindow.Btn_Borderless_Reset.clicked.connect(BorderlessReset)
#MainWindow.cBx_Borderless.clicked.connect(prt_Borderless)

MainWindow.show()
sys.exit(app.exec_())
MainWindow = widgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)


'''
class MyNewWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyNewWindow, self).__init__()
        uic.loadUi('THOL_Launcher_GUI.ui', self)




if __name__ == "__main__":
    import sys
    app = wid.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
'''