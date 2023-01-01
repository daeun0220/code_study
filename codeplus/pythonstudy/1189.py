# 1189 컴백홈
dic = {}
def dfs(x, y, d,road) :

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    if x == 0 and y == c-1 :
        if d in dic :
            dic[d] += 1
        else :
            dic[d] = 1
        


r, c, k = map(int, input().split())
road = []
cnt = 0
for i in range(r) :
    rr = list(map(str, input().split()))
    road.append(rr)

answer = dfs(r,c,k,road)

for i in answer :
    if i == k :
        cnt += 1
print(cnt)
