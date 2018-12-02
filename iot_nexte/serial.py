import minimalmodbus
import serial

# Communication constants
BAUD_RATE = 4800
TIMEOUT = 3
PARITY = serial.PARITY_EVEN

# Register constants
ACTIVE_POWER = 72
POWER_FACTOR = 96
TOTAL_ACTIVE_ENERGY = 128
TOTAL_REACTIVE_ENERGY = 134

devices = {}


def addDevice(address):
    newInst = minimalmodbus.Instrument('/dev/ttyUSB0', address)
    newInst.serial.baudrate = BAUD_RATE
    newInst.serial.timeout = TIMEOUT
    newInst.serial.parity = PARITY

    devices[address] = newInst

def readRegister():

