def auth(f):
    def w(u):
        if u=="admin": f(u)
    return w