import time
import GetData
import keyboard
from threading import Thread

takeOff = True
maxSpeed = float(input('Введите необходимую скорость: '))
maxAltitude = float(input('Введите необходимую высоту: '))
mainDeg = GetData.giveDeg()

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
        if deg > mainDeg:
            deg = GetData.giveDeg()
            keyboard.send("0")
            time.sleep(0.1)
        if deg < mainDeg:
            deg = GetData.giveDeg()
            keyboard.send("Enter")
            time.sleep(0.1)

Thread(target=AutoThrust).start()
Thread(target=AutoAltitude).start()