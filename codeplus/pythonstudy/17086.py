# 17086 아기상어2
from collections import deque
n, m = map(int,input().split())
shark = []
for i in range(n) :
    s = list(map(int,input().split()))
    shark.append(s)
q = deque()
#check = []
#for i in range(n) :
#    check.append([0]*m)

dx = [-1,-1,-1,0,1,0,1,1]
dy = [-1,0,1,1,1,-1,0,-1]


def bfs() :
    while q :
        x, y = q.popleft()
        for i in range(8) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and shark[nx][ny] == 0 :
                q.append((nx,ny))
                shark[nx][ny] = shark[x][y] + 1 


for i in range(n) :
    for j in range(m) :
        if shark[i][j] == 1 :
            q.append((i,j))
        
bfs()   
cnt = 0          
for i in range(n) :
    for j in range(m) :
        cnt = max(cnt, shark[i][j])
print(cnt-1)
