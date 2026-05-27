# 초, 노, 빨이 각각 켜지는 주기가 주어질 때
# 처음으로 노란불이 동시에 켜지는 순간을 찾는 문제

def solution(signals):
    
    hap = []

    for i in range(len(signals)):
        hap.append(sum(signals[i]))

    yellow = []
    for i in range(len(signals)):
        yellow.append([signals[i][0], signals[i][0] + signals[i][1] - 1])
    
    t = 1
    while(True):
        check = []
        cnt = 0

        if (t == 1):
            initial = []
            for i in range(len(hap)):
                initial.append((t - 1) % hap[i])
            
            for i in range(len(yellow)):
                if (initial[i] >= yellow[i][0] and initial[i] <= yellow[i][1]):
                    cnt += 1
            
            if (cnt == len(hap)):
                return t
        else:
            for i in range(len(hap)):
                check.append((t - 1) % hap[i])
            
            if (initial == check):
                return -1
        
            for i in range(len(yellow)):
                if (check[i] >= yellow[i][0] and check[i] <= yellow[i][1]):
                    cnt += 1
                
            if (cnt == len(hap)):
                return t
        t += 1


# 공식은 (초+노+빨)x - (초+노-1) ~ (초+노+빨)x - (빨)
# 노란색 1초면 그냥 (초+노+빨)x - (초+노-1)

# 최소공배수적인 사고
# 시간을 주기로 나눠서 모든 신호등의 노란불이 켜지는 순간을 구한다
# -1인 경우는 신호등이 세 개라고 가정했을 때 t=1 -> (a, b, c) ... t=x -> (a, b, c)가 나오는 순간
# 앞으로의 패턴이 처음부터 똑같이 반복된다!!