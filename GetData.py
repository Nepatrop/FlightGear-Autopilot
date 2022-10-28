import numpy as np

def giveSpeed():
    filename = 'data/speedData.txt'
    data = np.loadtxt(filename, delimiter=',', skiprows=1, dtype=float)
    speed = data[-1]
    return speed

def giveDeg():
    filename = 'data/degData.txt'
    data = np.loadtxt(filename, delimiter=',', skiprows=1, dtype=float)
    deg = data[-1]
    return deg

def giveAltitude():
    filename = 'data/altitudeData.txt'
    data = np.loadtxt(filename, delimiter=',', skiprows=1, dtype=float)
    altitude = data[-1]
    return altitude