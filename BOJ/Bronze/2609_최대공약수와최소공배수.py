# BOJ 2609 최대공약수와 최소공배수
# a,b가 서로소인 경우를 고려해 n=1부터 시작해야 한다

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