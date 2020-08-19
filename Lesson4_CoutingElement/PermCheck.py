# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    B = set(range(1, len(A)+1))
    C = B - set(A)
    if len(C) == 0:
        return 1
    return 0