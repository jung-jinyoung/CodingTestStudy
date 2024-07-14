def solution(strs, t):
    answer = 0
    # 중복 제거
    strs = set(strs) 
    n = len(t)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        # 최소값 비교를 위해 최대값으로 초기화
        dp[i] = float('inf')
        for k in range(1, 6):
            if i - k < 0:
                s = 0
            else:
                s = i - k
            if t[s:i] in strs:
                dp[i] = min(dp[i], dp[i - k] + 1)
    if dp[-1] == float('inf'):
        return -1
    return dp[-1]
            