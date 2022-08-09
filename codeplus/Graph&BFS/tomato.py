# 7576번 토마토
from collections import deque 
m,n = map(int,input().split())
tomato = [list(map(int,input().split())) for i in range(n)]
check = [[False]*m for i in range(n)]
day = [[-1]*m for i in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
q = deque()
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1: # 1이 익은거
            day[i][j] = 0
            q.append((i,j))
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if tomato[nx][ny] == 0 and day[nx][ny] == -1:
                q.append((nx,ny))
                day[nx][ny] = day[x][y] + 1

ans = max([max(i) for i in day])
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 0 and day[i][j] == -1:
            ans = -1    # 안익을 수 있는 경우 return -1 
print(ans)

