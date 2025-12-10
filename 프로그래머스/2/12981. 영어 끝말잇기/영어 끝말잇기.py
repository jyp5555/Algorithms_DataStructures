def solution(n, words):
    answer = [0,0]
    wordPerson = {}
    personOrder = [0 for x in range(n)]
    for i, word in enumerate(words):
        if(i==0): 
            personOrder[1] += 1
            wordPerson[word] = 1
            continue
        
        personOrder[(i+1)%n] += 1            
            
        if(wordPerson.get(word)) :
            answer[0] = n if (i+1)%n == 0 else (i+1)%n
            answer[1] = personOrder[(i+1)%n]
            return answer
        
        if(words[i-1][-1] != word[0]):
            answer[0] = n if (i+1)%n == 0 else (i+1)%n
            answer[1] = personOrder[(i+1)%n]
            return answer
        
        if(not wordPerson.get(word)) :
            wordPerson[word] = 1

    return answer