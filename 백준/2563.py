# 색종이

n = int(input())
check = [[True for _ in range(100)] for _ in range(100)]
cnt = 0
for i in range(n) :
    a, b = map(int, input().split())
    for x in range(a,a+10) :
        for y in range(b,b+10) :
            if check[x][y] == True :
                cnt += 1
                check[x][y] = False
print(cnt)
