# 14891 톱니바퀴  
from collections import deque  # 큐 사용 이유
# array = [1,2,3,4] --> array.rotate(2) -->  
# 오른쪽 톱니바퀴
def right(x, d) :
    if x > 4 or gears[x-1][2] == gears[x][6] :
        return
    if gears[x-1][2] != gears[x][6] :
        right(x+1, -d)
        gears[x].rotate(d)
# 왼쪽 톱니바퀴 
def left(x, d) :
    if x < 1 or gears[x][2] == gears[x+1][6] :
        return
    if gears[x][2] != gears[x+1][6] :
        left(x-1, -d)
        gears[x].rotate(d)

gears = {}
for i in range(1, 5) :
    gears[i] = deque((map(int,input())))
k = int(input())
for i in range(k) :
    x, d = map(int, input().split())
    
    right(x+1, -d)
    left(x-1, -d)
    gears[x].rotate(d)

answer = 0
for i in range(4) :
    answer += gears[i+1][0] * (2**i)

print(answer)



    


