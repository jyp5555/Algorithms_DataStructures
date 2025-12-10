def solution(n,a,b):
    answer = 0
    
    r = 1
    rr = 1
    round = [ x for x in range(n+1)]
    s = True
    
    while s : 
        round1 = [0]
        
        while rr < n:            
            if round[rr] == a and round[rr+1] == b:
                answer = r
                s = False
                break
            elif round[rr] == a or round[rr+1] == a:
                round1.append(a)
                rr += 2
            elif round[rr] == b or round[rr+1] == b:
                round1.append(b)
                rr += 2
            else:
                round1.append(round[rr])
                rr+=2
        round = round1
        rr = 1
        n = len(round)
        r += 1
        if rr >= n and s == True :
            answer = 

    return answer

print(solution(8,2,3))