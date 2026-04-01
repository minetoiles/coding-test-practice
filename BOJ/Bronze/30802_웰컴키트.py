# BOJ 30802 웰컴키트
n = int(input())
tsize = list(map(int, input().split()))
t, p = map(int, input().split())

tsum = 0
for tshirt in tsize:
    leftover = tshirt % t
    tnumber = tshirt // t
    if (tshirt != 0 and tnumber == 0):
        tsum += 1
    else:
        if (leftover != 0):
            tsum += (tnumber + 1)
        else:
            tsum += tnumber

print(tsum)
print(n//p, n%p)
