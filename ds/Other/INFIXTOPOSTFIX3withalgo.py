OPERATORS = set(['+', '-', '*', '/', '(', ')', '^'])
PRIORITY = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}


def infix_to_postfix(expression):
    stack = []
    output = ''
    count = 1
    # "(A+B*C^D/E)"
    for ch in expression:
        print(f"count={count}")
        if ch not in OPERATORS:
            print(f"-->NOT IN--> ch>{ch} not in opreator>{OPERATORS}")
            output += ch
        elif ch == '(':
            print(f"--> ch>{ch} == '(' --> ''")
            stack.append('(')
            print(stack)

        elif ch == ')':
            print(f"--> ch>{ch} == ')' --> ''")
            while stack and stack[-1] != '(':
                print(f"--> ch>{ch} == ')' --> ''")
                print(f"pop = )")
                output += stack.pop()
                print(f"output = {output} ")

            stack.pop()
        else:
            print("-->else")
            while stack and stack[-1] != '(' and PRIORITY[ch] <= PRIORITY[stack[-1]]:
                print(
                    f' ''ELSE-->while stack>{stack} |AND| stack[-1]>{stack[-1]} =! |AND| PRIORITY[ch]>{PRIORITY[ch]}| <= |PRIORITY[stack[-1]>{PRIORITY[stack[-1]]} h''')
                output += stack.pop()
                print(f"output = {output}")
            stack.append(ch)
            print(f"stack = {stack}")
        count = count+1
    while stack:
        output += stack.pop()
    return output


expression = "(A+B*C^D/E)"
infix_to_postfix(expression)
# expression = input('Enter infix expression')
print('infix expression: ', expression)
print('postfix expression: ', infix_to_postfix(expression))
