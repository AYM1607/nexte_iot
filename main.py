import iot_nexte.serial as serial

serial.addDevice(1)
data = serial.getData(1)

print(data)
