import time
import GetData
import keyboard
from threading import Thread
##from main import maxAltitude
##from main import maxSpeed

maxAltitude = 3000
takeOff = True
vOne = 60
groundLevel = GetData.giveAltitude()
maxPitch = 10
minPitch = -10

def PitchPlus():
    truePitch = GetData.givePitch()
    if (truePitch >= 8) and (truePitch <= 10):
        time.sleep(0.2)
    else:
        if truePitch <= maxPitch:
            keyboard.send("Down")
            time.sleep(0.2)
        else:
            keyboard.send("Up")
            time.sleep(0.2)

def PitchMinus():
    truePitch = GetData.givePitch()
    if truePitch >= minPitch:
        keyboard.send("Up")
        time.sleep(0.2)
    else:
        keyboard.send("Down")
        time.sleep(0.2)

def PitchSet(needPitch):
    truePitch = GetData.givePitch()
    while truePitch != needPitch:
        if truePitch < needPitch:
            PitchPlus()
        if truePitch > needPitch:
            PitchMinus()

def VerSpeedSet(needVSpeed):
    verticalSpeed = GetData.giveVerticalSpeed()
    while verticalSpeed != needVSpeed:
        if verticalSpeed < needVSpeed:
            PitchPlus()
        if verticalSpeed > needVSpeed:
            PitchMinus()

while takeOff:
    speed = GetData.giveSpeed()
    if speed < vOne:
        time.sleep(1)
        continue

    altitude = GetData.giveAltitude()
    while altitude < (groundLevel + 2000):
        speed = GetData.giveSpeed()
        if speed > vOne:
            needVerticalSpeed = 10
            VerSpeedSet(needVerticalSpeed)