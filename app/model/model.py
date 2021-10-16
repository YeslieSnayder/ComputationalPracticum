import numpy
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

        self.n0 = 10
        self.N = 100

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

    def euler_lte(self):
        return self._lte(self._euler_method, self.x0, self.X, count=self.steps, y0=self.y0)

    def improved_euler_lte(self):
        return self._lte(self._improved_euler_method, self.x0, self.X, count=self.steps, y0=self.y0)

    def runge_kutta_lte(self):
        return self._lte(self._runge_kutta_method, self.x0, self.X, count=self.steps, y0=self.y0)

    def euler_gte(self):
        return self._gte(self._euler_method, self.x0, self.X, count=self.steps, y0=self.y0)

    def improved_euler_gte(self):
        return self._gte(self._improved_euler_method, self.x0, self.X, count=self.steps, y0=self.y0)

    def runge_kutta_gte(self):
        return self._gte(self._runge_kutta_method, self.x0, self.X, count=self.steps, y0=self.y0)

    def n_plane(self):
        return np.linspace(self.n0, self.N, self.N - self.n0 + 1, dtype=np.int)

    def euler_lte_errors(self):
        return np.array([
            numpy.amax(self._lte(self._euler_method, self.x0, self.X, y0=self.y0, count=n))
            for n in range(self.n0, self.N + 1)
        ])

    def improved_euler_lte_errors(self):
        return np.array([
            numpy.amax(self._lte(self._improved_euler_method, self.x0, self.X, y0=self.y0, count=n))
            for n in range(self.n0, self.N + 1)
        ])

    def runge_kutta_lte_errors(self):
        return np.array([
            numpy.amax(self._lte(self._runge_kutta_method, self.x0, self.X, y0=self.y0, count=n))
            for n in range(self.n0, self.N + 1)
        ])

    def euler_gte_errors(self):
        return np.array([
            numpy.amax(self._gte(self._euler_method, self.x0, self.X, y0=self.y0, count=n))
            for n in range(self.n0, self.N + 1)
        ])

    def improved_euler_gte_errors(self):
        return np.array([
            numpy.amax(self._gte(self._improved_euler_method, self.x0, self.X, y0=self.y0, count=n))
            for n in range(self.n0, self.N + 1)
        ])

    def runge_kutta_gte_errors(self):
        return np.array([
            numpy.amax(self._gte(self._runge_kutta_method, self.x0, self.X, y0=self.y0, count=n))
            for n in range(self.n0, self.N + 1)
        ])
