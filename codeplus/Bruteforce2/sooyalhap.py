# 1182 부분수열의 합

# 모든 경우 다 해봐야한다

n, s = map(int, input().split())
num = list(map(int,input().split()))
ans = 0
def go(a,b):
    global ans
    if a == n:
        if b == s:
            ans += 1
        return
    go(a+1, b+num[a])
    go(a+1, b)

go(0,0)
if s == 0:
    ans -= 1
print(ans)


