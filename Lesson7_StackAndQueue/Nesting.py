# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    stack = []
    
    for c in S: 
        if c == '(':
            stack.append(c) 
    
        if len(stack) == 0:
            return 0
        elif c == ')':
            if stack.pop() != '(':
                return 0
    
    if len(stack) == 0:
        return 1
    return 0