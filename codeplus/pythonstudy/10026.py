# 10026 적록색약

n = int(input())
pic = []
for i in range(n) :
    p = input()
    pic.append(p)
visited = [[False] * n for i in range(n)]

cnt1, cnt2 = 0, 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y) :
    visited[x][y] = True
    current_color = pic[x][y]

    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

       
