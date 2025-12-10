def solution(s):
    answer = True
    openList = []
    for i, ss in enumerate(s) : 
        if i== 0 and ss ==')':
            answer = False
            break
        if ss== '(':
            openList.append(ss)
        else:
            if not openList : 
                answer = False
                break
            openList.pop()
    if openList:
        answer = False
    return answer