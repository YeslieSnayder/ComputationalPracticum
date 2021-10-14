import numpy as np


class ConsoleView:
    def __init__(self):
        pass

    @staticmethod
    def show_table(table: np.ndarray, method_name: str):
        print('-' * 60, sep='')
        print(f'\t\t\t{method_name}')
        print('-' * 60)
        print('\t', 'X', 'Exact', 'Euler', 'LTE', 'GTE', sep='\t')
        if not (len(table) >= 1 and len(table[0]) != 5):
            pass
        for i in range(len(table[0])):
            print(i + 1, table[0][i], table[1][i], table[2][i], table[3][i], table[4][i], sep='\t')
        print('-' * 60)
