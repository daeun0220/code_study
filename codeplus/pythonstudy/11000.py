n = int(input())
classroom = []
for i in range(n) :
    s, t = map(int, input().split())
    classroom.append([s, t])

classroom.sort(key = lambda x : x[0])
count = 0
for i in range(n-1) :
    if classroom[i][1] <= classroom[i+1][0] :
        continue
    else :
        count += 1
print(count)