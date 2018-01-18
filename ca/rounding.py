a = int(input())

arr = []

for x in range(a):
    var1, var2 = input().split()
    c = float(var1)/float(var2)
    if c > 0:
        c += 0.5
    elif c < 0:
        c -= 0.5
    arr.append(int(c))
print(*arr, sep=' ')