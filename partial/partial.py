from functools import partialmethod


class Pessoa:
    def __init__(self):
        self._vivo = True

    @property
    def vivo(self):
        return self._vivo

    def set_state(self, valor):
        self._vivo = valor

    morrer = partialmethod(set_state, False)
    renascer = partialmethod(set_state, True)
