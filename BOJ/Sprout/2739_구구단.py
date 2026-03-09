# BOJ 2739 구구단
# 파이썬 print() 함수에서 문자열과 변수를 함께 출력할 때는 ,로 구분하여 출력
a = int(input())

for i in range(1, 10):
    print(a, "*", i, "=", a * i)