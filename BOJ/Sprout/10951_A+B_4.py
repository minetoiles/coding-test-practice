# BOJ 10951 A+B - 4
# EOFError는 입력이 더 이상 없을 때 발생하는 예외

while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except EOFError:
        break

# sys.stdin.readline()은 입력이 더 이상 없을 때 빈 문자열을 반환하므로
# EOFError 대신 빈 문자열을 체크하여 반복문을 종료할 수 있음
import sys
while True:
    line = sys.stdin.readline()
    if not line:
        break
    a, b = map(int, line.split())
    print(a + b)