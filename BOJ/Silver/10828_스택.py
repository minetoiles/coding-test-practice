class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def push(self, data):
        if self.top is None:
            self.top = Node(data)
            self.count += 1
            return
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
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None
    
    def size(self):
        return self.count


if __name__ == "__main__":
    s = Stack()
    
    n = int(input())
    for i in range(n):
        cmd = input()
    
        if (cmd == "push"):
            command, num = cmd.split()
            number = int(num)
            s.push(number)
        elif (cmd == "pop"):
            print(s.pop())
        elif (cmd == "size"):
            print(s.size())
        elif (cmd == "empty"):
            print(s.is_empty())
        elif (cmd == "top"):
            print(s.peek())