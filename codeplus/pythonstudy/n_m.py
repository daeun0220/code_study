def solution(board, skill):
    answer = 0
    tmp = [[0] * (len(board[0]) + 1) for i in range(len(board)+1)]
    for stype, r1, c1, r2, c2, degree in skill :
        if type == 2 :
            degree = -degree
        tmp[r1][c1] -= degree
        tmp[r1][c2+1] += degree
        tmp[r2+1][c1] += degree
        tmp[r2+1][c2+1] -= degree
    
    for i in range(len(tmp)-1):
        for j in range(len(tmp[0])-1):
            tmp[i][j+1] += tmp[i][j]
    
    for i in range(len(tmp)-1):
        for j in range(len(tmp)-1):
            tmp[i][j+1] += tmp[i][j]
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] + tmp[i][j] > 0 :
                answer += 1
    
    return answer