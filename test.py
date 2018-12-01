import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)


from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.register_read_message import ReadInputRegistersResponse

client = ModbusClient(method="rtu", port="/dev/ttyUSB0", stopbits=1, bytesize=8, parity="E", baudrate=9600, timeout=3)

connection = client.connect()

print(connection)

result = client.read_holding_registers(48, 1, unit=0x01)

print(result)
print(result.raw)

client.close()
