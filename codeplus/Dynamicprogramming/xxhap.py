#1699 제곱수의 합
# 계속 시간초과... 시간초과 계산해보기 
import math
n = int(input())
d = [100000] * (n+1)

for i in range(1,n+1):
    if math.sqrt(i) == int(math.sqrt(i)):
            d[i] = 1

   # 이중 for문 때문에 시간초과 뜨는것같다.
for i in range(1,n+1):   
    d[i] = i 
    j =1              
    while j*j <= i:
        if d[i] > d[i-j*j]+1:
            d[i] = d[i-j*j]+1
        j += 1
    
print(d[n])