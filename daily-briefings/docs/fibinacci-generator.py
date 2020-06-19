### Generator
def fibonacci(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b


## Iterator
class Fib():
    def __init__(self, max):
        self.max = max
    
    def __iter__(self):
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        retval = self.a
        if retval > self.max:
            raise StopIteration
        else:
            self.a, self.b = self.b, self.a + self.b
            return retval




if __name__ == "__main__":
    for n in fibonacci(100):
        print(n)
    
    f = Fib(20)
    # import pdb; pdb.set_trace()
    for v in f:
        print(v)
