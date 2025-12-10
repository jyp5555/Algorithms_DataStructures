def solution(s, skip, index):
    answer = ''
    alphabet = set([chr(x) for x in range(97,123)])
    r = list(alphabet - set(skip))
    r.sort()
    wordMap = {}
    for i,w in enumerate(r):
        k = i+index
        if k >= len(r):
            k = k % len(r)
        wordMap[w] = r[k]
    for string in s:
        answer+=wordMap[string]
            
                
    return answer