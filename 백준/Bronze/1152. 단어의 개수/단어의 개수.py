sentence = input().strip()
if len(sentence) == 0 : 
    print(0)
else:
    count = 1
    for i, word in enumerate(sentence):
        if((i == 0 or i == len(sentence)-1) and word == ' ') : continue
        if(word == ' '): 
          count+=1
        else: continue
    print(count)
