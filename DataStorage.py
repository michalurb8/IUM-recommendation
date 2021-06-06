import readData
from MainModel import MainModel
from NaiveModel import NaiveModel
from Evaluator import Evaluator

class DataStorage:
    def __init__(self):
        self._getData()
        self.model = MainModel(self.sessionsData, self.userIds, self.productIds)
        self.naive = NaiveModel(self.sessionsData, self.productIds, readData.getProductCategoryData())
        self.eval = Evaluator(self.sessionsData, self.userIds, self.productIds)

    def _getData(self):
        self.sessionsData = readData.getSessionData()
        self.userIds = readData.getUserIds()
        self.productIds = readData.getProductIds()
    
    def evaluateModel(self):
        return self.eval.evaluateModel(self.model)

    def evaluateNaive(self):
        return self.eval.evaluateModel(self.naive)