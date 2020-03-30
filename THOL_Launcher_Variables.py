from configparser import ConfigParser

# ----------------------------------------------

# Normal Variables
# Null attribute for cases in which no input is needed.
Null = ''

# ----------------------------------------------

# ini File Path Variables
# Function for assembling the *.ini setting file paths
def get_path_of_ini(ini_name):
    some_name = 'settings/', ini_name, '.ini'
    new = ''
    for x in some_name:
        new += x
    return new

# get_path_of_ini('accountKey') generates 'settings/accountKey.ini'
ini_default_settings = get_path_of_ini('defaultSettings')
ini_key = get_path_of_ini('accountKey')
ini_allow_saving_speech = get_path_of_ini('allowSavingSpeech')
ini_auto_login = get_path_of_ini('autoLogIn')
ini_baby_body_down_fac = get_path_of_ini('babyBodyDownFactor')
ini_baby_head_down_fac = get_path_of_ini('babyHeadDownFactor')
ini_blend_out_fr_fraction = get_path_of_ini('blendOutputFrameFraction')
ini_blend_out_fr_pairs = get_path_of_ini('blendOutputFramePairs')
ini_borderless = get_path_of_ini('borderless')
ini_borderless_h_adjust = get_path_of_ini('borderlessHeightAdjust')
ini_chk_rev_spelling = get_path_of_ini('checkReviewSpelling')
ini_vsync = get_path_of_ini('countingOnVsync')
# ini_culvert_stone_sprites = get_path_of_ini('culvertStoneSprites')
ini_custom_server_address = get_path_of_ini('customServerAddress')
ini_custom_server_port = get_path_of_ini('customServerPort')
ini_e_right_click = get_path_of_ini('eKeyForRightClick')
ini_email = get_path_of_ini('email')
ini_emot_duration = get_path_of_ini('emotDuration')
ini_emot_words = get_path_of_ini('emotionWords')
ini_live_triggers = get_path_of_ini('enableLiveTriggers')
ini_speed_control_keys = get_path_of_ini('enableSpeedControlKeys')
ini_big_cursor = get_path_of_ini('forceBigPointer')
ini_fov_scale_game = get_path_of_ini('fovScale')
ini_fov_scale_hud = get_path_of_ini('fovScaleHUD')
ini_fullscreen = get_path_of_ini('fullscreen')
ini_ground_tile_edge_blur_radius = get_path_of_ini('groundTileEdgeBlurRadius')
ini_half_framerate = get_path_of_ini('halfFrameRate')
ini_hard_quit_mode = get_path_of_ini('hardToQuitMode')
ini_hide_ui = get_path_of_ini('hideGameUI')
ini_hide_playback_display = get_path_of_ini('hidePlaybackDisplay')
ini_keep_past_recordings = get_path_of_ini('keepPastRecordings')
ini_mouse_spd = get_path_of_ini('mouseSpeed')
ini_music_volume = get_path_of_ini('musicLoudness')
ini_music_off = get_path_of_ini('musicOff')
ini_old_head_down_fac = get_path_of_ini('oldHeadDownFactor')
ini_old_head_forward_fac = get_path_of_ini('oldHeadForwardFactor')
ini_pause_on_minimize = get_path_of_ini('pauseOnMinimize')
ini_rec_audio = get_path_of_ini('recordAudio')
ini_rec_audio_length = get_path_of_ini('recordAudioLengthInSeconds')
ini_rec_game = get_path_of_ini('recordGame')
ini_res_height = get_path_of_ini('screenHeight')
ini_res_width = get_path_of_ini('screenWidth')
ini_skip_fps_measure = get_path_of_ini('skipFPSMeasure')
ini_sfx_buffer_size = get_path_of_ini('soundBufferSize')
ini_sfx_volume = get_path_of_ini('soundEffectsLoudness')
ini_sfx_off = get_path_of_ini('soundEffectsOff')
ini_sfx_sample_rate = get_path_of_ini('soundSampleRate')
ini_spell_check = get_path_of_ini('spellCheckOn')
ini_target_fps = get_path_of_ini('targetFrameRate')
ini_tutorial_done = get_path_of_ini('tutorialDone')
ini_use_custom_server = get_path_of_ini('useCustomServer')

