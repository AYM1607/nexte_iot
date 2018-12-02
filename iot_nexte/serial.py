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


def readFloat(registerAddress, deviceAddress):
    device = devices[deviceAddress]
    return device.readFloat(registerAddress, 3, 2)


def getData(address):
    data = {}
    data['kw'] = readFloat(ACTIVE_POWER, address)/1000
    data['pf'] = readFloat(POWER_FACTOR, address)
    data['kwh'] = readFloat(TOTAL_ACTIVE_ENERGY, address)
    data['kvarh'] = readFloat(TOTAL_REACTIVE_ENERGY, address)
    return data
    
