#!/usr/bin/python36

__author__="Rekt77"

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self,data):
        self.head = Node(data)
        
    def addNode(self,data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)

    def removeNode(self,data):
        cur = self.head

        while cur.next is not None :
            if data == self.head.data :
                self.head = cur.next
                break
            
            if cur.next.data == data :
                cur.next = cur.next.next
                return
            else : print("item does not exist in linked list")

    def print(self):
        cur = self.head
        while cur is not None:
            try :
                print("cur val: %d, next val : %d"%(cur.data,cur.next.data))
            except AttributeError:
                print("cur val: %d, next val : None"%(cur.data))
            if cur.next is not None:
                cur = cur.next
            else :
                break


if __name__=="__main__":
    myLink= LinkedList(50)
    myLink.addNode(60)
    myLink.addNode(70)
    myLink.addNode(80)
    myLink.addNode(90)
    myLink.print()

    print("")
    myLink.removeNode(50)
    myLink.removeNode(70)
    myLink.print()
