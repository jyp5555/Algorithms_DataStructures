def solution(s):
    answer = ''
    r = list(map(int, s.split(" ")))
    answer = str(min(r)) +" " + str(max(r))
    return answer