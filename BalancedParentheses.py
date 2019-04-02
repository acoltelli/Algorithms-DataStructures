from Stack import *


def parentheses(str):
    stack = Stack(len(str))

    for i in str:    
        if i in "([{":
            stack.push(i)
        else: # )]}
            top = stack.pop()
            if not pair(top, i): #does the last item added to stack match(type of parenthese) current item
                return False #if does not match, means that parentheses in str are out of order and not matching
    if stack.isEmpty():
        return True
    return False

def pair(open, close):
    return "([{".index(open) == ")]}".index(close)  # check if type of parenthese matches 


print parentheses('{{([][])}()}')
print parentheses('[{()]')
print parentheses('{(([])[])[]]}')
print parentheses('{(([])[])[]}[]')





