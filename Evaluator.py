import readData
from datetime import datetime

class Evaluator:
    def __init__(self):
        self._getData()

    def _getData(self):
        self.sessionsData = readData.getSessionData()
        self.userIds = readData.getUserIds()
        self.productIds = readData.getProductIds()

    def _checkIfBought(self, userId: int, productId: int, viewTime: datetime) -> bool:
        for session in self.sessionsData:
            if session[0] == userId and session[1] == productId and session[3] > viewTime:
                return True
        return False

    def evaluateModel(self, model) -> float:
        score = 0
        iter10p = len(self.sessionsData[:15000])//10
        for sessionNum, session in enumerate(self.sessionsData[:15000]): #for every VIEW session
            if sessionNum%iter10p == 0:
                print(sessionNum, "/", iter10p*10, 10*sessionNum//iter10p, "% DONE")
            if session[2] == "BUY_PRODUCT": continue
            recommended = model.ask(session[1]) #generate prediction for the product
            for i, productId in enumerate(recommended): #for each recommended product with index i
                if self._checkIfBought(session[0], productId, session[3]): #if product bought later 
                    score += 1/(i+1) #score increases (first item recommended gets higher score than the next)
        return score