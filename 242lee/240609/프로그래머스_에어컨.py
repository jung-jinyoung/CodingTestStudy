def solution(temperature, t1, t2, a, b, onboard):
    temperature += 11
    t1 += 11
    t2 += 11
    dp = [[float('inf')] * 53 for _ in range(len(onboard))]

    dp[0][temperature] = 0

    for minute in range(1, len(onboard)):
        if onboard[minute] == 1:  # 사람이 탑승하면
            l, r = t1, t2 + 1
        else:
            l, r = 1, 52

        for temp in range(l, r):
            if temp == temperature:
                dp[minute][temp] = min(dp[minute - 1][temp], dp[minute - 1][temp + 1], dp[minute - 1][temp - 1])
            elif temp > temperature:
                dp[minute][temp] = dp[minute - 1][temp + 1]
            elif temp < temperature:
                dp[minute][temp] = dp[minute - 1][temp - 1]

            dp[minute][temp] = min(
                dp[minute][temp], dp[minute - 1][temp] + b,
                dp[minute - 1][temp - 1] + a, dp[minute - 1][temp + 1] + a
            )

    return min(dp[-1])
