# 2023 신기한 소수 
# 시간복잡도....
n = int(input())
MAX = int('9'* n) 
MIN = int('2'+'0'*(n-1))
def soo(x) :
    if x == 1 :
        return 1 
    for i in range(2,x) :
        if x % i == 0 :
            return 1
    return 0  # 소수

for i in range(MIN, MAX+1) :
    if i % 2 != 0 :
        ans = 0
        if soo(i) == 0 :
            for j in range(len(str(i))) :
                s = str(i)[:j+1]
                if soo(int(s)) != 0 :
                    ans = 1
            if ans == 0 :
                print(i)
        


