# 1789

s = int(input())
count = 0
sum = 0
while True :
    if sum > s :
        break
    count += 1
    sum += count
print(count - 1)