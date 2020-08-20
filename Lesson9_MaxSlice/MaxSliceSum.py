# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    if len(A) == 1:
        return A[0]
    res = A[0]
    ma = 0
    for a in A:
        ma = max(a, ma + a)
        res = max(ma, res)
    return res