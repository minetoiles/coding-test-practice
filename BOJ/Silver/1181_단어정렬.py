import sys
n = int(input())
word = []
for _ in range(n):
    word.append(sys.stdin.readline().strip())

word.sort(key=lambda x: (len(x), x))

pre = ''
for w in word:
    if pre != w:
        print(w)
    pre = w