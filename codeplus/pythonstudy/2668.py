# 2668
# dfs
n = int(input())
n_list = [[] for i in range(n+1)]
for i in range(1, n+1) :
    n_list[i].append(int(input()))
answer = []


def dfs(num) :
    if visited[num] == False:
        visited[num] = True
        for i in n_list[num] :
            n_list1.add(num)
            n_list2.add(i)

            if n_list1 == n_list2 :
                answer.extend(list(n_list2))
                return
            
            dfs(i)
    visited[num] = False

for i in range(1, n+1):
    visited = [False] * (n+1)
    n_list1 = set()
    n_list2 = set()

    dfs(i)

answer = list(set(answer))
answer.sort()

print(len(answer))
for i in range(len(answer)) :
    print(answer[i])

