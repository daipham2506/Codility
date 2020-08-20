# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    if len(A) < 3:
        return 0
    A = sorted(A)
    for i in range(len(A)-2):
        if A[i] + A[i+1] > A[i+2]:
            return 1
    return 0