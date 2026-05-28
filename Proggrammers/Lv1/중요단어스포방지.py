def solution(message, spoiler_ranges):
    answer = 0

    important = {}
    index = []
    for i in range(len(spoiler_ranges)):
        start = spoiler_ranges[i][0]
        end = spoiler_ranges[i][1]
            
        while (True):
            if (start == 0 or message[start-1] == " " or message[start] == " "):
                break
            start -= 1
        while (True):
            if (end == len(message)-1 or message[end+1] == " " or message[end] == " "):
                break
            end += 1
        
        message_parts = message[start:end+1].split(" ")
        idx_end = 0
        for i in range(len(message_parts)):
            if (index.count([start+i+idx_end, start+len(message_parts[i])+idx_end-1]) == 0):
                index.append([start+i+idx_end, start+len(message_parts[i])+idx_end-1])
                if (important.get(message_parts[i]) == None):
                    important[message_parts[i]] = 1
                else:
                    important[message_parts[i]] += 1

            idx_end += len(message_parts[i]) + 1

    m = message.split(" ")
    for i in range(len(important)):
        if (m.count(list(important.keys())[i]) == important[list(important.keys())[i]]):
            answer += 1
                    
    
    return answer

# print(solution("my phone number is 01012345678 and may i have your phone number", [[5,5],[25,28],[34,40],[53,59]]))

# print(solution("ab ab", [[0,0], [0,1]])) => 이 케이스는 0이 나와야 함
# 단어 범위도 저장해서 확인해야 함

print(solution("ab ab", [[0,0], [3,3]]))

# 중요한 단어 개수 return!
# 스포 방지 되어있는 단어들을 줍줍
# 이걸 어떻게 찾지..
# 해당 단어의 앞 뒤가 공백 or 시작점 끝점인지 확인해서 찾기
# 그 단어가 다른 곳에서 등장했는지 찾기
# 다른 곳에서 등장하지 않았다면 중요 단어 + 1
