# 1018 체스판 다시 칠하기
n, m = map(int, input().split())
board = []
for i in range(n) :
    b = input()
    board.append(b)
tmp = 0
for i in range(n-7) :
    for j in range(m-7) :
        chess = board[i[j:j+8]]
        cnt1 = chess.count("BW")
        cnt2 = chess.count("WB")
        cnt = max(cnt1, cnt2)
        if cnt >= tmp :
            tmp = cnt
            check = j 
    
