n = 1
for _ in range(3):
    n*=int(input())
n = str(n)
wordCount = {str(n): 0 for n in range(10)}
for i in n:
    wordCount[i] += 1
for j in range(10):
    print(wordCount[str(j)])