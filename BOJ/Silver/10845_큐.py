# BOJ 10845 큐
# 문제 조건을 잘 읽자
# 시간 초과 방지를 위해 sys사용, 출력 한 번에
# deque 함수 공부...
import sys
input = sys.stdin.readline
from collections import deque
n = int(input())

q = deque()
result = []

for i in range (n):
    cmd = input().split()
    
    if (cmd[0] == "push"):
        q.append(int(cmd[1]))
    elif (cmd[0] == "pop"):
        if (len(q) == 0):
            result.append("-1")
        else:
            result.append(str(q.popleft()))
    elif (cmd[0] == "size"):
        result.append(str(len(q)))
    elif (cmd[0] == "empty"):
        if (len(q) == 0):
            result.append("1")
        else:
            result.append("0")
    elif (cmd[0] == "front"):
        if (len(q) == 0):
            result.append("-1")
        else:
            num = q.popleft()
            result.append(str(num))
            q.appendleft(num)
    elif (cmd[0] == "back"):
        if (len(q) == 0):
            result.append("-1")
        else:
            num = q.pop()
            result.append(str(num))
            q.append(num)

print("\n".join(result))