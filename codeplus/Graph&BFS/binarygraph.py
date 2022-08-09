# 1707 이분 그래프
import sys

t = int(input())
for i in range(t):
    n,m = map(int, input().split())
    a = [[] for _ in range(n)]
    color = [0] * n
    for _ in range(m):
        u, v = map(int, input().split())
        a[u-1].append(v-1)
        a[v-1].append(u-1)   # 연결리스트

def dfs(x,c):
    color[x] = c
    for y in a[x]:
        if color[y] == 0:
            if not dfs(y, 3-c):
                return False
            elif color[y] == color[x]:
                return False
    return True


ans = True
for i in range(n):
    if color[i] == 0:
        if not dfs(i,1):    # dfs(0,1)
            ans = False

if ans:
    print('YES')
else:
    print('NO')