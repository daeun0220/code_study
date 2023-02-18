# 1388  바닥장식
from collections import deque
n, m = map(int, input().split())
floor = [list(input()) for i in range(n)]
visited = []
for i in range(n) :
    visited.append([0]*m)
'''
def bfs(a, b) :  # 함수로 해야하나ㅏ
    q = deque([(a,b)])
    while q :
        x, y = q.popleft()
        if floor[x][y] == '|' and visited[x][y] == 0 :
            visited[x][y] = 1 
            if x+1 < n and floor[x+1][y] == '|' and visited[x+1][y] == 0 :
                q.append((x+1,y))
                visited[x+1][y] = 1
        elif floor[x][y] == '-' and visited[x][y] == 0 :
            visited[x][y] = 1
            if y+1 < m and floor[x][y+1] == '-' and visited[x][y+1] == 0 :
                q.append((x,y+1))
                visited[x][y+1] = 1
'''
def bfs(a,b) :
    q = deque([(a,b)])
    while q :
        x, y = q.popleft()
        if floor[x][y] == '-':
            floor[x][y] = '1'
            if y+1 < m and floor[x][y+1] == '-' :
                q.append((x,y+1))
        elif floor[x][y] == '|':
            floor[x][y] = '1'
            if x+1 < n and floor[x+1][y] =='|':
                q.append((x+1,y))

count = 0
for i in range(n) :
    for j in range(m) :
        if floor[i][j] != '1':
            bfs(i,j)
            count += 1
print(count)
