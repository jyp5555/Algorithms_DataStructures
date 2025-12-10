def solution(n):
    countOne = bin(n)[2:].count('1')
    while True:
        n+=1
        if countOne == bin(n)[2:].count('1') : 
            return n
            break