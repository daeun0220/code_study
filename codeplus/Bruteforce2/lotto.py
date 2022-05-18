# 6603번 로또

def solve(a, index, lotto):
    if len(lotto) == 6:  # 정답 도출될때
        print(' '.join(map(str,lotto)))
        return
    if index == len(a):   
        return
    solve(a, index+1, lotto+[a[index]])   # 다음 경우 호출 방법
    solve(a, index+1, lotto)   

while True:
    s = list(map(int,input().split()))
    k = s[0]
    if k == 0:
        break
    del s[0]
    solve(s, 0, [])
    print()
