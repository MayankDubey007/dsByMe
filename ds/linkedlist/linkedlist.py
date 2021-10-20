class node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linklist:
    def __init__(self):
        self.start = None

    def viewList(self):
        if self.start == None:
            print("list is empty")
        else:
            temp = self.start
            while temp != None:
                print(temp.data, end="  ")
                # temp=temp.next

    def delteFst(self):
        if self.start == None:
            print("linked list is empty")
        else:
            temp = self.start
            self.start = self.start.next

    def insertLst(self, value):
        newnode = node(value)
        if (self.start == None):
            self.start == newnode
        else:
            temp = self.start
            while temp.next == None:
                temp = temp.next
                temp.next == newnode


mylist = linklist()
mylist.insertLst(10)
mylist.insertLst(20)
mylist.insertLst(30)
mylist.insertLst(40)
mylist.insertLst(50)
mylist.insertLst(60)
mylist.insertLst(70)
mylist.insertLst(80)
mylist.insertLst(90)
mylist.viewList()
