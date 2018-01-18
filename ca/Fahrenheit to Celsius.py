a = int(input())

arr = [int(x) for x in input().split()]

arr1 = []

for x in range(a):
    b = arr[x]
    c = (b - 32) / 1.8
    arr1.append(int(round(c)))

print(*arr1, sep=' ')