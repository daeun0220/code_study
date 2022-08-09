
n = int(input())
p = list(map(int, input().split()))

p.sort()

ptime = 0
for i in range(n):
    ptime += (n-i)*p[i]
    
print(ptime)