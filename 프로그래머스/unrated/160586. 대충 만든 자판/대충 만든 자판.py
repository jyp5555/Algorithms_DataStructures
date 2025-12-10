def solution(keymap, targets):
    answer = []
    
    keydict = {}
    
    for key in keymap : 
        for i,word in enumerate(key, start=1) :
            if(word in keydict.keys()) : 
                if(i < keydict[word]) : 
                    keydict[word] = i
            else:
                 keydict[word] = i   
    
    for target in targets:
        sum = 0
        for t in target:
            if(t not in keydict.keys()):
                sum = -1
                break
            sum += keydict[t]
        
        answer.append(sum)
    
    return answer