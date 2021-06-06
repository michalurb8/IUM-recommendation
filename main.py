from NaiveModel import NaiveModel
from MainModel import MainModel
from Evaluator import Evaluator

if __name__ == '__main__':
    m = MainModel()
    m.fit()
    n = NaiveModel()
    e = Evaluator()
    print("main score:", e.evaluateModel(m))
    print("naive score:", e.evaluateModel(n))
