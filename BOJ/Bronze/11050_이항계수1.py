n, k = map(int, input().split())

def calc(n, k):
    if (k == 0 or k == n):
        return 1
    return calc(n-1, k-1) + calc(n-1, k)

print(calc(n, k))