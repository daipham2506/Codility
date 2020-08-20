# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    myDict = {}
    
    for item in A:
        myDict[item] = 0 
        
    for item in A:
        myDict[item] += 1

    index_dominator = []

    for index in range( len(A) ):
        if myDict[ A[index] ] > float( len(A) / 2):
            index_dominator += [index]
    
    if len(index_dominator) == 0:
        return -1
    else:
        return index_dominator[0]