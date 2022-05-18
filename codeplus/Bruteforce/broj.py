# 1748 수 이어 쓰기1
import sys
input = sys.stdin.readline
N = int(input())

length = len(str(N))
sum = 0
for i in range(length-1):
    sum += (i+1)*9*10**i

print(sum+ length*(N-10**(length-1)+1))

    