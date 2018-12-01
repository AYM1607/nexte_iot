import minimalmodbus
import serial

instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)

instrument.serial.baudrate = 9600
instrument.serial.parity = serial.PARITY_EVEN

print(instrument)

