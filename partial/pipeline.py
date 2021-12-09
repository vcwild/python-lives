from closure import timer


class Pipeline:
    def __init__(self, *filters):
        self.filters = filters

    @timer
    def __call__(self, value):
        response = value

        for filter in self.filters:
            response = filter(response)

        return response


def soma_um(param):
    return param + 1


def tira_dez(param):
    return param - 10
