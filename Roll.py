import time
import GetData
import keyboard

takeOff = True
maxRoll = 20
minRoll = -20
vOne = 60
mainDeg = GetData.giveDeg()

while takeOff:
    roll = GetData.giveRoll()
    if roll > 1:
        keyboard.send("Left")
        time.sleep(1)

    if roll < -1:
        keyboard.send("Right")
        time.sleep(1)

    deg = GetData.giveDeg()
    if (deg - mainDeg) > 1:
        keyboard.send("Left")
        time.sleep(1)
    if (deg - mainDeg) < -1:
        keyboard.send("Right")
        time.sleep(1)