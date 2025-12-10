import math
def solution(brown, yellow):
    answer = []
    
    y1 = (((4-brown)/2) + math.sqrt(((brown-4)/2)*((brown-4)/2) - 4*yellow))/2
    y2 = (((4-brown)/2) - math.sqrt(((brown-4)/2)*((brown-4)/2) - 4*yellow))/2
    
    answer = [y2*-1 +2, y1*-1 + 2]
    return answer