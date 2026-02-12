class Dog: pass
class Cat: pass
def factory(t):
    return Dog() if t=="dog" else Cat()