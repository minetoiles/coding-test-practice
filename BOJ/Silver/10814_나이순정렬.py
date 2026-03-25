import sys
n = int(input())

data = []
for i in range(n):
    num, name = map(str, sys.stdin.readline().split())
    data.append((int(num), name))
    
data.sort(key = lambda x: x[0])

for age, name in data:
    print(age, name)
