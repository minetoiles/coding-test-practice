max = 0
idx = -1
for i in range(0, 8):
    a = int(input())
    if (a > max):
        max = a
        idx = i+1
        
print(max)
print(idx)
