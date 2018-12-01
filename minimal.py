import minimalmodbus
import serial

instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)

instrument.serial.baudrate = 4800
instrument.serial.parity = serial.PARITY_EVEN
instrument.serial.timeout = 3

# print(instrument)

voltage = instrument.read_float(48, functioncode=3, numberOfRegisters=2)

print(voltage)
