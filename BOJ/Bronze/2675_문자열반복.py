# BOJ 2675 문자열 반복

cnt = int(input())
for i in range(0, cnt):
    n, s = input().split()
    num = int(n)
    p = ""
    for j in range(0, len(s)):
        p += s[j] * num
    print(p)