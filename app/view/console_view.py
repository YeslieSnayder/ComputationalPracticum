from tabulate import tabulate

from app.model.model import Model


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

    @staticmethod
    def print_table(table: dict):
        print('-' * 62)
        print(tabulate(table, headers='keys'))
        print('-' * 62)
