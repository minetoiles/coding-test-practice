# BOJ 2751 수 정렬하기 2
# sys.stdin.readline()을 사용하여 입력 속도 향상
import sys

n = int(input())
num = []

for i in range(n):
    num.append(int(sys.stdin.readline()))

num.sort()

for j in num:
    print(j, end=" ")