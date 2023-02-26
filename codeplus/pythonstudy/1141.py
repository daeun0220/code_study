#1141 접두사

n = int(input())
word = []
for i in range(n) :
    w = input()
    word.append(w)

word = list(set(word))
word.sort(key = lambda x : len(x))
count = 0
for i in range(len(word)) :
    check = 0
    for j in range(i+1, len(word)) :
        if word[i] in word[j] :
            check = 1
    
    if check == 0 :
        count += 1
    
print(count)