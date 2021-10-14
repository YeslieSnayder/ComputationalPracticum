from app.model.exceptions.incorrect_params_error import IncorrectParamsError


class IncorrectParamTypeError(IncorrectParamsError):
    def __init__(self, param, given_type, expected):
        self.message = f'Parameter "{param}" has incorrect type. Expected: {expected}, but given: {given_type}'
