import iot_nexte.storage as storage

#data = [1, 2, 3]

#storage.saveData(data, 'test.data')

newData = storage.getData('test.data')

print('This is the stored data')
print(newData)
