import math
t = int(input())

arr1 = []
while t is not 0:
    arr = [int(x) for x in input().split()]
    sum = 0
    count = 0
    for i in arr:
        if i is not 0:
            sum += i
            count += 1
    t -= 1
    avg = (sum / count) + 0.5 #0.5 for ceil or floor the value
    avg = int(avg)
    arr1.append(avg)
print(*arr1, sep=' ')