import math
def solution(today, terms, privacies):
    answer = []
    termMap = {l.split(" ")[0] : int(l.split(" ")[1]) for l in terms}
    tyy, tmm, tdd = map(int, today.split("."))
    
    for i, pravacy in enumerate(privacies):
        d,k = map(str,pravacy.split(" "))
        yy, mm, dd = map(int, d.split("."))
        
        if(mm + termMap[k] > 12) : 
            
            yy += math.floor((mm + termMap[k])/12) if((mm +termMap[k]) % 12 != 0) else math.floor((mm + termMap[k])/12)-1
            mm = math.floor((mm + termMap[k]) % 12) if (mm +termMap[k]) % 12 != 0 else 12
            if(dd - 1 < 1) : 
                if (mm - 1 < 1) : 
                    mm = 12
                else : 
                    mm -= 1
                dd = 28
            else :
                dd -= 1
        else :
            mm = math.floor((mm + termMap[k]) % 12) if mm +termMap[k] != 12 else 12            
            if(dd - 1 < 1) :
                print("here")
                if (mm - 1 < 1) : 
                    mm = 12
                else :                 
                    mm -= 1
                dd = 28
            else :                
                dd -= 1
        
        if tyy > yy :
            answer.append(i+1)
            continue
        elif tyy == yy and tmm > mm : 
            answer.append(i+1)
            continue
        elif tyy == yy and tmm == mm and tdd > dd :
            answer.append(i+1)
            continue
        
    return answer