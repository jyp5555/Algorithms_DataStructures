import math
def solution(n):
    ans = 0
    if n <= 1: return n

    if n % 2 == 1:
        ans = 1 + solution(n//2)
    else:
        ans = solution(n//2)
    
    return ans