from threading import Thread
import time
num=10
def one():
    while(1 !=num):
        print("1")
        time.sleep(2)
    
def two():
    while(1 != num):
        print("2")
        time.sleep(5)


p1 = Thread(target = one)
p2 = Thread(target = two)

p1.start()
p2.start()
