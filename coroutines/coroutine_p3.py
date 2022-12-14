# coroutine.py
#
# A decorator function that takes care of starting a coroutine
# automatically on call.

def coroutine(func):
    def start(*args,**kwargs):
        cr = func(*args,**kwargs)
        next(cr)       
        return cr
    return start

# Example use
if __name__ == '__main__':
    @coroutine
    def grep(pattern):
        print("Looking for %s" % pattern)
        while True:
            line = (yield)
            if pattern in line:
                print(line,)

    g = grep("python")
    # Notice how you don't need a next() call here
    g.send("Yeah, but python, but yeah, but no")
    g.send("A series of python")
    g.send("python generators rock!") 