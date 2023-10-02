# 7795 먹을 것인가 먹힐 것인가

def cal(a, b) :
    cnt = 0
    for i in a :
        for j in b :
            if i > j :
                cnt += 1
            else :
                break
    return cnt

t = int(input())
for _ in range(t) :
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    ans = cal(a, b)
    print(ans)


