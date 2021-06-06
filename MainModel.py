from sklearn.neighbors import NearestNeighbors
import numpy as np
from ModelInterface import ModelInterface
from joblib import dump, load
import readData

BUY_WEIGHT = 5
VIEW_WEIGHT = 1

class MainModel(ModelInterface):
    def __init__(self):
        self._getData()
        self._createMatrix()
        self.model = None

    def _getData(self):
        self.sessionsData = readData.getTrainingSessions()
        self.userIds = readData.getUserIds()
        self.productIds = readData.getProductIds()

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

    def _createMatrix(self):
        userCount = len(self.userIds)
        productCount = len(self.productIds)
        self.matrix = np.zeros((productCount, userCount))
        for session in self.sessionsData:
            product_id = session[1]
            product_index = self._getProductIndex(product_id)
            user_id = session[0]
            user_index = self._getUserIndex(user_id)
            change = BUY_WEIGHT if session[2] == "BUY_PRODUCT" else VIEW_WEIGHT #Viewing product contributes much less than buying
            self.matrix[product_index][user_index] += change

    def fit(self):
        self.model = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=10)
        self.model.fit(self.matrix)
    
    def toFile(self):
        dump(self.model, 'mainmodel.joblib')

    def fromFile(self):
        try:
            self.model = load('mainmodel.joblib')
        except:
            raise Exception("No model file found")
    
    def ask(self, product_id: int, k: int = 5):
        if self.model == None:
            raise Exception('Model must be fit first')
        product = [self.matrix[self._getProductIndex(product_id), :]]
        result = self.model.kneighbors(product, n_neighbors=k+1) #calculate one more than needed
        result = result[1][0]
        result = [self.productIds[item] for item in result]
        return result[1:] #product best matches itself, so exclude the first one