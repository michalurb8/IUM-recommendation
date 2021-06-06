from datetime import datetime
from ModelInterface import ModelInterface
import readData

K = 5

class Evaluator:
    def __init__(self):
        self._getData()

    def _getData(self):
        self.testSessions = readData.getTestSessions()

    def _checkIfBought(self, userId: int, productId: int, viewTime: datetime, sessionId: int) -> bool:
        for session in self.testSessions:
            if session[0] == userId and session[1] == productId and session[3] > viewTime and session[4] == sessionId:
                return True
        return False

    def evaluateModel(self, model: ModelInterface) -> float:
        score = 0
        for session in self.testSessions: #for every VIEW session
            if session[2] == "BUY_PRODUCT": continue
            recommended = model.ask(session[1], K) #generate K predictions for the product
            for i, productId in enumerate(recommended): #for each recommended product with index i
                if self._checkIfBought(session[0], productId, session[3], session[4]): #if product bought later by this user
                    score += 1/(i+5) # assign score (each item recommended gets higher score than the next)
        return score