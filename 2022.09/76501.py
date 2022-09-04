# 음양 더하기
def solution(absolutes, signs):
    answer = 0
    for i, v in enumerate(absolutes):
        answer = answer + v if signs[i] else answer-v
        
    return answer