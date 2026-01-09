username = "yashmahajancd"

# --------------------  SCOPE  ---------------------------

def func():
    # username = "chai"
    print(username)
    
print(username)           # yashmahajancd
func()                    # yashmahajancd

# ---------------------------------------------------------

x = 99

# def func2(y):
#     z = x + y
#     return z

# result = func2(1)
# print(result)           # 100

# ---------------------------------------------------------

# def func3():
#     global x
#     x = 12
    
# func3()
# print(x)                # 12

# ---------------------------------------------------------

# def f1():
#     x = 88
#     def f2():
#         print(x)
#     f2()
# f1()                      # 88

# --------------------  CLOSURE  --------------------------

# def f1():
#     x = 88
#     def f2():
#         print(x)
#     return f2
# my_result = f1()                      
# my_result()                 # 88

# ---------------------------------------------------------

def chaicoder(num):
    def actual(x):
        return x ** num
    return actual

a = chaicoder(2)
b = chaicoder(3)

print(a(3))
print(b(3))