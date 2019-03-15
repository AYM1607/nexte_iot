import minimalmodbus
import serial
from . import storage

# Communication constants
BAUD_RATE = 4800
TIMEOUT = 3
PARITY = serial.PARITY_EVEN

# Register constants
ACTIVE_POWER = 72
POWER_FACTOR = 96
TOTAL_ACTIVE_ENERGY = 128
TOTAL_REACTIVE_ENERGY = 134

# Storage constants
FILE_NAME = '/home/pi/nexte/nexte_iot_code/iot_nexte/readings.data'

devices = {}


def _initializeDeviceInStorage(address):
    allData = storage.getData(FILE_NAME).copy()
    allData[address] = {}
    allData[address]['kwh'] = 0
    allData[address]['kvarh'] = 0
    storage.saveData(allData, FILE_NAME)
    return allData.get(address).copy()


def _getPastReadings(address):
    allData = storage.getData(FILE_NAME).copy()
    data = allData.get(address)
    if data is None:
        return _initializeDeviceInStorage(address)
    return data


def _updateReadings(address):
    allData = storage.getData(FILE_NAME).copy()
    currentData = {}
    currentData['kwh'] = readFloat(TOTAL_ACTIVE_ENERGY, address)
    currentData['kvarh'] = readFloat(TOTAL_REACTIVE_ENERGY, address)
    allData[address] = currentData
    storage.saveData(allData, FILE_NAME)


def addDevice(address):
    newInst = minimalmodbus.Instrument('/dev/ttyUSB0', address)
    newInst.serial.baudrate = BAUD_RATE
    newInst.serial.timeout = TIMEOUT
    newInst.serial.parity = PARITY

    devices[address] = newInst


def readFloat(registerAddress, deviceAddress):
    device = devices[deviceAddress]
    return device.read_float(registerAddress, 3, 2)


def getData(address):
    pastReadings = _getPastReadings(address)
    data = {}
    data['kw'] = readFloat(ACTIVE_POWER, address)/1000
    data['pf'] = readFloat(POWER_FACTOR, address)
    data['kwh'] = readFloat(TOTAL_ACTIVE_ENERGY, address) - pastReadings.get('kwh')
    data['kvarh'] = readFloat(TOTAL_REACTIVE_ENERGY, address) - pastReadings.get('kvarh')
    _updateReadings(address)
    return data
