from functools import singledispatchmethod

from abc import ABC


class Edu(ABC):
    ...


class Duduzinho(Edu):
    ...


class Pessoa:
    def __init__(self) -> None:
        self._status = "ok"

    @singledispatchmethod
    def chamei(self, p):
        raise NotImplementedError("Opa, caiu na genérica")

    @chamei.register
    def _(self, p: Edu):
        print(f"{self._status}: Caí na lógica do Edu")


p = Pessoa()
