'''
첫 번째 집과 마지막 집도 인접한 것
두 가지 조건으로 나누어서 생각해야함
1. 첫번째 집을 털고, 마지막 집을 털지 않는 경우 
2. 그 반대의 경우
'''

def solution(money):
    dp1 = [0] * len(money)
    dp2 = [0] * len(money)

    # 1번 집을 터는 경우
    dp1[0] = money[0]
    
    # 마지막 집 털지 않음
    for i in range(1, len(money) - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])

    # 1번 집을 안터는 경우
    dp2[0] = 0
    for i in range(1, len(money)):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])

    return max(dp1[-2], dp2[-1])
