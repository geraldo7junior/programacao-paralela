from threading import Thread
from time import sleep

class Hello:
    def foo(self):
        sleep(3);
        print("Hello World")

hello = Hello()
thread = Thread(target=hello.foo)
thread.start()
