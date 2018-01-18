a = int(input())

arr=[x for x in input().split()]

MySum = 0

for i in range(a):
    b = int(arr[i])
    MySum += b

print(MySum)