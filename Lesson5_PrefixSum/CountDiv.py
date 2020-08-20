def solution(A, B, K):
    c = 0
    if A%K==0:
        c+=1
    return int(B/K) - int(A/K) + c