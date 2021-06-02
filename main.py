from Evaluator import Evaluator
from Model import Model
from NaiveModel import NaiveModel
from Evaluator import Evaluator

if __name__ == '__main__':
    print("Fitting the main model... ", end="")
    m = Model()
    print("DONE")
    print("Fitting the naive model... ", end="")
    n = NaiveModel()
    print("DONE")

    print("Example main answer:", m.ask(1012))
    print("Example naive answer:", n.ask(1012))

    print("Preparing the evaluator... ", end="")
    e = Evaluator()
    print("DONE")

    mScore = e.evaluateModel(m)
    nScore = e.evaluateModel(n)

    print(mScore, " ", nScore)