import argparse
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import readData

def getUserIndex(userId: int) -> int:
    try:
        index = userIds.index(userId)
    except:
        print("ERROR: Trying to use an ID of a nonexistent user: ", userId)
        return 0
    return index

def getProductIndex(productId: int) -> int:
    try:
        index = productIds.index(productId)
    except:
        print("ERROR: Trying to use an ID of a nonexistent product: ", productId)
        return 0
    return index

if __name__ == '__main__':
    sessionsData = readData.getSessionData()
    userIds = readData.getUserIds()
    productIds = readData.getProductIds()
    userCount = len(userIds)
    productCount = len(productIds)
    matrix = np.zeros((userCount, productCount))
    for session in sessionsData:
        user_id = session[0]
        user_index = getUserIndex(user_id)
        product_id = session[1]
        product_index = getProductIndex(product_id)

        change = 1 if session[2] == "BUY_PRODUCT" else 0.1

        matrix[user_index][product_index] += change
    print(np.sum(matrix))