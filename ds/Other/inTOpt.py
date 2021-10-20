def isOperand(c):
    if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9'):
        return True


a = +
print(isOperand("a"))
# def toPostfix(infix):
#     stack = []
#     postfix = ''

#     for c in infix:
#         if isOperand(c):

#             postfix += c
#         else:
#             if isLeftParenthesis(c):
#                 stack.append(c)
#             elif isRightParenthesis(c):
#                 operator = stack.pop()
#                 while not isLeftParenthesis(operator):
#                     postfix += operator
#                     operator = stack.pop()
#             else:
#                 while (not isEmpty(stack)) and hasLessOrEqualPriority(c, peek(stack)):
#                     postfix += stack.pop()
#                 stack.append(c)

#     while (not isEmpty(stack)):
#         postfix += stack.pop()
#     return postfix


# infx = '3*(x+1)-2/2'
# print(toPostfix(infx))
