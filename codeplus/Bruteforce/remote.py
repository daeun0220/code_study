# 리모컨 
import sys
input = sys.stdin.readline
N = int(input())
ans = abs(100-N)
M = int(input())
num = [0,1,2,3,4,5,6,7,8,9]
button = list(map(int, input().split()))

# range를 1000000 으로 잡은 이유 --> 500000번 채널일 경우 최적의 해 구하기 위해서 필요한 범위이므로
for i in range(1000001):
    i = str(i)
    for j in range(len(i)):
        if int(i[j]) in button:
            break
        elif j == len(i) - 1:
            ans = min(ans, len(i) + abs(int(i) - N))
print(ans)