#----------------------------------------------
#              SilencingTheGamer
#----------------------------------------------
#              Create by IPewzner
#----------------------------------------------
# This script is used to remind my brother
# to not raise his voice too loud when he 
# plays video games.
# so to teach him to be quieter when he plays 
# I made this script that dims the screen to 
# 5 seconds when his voice is over the max 
# volume.
#----------------------------------------------
#   If you use it, do it at your own risk!
#----------------------------------------------
#                   Enjoy!
#----------------------------------------------


import sounddevice as sd
import screen_brightness_control as sbc
from datetime import datetime 
import numpy as np

ALLOWED_VOLUME = 50
PENALTY_TIME = 5 * 1000     #microsecond
RUN_TIME = 2*60*60*1000     #microsecond   2 hr * 60 min * 60 sec * 1000 microsec
DARK_MODE = 0.5             #dark the screen to (initielBrightness / darkMode)
FALSE=0
TRUE=1

darkMode = FALSE
lastTime = datetime.now().microsecond
initialBrightness=sbc.get_brightness()

def print_sound(indata, outdata, frames, time, status):
    global lastTime
    global initialBrightness
    global darkMode

    volume_norm = np.linalg.norm(indata)*10
    
    if not darkMode:
        if  (int(volume_norm) > ALLOWED_VOLUME):
            lastTime = datetime.now().microsecond
            sbc.set_brightness(int(initialBrightness*DARK_MODE))
            darkMode = TRUE
        else:
            initialBrightness = sbc.get_brightness()
    else:
        if ((lastTime-datetime.now().microsecond) > PENALTY_TIME):
            sbc.set_brightness(initialBrightness)
            darkMode = FALSE

with sd.Stream(callback=print_sound):
    sd.sleep(RUN_TIME)

