from collections import deque
max = 200000
check = [False]*(max+1)
dist = [-1]*(max+1)
n, k = map(int,input().split())
q = deque()
check[n] = True
dist[n] = 0
q.append(n)

while q:
    now = q.popleft()
    for nxt in [now+1, now-1, now*2]:
        if 0 <= nxt <= max and check[nxt] ==False:
            check[nxt] = True
            dist[nxt] = dist[now] + 1
            q.append(nxt)
print(dist[k])