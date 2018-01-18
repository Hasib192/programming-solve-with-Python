t = int(input())

arr = ['under','normal','over','obese']

arr1 = []
for i in range(t):
    var1, var2 = input().split()
    var2 = float(var2)
    bmi = int(var1) / float(var2 ** 2)
    bmi = float(bmi)
    if bmi > 0.0 and bmi <= 18.5:
        arr1.append(arr[0])
    elif bmi > 18.5 and bmi <= 25.0:
        arr1.append(arr[1])
    elif bmi > 25.0 and bmi <= 30.0:
        arr1.append(arr[2])
    elif bmi>30.0:
        arr1.append(arr[3])
print(*arr1, sep=' ')