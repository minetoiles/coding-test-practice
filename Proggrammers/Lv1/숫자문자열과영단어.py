# 숫자문자열과 영단어
# 파이썬은 for문 내에서 i값을 변경해도 순서대로 진행됨
# while문을 사용해서 i값을 변경해가며 진행하기

def solution(s):
    answer = ''
    i = 0

    while i < len(s):
        if s[i:i+3] == 'one':
            answer += '1'
            i += 3

        elif s[i:i+3] == 'two':
            answer += '2'
            i += 3

        elif s[i:i+5] == 'three':
            answer += '3'
            i += 5

        elif s[i:i+4] == 'four':
            answer += '4'
            i += 4

        elif s[i:i+4] == 'five':
            answer += '5'
            i += 4

        elif s[i:i+3] == 'six':
            answer += '6'
            i += 3

        elif s[i:i+5] == 'seven':
            answer += '7'
            i += 5

        elif s[i:i+5] == 'eight':
            answer += '8'
            i += 5

        elif s[i:i+4] == 'nine':
            answer += '9'
            i += 4

        elif s[i:i+4] == 'zero':
            answer += '0'
            i += 4

        else:
            answer += s[i]
            i += 1

    return int(answer)