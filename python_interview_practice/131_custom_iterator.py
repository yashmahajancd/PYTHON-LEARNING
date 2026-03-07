class Count:
    def __iter__(self): self.i=0; return self
    def __next__(self):
        if self.i<3:
            self.i+=1; return self.i
        raise StopIteration