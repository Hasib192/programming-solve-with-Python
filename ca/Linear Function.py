t = eval(input())
answer = []
for i in range(t):
    x1, y1, x2, y2 = input().split()
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)
    # y = ax + b
    # a = diff(y) / diff(x)
    a = int(y2 - y1 // x2 - x1)
    # y = ax + b implies that, y - ax = b, where y and x is the first value from the value
    b = int(y1 - a * x1)
    answer.append('({0}, {1})', format(a, b))
print(*answer, sep=' ')
