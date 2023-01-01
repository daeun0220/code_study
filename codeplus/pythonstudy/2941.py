# 2941 크로아티아 알파벳

alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

word = input()
answer = 0

count = 0
for i in alpha :
    if i in word :
        count += 1
        word.replace(i, "a")

answer = len(word)
print(answer)
print(word)
print(count)



'''
c = 0
while c < len(word) :
    if word[c] == "a" :
        answer += 1
        c += 1
    if word[c] == "b" :
        answer += 1
        c += 1
    if word[c] == "c" :
        if word[c+1] == "=" :
            answer += 1
            c += 2
        elif word[c+1] == "-" :
            answer += 1
            c += 2
        else :
            answer += 1
            c += 1
    if word[c] == "d" :
        if word[c+1] == "=" :
            answer += 1
            c += 2
        elif word[c+1] == "-" :
            answer += 1
            c += 2
        else :
            answer += 1
            c += 1
'''


