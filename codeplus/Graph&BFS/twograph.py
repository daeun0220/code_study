# 1707 이분 그래프
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

k = int(input())
for i in range(k):
    n,m  = map(int,input().split())
    a = [[] for i in range(n+1)]
    color = [0] * (n+1)
    for j in range(m):
        u,v = map(int,input().split())
        a[u].append(v)
        a[v].append(u)


    def dfs(x,c):     # 함수는 따로 빼줘도 ㄱㅊ..?
        color[x] = c 
        for y in a[x]:
            if color[y] == 0:
                if not dfs(y, 3-c):
                    return False
            elif color[y] ==color[x]:
                return False
        return True

    ans = True
    for i in range(1,n+1):
        if color[i] ==0:
            if not dfs(i,1):
                ans = False
    print('YES' if ans else 'NO')

