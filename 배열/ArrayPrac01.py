# import sys
# s = sys.stdin.readline()
words = input().strip()
alphabet = [0 for i in range(26)]

if(len(words) > 0):
    for word in words:
        if(word.isalpha()&word.isupper()):
            alphabet[ord(word)-65] += 1
        elif(word.isalpha()&word.islower()):
            alphabet[ord(word)-97] += 1

for i in range(len(alphabet)):
    if(i == len(alphabet)): print(alphabet[i], end="")
    print(alphabet[i],end=" ")