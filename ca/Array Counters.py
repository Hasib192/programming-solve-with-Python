t = int(input())

arr1 = []

arr = [x for x in input().split()]

for i in range (t):
    wsd = arr[i]
    l = len(wsd)
    l = int(l)
    wsd = int(wsd)
    s = 0
    while wsd is not 0:
        d = wsd % 10
        s += d * l
        l -= 1
        wsd = wsd /10
        wsd = int(wsd)
    arr1.append(s)
print(*arr1, sep=' ')