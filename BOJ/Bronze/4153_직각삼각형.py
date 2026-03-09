# BOJ 4153 직각삼각형

while True:
    t = list(map(int, input().split()))
    
    if (t[0] == 0 and t[1] == 0 and t[2] == 0):
        break
    
    t.sort()
    if t[0]**2+t[1]**2 == t[2]**2:
        print("right")
    else:
        print("wrong")
