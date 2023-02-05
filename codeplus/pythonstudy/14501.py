# 14501 퇴사   top-down dp .... 
n = int(input())
t_list = []
p_list = []
for i in range(n) :
    t, p = map(int, input().split())
    t_list.append(t)
    p_list.append(p)

dp = [0] * (n+1)
# 역순으로 진행 !!
for i in range(len(t_list)-2, -1, -1) :
    if t_list[i] + i < n+1 :
        dp[i] = max(p_list[i] + dp[i+ t_list[i]], dp[i+1]) # 최댓값 나오게됨
    else :
        dp[i] = dp[i+1]

print(dp[0])

