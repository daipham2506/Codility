# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    N = len(A)
    B = set(range(1,N+2))
    C = B - set(A)
    return C.pop()