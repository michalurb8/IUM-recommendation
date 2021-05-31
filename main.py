import argparse
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import readData

if __name__ == '__main__':
    sessionsData = readData.getData()[0]
    userCount = readData.getUserCount()
    productCount = readData.getProductCount()
    matrix = np.zeros((userCount, productCount))
    #trzeba zrobic inaczej ale musze konczyc, jednak latwiej bedzie wgrac baze uzytkownikow i produktow zeby wiedziec jakie maja id zeby latwiej zrobic macierz, jutro rano sie za to zabiore