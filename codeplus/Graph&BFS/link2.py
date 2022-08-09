# 11724번 연결 요소의 개수 
# DFS의 시작이 연결요소 찾은걸 의미함. 
# 즉 DFS 시작하는 개수 세서 연결요소 개수 구할 수 있음

n,m = map(int, input().split())
arr = [[] for i in range(n+1)]
check = [False] * (n+1)
for i in range(m):
    u,v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

def dfs(x):
    check[x] = True
    for i in arr[x]:
        if check[i] == False:
            dfs(i)
count = 0
for i in range(1, n+1):
    if not check[i]:
        dfs(i)
        count += 1
print(count)
    








