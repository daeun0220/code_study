# 1912 연속합

n = int(input())
number = list(map(int, input().split()))
dp = [0]*n
dp[0] = number[0]

for i in range(1,n) :
    dp[i] = max(number[i], dp[i-1] + number[i])
print(max(dp))