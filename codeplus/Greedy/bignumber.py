n,m,k = map(int,input().split())
num = list(map(int,input().split()))
num = set(num)
num = list(num)
num.sort()

a = num[-1] * (m//k*k)
b = num[-2] * (m%k)
print(a+b)
