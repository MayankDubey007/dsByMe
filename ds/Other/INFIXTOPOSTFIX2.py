def inFixToPostFix():
    inFix = '3*(x+1)-2/2'
    postFix = ''
    s = Stack()
    for c in inFix:
        # if elif chain for anything that c can be
        if c in "0123456789x":
            postFix += c
        elif c in "+-":
            if s.isEmpty():
                s.push(c)
            elif s.top() =='(':
                s.push(c)
        elif c in "*/":
            if s.isEmpty():
                s.push(c)
            elif s.top() in "+-(":
                s.push(c)
        elif c == "(":
            s.push(c)
        elif c == ")":
            while s.top() != '(':
                postFix += s.pop()
            s.pop()
        else:
            print("Error")
    print(postFix)
print(inFixToPostFix())