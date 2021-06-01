import argparse
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from Model import Model

if __name__ == '__main__':
    m = Model()
    print(m.ask(120))
