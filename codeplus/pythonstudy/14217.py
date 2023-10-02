# 14217 그래프탐색
from collections import deque

def bfs() :
    visited = [-1 for _ in range(n+1)]   # 방문 못할 경우 -1 
    q = deque()
    q.append((1,0))
    visited[1] = 0
    while q :
        city, time = q.popleft()
        for ncity in graph[city] :
            if visited[ncity] == -1 :
                visited[ncity] = time + 1
                q.append((ncity, time+1))
    return visited[1:]

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]   # 연결리스트 
for _ in range(m) :
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

q = int(input())
for _ in range(q) :
    a, i, j = map(int, input().split())
    if a == 1 :
        graph[i].append(j)
        graph[j].append(i)
        ans = bfs()
        print(*ans)    # print(*list) 할 경우 리스트 요소 한번에 [] 없이 출력
    elif a == 2 :
        graph[i].remove(j)
        graph[j].remove(i)
        ans = bfs()
        print(*ans)