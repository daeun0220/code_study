# 1149 RGB 거리
# DP 문제 !
n = int(input()) 
paint = []
for i in range(n) : 
    r,g,b = map(int, input().split())
    paint.append([r, g, b])

for i in range(1,n):
    paint[i][0] = min(paint[i-1][1] + paint[i][0], paint[i-1][2] + paint[i][0])
    paint[i][1] = min(paint[i-1][0] + paint[i][1], paint[i-1][2] + paint[i][1])
    paint[i][2] = min(paint[i-1][0] + paint[i][2], paint[i-1][1] + paint[i][2])

print(min(paint[n-1][0], paint[n-1][1], paint[n-1][2]))