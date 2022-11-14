# 리스트를 딕셔너리에 넣어 계산하기 

import collections
n = int(input())
votes = list(map(int,input().split()))
candidate = {}
for i in range(len(votes)):
    if votes[i] not in candidate:
        candidate[votes[i]] = 1
    else:
        candidate[votes[i]] = candidate[votes[i]] + 1

answer = max(candidate.values())

answers = []
for i in range(1,n+1):
    if i in candidate:
        if answer == candidate[i]:
            answers.append(i)

print(answer)
print(answers)
print(candidate)