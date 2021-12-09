from datetime import datetime
from functools import wraps
from time import sleep


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(datetime.utcnow())
        sleep(1)
        result = func(*args, **kwargs)
        print(datetime.utcnow())
        return result

    return wrapper


@timer
def teste_func():
    print("Teste")
