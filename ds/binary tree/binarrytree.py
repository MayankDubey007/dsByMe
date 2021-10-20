class Node:
    def __init__(self,data):
        self.data = data
        self.rightN = None
        self.leftN = None
class binaryTree:
    def __init__(self):
        self.root = None
    def inorder(self):
        if(self.root == None):
            print("tree Is Empty....")
        else:
            self._inorder(self.root)
    def _inorder(self,temp):
        if temp:
            self.inorder(temp.leftN)
            print(temp.data,end=" ") 
            self._inorder(temp.rightN)
    def preorder(self):
        if(self.root == None):
            print("tree Is Empty....")
        else:
            self._preorder(self.root)
    def _preorder(self,temp):
        if temp:
            print(temp.data,end=" ") 
            self.preorder(temp.leftN)
            self._preorder(temp.rightN)
    def insert(self,data):
        if data < self.data:
            if self.leftN == None:
                self.leftN = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.rightN == None:
                self.rightN = Node(data)
            else:
                self.rightN.insert(data)    
obj = binaryTree()
# first = Node(1)
# second = Node(2)
# third = Node(3)
# fourth = Node(4)
# fifth = Node(5)
# sixth = Node(6)
# seventh = Node(7)
# first.leftN = second
# print(first.data)
# print(first.leftN.data)
                #         1
                #       /   \
                #      2     3
                #     / \   / \
                #    4   5 6   7
# obj.root = first 
# first.rightN = second 
# first.leftN = third
# second.rightN = fourth
# second.leftN = fifth
# third.rightN = sixth
# third.leftN = seventh
# print(first.leftN.leftN.data)
obj.insert(10)
obj.insert(5)
obj.insert(15)
obj.insert(2)
obj.inorder()
print()