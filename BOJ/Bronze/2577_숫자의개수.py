# BOJ 2577 숫자의 개수
# str() 함수를 사용하여 숫자를 문자열로 변환
# 문자열의 count() 메서드를 사용하여 각 숫자의 개수를 세어 출력

a = int(input())
b = int(input())
c = int(input())

sum = a * b * c
s = str(sum)
print(s.count('0'))
print(s.count('1'))
print(s.count('2'))
print(s.count('3'))
print(s.count('4'))
print(s.count('5'))
print(s.count('6'))
print(s.count('7'))
print(s.count('8'))
print(s.count('9'))