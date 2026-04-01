# BOJ 2798 블랙잭

n, m = map(int, input().split())
cards = list(map(int, input().split()))
max_sum = 0
sum = 0
for i in range(n):
    sum += cards[i]
    for j in range(i+1, n):
        if (sum >= m):
            continue
        sum += cards[j]
        for k in range(j+1, n):
            if (sum >= m):
                continue
            sum += cards[k]
            if (max_sum < sum and sum <= m):
                max_sum = sum
    sum = 0     
print(max_sum)

            
            