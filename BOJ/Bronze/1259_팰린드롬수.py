# BOJ 1259 팰린드롬수

while True:
    n = input()
    if n == '0':
        break
    
    flag = 1
    for i in range (len(n)//2):
        if (n[i] != n[len(n)-i-1]):
            flag = 0
            break
    
    if (flag == 1):
        print("yes")
    else:
        print("no")
    
    
        