# 16194 카드 구매하기2 

n = int(input())
p = [0] + list(map(int, input().split()))

d = [0] + [1001]*n

for i in range(1,n+1):
    for j in range(1,i+1):
        d[i] = min(d[i], d[i-j]+p[j])

print(d[n])