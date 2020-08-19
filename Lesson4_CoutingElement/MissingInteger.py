# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    B = set(filter(lambda x: x >0, A))
    C = set(range(1,len(B)+2))
    D = C - B
    
    return min(D)