from typing import Protocol, runtime_checkable
from functools import singledispatch

@runtime_checkable
class Protocolo(Protocol):
    def interface(self):
        ...

class Du:
    def interface(self):
        ...

class Duduzinho:
    ...

@singledispatch
def generic(arg):
    print('generic')

@generic.register
def _(arg: Protocolo):
    print('Protocols')


generic(Du())
generic(Duduzinho())
