# 삼각형과 세 변

while True :
    a, b, c = map(int, input().split())
    if a == b == c == 0 :
        break
    if max(a, b, c) >= a + b + c - max(a, b, c) :
        print("Invalid")
    elif a == b and b == c and a == c :
        print("Equilateral")
    elif a != b and b != c and a != c :
        print("Scalene")
    else :
        print("Isosceles")