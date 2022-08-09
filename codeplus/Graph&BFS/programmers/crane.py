
def solution(board, moves):
    answer = 0
    n = len(board)
    m = len(moves)
    basket = []
    for i in range(m):
        moves[i] = moves[i] - 1
    for i in moves:
        count = 0
        for j in range(n):
            if count == 1:
                continue    # 밑 if문 수행하지 않는다
            if board[j][i] != 0:
                count += 1
                basket.append(board[j][i])
                board[j][i] = 0
                if len(basket) > 1: 
                    if basket[-1] == basket[-2]:
                        basket.pop()
                        basket.pop()
                        answer += 2
    return basket


n = int(input())
board = []
for i in range(n):
    b = list(map(int,input().split()))
    board.append(b)
moves = list(map(int,input().split()))
print(solution(board, moves))
