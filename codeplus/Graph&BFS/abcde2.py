# 13023번  ABCDE

n,m = map(int,input().split())
arr = [[] for i in range(n)]   # 이중리스트 만들어주고
check = [False] * n

for i in range(m):
    a, b = map(int,input().split())
    arr[a].append(b)        # 그래프를 인접 리스트 방식으로 표현  
    arr[b].append(a)        # 인접리스트 많이 사용

def dfs(index, number):
    if number == 4:
        print(1)
        return   # 그냥 return 하는건...?
    for i in arr[index]:
        if not check[i]: # True면
            check[i] = True
            dfs(i, number+1)
            check[i] = False

# 노드 순서대로 방문
for i in range(n):
    check[i] = True
    dfs(i, 0)
    check[i] = False

print(0)    # print(1) 하고 끝난게 아니면 print(0)
