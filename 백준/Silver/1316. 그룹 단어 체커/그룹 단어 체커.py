n = int(input().strip())
answer = []
for _ in range(n):
  words = input().strip()
  answer.append(words)
  wordMap = { w : list() for w in words}
  for i, word in enumerate(words):    
    if not wordMap[word]: 
      wordMap[word].append(i)
      continue
    if wordMap[word][-1] != i-1:
      answer.pop()
      break
    wordMap[word].append(i)
    
    
print(len(answer))
  