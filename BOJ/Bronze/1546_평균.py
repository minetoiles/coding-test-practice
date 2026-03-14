# BOJ 1546 평균
# split()으로 띄어쓰기 입력 처리

import sys

n = int(input())
score = list(map(int, sys.stdin.readline().split()))

sum = 0
for i in score:
    sum += (i / max(score)) * 100
sum /= n
print(sum)