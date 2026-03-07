# BOJ 10818 최소, 최대
import sys

n = int(sys.stdin.readline())
max = -1000000
min = 1000000
a = list(map(int, sys.stdin.readline().split()))
for i in range(0, n):
    if (a[i] > max):
        max = a[i]
    if (a[i] < min):
        min = a[i]
print(min, end=" ")
print(max)