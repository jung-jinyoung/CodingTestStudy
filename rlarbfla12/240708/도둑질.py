def solution(money):
    # 첫번째 집을 털었을 경우의 최대 금액 저장
    dp_1 = [0] * len(money)

    # 마지막 집을 털었을 경우의 최대 금액 저장
    dp_2 = [0] * len(money)

    # 첫번째 집을 털었을 경우 초기값
    dp_1[0] = money[0]

    # 첫번째 집을 털었을 경우 (마지막 집 털 수 X)
    for i in range(1, len(money) - 1):
        dp_1[i] = max(dp_1[i - 1], dp_1[i - 2] + money[i])

    # 첫번째 집을 털지 않았을 경우 초기값
    dp_2[0] = 0

    # 첫번째 집을 털지 않은 경우 (마지막 집 털 수 O)
    for j in range(1, len(money)):
        dp_2[j] = max(dp_2[j - 1], dp_2[j - 2] + money[j])

    # 첫번째 집을 털었을 경우와 마지막 집을 털었을 경우 중 더 큰 값 반환
    return max(dp_1[-2], dp_2[-1])
