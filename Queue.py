#!/usr/bin/python36
__author__ = "Rekt77"

class StaticQueue:

    def __init__(self,size):
        self.queue=list()
        self.size = size

    def enqueue(self,item):
        if(len(self.queue)>=self.size):
            print("[-]WARN : Queue over flow!!")
        else :
            self.queue.insert(0,item)

    def dequeue(self):
        try:
            self.queue.pop()
            return 1

        except IndexError:
            return 0

    def print(self):
        print(self.queue)


class DynamicQueue:

    def __init__(self):
        self.queue=list()

    def enqueue(self,item):
        self.queue.insert(0,item)

    def dequeue(self):
        try:
            self.queue.pop()
            return 1
        except IndexError:
            return 0

    def print(self):
        print(self.queue)


if __name__ == "__main__":

    myQueue = StaticQueue(10)
    for i in range(0,myQueue.size):
        myQueue.enqueue(i)
        
    myQueue.print()
    
    while myQueue.dequeue():
        myQueue.print()
