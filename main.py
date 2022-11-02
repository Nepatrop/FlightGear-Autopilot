import time
import numpy as np
import keyboard
import GetData
from threading import Thread

maxSpeed = float(input('Введите необходимую скорость: '))
mainDeg = GetData.giveDeg()
takeOff = True
pitch = 0

def AutoThrust():
    speed = GetData.giveSpeed()
    while takeOff:
        if speed < maxSpeed:
            speed = GetData.giveSpeed()
            keyboard.send("PageUp")
            time.sleep(0.1)
        if speed > maxSpeed:
            speed = GetData.giveSpeed()
            keyboard.send("PageDown")
            time.sleep(0.1)

def AutoDeg():
    deg = GetData.giveDeg()
    while takeOff:
        if deg == mainDeg:
            deg = GetData.giveDeg()
            time.sleep(1)
        if deg > mainDeg:
            deg = GetData.giveDeg()
            keyboard.send("0")
            time.sleep(0.1)
        if deg < mainDeg:
            deg = GetData.giveDeg()
            keyboard.send("Enter")
            time.sleep(0.1)

def AutoAltitude():
    global pitch
    realAltitude = GetData.giveAltitude()
    takeoffAltitude = realAltitude + 1000
    while takeOff:
        if (realAltitude <= takeoffAltitude) and (pitch <= 15):
            keyboard.send("Down")
            pitch = pitch + 5
            time.sleep(0.25)
        if takeoffAltitude - realAltitude <= 100:
            while pitch != 10:
                keyboard.send("Up")
                pitch = pitch - 5
                time.sleep(0.25)
        if takeoffAltitude - realAltitude <= 20:
            while pitch != 5:
                keyboard.send("Up")
                pitch = pitch - 5
                time.sleep(0.25)

Thread(target=AutoThrust).start()
Thread(target=AutoAltitude).start()