# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    n = len(A)
    if n == 0:
        return A
        
    K = K % n
    if K == 0:
        return A
    
    return A[n-K:] + A[:n-K]