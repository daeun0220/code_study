# 1062 가르침
n, k = map(int, input().split())
words = [input() for i in range(n)]
k_words = ["a", "c", "i", "n", "t"]
w_words = []
n_words = []
count = 0
if k < 5 :
    print(0)
else :
    k = k - 5 
    for i in words :
        w = []
        for j in i[4:-4] :
            if j in k_words :
                continue
            else :
                if j not in w :
                    w.append(j)
        w_words.append(w)
    w_words.sort(key = lambda x : len(x)) 

    for i in w_words :
        check = 0
        for j in i :
            if j in n_words :
                check += 1
        if len(i) - check <= k:
            count += 1
            n_words = list(set(n_words + i))
            k = k - len(i) + check
    
    print(count)

print(w_words)