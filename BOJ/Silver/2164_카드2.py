# BOJ 2164 카드2

from collections import deque

n = int(input())
card = deque()

for i in range(n, 0, -1):
    card.append(i)

while len(card) != 1:
    card.pop()
    up = card.pop()
    card.appendleft(up)
print(card[0])