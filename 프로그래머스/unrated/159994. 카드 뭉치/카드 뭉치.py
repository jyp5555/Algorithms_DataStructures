def solution(cards1, cards2, goal):
    answer = 'Yes'
    
    for i, g in enumerate(goal):
        if( g != cards1[0] and g != cards2[0]) :
            answer = 'No'
            break
        if(len(cards1) > 0 and g == cards1[0]) : 
            del cards1[0]
            cards1.append('0')
            continue
        if(len(cards2) > 0 and g == cards2[0]):
            del cards2[0]
            cards2.append('0')
            continue
    
    return answer