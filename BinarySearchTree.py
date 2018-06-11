#!/usr/bin/python36
__author__ = "Rekt77"

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self,data):
        self.root = Node(data)
        self.inorder_list = list()
        self.preorder_list = list()
        self.postorder_list = list()

    def addNode(self,cur,data):
        
        if cur.data > data:

            if cur.left is not None :
                self.addNode(cur.left,data)
            else:
                cur.left = Node(data)

        elif cur.data < data :
            if cur.right is not None :
                self.addNode(cur.right,data)
                    
            else :
                cur.right = Node(data)


    def preorder(self,cur):
        
        self.preorder_list.append(cur.data)
        
        if cur.left is not None:
            self.preorder(cur.left)
            
        if cur.right is not None:
            self.preorder(cur.right)

    def inorder(self,cur):
        
        if cur.left is not None:
            self.inorder(cur.left)
            
        self.inorder_list.append(cur.data)
        
        if cur.right is not None:
            self.inorder(cur.right)
            
    def postorder(self,cur):

        if cur.left is not None:
            self.postorder(cur.left)

        if cur.right is not None:
            self.postorder(cur.right)

        self.postorder_list.append(cur.data)
        
        
                
if __name__ == "__main__" :
    myBST = BinarySearchTree(15)
    for i in range(30,0,-2):
        myBST.addNode(myBST.root,i)

    myBST.preorder(myBST.root)
    myBST.inorder(myBST.root)
    myBST.postorder(myBST.root)

    print(myBST.preorder_list)
    print(myBST.inorder_list)
    print(myBST.postorder_list)

            
            
                
        
        
