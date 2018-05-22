answer = []

test_cases = eval(input())

for test_case in range(test_cases):
    x1, y1, x2, y2 = [int(x) for x in input().split()]
    m = int((y2-y1)/(x2-x1))
    g = int(y1 - m * x1)
    answer.append('({0} {1})'.format(m, g))

print(' '.join(answer))