# -----------------------------------

# Default Setting Variables
# Function parses through defaultSettings.ini and
# returns setting value.
def read_ini(setting):
    parser = ConfigParser()
    parser.read('settings/defaultSettings.ini')
    return(parser.get('settings', setting))

# Default Setting Variables
# Values default settings get stored in variables.
default_email = read_ini('email')
default_key = read_ini('accountKey')
default_borderless = read_ini('borderless')

default_key = read_ini('accountKey')
default_allow_saving_speech = read_ini('allowSavingSpeech')
default_auto_login = read_ini('autoLogIn')
default_baby_body_down_fac = read_ini('babyBodyDownFactor')
default_baby_head_down_fac = read_ini('babyHeadDownFactor')
default_blend_out_fr_fraction = read_ini('blendOutputFrameFraction')
default_blend_out_fr_pairs = read_ini('blendOutputFramePairs')
default_borderless = read_ini('borderless')
default_borderless_h_adjust = read_ini('borderlessHeightAdjust')
default_chk_rev_spelling = read_ini('checkReviewSpelling')
default_vsync = read_ini('countingOnVsync')
# default_culvert_stone_sprites = read_ini('culvertStoneSprites')
default_custom_server_address = read_ini('customServerAddress')
default_custom_server_port = read_ini('customServerPort')
default_e_right_click = read_ini('eKeyForRightClick')
default_email = read_ini('email')
default_emot_duration = read_ini('emotDuration')
# default_emot_words = read_ini('emotionWords')
default_emot_happy = read_ini('emotHappy')
default_emot_mad  = read_ini('emotMad')
default_emot_angry = read_ini('emotAngry')
default_emot_sad = read_ini('emotSad')
default_emot_devious = read_ini('emotDevious')
default_emot_joy = read_ini('emotJoy')
default_emot_blush = read_ini('emotBlush')
default_emot_hubba = read_ini('emotHubba')
default_emot_ill = read_ini('emotIll')
default_emot_yoohoo = read_ini('emotYoohoo')
default_emot_hmph = read_ini('emotHmph')
default_emot_love = read_ini('emotLove')
default_emot_oreally = read_ini('emotOreally')
default_emot_shock = read_ini('emotShock')
default_live_triggers = read_ini('enableLiveTriggers')
default_speed_control_keys = read_ini('enableSpeedControlKeys')
default_big_cursor = read_ini('forceBigPointer')
default_fov_scale_game = read_ini('fovScale')
default_fov_scale_hud = read_ini('fovScaleHUD')
default_fullscreen = read_ini('fullscreen')
default_ground_tile_edge_blur_radius = read_ini('groundTileEdgeBlurRadius')
default_half_framerate = read_ini('halfFrameRate')
default_hard_quit_mode = read_ini('hardToQuitMode')
default_hide_ui = read_ini('hideGameUI')
default_hide_playback_display = read_ini('hidePlaybackDisplay')
default_keep_past_recordings = read_ini('keepPastRecordings')
default_mouse_spd = read_ini('mouseSpeed')
default_music_volume = read_ini('musicLoudness')
default_music_off = read_ini('musicOff')
default_old_head_down_fac = read_ini('oldHeadDownFactor')
default_old_head_forward_fac = read_ini('oldHeadForwardFactor')
default_pause_on_minimize = read_ini('pauseOnMinimize')
default_rec_audio = read_ini('recordAudio')
default_rec_audio_length = read_ini('recordAudioLengthInSeconds')
default_rec_game = read_ini('recordGame')
default_res_height = read_ini('screenHeight')
default_res_width = read_ini('screenWidth')
default_skip_fps_measure = read_ini('skipFPSMeasure')
default_sfx_buffer_size = read_ini('soundBufferSize')
default_sfx_volume = read_ini('soundEffectsLoudness')
default_sfx_off = read_ini('soundEffectsOff')
default_sfx_sample_rate = read_ini('soundSampleRate')
default_spell_check = read_ini('spellCheckOn')
default_target_fps = read_ini('targetFrameRate')
default_tutorial_done = read_ini('tutorialDone')
default_use_custom_server = read_ini('useCustomServer')