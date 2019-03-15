import iot_nexte.serial as serial
import iot_nexte.web as web


# --------- Add devices to the serial communication buffer.
serial.addDevice(1)
# serial.addDevice(2)

# --------- Get data stored in the device's registers.
device1Data = serial.getData(1)
# device2Data = serial.getData(2)

print(device1Data)

# --------- Send data to the API and get status code.
# status1 = web.sendMeterData(meterId=7, payload=device1Data)
# status2 = web.sendMeterData(meterId=8, parload=device2Data)


# --------- Log status code to the console.
# print(status1)
# print(status2)
