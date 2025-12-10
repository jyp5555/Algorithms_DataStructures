from itertools import *
def solution(word):
    answer = 0
    alphabet = 'AEIOU'
    dictionary = []
    dictionary.extend(list(permutations(alphabet, 1)))
    dictionary.extend(list(product(alphabet, repeat = 2)))
    dictionary.extend(list(product(alphabet, repeat = 3)))
    dictionary.extend(list(product(alphabet, repeat = 4)))
    dictionary.extend(list(product(alphabet, repeat = 5)))
    dictionary.sort()
    for i,d in enumerate(dictionary):
        if word == ''.join(d):
            return i+1
    print(dictionary)
    return answer