#6064 카잉 달력


def cain(M,N,x,y):
    while x <= M*N:
        if (x-y)%N == 0:
            return x
        x += M 
    return -1
        

T = int(input())
for i in range(T):   
    M,N,x,y = map(int, input().split())
    print(cain(M,N,x,y))