# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    res = [0]*N
    ma = 0
    for a in A:
        if 1 <= a <= N:
            res[a-1] +=1
            ma = max(ma, res[a-1])
        elif a == N+1:
            res = [ma]*N
    
    return res