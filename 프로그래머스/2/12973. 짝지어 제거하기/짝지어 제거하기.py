from collections import deque

def solution(s):
    answer = -1
    
    st = deque()
    
    for ss in s:
        if(st and (st[-1] == ss)) : st.pop()
        else : st.append(ss)
    
    if st : return 0
    else : return 1
    return answer