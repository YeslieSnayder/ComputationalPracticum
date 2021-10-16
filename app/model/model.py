import numpy as np

from app.model.approximations.euler_method import EulerApproximation
from app.model.approximations.improved_euler_method import ImprovedEulerApproximation
from app.model.approximations.runge_kutta_method import RungeKuttaApproximation
from app.model.errors.lte import LocalTruncationError
from app.model.errors.gte import GlobalTruncationError


class Model:
    def __init__(self):
        self.__solution_function = lambda x: (x * (1 + x ** 2 / 3)) / (1 - x ** 2 / 3)
        self.__derivative_function = lambda x, y: (y ** 2 + x * y - x ** 2) / x ** 2

        self._euler_method = EulerApproximation(self.__derivative_function)
        self._improved_euler_method = ImprovedEulerApproximation(self.__derivative_function)
        self._runge_kutta_method = RungeKuttaApproximation(self.__derivative_function)
        self._lte = LocalTruncationError(self.__solution_function)
        self._gte = GlobalTruncationError(self.__solution_function)

        self.x0 = 1.
        self.y0 = 2.
        self.X = 1.5
        self.steps = 6

    def x_plane(self):
        return np.linspace(self.x0, self.X, self.steps, dtype=np.float32)

    def exact(self):
        return self.__solution_function(self.x_plane())

    def euler_method(self):
        return self._calculate_approximation(self._euler_method)

    def improved_euler_method(self):
        return self._calculate_approximation(self._improved_euler_method)

    def runge_kutta_method(self):
        return self._calculate_approximation(self._runge_kutta_method)

    def _calculate_approximation(self, method):
        xs = self.x_plane()
        arr = np.zeros(shape=self.steps)
        arr[0] = self.__solution_function(xs[0])
        step = float(xs[1] - xs[0])
        for i in range(1, self.steps):
            arr[i] = method(xs[i - 1], arr[i - 1], step)
        return arr

    def euler_lte(self, start, end, y0, steps=-1, step=0):
        # TODO: Check step and steps and raise error
        if step != 0:
            return self._lte(self._euler_method, start, end, step=step, y0=y0)
        elif steps > 0:
            return self._lte(self._euler_method, start, end, steps=steps, y0=y0)
        else:
            # TODO: Raise error
            return 0

    def improved_euler_lte(self, start, end, y0, steps=-1, step=0):
        # TODO: Check step and steps and raise error
        if step != 0:
            return self._lte(self._improved_euler_method, start, end, step=step, y0=y0)
        elif steps > 0:
            return self._lte(self._improved_euler_method, start, end, steps=steps, y0=y0)
        else:
            # TODO: Raise error
            return 0

    def runge_kutta_lte(self, start, end, y0, steps=-1, step=0):
        # TODO: Check step and steps and raise error
        if step != 0:
            return self._lte(self._runge_kutta_method, start, end, step=step, y0=y0)
        elif steps > 0:
            return self._lte(self._runge_kutta_method, start, end, steps=steps, y0=y0)
        else:
            # TODO: Raise error
            return 0

    def euler_gte(self, start, end, y0, steps=-1, step=0):
        # TODO: Check step and steps and raise error
        if step != 0:
            return self._gte(self._euler_method, start, end, step=step, y0=y0)
        elif steps > 0:
            return self._gte(self._euler_method, start, end, steps=steps, y0=y0)
        else:
            # TODO: Raise error
            return 0

    def improved_euler_gte(self, start, end, y0, steps=-1, step=0):
        # TODO: Check step and steps and raise error
        if step != 0:
            return self._gte(self._improved_euler_method, start, end, step=step, y0=y0)
        elif steps > 0:
            return self._gte(self._improved_euler_method, start, end, steps=steps, y0=y0)
        else:
            # TODO: Raise error
            return 0

    def runge_kutta_gte(self, start, end, y0, steps=-1, step=0):
        # TODO: Check step and steps and raise error
        if step != 0:
            return self._gte(self._runge_kutta_method, start, end, step=step, y0=y0)
        elif steps > 0:
            return self._gte(self._runge_kutta_method, start, end, steps=steps, y0=y0)
        else:
            # TODO: Raise error
            return 0
