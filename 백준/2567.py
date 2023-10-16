# 색종이2
n = int(input())
check = [[0 for _ in range(101)] for _ in range(101)]
cnt = 0 
for i in range(n) :
    a, b = map(int, input().split())
    for x in range(a, a+10) :
        for y in range(b, b+10) :
            check[x][y] = 1

dx = [1,-1,0,0]
dy = [0,0,1,-1]
for i in range(101) :
    for j in range(101) :
        if check[i][j] == 1 :
            for k in range(4) :
                x = i + dx[k]
                y = j + dy[k]
                if 0 <= x <= 100 and 0 <= y <= 100 :
                    if check[x][y] == 0 :
                        cnt += 1
                        
                            

print(cnt)