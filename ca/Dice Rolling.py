import math

t = int(input())

arr1 = []

for i in range (t):
    x = float(input())
    res = math.floor(x * 6) + 1
    arr1.append(res)
print(*arr1, sep=' ')