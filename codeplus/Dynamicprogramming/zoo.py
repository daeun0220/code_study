# 1309 동물원

n = int(input())
d = [[0,0,0] for i in range(n+1)]
d[1][0] = 1
d[1][1] = 1
d[1][2] = 1 
for i in range(2,n+1):
    d[i][0] = d[i-1][1] + d[i-1][2] + d[i-1][0]
    d[i][1] = d[i-1][2] + d[i-1][0]
    d[i][2] = d[i-1][1] + d[i-1][0]

    for j in range(3):
        d[i][j] = d[i][j] % 9901

print(sum(d[n]) % 9901)


# 메모리 초과....