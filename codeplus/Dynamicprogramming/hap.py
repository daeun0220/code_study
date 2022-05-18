# 1912 연속합

n = int(input())
a = [0] + list(map(int, input().split()))

d = [-1000*100000]*(n+1)


for i in range(1,n+1):
    d[i] = max(d[i], a[i]+d[i-1], a[i])

print(max(d))

    

