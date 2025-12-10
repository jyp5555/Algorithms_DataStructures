import itertools
import math

def makeNums(numbers):
    candidate = []
    for i in range(1, len(numbers)+1):
        candidate.extend(list(itertools.permutations(numbers,i)))
    for i in range(len(candidate)):
        candidate[i] = int(''.join(candidate[i]))
    return list(set(candidate))

def checkPrime(candidate):
    count = 0
    for i in candidate:
        ls =[]
        if i==2:
            count = 1
        elif i>2:
            for j in range(1,math.ceil(math.sqrt(i))+1):
                if(i%j == 0):
                    ls.append(j)
            if len(ls)==1:
                count += 1 
            
    return count

def solution(numbers):
    answer = 0
    answer = checkPrime(makeNums(numbers))
    return answer