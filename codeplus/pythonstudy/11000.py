# 11000 강의실 배정
import heapq

n = int(input())
classtime = []
room = []
for i in range(n) :
    s, t = map(int, input().split())
    classtime.append([s, t])

classtime.sort(key = lambda x : x[0])
heapq.heappush(room, classtime[0][1]) # 정렬 후 첫번째 강의 끝나는 시간

for i in range(1, n) :
    if classtime[i][0] < room[0] :
        heapq.heappush(room, classtime[i][1])
    else :
        heapq.heappop(room)
        heapq.heappush(room, classtime[i][1])

print(len(room))