# Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log
# Eyes - eyes.mp3 - every 30 min - EyDone - log
# Physical activity - physical.mp3 every - 45 min - ExDone - log
#
# Rules
# Pygame module to play audio

import time
from pygame import mixer


def gettime():
    ctime = time.asctime(time.localtime(time.time()))
    return ctime


def log(x):
    t = open("health.txt" ,"wt")
    t.write("At ")
    t.write(str(gettime()))
    t.write(f"=>{x}")
    t.close()


"""I have copied this function but you should understand this"""


def music(announcement,mp3,stopword,logname):
    """ >>>>>>This function takes 05 parameters as described below:
        1)announcement (str) - This takes what is to be announced while starting music
        2)mp3 (mp3 filename) - This takes name of the music file.
        3)vol (int) - This takes what should be the volume of the music to be played
        4)stopword (str) - This takes what should be entered to stop the music
        5)logname(str) - Type of activity by which your log is saved"""
    print(announcement)
    mixer.init()
    mixer.music.load(mp3)
    # mixer.music.set_volume(vol)
    mixer.music.play()
    print(f"Enter {stopword} to Stop the music")
    while(True):
        int = input()
        int2 = int.capitalize()
        if int2 == stopword:
            mixer.music.stop()
            log(f"User has {logname}")
            break
        else:
            print(f"Enter valid input\nEnter{stopword} to stop the music")
            continue

watertime = time.time()
eyetime = time.time()
phytime = time.time()
"""Local time is in seconds so we have to convert 30 min or 45 min into seconds"""
waterzone = 21 * 60  # We want the user to drink water in every 32 mins
eyezone = 22 * 60
phyzone = 45*60





while (True):
    if time.time() - watertime >= waterzone:
        music("Time for a glass of water", "water.mp3", "Drank", "drunk a glass of water")
        print("Done")
        watertime = time.time()
        continue



    if time.time() - eyetime >= eyezone:
        music("Time for a glass of water", "eyes.mp3", "Eyedone", "done the exercise of eyes")
        print("Done")
        eyetime = time.time()
        continue

    if time.time() - phytime >= phyzone:
        music("Time for a glass of water", "physical.mp3", "Exdone", "done exercise")
        print("Done")
        phytime = time.time()
        continue


