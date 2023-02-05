# 14501 퇴사
n = int(input())
t_list = []
p_list = []
for i in range(n) :
    t, p = map(int, input().split())
    t_list.append(t)
    p_list.append(p)

dist = [0] * (n+1)
check = [False] * (n+1)
'''
for i in range(n) :
    if dist[i] == 0 and i+1 + t_list[i] < n+1 and not check[i] :
        dist[i] += p_list[i]
        check[i] = True
'''
def dp(d, dist, check) :
    for i in range(n) :
        if dist[i] == 0 and i+1 + t_list[i] < n+1 and not check[i] :
            dist[i] += p_list[i]
            check[i] = True
            dp(d + t_list[i])

for i in range(n) :
    dp(i)

print(dp(n))

