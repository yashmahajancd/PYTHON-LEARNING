class A:
    def __iter__(self): return iter([1,2,3])

obj = A()

for i in obj:
    print(i)