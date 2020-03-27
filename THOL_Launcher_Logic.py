'''
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from THOL_Launcher_GUI import Ui_MainWindow
'''

import sys
from configparser import ConfigParser
import PyQt5.QtCore as core
import PyQt5.QtWidgets as widgets
import PyQt5.QtGui as gui
import PyQt5.uic as uic
from THOL_Launcher_GUI import Ui_MainWindow

app = widgets.QApplication(sys.argv)
MainWindow = uic.loadUi("THOL_Launcher_GUI.ui")

#----------------------------------------------

def readIni(setting):
    parser = ConfigParser()
    parser.read('settings/defaultSettings.ini')
    return(parser.get('settings', setting))

print("Borderless:", bool(int(readIni('borderless'))))

#borderlessDefault = readIni('borderless')

# --- ini File Paths
iniDefaultSettings = "settings/defaultSettings.ini"
iniEmail = "settings/email.ini"
iniKey = "settings/accountKey.ini"
iniBorderless = "settings/borderless.ini"


'''
username = open(iniEmail, "r")
usernameContents = username.read()
MainWindow.LE_Username.setText(usernameContents)

f = open(iniKey, "r")
accountKeyContents = f.read()
MainWindow.LE_Key.setText(accountKeyContents)
'''

class widgetUseIni:
    def __init__(self, widget):
        super().__init__()
        self.widget = widget

    def ReadIniLineEdit(self, iniFilePath):
        self.iniFilePath = iniFilePath
        with open(self.iniFilePath, "r") as varLERead:
            self.iniLEContent = varLERead.read()
        self.widget.setText(self.iniLEContent)
        print("LineEdit Content: ", self.iniLEContent)

    def ReadIniCheckbox(self, iniFilePath):
        self.iniFilePath = iniFilePath
        with open(iniFilePath, "r") as varCBRead:
            self.iniCBContent = varCBRead.read()
        self.widget.setText(self.iniCBContent)
        print(self.iniCBContent)

    def WriteIniLineEdit(self, iniFilePath):
        self.iniFilePath = str(iniFilePath)
        with open(self.iniFilePath, "w") as self.varLEWrite:
            self.varLEWrite.write(self.widget.text())
        print("Writing:", self.widget.text(), "\nto:", self.iniFilePath)


# --- Creates References of the Reading Classes
UsernameClass = widgetUseIni(MainWindow.LE_Username)
KeyClass = widgetUseIni(MainWindow.LE_Key)

# --- Creates References of the Writing Classes
#UsernameWriteClass = widgetWriteIni(iniEmail, MainWindow.LE_Username)
#KeyWriteClass = widgetWriteIni(iniKey, MainWindow.LE_Key)

# --- initiates reading of the *.ini files
UsernameClass.ReadIniLineEdit(iniEmail)
KeyClass.ReadIniLineEdit(iniKey)

# --- When triggered, writes the values to the *.ini files
UsernameClass.WriteIniLineEdit("settings/email.ini")
# MainWindow.LE_Username.editingFinished.connect(UsernameClass.WriteIniLineEdit("settings/email.ini"))
MainWindow.LE_Key.editingFinished.connect(KeyClass.WriteIniLineEdit)
#MainWindow.LE_Key

# --- when triggered with the Reset Button, resets the corresponding widget
class widgetReset:
    def __init__(self, widget):
        super().__init__()
        self.widget = widget

    def ResetCheckbox(self, ResetButton, defaultValue):
        self.ResetButton = ResetButton
        self.defaultValue = defaultValue
        self.defaultValue = int(self.defaultValue)
        if self.defaultValue == 1:
            self.defaultValue += 1
        self.widget.setCheckState(self.defaultValue)
        self.ResetButton.setVisible(False)

borderlessReset = widgetReset(MainWindow.cBx_Borderless)
MainWindow.Btn_Borderless_Reset.clicked.connect(borderlessReset.ResetCheckbox(MainWindow.Btn_Borderless_Reset, readIni('borderless')))

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
    Borderless.close()


MainWindow.cBx_Borderless.stateChanged.connect(BorderlessChangeState)


MainWindow.show()
sys.exit(app.exec_())
MainWindow = widgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)



'''
# Integrated in class widget Interaction
#def BorderlessReset():
#    MainWindow.cBx_Borderless.setCheckState(2)
#    MainWindow.Btn_Borderless_Reset.setVisible(False)

def changeUsername():
    username = open("settings/email.ini", "w+")
    username.write(MainWindow.LE_Username.text())
    #UNTextContent = MainWindow.LE_Username.text()
    print(MainWindow.LE_Username.text())

#class widgetReadFromIni:
#    def __init__(self, iniFilePath, widget):
#        super().__init__()

#MainWindow.Btn_Borderless_Reset.clicked.connect(BorderlessReset)
#MainWindow.cBx_Borderless.clicked.connect(prt_Borderless)

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