from tabulate import tabulate

from app.model.model import Model
from app.model.exceptions.incorrect_params_error import IncorrectParamsError


class ConsoleView:
    def __init__(self, model: Model):
        self.model = model

        self.page1_config = {'show_y': True, 'show_euler': True, 'show_IE': True, 'show_RK': True}
        self.page2_config = {'show_euler': True, 'show_IE': True, 'show_RK': True}
        self.page3_config = {'show_euler': True, 'show_IE': True, 'show_RK': True}

    def update_page1(self) -> None:
        data = {'X': self.model.x_plane()}
        if self.page1_config['show_y']:
            data['Y exact'] = self.model.exact()
        if self.page1_config['show_euler']:
            data['Y Euler'] = self.model.euler_method()
        if self.page1_config['show_IE']:
            data['Y Improved Euler'] = self.model.improved_euler_method()
        if self.page1_config['show_RK']:
            data['Y Runge Kutta'] = self.model.runge_kutta_method()
        self.show_page1(data)

    def show_page1(self, data=None) -> None:
        if data is None:
            self.update_page1()
            return
        ConsoleView.print_table(data)

    def update_page2(self, method: ['lte', 'gte'] = None) -> None:
        if method is not None and method not in ['lte', 'gte']:
            raise IncorrectParamsError('"method" with values "lte" or "gte"')

        data = {'X': self.model.x_plane()}
        if method == 'gte':
            if self.page2_config['show_euler']:
                data['Euler GTE Error'] = self.model.euler_gte()
            if self.page2_config['show_IE']:
                data['Improved Euler GTE Error'] = self.model.improved_euler_gte()
            if self.page2_config['show_RK']:
                data['Runge Kutta GTE Error'] = self.model.runge_kutta_gte()
        else:
            if self.page2_config['show_euler']:
                data['Euler LTE Error'] = self.model.euler_lte()
            if self.page2_config['show_IE']:
                data['Improved Euler LTE Error'] = self.model.improved_euler_lte()
            if self.page2_config['show_RK']:
                data['Runge Kutta LTE Error'] = self.model.runge_kutta_lte()
        self.show_page1(data)

    def show_page2(self, data=None, method: ['lte', 'gte'] = None) -> None:
        if data is None:
            self.update_page2(method)
            return
        ConsoleView.print_table(data)

    @staticmethod
    def print_table(table: dict):
        print(tabulate(table, headers='keys', tablefmt='fancy_grid'))
