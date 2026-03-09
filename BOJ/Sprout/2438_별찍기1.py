# BOJ 2438 별 찍기 - 1
# 파이썬 for문은 range() 함수 사용
# range() 함수는 시작값, 끝값, 간격을 인자로 받음
# for i in range(0, a): -> 0부터 a-1까지 반복
# print() 함수는 기본적으로 줄바꿈을 포함하지만, end=""로 줄바꿈 제거 가능
a = int(input())

for i in range (0, a):
    for j in range(0, i + 1):
        print("*", end="")
    print()