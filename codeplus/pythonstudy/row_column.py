def solution(rows, columns, queries):
    answer = []
    board = []
    for i in range(rows):
        b = [(j+1)+(i*columns) for j in range(columns)]
        board.append(b)

    for i in range(len(queries)) :
        min_list = []
        x1, y1, x2, y2 = queries[i][0], queries[i][1], queries[i][2], queries[i][3]
        
        for j in range(4) :
            if j == 0 :
                for a in range(y2-y1) :
                    board[x1-1][y2-1 - a] = board[x1-1][y2-2 - a]
                    min_list.append(board[x1-1][y2-1 - a])
            elif j == 1 :
                for b in range(x2-x1) :
                    board[b + x1-1][y1-1] = board[b + x1][y1-1]
                    min_list.append(board[b + x1-1][y1-1])
            elif j == 2 :
                for c in range(y2-y1) :
                    board[x2-1][c + y1-1] = board[x2-1][c + y1]
                    min_list.append(board[x2-1][c + y1-1])
            elif j == 3 :
                for d in range(x2-x1) :
                    board[x2-1 - d][y2-1] = board[x2-2 - d][y2-1]
                    min_list.append(board[x2-1 - d][y2-1])
                    
        answer.append(min(min_list))
    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))