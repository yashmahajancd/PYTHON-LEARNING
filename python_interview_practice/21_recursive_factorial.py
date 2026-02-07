def fact(i):
    return 1 if i==0 else i*fact(i-1)
print(fact(5))