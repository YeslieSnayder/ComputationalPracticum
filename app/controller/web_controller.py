from model.model import Model


class WebController:
    def __init__(self, model: Model, view):
        self.model = model
        self.view = view

        self.page1_config = {'show_y': True, 'show_euler': True, 'show_ie': True, 'show_rk': True}
        self.page2_config = {'method': 'lte', 'show_euler': True, 'show_ie': True, 'show_rk': True}
        self.page3_config = {'method': 'lte', 'show_euler': True, 'show_ie': True, 'show_rk': True}

    def run(self):
        self.view.run()

    def onUpdatePage1(self, params):
        if params is not None:
            self._parse_params(1, params)
        self.view.show_page1(**self.page1_config)

    def onUpdatePage2(self, params):
        if params is not None:
            self._parse_params(2, params)
        self.view.show_page2(**self.page2_config)

    def onUpdatePage3(self, params):
        if params is not None:
            self._parse_params(3, params)
        self.view.show_page3(**self.page3_config)

    def _parse_params(self, page, params):
        if 'n0_field' in params and params['n0_field']:
            self.model.n0 = int(params['n0_field'])
        if 'N_field' in params and params['N_field']:
            self.model.N = int(params['N_field'])
        if 'x0_field' in params and params['x0_field']:
            self.model.x0 = float(params['x0_field'])
        if 'X_field' in params and params['X_field']:
            self.model.X = float(params['X_field'])
        if 'y0_field' in params and params['y0_field']:
            self.model.y0 = float(params['y0_field'])
        if 'steps_field' in params and params['steps_field']:
            self.model.steps = int(params['steps_field'])
        if 'method_field' in params and (params['method_field'] == 'lte' or params['method_field'] == 'gte'):
            if page == 2:
                self.page2_config['method'] = params['method_field']
            elif page == 3:
                self.page3_config['method'] = params['method_field']
        if page == 1:
            self.page1_config['show_y'] = params['exact']
            self.page1_config['show_euler'] = params['euler']
            self.page1_config['show_ie'] = params['improved']
            self.page1_config['show_rk'] = params['runge_kutta']
        elif page == 2:
            self.page2_config['show_euler'] = params['euler']
            self.page2_config['show_ie'] = params['improved']
            self.page2_config['show_rk'] = params['runge_kutta']
        elif page == 3:
            self.page3_config['show_euler'] = params['euler']
            self.page3_config['show_ie'] = params['improved']
            self.page3_config['show_rk'] = params['runge_kutta']
