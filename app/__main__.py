import numpy as np

from model.model import Model
from view.console_view import ConsoleView


class Application:
    def __init__(self):
        self.x0 = 1.
        self.y0 = 2.
        self.X = 1.5
        self.steps = 6

        self.solution_function = lambda x: (x * (1 + x**2 / 3)) / (1 - x**2 / 3)
        self.derivative_function = lambda x, y: (y ** 2 + x * y - x ** 2) / x ** 2

        self.model = Model(self.solution_function, self.derivative_function)
        self.view = ConsoleView()

    def run(self):
        table = np.zeros(shape=(5, 6), dtype=np.float32)
        error_table = np.zeros(shape=(6, 6), dtype=np.float32)
        table[0] = np.linspace(self.x0, self.X, self.steps)
        step = float(table[0][1] - table[0][0])

        for i, x in enumerate(table[0]):
            table[1][i] = self.solution_function(x)  # Exact y
            if i == 0:  # Initial values
                table[2][i] = self.y0
                table[3][i] = self.y0
                table[4][i] = self.y0
            else:
                table[2][i] = self.model.euler_method(table[0][i - 1], table[2][i - 1], step)
                table[3][i] = self.model.improved_euler_method(table[0][i - 1], table[2][i - 1], step)
                table[4][i] = self.model.runge_kutta_method(table[0][i - 1], table[2][i - 1], step)
        error_table[0] = self.model.euler_lte(self.x0, self.X, self.y0, step=step)
        error_table[1] = self.model.improved_euler_lte(self.x0, self.X, self.y0, step=step)
        error_table[2] = self.model.runge_kutta_lte(self.x0, self.X, self.y0, step=step)

        error_table[3] = self.model.euler_gte(self.x0, self.X, self.y0, step=step)
        error_table[4] = self.model.improved_euler_gte(self.x0, self.X, self.y0, step=step)
        error_table[5] = self.model.runge_kutta_gte(self.x0, self.X, self.y0, step=step)

        self.view.show_table(table)
        self.view.show_table(error_table)


if __name__ == '__main__':
    app = Application()
    app.run()
