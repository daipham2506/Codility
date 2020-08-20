# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    if len(A) < 3:
        return 0
    A = sorted(A)
    return max(A[0]*A[1]*A[-1], A[-1]*A[-2]*A[-3])