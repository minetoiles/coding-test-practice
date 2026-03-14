# BOJ 1181 단어 정렬
# sort()의 key 매개변수에 람다 함수를 사용하여 길이와 사전 순으로 정렬

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