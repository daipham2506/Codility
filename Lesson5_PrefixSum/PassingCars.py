# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    res = 0
    count_zero = 0
    for a in A:
        if a == 0:
            count_zero +=1
        else:
            res += count_zero
        
        if res > 1000000000:
            return -1
    return res