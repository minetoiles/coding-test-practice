def solution(today, terms, privacies):
    answer = []
    # terms 는 dictionary t로 보관
    
    for i in range(len(privacies)):
        # privacies 날짜, 약관으로 나누기
        # 날짜는 연도, 월, 일로 나누기
        
        # t[privacies] * 28을 일에 더해주고
        # 28로 나눈 몫을 월로 올림
        # 12로 나눈 몫을 연도로 올림
        
        # 날짜를 YYYY.MM.DD 문자열 형식으로 변환
        
        # today보다 작으면 result에 append
    
    return answer