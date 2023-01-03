# 19941 햄버거 분배

n, k = map(int, input().split())
hp = input()
check = [0] * n
cnt = 0
for i in range(n):
    if hp[i] == "P" :
        for j in range(1,k+1):
            if hp[i] == "P" and check[i] == 0 :
                if i - j >= 0 :
                    if hp[i-j] == "H" and check[i-j] == 0 :
                        check[i-j] = 1
                        cnt += 1
                        break
                    elif hp[i-j] == "H" and check[i-j] == 1 :
                        if i + j <= n-1 :
                            if hp[i+j] == "H" and check[i+j] == 0 :
                                check[i+j] = 1
                                cnt += 1
                                break
                elif i + j <= n-1 :
                    if hp[i+j] == "H" and check[i+j] == 0 :
                        check[i+j] = 1
                        cnt += 1
                        break 

print(cnt)
