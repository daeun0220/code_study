# 11724 연결 요소의 개수
import sys
sys.setrecursionlimit(100000)  # 최대 재귀한도 깊이 설정
n,m = map(int,input().split())

a = [[] for i in range(n)]
check = [False] * (n)
count = 0
for i in range(m):
    u,v = map(int,input().split())
    a[u-1].append(v-1)  # append() 부분에서는 왜 -1 하는거지
    a[v-1].append(u-1)


def dfs(x):
    global check
    check[x] = True
    for y in a[x]:
        if check[y] == False:
            dfs(y)

# dfs 시작 = 연결 요소 새로 찾음 
for i in range(n):
    if not check[i]:
        dfs(i)
        count +=1

print(count)

    
