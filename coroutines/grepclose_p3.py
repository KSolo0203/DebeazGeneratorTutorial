# grepclose.py
#
# A coroutine that catches the close() operation

from coroutine_p3 import coroutine

@coroutine
def grep(pattern):
    print("Looking for %s" % pattern)
    try:
        while True:
            line = (yield)
            if pattern in line:
                print(line,)
    except GeneratorExit:
        print("Going python away. Goodbye!")

# Example use
if __name__ == '__main__':
    g = grep("python")
    g.send("Yeah, python, but no, but yeah, but no")
    g.send("A series of python tubes")
    g.send("python generators rock!")
    g.close()

