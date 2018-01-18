n = int(input())

arr = []

for i in range(n):
    a, b, c = input().split()
    triangle = 0
    a = int(a)
    b = int(b)
    c = int(c)
    if a+b > c and b+c > a and c+a > b:
        triangle = 1
    arr.append(triangle)
	
print(*arr, sep=' ')

