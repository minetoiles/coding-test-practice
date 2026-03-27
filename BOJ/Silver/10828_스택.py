# BOJ 10828 스택

import sys
input = sys.stdin.readline
from collections import deque
n = int(input())

s = deque()
result = []

for i in range (n):
    cmd = input().split()
    
    if (cmd[0] == "push"):
        s.append(int(cmd[1]))
    elif (cmd[0] == "pop"):
        if (len(s) == 0):
            result.append("-1")
        else:
            result.append(str(s.pop()))
    elif (cmd[0] == "size"):
        result.append(str(len(s)))
    elif (cmd[0] == "empty"):
        if (len(s) == 0):
            result.append("1")
        else:
            result.append("0")
    elif (cmd[0] == "top"):
        if (len(s) == 0):
            result.append("-1")
        else:
            num = s.pop()
            result.append(str(num))
            s.append(num)
            
print("\n".join(result))