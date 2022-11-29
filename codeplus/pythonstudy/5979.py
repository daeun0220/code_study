# 5979 택배 배송
# 그래프 -- 다익스트라
import heapq
import sys
INF = sys.maxsize

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(m) :
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

q = []
distance = [INF]*(n+1)
heapq.heappush(q,(0,1)) # 시작 노드 설정
distance[1] = 0  # 시작값은 0
while q :  # 큐에 남아있는 노드가 없으면 끝 / 도착 노드가 빠지면 종료
    dist, now = heapq.heappop(q)
    if distance[now] < dist :  # 기존 값보다 크면 X
        continue
    for i in graph[now] :
        cost = dist + i[1]
        if cost < distance[i[0]] :  # 기존값보다 작으면 갱신
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))


print(distance[n])