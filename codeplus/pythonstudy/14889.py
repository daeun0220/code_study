# 14889 스타트와 링크
from itertools import combinations
n = int(input())
smap = []
total = []
answer = 100000000
for i in range(n) :
    s = list(map(int, input().split()))
    s_sum = sum(s)
    smap.append(s)
    total.append(s_sum)

m = [i for i in range(n)]
for start in list(combinations(m , n//2)):
    s_cnt, l_cnt = 0, 0
    link = list(set(m) - set(start))     # 계산 시 주의 set
    for i, j in list(combinations(start, 2)) :
        s_cnt += smap[i][j]
        s_cnt += smap[j][i]
    for i, j in list(combinations(link, 2)) :
        l_cnt += smap[i][j]
        l_cnt += smap[j][i]
    #l_cnt = sum(total) - s_cnt  안됨
    answer = min(answer, abs(s_cnt - l_cnt))
print(answer)