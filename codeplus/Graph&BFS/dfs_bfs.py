# 1260 DFS와 BFS

from collections import deque
n,m,start = map(int,input().split())

a = [[] for i in range(n+1)]
check = [False] * (n+1)

for i in range(m):
    u,v = map(int, input().split())
    a[u].append(v)
    a[v].append(u)    # 인접 리스트....? 
for i in range(n):
    a[i].sort()    # a[n].sort() 는 안하는건가...? 

def dfs(x):
    global check
    check[x] = True
    print(x, end=" ")
    for y in a[x]:
        if check[y] == False:
            dfs(y)

def bfs(start):
    check = [False] * (n+1)
    q = deque() 
    q.append(start)
    check[start] = True
    while q:  # 큐 안이 다 사라지기 전까지 실행
        x = q.popleft() # 큐는 FIFO
        print(x , end=' ')
        for y in a[x]:
            if check[y] == False:
                check[y] = True
                q.append(y)

dfs(start)
print()
bfs(start)
print()