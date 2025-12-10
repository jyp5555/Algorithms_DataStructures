def solution(n):
    answer = 0
    zeroToN = [x for x in range(n+1)]
    fiboSum = [0,1]
    q = [0, 1]
    for i in range(2,n+1):
        fiboSum.append(fiboSum[i-2] + fiboSum[i-1])
        q.append(fiboSum[i] % 1234567)
    
    return q[-1]