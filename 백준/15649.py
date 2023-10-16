# N과 M(1)

n, m = map(int, input().split())
arr = [ 0 for _ in range(m)]
visit = [True for _ in range(n)]
answer = []


def permutation(n, m, depth) :
    if depth == m :
        for i in arr :
            answer.append(i)
        return
    
    for i in range(n) :
        if visit[i] == True :
            visit[i] = False
            arr[depth] = i + 1
            permutation(n,m,depth+1)
            visit[i] = True

