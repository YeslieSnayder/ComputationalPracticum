import numpy as np


class ConsoleView:
    def __init__(self):
        pass

    @staticmethod
    def show_table(table: np.ndarray):
        print('-' * 60)
        print('X', 'Y Exact', 'Y Euler', 'Y Improved', 'Y Runge Kutta', sep='\t\t')
        if not (len(table) >= 1 and len(table[0]) != 5):
            pass
        for i in range(len(table[0])):
            for j in range(len(table)):
                print(table[j][i], end='\t\t')
            print()
        print('-' * 60)
