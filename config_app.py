import sys
from time import sleep
import pyshorteners
from os import system
import webbrowser
CopyRight = """
 _   _______ _         _                _                       
| | | | ___ \ |       | |              | |                      
| | | | |_/ / |    ___| |__   ___  _ __| |_ ___ _ __   ___ _ __ 
| | | |    /| |   / __| '_ \ / _ \| '__| __/ _ \ '_ \ / _ \ '__|
| |_| | |\ \| |___\__ \ | | | (_) | |  | ||  __/ | | |  __/ |   
 \___/\_| \_\_____/___/_| |_|\___/|_|   \__\___|_| |_|\___|_|   
                     Coded by | twitter:@S75XD & @F14Commander                                                                                                         
"""

def Write_Text_Animation(Message): #Programmet By twitter @F14Commander Github @xF14x
    for char in Message:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char !="\n":
            sleep(0.01)
        else:
            sleep(0.01)