# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # The trick to this problem is 
    # that the min average slice has "the length of 2 or 3"
    # So, we only need to calculate the avg of the slices of length 2 and 3

    min_average = float('inf')
    min_position = 0

    for i in range(len(A)-2):
        average_len_2 = float( (A[i] + A[i+1]) / 2)
        average_len_3 = float( (A[i] + A[i+1] + A[i+2]) / 3)
        
        current_min = min(average_len_2, average_len_3)
        if current_min < min_average:
            min_average = current_min
            min_position = i
    
    last_average = float( (A[-2] + A[-1]) / 2 )
    if last_average < min_average:
        min_average = last_average
        min_position = len(A)-2
    
    return min_position