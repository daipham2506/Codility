# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    mySet = set(range(1,X+1))
    for i,a in enumerate(A):
        if a in mySet:
            mySet.remove(a)
        if mySet == set():
            return i
    return -1