import numpy as np

from model.errors.gte import GlobalTruncationError
from model.errors.lte import LocalTruncationError


def show_table(table: np.ndarray, method_name: str):
    print('-'*60, sep='')
    print(f'\t\t\t{method_name}')
    print('-'*60)
    print('\t', 'X', 'Exact', 'Euler', 'LTE', 'GTE', sep='\t')
    if not (len(table) >= 1 or len(table[0]) != 5):
        pass
    for i in range(len(table[0])):
        print(i+1, table[0][i], table[1][i], table[2][i], table[3][i], table[4][i], table[5][i], table[6][i], sep='\t')
    print('-'*60)


def euler_method(func, xi, yi, step=0.1):
    """

    :param func: derivative function which is initially given.
    :param xi:
    :param yi:
    :param step:
    :return: next approximate value for Y.
    """
    return yi + step * func(xi, yi)


def improved_euler_method(func, xi, yi, step=0.1):
    """

    :param func:
    :param xi:
    :param yi:
    :param step:
    :return: next approximate value for Y.
    """
    return yi + step * func(xi + step / 2, yi + step / 2 * func(xi, yi))


def runge_kutta_method(func, xi, yi, step=0.1):
    """

    :param func:
    :param xi:
    :param yi:
    :param step:
    :return: next approximate value for Y.
    """
    k1 = func(xi, yi)
    k2 = func(xi + step / 2, yi + step * k1 / 2)
    k3 = func(xi + step / 2, yi + step * k2 / 2)
    k4 = func(xi + step, yi + step * k3)
    return yi + step / 6 * (k1 + 2 * k2 + 2 * k3 + k4)


def local_error(func, derivative_func, method, y0, start=1., end=1.5, steps=5):
    arr = np.zeros(shape=steps, dtype=np.float32)
    xi = start
    y_real = y0
    for i, x in enumerate(np.linspace(start, end, steps)):
        if i == 0:
            arr[i] = 0
            continue
        y_approximate = method(derivative_func, xi, y_real)
        y_real = func(x)
        arr[i] = y_real - y_approximate
        xi = x
    return arr


def global_error(func, derivative_func, method, y0, start=1., end=1.5, steps=5):
    arr = np.zeros(shape=steps, dtype=np.float32)
    xi = start
    y_approximate = y0
    for i, x in enumerate(np.linspace(start, end, steps)):
        if i == 0:
            arr[i] = 0
            continue
        y_approximate = method(derivative_func, xi, y_approximate)
        y_real = func(x)
        arr[i] = y_real - y_approximate
        xi = x
    return arr


def func(x):
    return (x * (1 + x**2 / 3)) / (1 - x**2 / 3)    # y(1) = 2


def derivative_func(x, y):
    return (y ** 2 + x * y - x ** 2) / x ** 2


def calculate_table(method, x0, y0):
    table = np.zeros(shape=(7, 6), dtype=np.float32)
    table[0] = np.linspace(1, 1.5, 6)
    for i, x in enumerate(table[0]):
        table[1][i] = func(x)  # Exact y
        if i == 0:
            table[2][i] = func(x)   # Initial value
        else:
            table[2][i] = method(derivative_func, table[0][i-1], table[2][i - 1])
    table[3] = local_error(func, derivative_func, method, y0, steps=6)
    table[4] = global_error(func, derivative_func, method, y0, steps=6)

    # lte = LocalTruncationError(func, method)
    # gte = GlobalTruncationError(func, method)
    # table[5] = lte(1, 1.5, count=6)
    # table[6] = gte(1., 1.5, step=.1)

    return table


if __name__ == '__main__':
    table = calculate_table(euler_method, 1., 2.)
    show_table(table, 'Euler method')

    print()
    table = calculate_table(improved_euler_method, 1., 2.)
    show_table(table, 'Improved Euler method')

    print()
    table = calculate_table(runge_kutta_method, 1., 2.)
    show_table(table, 'Runge Kutta method')
