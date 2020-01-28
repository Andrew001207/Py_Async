from time import time

def gen(s):
    for i in s:
        yield i

def gen_filename():
    while True:
        yield f'{int(1000 * time())}.png'

g = gen_filename()