# 2910 빈도 정렬

n, c = map(int, input().split())
message = list(map(int, input().split()))
dic = {}
answer = []
for i in message :
    if i not in dic :
        dic[i] = 1
    else:
        dic[i] += 1

dic = dict(sorted(dic.items(), key=lambda x : x[1], reverse=True))

for k, v in dic.items() :
    for i in range(v) :
        answer.append(k)

print(answer)
#print(dic)
