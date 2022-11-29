# 2606 바이러스

n = int(input())
m = int(input())
graph = [[]*n for _ in range(n+1)]
for i in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
visited = [0]*(n+1)

def dfs(start, graph) :
    global count
    visited[start] = 1
    for i in graph[start] :
        if visited[i] == 0 :
            dfs(i, graph)
            count += 1

dfs(1, graph)
print(count)