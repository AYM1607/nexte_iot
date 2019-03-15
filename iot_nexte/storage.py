import pickle


def saveData(data, filename):
    writeFile = open(filename, 'wb')
    pickle.dump(data, writeFile)
    writeFile.close()


def getData(filename):
    readFile = open(filename, 'rb')
    data = pickle.load(readFile)
    readFile.close()
    return data
