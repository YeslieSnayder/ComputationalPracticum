from app.model.model import Model


class Controller:
    def __init__(self, model: Model, view):
        self.model = model
        self.view = view

    def show_page1(self):
        self.view.show_page1()

    def show_page2(self):
        self.view.show_page2()

    def show_page3(self):
        self.view.show_page3()
