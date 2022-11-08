import numpy as np

def giveAltitude():
    filename = 'data/altitudeData.txt'
    data = np.loadtxt(filename, delimiter=',', skiprows=1, dtype=float)
    altitude = data[-1]
    return altitude

def giveSpeed():
    filename = 'data/speedData.txt'
    data = np.loadtxt(filename, delimiter=',', skiprows=1, dtype=float)
    speed = data[-1]
    return speed

def giveVerticalSpeed():
    filename = 'data/verticalSpeedData.txt'
    data = np.loadtxt(filename, delimiter=',', skiprows=1, dtype=float)
    vSpeed = data[-1]
    return vSpeed

def giveDeg():
    filename = 'data/degData.txt'
    data = np.loadtxt(filename, delimiter=',', skiprows=1, dtype=float)
    deg = data[-1]
    return deg

def givePitch():
    filename = 'data/pitchData.txt'
    data = np.loadtxt(filename, delimiter=',', skiprows=1, dtype=float)
    pitch = data[-1]
    return pitch

def giveRoll():
    filename = 'data/rollData.txt'
    data = np.loadtxt(filename, delimiter=',', skiprows=1, dtype=float)
    roll = data[-1]
    return roll