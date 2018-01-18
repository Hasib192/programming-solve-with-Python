a = int(input())

arr= []

for i in range(a):
    var1, var2 = input().split()
    c = min(int(var1), int(var2))
    arr.append(c)
print(*arr, sep=' ')