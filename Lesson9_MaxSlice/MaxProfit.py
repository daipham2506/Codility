# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    if(len(A)==0):
        return 0
    res = 0
    mi = A[0]
    for a in A[1:]:
        mi = min(mi, a)
        res = max(res, a - mi)
    return res