def mainRun():
    import time
    import GetData
    import keyboard
    import PyQt5
    import threading
    from PyQt5 import QtCore, QtGui, QtWidgets
    from threading import Thread
    import connector

    mainDeg = GetData.giveDeg()
    print(mainDeg)
    vOne = 55
    groundLevel = GetData.giveAltitude()
    print(groundLevel)
    takeOff = connector.takeOffList[0]
    maxPitch = 10
    minPitch = -5
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
        alt = GetData.giveAltitude()
        while takeOff and alt <= groundLevel + 10:
            if deg == mainDeg:
                deg = GetData.giveDeg()
                time.sleep(1)
            elif deg > mainDeg:
                deg = GetData.giveDeg()
                keyboard.send("0")
                time.sleep(0.5)
            elif deg < mainDeg:
                deg = GetData.giveDeg()
                keyboard.send("Enter")
                time.sleep(0.5)

    def PitchPlus():
        truePitch = GetData.givePitch()
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
                time.sleep(0.1)
                maxRoll = maxRoll - 5

            if (roll < -2) and (maxRoll <= 15):
                keyboard.send("Right")
                time.sleep(0.1)
                maxRoll = maxRoll + 5

    Thread(target=AutoThrust).start()
    Thread(target=Altitude).start()
    Thread(target=Roll).start()


if __name__ == "__main__":
    import interface
    interface.interfaceRun()