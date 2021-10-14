from app.model.approximations.euler_method import EulerApproximation
from app.model.approximations.improved_euler_method import ImprovedEulerApproximation
from app.model.approximations.runge_kutta_method import RungeKuttaApproximation
from app.model.errors.lte import LocalTruncationError
from app.model.errors.gte import GlobalTruncationError


class Model:
    def __init__(self, solution_function, derivative_function):
        self._euler_method = EulerApproximation(derivative_function)
        self._improved_euler_method = ImprovedEulerApproximation(derivative_function)
        self._runge_kutta_method = RungeKuttaApproximation(derivative_function)
        self._lte = LocalTruncationError(solution_function)
        self._gte = GlobalTruncationError(solution_function)

    def euler_method(self, xi, yi, step):
        return self._euler_method(xi, yi, step)

    def improved_euler_method(self, xi, yi, step):
        return self._improved_euler_method(xi, yi, step)

    def runge_kutta_method(self, xi, yi, step):
        return self._runge_kutta_method(xi, yi, step)

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
