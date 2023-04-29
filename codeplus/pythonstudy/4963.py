# 4963 섬의개수
from collections import deque

def bfs(a, b, graph, visited) :
    q = deque()
    q.append((a,b))
    visited[a][b] = 1
    dx = [0,0,1,-1,1,1,-1,-1]
    dy = [1,-1,0,0,1,-1,1,-1]
    while q :
        x, y = q.popleft()
        for i in range(8) :
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and visited[nx][ny] == 0 :
                if graph[nx][ny] == 1 :
                    bfs(nx, ny, graph, visited)
                
while True :
    w, h = map(int, input().split())
    graph = []
    if w == 0 and h == 0 : break

    for i in range(h) :
        g = list(map(int,input().split()))
        graph.append(g)

    visited = [[0]*w for i in range(h)]
    cnt = 0
    for i in range(h) :
        for j in range(w) :
            if graph[i][j] == 1 :
                cnt += 1
                bfs(i,j,graph,visited)

    print(cnt)
