class A:
    def __init__(self):
        self._x = 10
    @property
    def x(self):
        return self._x