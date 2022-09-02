# 같은 숫자는 싫어
def solution(arr):
    answer = [arr[0]]
    for a in arr :
        if answer[-1] != a :
            answer.append(a)
    return answer