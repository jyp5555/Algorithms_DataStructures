def solution(s):
    
    countDo = 0
    countZero = 0
    
    while True:
        if s == '1' : 
            break
        countZero += s.count('0')
        s = s.replace("0", "")
        s = str(bin(len(s))[2:])
        countDo += 1
        
    answer = [countDo, countZero]

    return answer