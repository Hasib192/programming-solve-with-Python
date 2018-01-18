t = int(input())

arr = []

for i in range(t):
    a, b, c = input().split()
    d = int(a) * int(b) + int(c)
    s = 0
    while int(d) is not 0:
        e = d%10
        s += int(e)
        d = int(d)/10
    arr.append(s)
print(*arr, sep=' ')