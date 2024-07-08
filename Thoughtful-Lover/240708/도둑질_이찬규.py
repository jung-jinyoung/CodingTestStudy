# 조건 1. 전체 money 배열의 개수 중 절반 이하만 뽑는다.
# 조건 2. 값이 0인 값은 뽑지 않는다.
# 조건 3. 이웃한 두 집을 고를 수는 없다.


from collections import deque

def solution(money):
    money_idx = deque()
    length = len(money)
    start = 0
    while True:
        if start >= length:
            break
        if start == 0:
            start += 1
        elif money[start] >= money[start+1]:
            money_idx.append(start)
            start += 1
        else:
            money_idx.append(start+1)
            start += 2
        continue
    answer = 0
    for idx in money_idx:
        answer += money[idx]
    return answer

