import time
import GetData
import keyboard
from threading import Thread
import interface
import connector

mainDeg = GetData.giveDeg()
vOne = 55
groundLevel = GetData.giveAltitude()
maxPitch = 15
minPitch = -15
takeOff = connector.takeOffList[-1]
print("main")
print(takeOff, "main")

def AutoThrust():
    speed = GetData.giveSpeed()
    while not takeOff:
        time.sleep(1)
    while takeOff:
        maxSpeed = connector.speedList[0]
        if speed < maxSpeed:
            speed = GetData.giveSpeed()
            keyboard.send("PageUp")

        if speed > maxSpeed:
            speed = GetData.giveSpeed()
            keyboard.send("PageDown")


def AutoDeg():
    while not takeOff:
        time.sleep(1)
    deg = GetData.giveDeg()
    while takeOff:
        if deg == mainDeg:
            deg = GetData.giveDeg()
            time.sleep(1)
        elif (deg - mainDeg) > 2:
            deg = GetData.giveDeg()
            keyboard.send("0")
            time.sleep(0.1)
        elif (deg - mainDeg) < -2:
            deg = GetData.giveDeg()
            keyboard.send("Enter")
            time.sleep(0.1)


def PitchPlus():
    truePitch = GetData.givePitch()
    if truePitch <= maxPitch:
        keyboard.send("Down")
        time.sleep(0.2)
    else:
        keyboard.send("Up")


def PitchMinus():
    truePitch = GetData.givePitch()
    if truePitch >= minPitch:
        keyboard.send("Up")
        time.sleep(0.2)
    else:
        keyboard.send("Down")


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


def Altitude():
    while not takeOff:
        time.sleep(1)
    while takeOff:
        maxAltitude = connector.altList[0]
        speed = GetData.giveSpeed()
        if speed < vOne:
            time.sleep(1)
            continue

        altitude = GetData.giveAltitude()
        while altitude < (groundLevel + 1000):
            speed = GetData.giveSpeed()
            if speed > vOne:
                needVerticalSpeed = 10
                VerSpeedSet(needVerticalSpeed)
            else:
                needVerticalSpeed = 5
                VerSpeedSet(needVerticalSpeed)

        while altitude < maxAltitude:
            PitchSet(5)

def Roll():
    maxRoll = 0
    while not takeOff:
        time.sleep(1)
    while takeOff:
        roll = GetData.giveRoll()
        if (roll > 2) and (maxRoll >= -15):
            keyboard.send("Left")
            time.sleep(0.2)
            maxRoll = maxRoll - 5

        if (roll < -2) and (maxRoll <= 15):
            keyboard.send("Right")
            time.sleep(0.2)
            maxRoll = maxRoll + 5

Thread(target=AutoThrust).start()
Thread(target=AutoDeg).start()
Thread(target=Altitude).start()
Thread(target=Roll).start()
takeOff = connector.takeOffList[0]