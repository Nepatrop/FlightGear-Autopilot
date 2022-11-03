import time
import GetData
import keyboard
from threading import Thread
from main import maxAltitude

takeOff = True
vOne = 40
pitch = 0
groundLevel = GetData.giveAltitude()

def PitchSet(newPitch):
    global pitch
    while pitch != newPitch:
        if pitch < newPitch:
            keyboard.send("Down")
            pitch += 5
            time.sleep(0.2)
        if pitch > newPitch:
            keyboard.send("Up")
            pitch -= 5
            time.sleep(0.2)

while takeOff:
    speed = GetData.giveSpeed()
    if speed < vOne:
        time.sleep(1)
        continue

    altitude = GetData.giveAltitude()
    while altitude < (groundLevel + 1000):
        PitchSet(10)
        time.sleep(1)
        print(altitude)
        if speed < vOne + 20:
            PitchSet(5)

    while altitude < maxAltitude:
        PitchSet(5)