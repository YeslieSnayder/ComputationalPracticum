from app.model.model import Model


class Controller:
    def __init__(self, model: Model, view):
        self.model = model
        self.view = view

    def update_page1(self):
        # update model by checking checkboxes
        self.view.update_page1()

    def show_page1(self):
        self.view.show_page1()
