#로또의 최고순위와 최저순위
def solution(lottos, win_nums):
    answer = []
    count = 0
    zero_count = 0
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            count += 1
        elif lottos[i] == 0:
            zero_count += 1
    
    # 최고 순위는 count + zero_count, 최저 순위는 count
    if count + zero_count == 6:
        answer.append(1)
    elif count + zero_count == 5:
        answer.append(2)
    elif count + zero_count == 4:
        answer.append(3)
    elif count + zero_count == 3:
        answer.append(4)
    elif count + zero_count == 2:
        answer.append(5)
    else:
        answer.append(6)
    
    if count == 6:
        answer.append(1)
    elif count == 5:
        answer.append(2)
    elif count == 4:
        answer.append(3)
    elif count == 3:
        answer.append(4)
    elif count == 2:
        answer.append(5)
    else:
        answer.append(6)
    return answer