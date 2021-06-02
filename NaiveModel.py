import readData
import numpy as np
from operator import itemgetter
from heapq import heappush, nlargest

BUY_WEIGHT = 1
VIEW_WEIGHT = 0.1

class NaiveModel:
    def __init__(self):
        self._getData()
        self._createProductPopularityList()
        self._createMPPCDict()

    def _getData(self):
        self.sessionsData = readData.getSessionData()
        self.productIds = readData.getProductIds()
        self.productsData = readData.getProductCategoryData()

    def _getProductIndex(self, productId: int) -> int:
        try:
            index = self.productIds.index(productId)
        except:
            print("ERROR: Trying to use an ID of a nonexistent product: ", productId)
            return 0
        return index

    def _createProductPopularityList(self):
        productCount = len(self.productsData)
        self.productPopularityList = np.zeros(productCount)
        for session in self.sessionsData:
            product_id = session[1]
            product_index = self._getProductIndex(product_id)
            change = BUY_WEIGHT if session[2] == "BUY_PRODUCT" else VIEW_WEIGHT #Viewing product contributes much less than buying
            self.productPopularityList[product_index] += change

    # dictionary of lists of products and their popularity (value) in given category (key)
    def _createMPPCDict(self):
        self.mppcDict = { }
        for product in self.productsData:
            product_id = product[0]
            product_popularity = self.productPopularityList[ self._getProductIndex(product_id) ]
            product_category = product[1]
            if product_category not in self.mppcDict: self.mppcDict[product_category] = []
            heappush(self.mppcDict[product_category], (product_id, product_popularity))

    def ask(self, product_id: int, k: int = 5):
        product_index = self._getProductIndex(product_id)
        product_category = self.productsData[product_index][1]
        return [ item[0] for item in nlargest(k, self.mppcDict[product_category], key = lambda x: x[1]) ]
