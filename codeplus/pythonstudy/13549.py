# 숨바꼭질3
from collections import deque
n, k = map(int, input().split())
map = [-1] * 100001
q = deque()
q.append(n)
map[n] = 0

while q :
    m = q.popleft()
    if m == k :
        print(map[m])
        break
    for i in (2*m, m-1, m+1) :
        if 0 <= i < 100001 and map[i] == -1 :
            if i == 2*m :
                map[i] = map[m]
                q.appendleft(i) # 더 높은 우선순위. 먼저 탐색됨
            else :
                map[i] = map[m] + 1
                q.append(i)

while len(topping) != 0 :
        if len(set(cut)) > len(set(topping)) :
            break
        cut.append(topping[0])
        del topping[0]
        if len(set(cut)) == len(set(topping)) :
            cnt += 1