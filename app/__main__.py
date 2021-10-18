import eel

from controller.web_controller import WebController
from model.model import Model
from view.web_view import WebView


model = Model()
view = WebView(model)
controller = WebController(model, view)


@eel.expose
def onUpdatePage1(page, params):
    print(page, params)
    controller.onUpdatePage1(params)


@eel.expose
def onUpdatePage2(page, params):
    print(page, params)
    controller.onUpdatePage2(params)


@eel.expose
def onUpdatePage3(page, params):
    print(page, params)
    controller.onUpdatePage3(params)


class Application:
    def __init__(self, model, view, controller):
        self.model = model
        self.view = view
        self.controller = controller

    def run(self):
        self.controller.run()


if __name__ == '__main__':
    app = Application(model, view, controller)
    app.run()
