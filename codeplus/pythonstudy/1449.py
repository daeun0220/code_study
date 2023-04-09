#1449 수리공 항승
# dp..? queue...?
from collections import deque
n, l = map(int, input().split())
w_drop = list(map(float, input().split()))
w_range = []
visited = [0] * n
w_drop.sort()
for i in w_drop :
    a,b = i-0.5, i+0.5
    w_range.append([a,b])

q = deque()
q.append((w_range[0][0], w_range[0][1]))
visited[0] = 1
cnt = 1

while q :
    x, y = q.popleft()
    nx, ny = x, x + l 
    for i in range(1, n) :
        if nx <= w_range[i][0] <= ny and nx <= w_range[i][1] <= ny and visited[i] == 0 :
            visited[i] = 1
        else:
            visited[i] = 1
            q.append((w_range[i][0], w_range[i][1]))
            cnt += 1
            
print(cnt)





