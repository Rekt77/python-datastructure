#!/usr/bin/python36

__author__="Rekt77"

class Node:
    def __init__(self,data,prev=None):
        self.data = data
        self.next = None
        self.prev = prev

class DoubleLinkedList:
    def __init__(self,data):
        self.head = Node(data)

    def addNode(self,data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data,cur)

    def removeNode(self,data):
        cur = self.head

        while cur.next is not None:
            if data ==self.head.data :
                self.head = cur.next
                cur.next.prev = None
                return

            if cur.next.data == data:
                cur.next = cur.next.next
                cur.next.prev = cur
                return

            else : print("item does not exist in linked list")

    def print(self):
        cur = self.head
        while cur is not None:
                print("cur val: %d"%cur.data,end=" / ")

                try:
                    print("prev val: %d"%cur.prev.data,end=" / ")
                    
                except AttributeError:
                    print("prev val : !!HeadNode!!",end=" / ")

                try:
                    print("next val: %d"%cur.next.data,end="\n")
                    
                except AttributeError:
                    print("next val : None",end="\n")

            
                if cur.next is not None:
                    cur = cur.next
                else :
                    break
            
if __name__=="__main__":
    myLink= DoubleLinkedList(50)
    myLink.addNode(60)
    myLink.addNode(70)
    myLink.addNode(80)
    myLink.addNode(90)
    myLink.print()

    print("")
    myLink.removeNode(50)
    myLink.removeNode(70)
    myLink.print()
        
