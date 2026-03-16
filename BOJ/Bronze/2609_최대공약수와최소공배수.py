a, b = map(int, input().split())

n = 1
num1 = 0
while True:
    if (a < n) or (b < n):
        break
    if (a % n == 0 and b % n == 0):
        num1 = n
    n += 1

num2 = num1 * (a//num1) * (b//num1)

print(num1)
print(num2)