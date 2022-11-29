#1244 스위치 켜고 끄기 

n = int(input())
switch = [-1] + list(map(int, input().split()))
m = int(input())
students = []
for i in range(m) :
    s, num = map(int, input().split())
    if s == 1 :
        for j in range(1,n+1) :
            if j % num == 0 :
                if switch[j] == 0 :
                    switch[j] = 1
                elif switch[j] == 1 :
                    switch[j] = 0
    elif s == 2 :
        for j in range(1,n+1) :
            if j == num :
                if switch[j] == 0 :
                    switch[j] = 1
                elif switch[j] == 1 :
                    switch[j] = 0
                cnt = min(num-1, n-num)
                for k in range(1, cnt+1) :
                    if switch[j-k] == switch[j+k] :
                        if switch[j-k] == 0 :
                            switch[j-k] = 1
                            switch[j+k] = 1
                        elif switch[j-k] == 1 :
                            switch[j-k] = 0
                            switch[j+k] = 0
                    else :
                        break

for i in range(1, n+1):
    print(switch[i], end = " ")
    if i % 20 == 0 :
        print()        
# ans1 = n // 20 
# ans2 = n % 20
# for i in range(ans1) :
#     print(switch[1 + 20*ans1 : 21 + 20*ans1])

# print(switch[n-ans2+1:n+1])
    

