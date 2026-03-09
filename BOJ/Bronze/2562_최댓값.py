# BOJ 2562 최댓값
# for 문 range(0, 9)로 9번 반복
max = 0
idx = -1
for i in range(0, 9):
    a = int(input())
    if (a > max):
        max = a
        idx = i+1
        
print(max)
print(idx)
