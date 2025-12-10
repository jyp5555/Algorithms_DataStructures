word = input().rstrip()
croaDoubt=[]
croa = ["c=","c-", "dz=", "d-", "lj", "nj","s=", "z="]
croaDoubtWord = ["c", "d", "dz", "l", "n", "s", "z"]
answer = []
for i, w in enumerate(word):
    print(f" {i} : {croaDoubt} : {answer}")
    if croaDoubt : 
        c = ''.join(croaDoubt)
        print(c)
        if c + w in croa : 
            croaDoubt = []
            answer.append(w)
            continue
        elif c + w == "dz":
            croaDoubt.append(w)
            continue
        else : 
            while(croaDoubt):
                answer.append(croaDoubt.pop())
            answer.append(w)
            continue
    if w in croaDoubtWord :
        croaDoubt.append(w)
    else :
        answer.append(w)
print(len(answer))