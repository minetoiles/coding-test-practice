# BOJ 1330 두 수 비교하기
# 파이썬 if문은 들여쓰기로 구분
# if, elif, else로 조건문 작성
# {} 대신 : 사용

a, b = map(int, input().split())

if (a > b):
    print(">")
elif (a < b): 
    print("<")
else:
    print("==")
