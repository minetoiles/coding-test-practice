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