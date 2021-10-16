from controller.controller import Controller
from model.model import Model
from view.console_view import ConsoleView


class Application:
    def __init__(self):
        self.model = Model()
        self.view = ConsoleView(self.model)
        self.controller = Controller(self.model, self.view)

    def run(self):
        self.controller.show_page1()


if __name__ == '__main__':
    app = Application()
    app.run()
