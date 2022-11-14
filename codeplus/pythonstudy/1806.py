# 1806 부분합
'''
def sooyal_hap(n, s, i, sooyal, hap, count) : # i 는 인덱스
    while hap < s :
        if i == n :
            count = 100001
            return count
        hap += sooyal[i]
        i += 1
        count += 1
    return count

n, s = map(int, input().split())
sooyal = list(map(int, input().split()))
count_list = []
for i in range(n) :
    count_list.append(sooyal_hap(n, s, i, sooyal, 0, 0))

if min(count_list) == 100001 :
    print(0)
else :
    print(min(count_list))
'''
# 투포인터 알고리즘 
n, s = map(int, input().split())
sooyal = list(map(int, input().split()))
start, end = 0, 0
hap = 0
count = 100001

while True :
    if hap >= s :
        count = min(count, end-start)
        hap -= sooyal[start]
        start += 1
    elif end == n :  # 끝까지 가면 break
        break
    else :
        hap += sooyal[end]
        end += 1
if count == 100001 :
    print(0)
else :
    print(count)

