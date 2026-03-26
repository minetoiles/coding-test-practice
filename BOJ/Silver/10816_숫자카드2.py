# BOJ 10816 숫자카드2
# 리스트 원소 개수 셀 때 count보다 collections Counter 사용

import sys
from collections import Counter

n = int(sys.stdin.readline()) # 카드 개수
data = []
data = list(map(int, sys.stdin.readline().strip().split()))

cntNum = []
m = int(sys.stdin.readline()) # 숫자 셀 카드
cntNum = list(map(int, sys.stdin.readline().strip().split()))

c = Counter(data)
for i in range (m):
    print(c[cntNum[i]], end=" ")