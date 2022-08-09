# 6603번 로또
import itertools

def lotto(k, s):
    s.pop(0)
    ans = itertools.combinations(s, 6)     # () 형태로 반환 
    return ans  


while True:
    s = input().split()  # 문자열로 받는다 
    if s[0] == "0":    # 0도 문자열로 
        break
    for i in lotto(s[0], s):
        print(" ".join(i))   # 문자열만 붙여줌 / int 형태 XX
    print()