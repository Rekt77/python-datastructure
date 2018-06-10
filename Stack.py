#!/usr/bin/python36
__author__ = "Rekt77"

class Stack:
    def __init__(self,size):
        self.stack=list()
        self.size = size

    def pop(self):
        try :
            self.stack.pop(0)
            return 1
        
        except IndexError :
            return 0

    def push(self,data):
        if self.size > len(self.stack):
            self.stack.insert(0,data)
        else :
            print("[-]WARN : Stack Overflow")

    def print(self):
        print(self.stack)


if __name__ == "__main__":

    myStack = Stack(10)
    for i in range(0,myStack.size):
        myStack.push(i)
        
    myStack.print()
    
    while myStack.pop():
        myStack.print()
