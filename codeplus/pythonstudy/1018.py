# 1018 체스판 다시 칠하기
n, m = map(int, input().split())
board = []
count = []
for i in range(n) :
    b = input()
    board.append(b)

for a in range(n-7) :
    for b in range(m-7) :
        tmp1 = 0
        tmp2 = 0
        for i in range(a, a + 8) :
            for j in range(b, b + 8) :
                if (i + j) % 2 == 0 :
                    if board[i][j] != "W" :
                        tmp1 += 1
                    if board[i][j] != "B" :
                        tmp2 += 1
                else :
                    if board[i][j] != "B" :
                        tmp1 += 1
                    if board[i][j] != "W" : 
                        tmp2 += 1
        count.append(min(tmp1,tmp2))
print(min(count))    
