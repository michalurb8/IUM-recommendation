from DataStorage import DataStorage

if __name__ == '__main__':

    data = DataStorage()
    m = data.evaluateModel()
    n = data.evaluateNaive()
    print(m)
    print(n)
