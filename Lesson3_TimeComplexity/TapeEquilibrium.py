# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    N = len(A)
    left = A[0]
    right = sum(A[1:])
    res = abs(left-right)
    if res == 0: return 0
    for i in range(1,N-1):
        left += A[i]
        right -= A[i]
        res = min(res, abs(left-right))
    return res