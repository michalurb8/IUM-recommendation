import readData
from sklearn.neighbors import NearestNeighbors
import numpy as np

class Model:
    def __init__(self):
        self._getData()
        self._createMatrix()
        self._fit()

    def _getUserIndex(self, userId: int) -> int:
        try:
            index = self.userIds.index(userId)
        except:
            print("ERROR: Trying to use an ID of a nonexistent user: ", userId)
            return 0
        return index

    def _getProductIndex(self, productId: int) -> int:
        try:
            index = self.productIds.index(productId)
        except:
            print("ERROR: Trying to use an ID of a nonexistent product: ", productId)
            return 0
        return index

    def _getData(self):
        self.sessionsData = readData.getSessionData()
        self.userIds = readData.getUserIds()
        self.productIds = readData.getProductIds()

    def _createMatrix(self):
        userCount = len(self.userIds)
        productCount = len(self.productIds)
        self.matrix = np.zeros((productCount, userCount))
        for session in self.sessionsData:
            product_id = session[1]
            product_index = self._getProductIndex(product_id)
            user_id = session[0]
            user_index = self._getUserIndex(user_id)
            change = 1 if session[2] == "BUY_PRODUCT" else 0.1 #Viewing product contributes much less than buying
            self.matrix[product_index][user_index] += change

    def _fit(self):
        self.model = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=10)
        self.model._fit(self.matrix)
    
    def ask(self, product_id: int, k: int = 5):
        user = [self.matrix[self._getUserIndex(product_id), :]]
        result = self.model.kneighbors(user, n_neighbors=k+1) #calculate one more that needed
        result = result[1][0]
        result = [self.userIds[item] for item in result]
        return result[1:] #product best matches itself, so exclude first one