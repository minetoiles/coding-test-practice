def solution(new_id):
    answer = ''
    
    new_id = new_id.lower()

    for i in range(len(new_id)):
        if new_id[i].isalnum() or new_id[i] in ['-', '_', '.']:
            if (new_id[i] != ' '):
                answer += new_id[i]
            else:
                answer += 'a'
    
    '''
    start_idx = -1
    count = 0
    idx = 0
    while True:
        if (idx >= len(answer)):
            break
        
        if (answer[idx] == '.' and start_idx == -1):
            start_idx = idx
        elif (answer[idx] == '.' and start_idx != -1):
            count += 1
        
        elif (count != 0 and answer[idx] != '.'):
            answer = answer[:start_idx + 1] + answer[start_idx+count+1:]
            count = 0
            start_idx = -1
        idx += 1
    if (count != 0):
        answer = answer[:start_idx + 1]
    '''
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    if answer[0] == '.':
        answer = answer[1:]
    elif answer[-1] == '.':
        answer = answer[:-1]

    if (len(answer) == 0):
        answer = 'a'
    
    if (len(answer) >= 16):
        answer = answer[0:15]
    if answer[-1] == '.':
        answer = answer[:-1]
    
    while len(answer) <= 2:
        answer += answer[len(answer) - 1]
            
    return answer

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("abcdefghijklmn.p"))