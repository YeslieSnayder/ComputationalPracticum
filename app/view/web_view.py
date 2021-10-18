import eel
import matplotlib.pyplot as plt

from app.model.model import Model
from app.model.exceptions.incorrect_params_error import IncorrectParamsError


class WebView:
    def __init__(self, model: Model):
        self.model = model

    def run(self):
        eel.init('view/static')
        eel.start('index.html', size=(1000, 600))

    def show_page1(self, show_y=True, show_euler=True, show_ie=True, show_rk=True) -> None:
        data = {'X': self.model.x_plane()}
        if show_y:
            data['Y exact'] = self.model.exact()
        if show_euler:
            data['Y Euler'] = self.model.euler_method()
        if show_ie:
            data['Y Improved Euler'] = self.model.improved_euler_method()
        if show_rk:
            data['Y Runge Kutta'] = self.model.runge_kutta_method()
        WebView._change_image(data, 1)

    def show_page2(self, method: ['lte', 'gte'] = None, show_euler=True, show_ie=True, show_rk=True) -> None:
        if method is not None and method not in ['lte', 'gte']:
            raise IncorrectParamsError('"method" with values "lte" or "gte"')

        data = {'X': self.model.x_plane()}
        if method == 'gte':
            if show_euler:
                data['Euler GTE Error'] = self.model.euler_gte()
            if show_ie:
                data['Improved Euler GTE Error'] = self.model.improved_euler_gte()
            if show_rk:
                data['Runge Kutta GTE Error'] = self.model.runge_kutta_gte()
        else:
            if show_euler:
                data['Euler LTE Error'] = self.model.euler_lte()
            if show_ie:
                data['Improved Euler LTE Error'] = self.model.improved_euler_lte()
            if show_rk:
                data['Runge Kutta LTE Error'] = self.model.runge_kutta_lte()
        WebView._change_image(data, 2)

    def show_page3(self, method: ['lte', 'gte'] = None, show_euler=True, show_ie=True, show_rk=True) -> None:
        if method is not None and method not in ['lte', 'gte']:
            raise IncorrectParamsError('"method" with values "lte" or "gte"')

        data = {'X': self.model.n_plane()}
        if method == 'gte':
            if show_euler:
                data['Euler GTE Error'] = self.model.euler_lte_errors()
            if show_ie:
                data['Improved Euler GTE Error'] = self.model.improved_euler_lte_errors()
            if show_rk:
                data['Runge Kutta GTE Error'] = self.model.runge_kutta_lte_errors()
        else:
            if show_euler:
                data['Euler LTE Error'] = self.model.euler_gte_errors()
            if show_ie:
                data['Improved Euler LTE Error'] = self.model.improved_euler_gte_errors()
            if show_rk:
                data['Runge Kutta LTE Error'] = self.model.runge_kutta_gte_errors()
        WebView._change_image(data, 3)

    def _change_image(table: dict, page_number: int) -> None:
        for key in table.keys():
            if key == 'X':
                continue
            plt.plot(table['X'], table[key], label=key)
        if page_number == 1:
            plt.xlabel('x')
            plt.ylabel('y')
        elif page_number == 2:
            plt.xlabel('x')
            plt.ylabel('Error')
        elif page_number == 3:
            plt.xlabel('n')
            plt.ylabel('Error')
        plt.legend()
        plt.savefig('view/static/img/graph.png', bbox_inches='tight', transparent=True)
        eel.updateImage()()
        plt.close()
