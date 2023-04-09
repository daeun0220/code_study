# 14503 로봇 청소기
from collections import deque
n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = []
for i in range(n) :
    g = list(map(int, input().split()))
    graph.append(g)
visited = [[0]*m for i in range(n)]
# 방향 순서 고려 (0,3,2,1)
dx = [-1,0,1,0]
dy = [0,1,0,-1]

visited[r][c] = 1
cnt = 1

while True :
    flag = 0 # 4방향 청소확인
    for i in range(4) :
        nx, ny = r + dx[(d+3)%4], c + dy[(d+3)%4]
        d = (d+3)%4
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 :
            if graph[nx][ny] == 0 :
                visited[nx][ny] = 1
                cnt += 1
                r, c = nx, ny
                flag = 1
                break

    # 4방향 다 청소했을 때
    if flag == 0 :
        if graph[r-dx[d]][c-dy[d]] == 1 :
            print(cnt)
            break
        else :
            r, c = r-dx[d], c-dy[d]


