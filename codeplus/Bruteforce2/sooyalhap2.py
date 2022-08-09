# 1182번 부분수열의 합 
import itertools

def sooyal(n,s):
    soo = []
    for i in range(n):
        num = itertools.combination(s,i)
        ans = sum(num)
        soo.append(ans)
    soo.sort()

    

n = int(input())
s = list(map(int,input().split()))
print(sooyal(n,s))
