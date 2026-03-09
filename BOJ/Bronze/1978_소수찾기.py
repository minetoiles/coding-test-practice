n = int(input())
cnt = 0
a = list(map(int, input().split()))
for i in range(n):
    if a[i] == 1:
        continue
    for j in range(2, a[i]):
        if a[i] % j == 0:
            break
    else:
        cnt += 1
print(cnt)