# BOJ 11866 요세푸스 문제0
# 큐 사용해서 제거할 원소 자리 전까지 pop해서 append
# 제거할 원소 pop해서 result에 저장 반복

from collections import deque
n, k = map(int, input().split())

data = deque()
for i in range(1, n+1):
    data.append(i)

result = []
for i in range(n):
    for j in range(k - 1):
        num = data.popleft()
        data.append(num)
    result.append(str(data.popleft()))

print("<", end="")
print(", ".join(result), end=">")