# 7576 토마토  bfs
from collections import deque
m, n = map(int, input().split())
box = []
for i in range(n) :
    b = list(map(int, input().split()))
    box.append(b)
# 익은 토마토부터 돌기

dx = [0,0,1,-1]
dy = [1,-1,0,0]
ans = 0 
q = deque()
for i in range(n) :
    for j in range(m) :
        if box[i][j] == 1 :
            q.append((i,j))

def bfs() :         
    while q :
        x,y = q.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m :
                if box[nx][ny] == 0 :
                    box[nx][ny] = box[x][y] + 1
                    q.append((nx,ny))
                #elif box[nx][ny] == -1 :
                #    visited[nx][ny] = 1

def simulate() :
    bfs()
    for i in box :
        for j in i :
            if j == 0 :
                return(-1)
        ans = max(ans, max(i))
    return(ans - 1)

print(simulate())


