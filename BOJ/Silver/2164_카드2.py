from collections import deque
n = int(input())
card = deque()
for i in range(n, 0, -1):
    card.append(i)
print(card)


while len(card) != 1:
    card.pop()
    up = card.pop()
    print(up)
    card.appendleft(up)
    print(card)
print(card[0])