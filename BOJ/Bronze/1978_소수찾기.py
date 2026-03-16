# BOJ 1978 소수 찾기
# for-else 구문을 사용하여 소수 판별
# 1은 소수가 아니다!!

n = int(input())
a = list(map(int, input().split()))

cnt = 0
for i in range(n):
    if a[i] == 1:
        continue
    for j in range(2, a[i]):
        if a[i] % j == 0:
            break
    else:
        cnt += 1
print(cnt)