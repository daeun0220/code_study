import sys
sys.setrecursionlimit(10000)  # 런타임에러 방지 

def dfs(x, y, bachu):
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < m) :
            if bachu[nx][ny] == 1 :
                bachu[nx][ny] = -1
                dfs(nx, ny, bachu)


t = int(input())
for i in range(t) :
    m, n, k = map(int, input().split())
    bachu = [ [0] * m for i in range(n) ]
    count = 0
    for i in range(k) :
        x, y = map(int, input().split())
        bachu[y][x] = 1

    for i in range(n) : # 행
        for j in range(m) :  # 열
            if bachu[i][j] > 0 :
                dfs(i, j, bachu)
                count += 1
    print(count)
