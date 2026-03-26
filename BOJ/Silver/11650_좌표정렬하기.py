# BOJ 11650 좌표정렬하기

import sys

n = int(input())

data = []
for i in range (n):
    x, y = map(int, sys.stdin.readline().split())
    data.append((x, y))

data.sort(key=lambda x:(x[1]))
data.sort(key=lambda x:(x[0]))
for x, y in data:
    print(x, y)