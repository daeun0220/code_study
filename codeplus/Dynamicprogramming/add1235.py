# 15990   1,2,3 더하기 5
# 1,2,3 더하기 문제로 사용할 수 없음


d = [[0]*4 for _ in range(100001)]

for i in range(1, 100001):
    if i-1 >= 0:
        d[i][1] = d[i-1][2] + d[i-1][3]
        if i == 1:
            d[i][1] = 1
    if i-2 >= 0:
        d[i][2] = d[i-2][1] + d[i-2][3]
        if i == 2:
            d[i][2] = 1
    if i-3 >= 0:
        d[i][3] = d[i-3][1] + d[i-3][2]
        if i == 3:
            d[i][3] = 1
    d[i][1] %= 1000000009
    d[i][2] %= 1000000009
    d[i][3] %= 1000000009

T = int(input())
for i in range(T):
    n = int(input())
    print((d[n][1]+ d[n][2]+ d[n][3])%1000000009)
    

