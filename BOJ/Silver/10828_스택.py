# BOJ 10828 스택

import sys
input = sys.stdin.readline

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
        self.count += 1

    def pop(self):
        if self.top is None:
            return -1
        node = self.top
        self.top = self.top.next
        self.count -= 1
        return node.data

    def peek(self):
        if self.top is None:
            return -1
        return self.top.data

    def is_empty(self):
        return 1 if self.top is None else 0

    def size(self):
        return self.count


s = Stack()
n = int(input())

result = []

for _ in range(n):
    cmd = input().split()

    if cmd[0] == "push":
        s.push(int(cmd[1]))
    elif cmd[0] == "pop":
        result.append(str(s.pop()))
    elif cmd[0] == "size":
        result.append(str(s.size()))
    elif cmd[0] == "empty":
        result.append(str(s.is_empty()))
    elif cmd[0] == "top":
        result.append(str(s.peek()))

print("\n".join(result))