open = ["[","{","("]
close = ["]","}",")"]
mystr = "{[]{()}}"
def check(mystr):
    stack = []
    top = len(stack)-1
    for i in mystr:
        if i in open:
            stack.append(i)
        elif i in close:
            pos = close.index(i)
            if ((len(stack)>0)and(open[pos]==stack[top])):
                stack.pop()
            else:
                return "unbalanced"    
    if len(stack)==0:
        return "balanced"
    else:
        return "unbalanced"
string = "{[]{()}}"
print(string,"-", check(string))