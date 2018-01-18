t = eval(input())
arr1 = []
arr = [x for x in input().split()]

for i in range(t):
    cs = eval(arr[i])
    count = 0
    while cs != 1:
        if cs % 2 is 0:
            cs = cs // 2 # '//' after division it gives the integer value
        else:
            cs = 3 * cs + 1
        count = count + 1
    arr1.append(count)
print(*arr1, sep=' ')

