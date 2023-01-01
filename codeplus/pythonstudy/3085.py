# 사탕게임

n = int(input())
candy = [list(input()) for i in range(n)]
answer = []

# 양옆 바꿀 때
for i in range(n) :
    ans = 0
    for j in range(n-1) :
        if candy[i][j] != candy[i][j+1] :
            tmp = candy[i][j]
            candy[i][j] = candy[i][j+1]
            candy[i][j+1] = tmp 

            # 이때 사탕 개수 세기
            # 양옆
            for a in range(n) :
                count = 1
                for b in range(n-1) :
                    if candy[a][b] == candy[a][b+1] :
                        count += 1
                    else :
                        break
                if ans < count :
                    ans = count 
            answer.append(ans)

            # 위아래
            for a in range(n-1) :
                count = 1
                for b in range(n) :
                    if candy[a][b] == candy[a+1][b] :
                        count += 1
                    else:
                        break
                if ans < count :
                    ans = count 
            answer.append(ans)

res = max(answer)
print(res)
print(answer)      