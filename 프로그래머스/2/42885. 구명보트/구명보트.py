from collections import deque

def solution(people, limit):
    answer = 0
    
    people.sort()
    people = deque(people)
    apeople = []
    min = 0
    max = len(people) - 1
    while len(people) > 1:
        if people[min] + people[max] <= limit:
            apeople.append(people.popleft() + people.pop())
            max = len(people) -1
        elif people[min] + people[max] > limit:
            apeople.append(people.pop())
            max = len(people) - 1
    answer = len(apeople) + len(people)
    return answer