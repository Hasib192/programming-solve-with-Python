t = int(input())

arr1 = []

for i in range(t):
    arr = [int(x) for x in input().split()]
    arr.sort()
    median = arr[1]
    arr1.append(median)
print(*arr1, sep=' ')