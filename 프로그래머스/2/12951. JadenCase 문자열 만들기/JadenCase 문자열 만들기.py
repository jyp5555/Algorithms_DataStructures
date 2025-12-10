def solution(s):
    answer = ''
    ls = list(s)
    for i,string in enumerate(ls) :
        if (i == 0 and string.isalpha()):
            ls[i] = string.upper()
        elif(s[i-1] == ' ' and string.isalpha()):
            ls[i] = string.upper()
        elif(string.isalpha()):
            if(string.isupper()) : ls[i] = string.lower()
        else:
            continue
    answer = ''.join(ls)
            
    return answer