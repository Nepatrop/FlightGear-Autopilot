import time
import GetData
import keyboard
from threading import Thread

takeOff = True
maxSpeed = float(input('Введите необходимую скорость: '))
maxAltitude = float(input('Введите необходимую высоту: '))
mainDeg = GetData.giveDeg()
vOne = 60
groundLevel = GetData.giveAltitude()
maxPitch = 10
minPitch = -10
maxRoll = 20
minRoll = -20

def AutoThrust():
    speed = GetData.giveSpeed()
    while takeOff:
        if speed < maxSpeed:
            speed = GetData.giveSpeed()
            keyboard.send("PageUp")
            time.sleep(0.05)
        if speed > maxSpeed:
            speed = GetData.giveSpeed()
            keyboard.send("PageDown")
            time.sleep(0.05)

def AutoDeg():
    deg = GetData.giveDeg()
    while takeOff:
        if deg == mainDeg:
            deg = GetData.giveDeg()
            time.sleep(1)
        if (deg - mainDeg) > 1:
            deg = GetData.giveDeg()
            keyboard.send("0")
            time.sleep(0.2)
        if (deg - mainDeg) < 1:
            deg = GetData.giveDeg()
            keyboard.send("Enter")
            time.sleep(0.2)

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

def Altitude():
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

def Roll():
    while takeOff:
        roll = GetData.giveRoll()
        if roll > 1:
            keyboard.send("Left")
            time.sleep(0.2)

        if roll < -1:
            keyboard.send("Right")
            time.sleep(0.2)

        deg = GetData.giveDeg()
        if (deg - mainDeg) > 1:
            keyboard.send("Left")
            time.sleep(0.2)
        if (deg - mainDeg) < -1:
            keyboard.send("Right")
            time.sleep(0.2)

Thread(target=AutoThrust).start()
Thread(target=Altitude).start()
Thread(target=Roll).start()