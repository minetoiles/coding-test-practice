
n = int(input())
tsize = list(map(int, input().split()))
t, p = map(int, input().split())

tsum = 0
for tshirt in tsize:
    leftover = tshirt % t
    tshirt //= t
    if (tshirt == 0):
        tsum += 1
    elif (leftover != 0):
        tsum += (tshirt + 1)
    else:
        tsum += tshirt

print(tsum)
print(n//p, n%p)
