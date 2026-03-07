def coro():
    g=coro(); next(g); g.send(10)