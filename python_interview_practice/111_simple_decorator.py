def deco(func):
    def wrapper():
        print("Before")
        func()
    return wrapper