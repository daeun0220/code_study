# 거리두기 확인하기

from collections import deque
def solution(places):
    answer = []
    for i in places :        
        answer.append(bfs(i))
    return answer

def bfs(p_list) :
    start = []
    
    for i in range(5) :
        for j in range(5) :
            if p_list[i][j] == "P" :
                start.append([i,j])
                
    for k in start :
        q = deque([k])  # 큐에 초기값 넣어준다  # 왜 리스트 표시..?
        visited = [[0]*5 for i in range(5)]
        distance = [[0]*5 for i in range(5)]
        visited[k[0]][k[1]] = 1
        
        while q :
            y, x = q.popleft()
            
            dx = [-1,1,0,0]
            dy = [0,0,-1,1]
            
            for i in range(4) :
                nx = x + dx[i]
                ny = y + dy[i]
                
                if nx < 0 or nx > 4 or ny < 0 or ny > 4 :
                    continue
                elif 0<=nx<5 and 0<=ny<5 and visited[ny][nx] == 0: 
                    if p_list[ny][nx] == 'O' :
                        q.append([ny,nx])
                        visited[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1
                    if p_list[ny][nx] == "P" and distance[y][x] <=1 :
                        return 0
    return 1