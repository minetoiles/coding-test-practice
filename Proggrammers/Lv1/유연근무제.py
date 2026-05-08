# 유연근무제
# schedules 직원들 희망 근무 시간 1차원 배열
# timelogs 직원들의 실제 근무 시간 2차원 배열
# startday 시작 요일 0: 월요일, 1: 화요일, ...,

def solution(schedules, timelogs, startday):
    answer = 0
    day = 0

    for i in range(len(schedules)):
        if schedules[i] % 100 < 50:
            schedules[i] = schedules[i] + 10
        elif schedules[i] % 100 == 60:
            schedules[i] = schedules[i] + 40
        else:
            schedules[i] = schedules[i] + 50

    for i in range(len(schedules)):
        for j in range(len(timelogs[i])):
            if timelogs[i][j] <= schedules[i]:
                if (startday + j)% 7 != 6 and (startday + j) % 7 != 0:
                    day += 1
        if day >= 5:
            answer += 1
        day = 0

    return answer
