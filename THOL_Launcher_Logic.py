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
import THOL_Launcher_Variables as vars
from THOL_Launcher_GUI import Ui_MainWindow

app = widgets.QApplication(sys.argv)
MainWindow = uic.loadUi("THOL_Launcher_GUI.ui")

# ----------------------------------------------

print("The OReally default value:", vars.default_emot_oreally)

'''
def read_ini(setting):
    parser = ConfigParser()
    parser.read('settings/defaultSettings.ini')
    return(parser.get('settings', setting))


# Null attribute for cases in which no input is needed.
Null = ""

# --- ini File Path Variables
ini_default_settings = "settings/defaultSettings.ini"
ini_key = "settings/accountKey.ini"
ini_allow_saving_speech = "settings/allowSavingSpeech.ini"
ini_auto_login = "settings/autoLogIn.ini"
ini_baby_body_down_fac = "settings/babyBodyDownFactor.ini"
ini_baby_head_down_fac = "settings/babyHeadDownFactor.ini"
ini_blend_output_frame_fraction = "settings/blendOutputFrameFraction.ini"
ini_blend_output_frame_pairs = "settings/blendOutputFramePairs.ini"
ini_borderless = "settings/borderless.ini"
ini_borderless_height_adjust = "settings/borderlessHeightAdjust.ini"
ini_chk_review_spelling = "settings/checkReviewSpelling.ini"
ini_vsync = "settings/countingOnVsync.ini"
ini_culvert_stone_sprites = "settings/culvertStoneSprites.ini"
ini_custom_server_address = "settings/customServerAddress.ini"
ini_custom_server_port = "settings/customServerPort.ini"
ini_e_right_click = "settings/eKeyForRightClick.ini"
ini_email = "settings/email.ini"
ini_emot_duration = "settings/emotDuration.ini"
ini_emot_words = "settings/emotionWords.ini"
ini_live_triggers = "settings/enableLiveTriggers.ini"
ini_speed_control_keys = "settings/enableSpeedControlKeys.ini"
ini_big_cursor = "settings/forceBigPointer.ini"
ini_fov_scale_game = "settings/fovScale.ini"
ini_fov_scale_hud = "settings/fovScaleHUD.ini"
ini_fullscreen = "settings/fullscreen.ini"
ini_ground_tile_edge_blur_radius = "settings/groundTileEdgeBlurRadius.ini"
ini_half_framerate = "settings/halfFrameRate.ini"
ini_hard_quit_mode = "settings/hardToQuitMode.ini"
ini_hide_ui = "settings/hideGameUI.ini"
ini_hide_playback_display = "settings/hidePlaybackDisplay.ini"
ini_keep_past_recordings = "settings/keepPastRecordings.ini"
ini_mouse_spd = "settings/mouseSpeed.ini"
ini_music_volume = "settings/musicLoudness.ini"
ini_music_off = "settings/musicOff.ini"
ini_old_head_down_fac = "settings/oldHeadDownFactor.ini"
ini_old_head_forward_fac = "settings/oldHeadForwardFactor.ini"
ini_pause_on_minimize = "settings/pauseOnMinimize.ini"
ini_rec_audio = "settings/recordAudio.ini"
ini_rec_audio_length = "settings/recordAudioLengthInSeconds.ini"
ini_rec_game = "settings/recordGame.ini"
ini_res_height = "settings/screenHeight.ini"
ini_res_width = "settings/screenWidth.ini"
ini_skip_fps_measure = "settings/skipFPSMeasure.ini"
ini_sound_buffer_size = "settings/soundBufferSize.ini"
ini_sfx_volume = "settings/soundEffectsLoudness.ini"
ini_sfx_off = "settings/soundEffectsOff.ini"
ini_sound_sample_rate = "settings/soundSampleRate.ini"
ini_spell_check = "settings/spellCheckOn.ini"
ini_target_fps = "settings/targetFrameRate.ini"
ini_tutorial_done = "settings/tutorialDone.ini"
ini_use_custom_server = "settings/useCustomServer.ini"


# --- Default Setting Variables
default_email = read_ini('email')
default_key = read_ini('accountKey')
default_borderless = read_ini('borderless')
'''

