def solution(temperature, t1, t2, a, b, onboard):
    answer = 0

    temperature += 11
    t1 += 11
    t2 += 11

    dp = [[float('inf')] * 53 for _ in range(len(onboard))]

    dp[0][temperature] = 0
    
    for minute in range(1, len(onboard)):

        if onboard[minute] == 1:
            l, r = t1, t2+1

        else : 
            l, r = 1, 52

        for t in range(l, r):
            #에어컨 off
            if t == temperature : 
                dp[minute][t] = min(dp[minute - 1][t], dp[minute - 1][t + 1], dp[minute - 1][t - 1])
            elif t > temperature:
                dp[minute][t] = dp[minute - 1][t + 1]
            elif t < temperature : 
                dp[minute][t] = dp[minute - 1][t - 1]
            #에어컨 on
            dp[minute][t] = min(dp[minute][t],dp[minute-1][t] + b, dp[minute - 1][t-1] + a, dp[minute - 1][t+1] + a)
    answer = min(dp[-1])
    # for d in dp:
    #     print(d)
    return answer
