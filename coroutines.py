from inspect import getgeneratorstate

def subgen():
    print(f"state :{getgeneratorstate(g)}")
    x = 'ready to accept msg'
    message = yield x
    print('Subgen received:', message)

def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g
    return inner

g = subgen()

#g.send(None)
#g.send('KZK')

class BlaException(Exception):
    pass

@coroutine
def average():
    count = 0
    summ = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print('done')
        except BlaException:
            print('Custom exception thrown')
            break
        else:
            count += 1
            summ += x
            average = round(summ / count, 2)
    return average

a = average()
a.send(10)
a.send(20)
try:
    g.throw(BlaException)
except StopIteration as e:
    print('average', e.value)