class widget_interact:
    # Takes in all the necessary attributes and stores them in variables.
    def __init__(self, widget, reset_button, reset_button_placeholder, iniFilePath, default_value):
        super().__init__()
        self.widget = widget
        self.reset_button = reset_button
        self.reset_button_placeholder = reset_button_placeholder
        self.iniFilePath = iniFilePath
        self.default_value = default_value

    # Reads stored text field(LE) value from *.ini setting file and
    # displays it in launcher.
    def LE_read_ini(self, iniFilePath):
        with open(iniFilePath, "r") as varLERead:
            self.iniLEContent = varLERead.read()
        self.widget.setText(self.iniLEContent)
        print("LineEdit Content: ", self.iniLEContent)

    # Reads stored checkbox(cBx) value from *.ini setting file and
    # displays it in launcher. Triggers check whether it is default value.
    def cBx_read_ini(self, iniFilePath, default_value):
        with open(iniFilePath, "r") as varCBRead:
            self.iniCBContent = varCBRead.read()
        print("of type:", type(self.iniCBContent))
        print("Current cBx borderless:", self.iniCBContent)
        # if (self.iniCBContent != "0") and (self.iniCBContent != "1"):
        #     self.iniCBContent = default_value
        #     self.cBx_write_ini()
        self.widget.setChecked(int(self.iniCBContent))
        self.cBx_default_visib(iniFilePath)
        print("Checkbox Content: ", self.iniCBContent)

    # Writes chosen text field(LE) content to according *.ini setting file.
    def LE_write_ini(self):
        with open(self.iniFilePath, "w") as self.varLEWrite:
            self.varLEWrite.write(self.widget.text())
        print("iniFilePath =", self.iniFilePath)
        # print("Writing:", self.widget.text(), "\nto:", iniFilePath)

    # Writes chosen checkbox(cBx) setting to according *.ini setting file,
    # then triggers 'cBx_default_visib()'.
    def cBx_write_ini(self, iniFilePath):
        with open(iniFilePath, "w") as self.varCBWrite:
            self.varCBWrite.write(str(int(self.widget.isChecked())))
        print("Writing:", self.widget.isChecked(), "\nto:", iniFilePath)
        self.cBx_default_visib(iniFilePath)

    # makes the reset button visible/invisible,
    # depending on according default value.
    def cBx_default_visib(self, iniFilePath):
        with open(iniFilePath, "r") as varCBRead:
            self.iniCBContent2 = int(varCBRead.read())
        print("is default value?:", self.iniCBContent2)
        if self.iniCBContent2 == int(self.default_value):
            self.reset_button.setVisible(False)
            self.reset_button_placeholder.setVisible(True)
        else:
            self.reset_button.setVisible(True)
            self.reset_button_placeholder.setVisible(False)

    # Resets the corresponding checkbox widget,
    # then removes the reset button.
    def cBx_reset(self):
        self.widget.setChecked(int(self.default_value))
        self.reset_button.setVisible(False)
        self.reset_button_placeholder.setVisible(True)

#----------------------------------------------

# Creates References of the widgetUseClass
username_class = widget_interact(MainWindow.LE_Username, vars.Null, vars.Null, vars.ini_email, vars.default_email)
key_class = widget_interact(MainWindow.LE_Key, vars.Null, vars.Null, vars.ini_key, vars.default_key)

fullscreen_class = widget_interact(MainWindow.cBx_Fullscreen, MainWindow.Btn_Fullscreen_Reset, MainWindow.lbl_Fullscreen_Reset_Ph, vars.ini_fullscreen, vars.default_fullscreen)
borderless_class = widget_interact(MainWindow.cBx_Borderless, MainWindow.Btn_Borderless_Reset, MainWindow.lbl_Borderless_Reset_Ph, vars.ini_borderless, vars.default_borderless)
vsync_class = widget_interact(MainWindow.cBx_VSync, MainWindow.Btn_VSync_Reset, MainWindow.lbl_VSync_Reset_Ph, vars.ini_vsync, vars.default_vsync)

# --- READ SETTINGS FROM *.INI ---
# initiates reading of the *.ini files
username_class.LE_read_ini(vars.ini_email)
key_class.LE_read_ini(vars.ini_key)
fullscreen_class.cBx_read_ini(vars.ini_fullscreen, vars.default_fullscreen)
borderless_class.cBx_read_ini(vars.ini_borderless, vars.default_borderless)
vsync_class.cBx_read_ini(vars.ini_vsync, vars.default_vsync)

# --- WRITE SETTINGS TO *.INI ---
# Text Fields (Line Edits(LE))
# Functionality: When triggered, writes the values to the *.ini files
MainWindow.LE_Username.editingFinished.connect(username_class.LE_write_ini)
MainWindow.LE_Key.editingFinished.connect(key_class.LE_write_ini)

# CheckBoxes (cBx)
# When the checkbox is clicked, it writes the new state to the setting *.ini and
# sets the visibility of the 
MainWindow.cBx_Fullscreen.stateChanged.connect(fullscreen_class.cBx_write_ini(vars.ini_fullscreen))
MainWindow.cBx_Borderless.stateChanged.connect(borderless_class.cBx_write_ini(vars.ini_borderless))
MainWindow.cBx_VSync.stateChanged.connect(vsync_class.cBx_write_ini(vars.ini_vsync))

# --- RESET SETTINGS FROM defaultSettings.ini
# CheckBoxes (cBx)
MainWindow.Btn_Fullscreen_Reset.clicked.connect(fullscreen_class.cBx_reset)
MainWindow.Btn_Borderless_Reset.clicked.connect(borderless_class.cBx_reset)
MainWindow.Btn_VSync_Reset.clicked.connect(vsync_class.cBx_reset)

# MainWindow.lbl_Fullscreen_Reset_Ph.setVisible(False)
# MainWindow.lbl_Borderless_Reset_Ph.setVisible(False)
# MainWindow.lbl_VSync_Reset_Ph.setVisible(False)

#----------------------------------------------
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