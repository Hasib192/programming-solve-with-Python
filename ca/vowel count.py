a = int(input())

arr = []

for i in range(a):
  s = input()
  count = 0
  vowels = set("aeiouy")
  for letter in s:
    if letter in vowels:
      count += 1
  arr.append(count)
print(*arr, sep=' ')