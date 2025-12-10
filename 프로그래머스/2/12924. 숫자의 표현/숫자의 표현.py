import math

def solution(n):
    answer = 1
    start = 1
    end = 2
    while (start < end):
        if sum(range(start, end+1)) < n : 
            end += 1
        elif sum(range(start, end+1)) > n :
            start += 1
        else :
            answer += 1
            # print(range(start, end+1))
            end+=1
            
    return answer