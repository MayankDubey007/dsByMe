class stack:
    def __init__(self):
        self.arr = []

    def push(self, data):
        self.arr.append(data)

    def pop(self):
        if not self.isEmpty():
            self.arr.pop()
        else:
            print("Stack is Empty")

    def peek(self):
        if not self.isEmpty():
            return self.arr[-1]

    def length(self):
        return len(self.arr)

    def isEmpty(self):
        if self.arr == []:
            return True
        else:
            return False

    def getStack(self):
        return self.arr

def reverse(string):
    stk = stack()
    ls = []
    newstr = ""
    for i in string:
        stk.push(i)
    ls = stk.getStack()
    for j in range(len(ls)):
        newstr += ls.pop()
    print(newstr)


st = stack()
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.push(5)
# st.peek()
print("******")
print(st.getStackItems())
# st.Reverse()
print("******")
print(st.length())
print(st.peek())

# st.size()
print(st.arr)
st.pop()
print(st.arr)
print(st.arr)
st.pop()
print(st.arr)
st.pop()
print(st.arr)
st.pop()
print(st.arr)
st.pop()
print(st.arr)
st.pop()
print(st.arr)
reverse("abcd")
