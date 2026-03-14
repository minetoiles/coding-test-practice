import sys
num1 = int(input())
list1 = list(map(int, sys.stdin.readline().split()))
list1.sort()

num2 = int(input())
list2 = list(map(int, sys.stdin.readline().split()))

for i in list2:
    start = 0
    end = num1-1
    
    found = 0
    
    while(start <= end):
        mid = (start + end)//2
        if (list1[mid] == i):
            found = 1
            break
        elif (list1[mid] > i):
            end = mid - 1
        else:
            start = mid + 1

    print(found)
    