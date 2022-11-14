# 1700 멀티탭 스케줄링
n, k = map(int,input().split())
elec = list(map(int, input().split()))
multitap = [0] * n 
count = 0
for i in range(k) :
    switch = 0
    tmp = 0
    if elec[i] in multitap :
        continue
    elif 0 in multitap :
        multitap[multitap.index(0)] = elec[i]
    else :
        for j in multitap :
            if j not in elec[i:] : # i+1 는 런타임에러 자꾸 남...
                switch = j
                break
            elif elec[i:].index(j) > tmp:   # j 가 elec에 있을때, 여러개 있을 떄 
                switch = j
                tmp = elec[i:].index(j)
        count += 1
        multitap[multitap.index(switch)] = elec[i]
   
print(count)