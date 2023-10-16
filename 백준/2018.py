# 수들의 합 5
# 투포인터
n = int(input())
start, end = 1, 1
hap = 1
cnt = 0
while start <= end :
    if hap == n :
        cnt += 1
    
    if hap > n :
        hap -= start
        start += 1
    elif hap <= n :
        end += 1
        hap += end

print(cnt)