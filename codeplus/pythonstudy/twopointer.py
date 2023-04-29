
array = [4,6,-2,9,2,-5]
front = 0
right = 0
target = 15

while right < len(array) :
    if sum(array[front:right]) < target :
        right += 1
    elif sum(array[front:right]) > target :
        front += 1
    elif sum(array[front:right]) == target :
        print(array[front:right])