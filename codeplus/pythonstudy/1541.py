# 1541 잃어버린 괄호
import re
s = input()
numbers = re.split('[+-]', s)
op = []
num = ""
for i in s :
    if i == "+" or i == "-" :
        op.append(i)


print(numbers)
print(op)