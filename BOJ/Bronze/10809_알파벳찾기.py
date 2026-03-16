# BOJ 10809 알파벳 찾기
# ord() 함수를 사용하여 문자의 ASCII 값을 구할 수 있음

s = input()

num = []
for i in range(26):
    num.append(-1)

j = 0
for letter in s:
    if (num[ord(letter)-97] == -1):
        num[ord(letter)-97] = j
    j+=1

for n in num:
    print(n, end=" ")