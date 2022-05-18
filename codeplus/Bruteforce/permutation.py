# 10972 다음 순열 

N = int(input())
p = list(map(int,input().split()))

up_p = sorted(p)
down_p = sorted(p,reverse=True)
if p == up_p:
    p[-1] = p[-2]
    p[-2] = N
    print(p)

elif p == down_p:
    print(-1)

else:
    for i in range(N):
        if i > i+1:
            k = i
            

