# BOJ 9012 괄호

from collections import deque

n = int(input())

for i in range(n):
    ps = input()
    if (len(ps) % 2 == 1):
        print("NO")
        continue

    s = list(ps)
    q = deque()
    for j in range(len(ps)):
        if (len(q) == 0):
            q.append(s.pop())
        else:
            spop = s.pop()
            qpop = q.popleft()
            if (spop == "(" and qpop == ")"):
                continue
            else:
                q.append(qpop)
                q.append(spop)
                
    if (len(q) != 0):
        print("NO")
    else:
        print("YES")
        