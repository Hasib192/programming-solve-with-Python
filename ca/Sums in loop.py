a = int(input())
mySum = 0
arr = []
for x in range(a):
    a, b = input().split()
    mySum = int(a) + int(b)
    arr.append(mySum)
print(*arr, sep=' ')