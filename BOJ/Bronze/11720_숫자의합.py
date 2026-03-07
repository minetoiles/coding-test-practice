n = int(input())
sum = 0
a = int(input())
for j in range(0, n):
    sum += a % 10
    a //= 10
print(sum)