import pickle


def saveData(data, fileName):
    fileObj = open(fileName, 'wb+')
    pickle.dump(data, fileObj)
    fileObj.close()


def loadData(fileName):
    fileObj = open(fileName, 'rb+')
    data = pickle.load(fileObj)
    fileObj.close()
    return data
