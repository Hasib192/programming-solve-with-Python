t = int(input())

arr1 = []
for i in range(t):
    a, b, n = input().split()
    s = 0
    for i in range(int(n)):
        d = int(a) + int(b) * int(i)
        s += d
    arr1.append(s)

print(*arr1, sep=' ')