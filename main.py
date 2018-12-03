import iot_nexte.serial as serial
import iot_nexte.web as web

serial.addDevice(1)
data = serial.getData(1)

status = web.sendMeterData(meterId=1, payload=data)

print(status)
print(data)
