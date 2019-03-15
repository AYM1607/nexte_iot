import iot_nexte.serial as serial
import iot_nexte.web as web

serial.addDevice(1)
# serial.addDevice(2)
device1Data = serial.getData(1)
# device2Data = serial.getData(2)
print(device1Data)
status1 = web.sendMeterData(meterId=1, payload=device1Data)
# status2 = web.sendMeterData(meterId=1, parload=device2Data)

print(status1)
# print(status2)
