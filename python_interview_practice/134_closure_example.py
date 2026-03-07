def outer(x):
    def inner(): return x
    return inner