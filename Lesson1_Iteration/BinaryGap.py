# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    n = bin(N)[2:]
    arr = []
    for i in range(len(n)):
        if n[i] == '1':
            arr.append(i)
    
    if len(arr) < 2:
        return 0
    
    res = 0
    for i in range(len(arr)-1):
        res = max(res, arr[i+1] - arr[i] - 1)
        
    return res