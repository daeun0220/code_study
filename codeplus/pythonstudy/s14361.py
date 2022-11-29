# 14361 swea 숫자가 같은 배수
t = int(input())
for i in range(t) :
    n = input()
    n_list = sorted(list(n))

    check = False
    k = 2
    while True :
        num = int(n) * k
        if len(str(num)) > len(n) :
            break
        if sorted(list(str(num))) == n_list :
            flag = True
            break
        k += 1
    
    if flag:
        answer = "possible"
    else:
        answer = "impossible"

    print(f"#{i} {answer}")

