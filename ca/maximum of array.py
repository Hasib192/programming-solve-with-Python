min = -999999
max = 999999
arr=[x for x in input().split()]
for i in range(300):
    b = int(arr[i])
    if b > min:
        min = b
    elif b < max:
        max = b
#print(min, max, sep=' ')