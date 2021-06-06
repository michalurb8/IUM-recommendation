from NaiveModel import NaiveModel
from MainModel import MainModel
from Evaluator import Evaluator

if __name__ == '__main__':
    m = MainModel()
    m.fromFile()
    print("Example main prediction:", m.ask(1015))
    n = NaiveModel()
    print("Example naive prediction:", n.ask(1015))
    e = Evaluator()
    print("main score:", e.evaluateModel(m))
    print("naive score:", e.evaluateModel(n))
