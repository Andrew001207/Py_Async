def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner

class BlaException(Exception):
    pass

def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            print('KKU')
        else:
            print('............', message)

    return "Returned value"

@coroutine
def delegator(g):
    yield from g
            