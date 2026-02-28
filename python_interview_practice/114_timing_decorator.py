import time
def timer(f):
    def wrap():
        s=time.time(); f(); print(time.time()-s)
    return wrap