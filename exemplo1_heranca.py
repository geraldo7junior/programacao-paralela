from threading import Thread
from time import sleep

class Hello(Thread):
    def run(self):
        sleep(3);
        print("Hello World")

thread = Hello()
thread.start()
