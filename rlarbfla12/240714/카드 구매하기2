N = int(input())
number = [0] + list(map(int, input().split()))

# dp[i]는 i개의 카드를 구매하는데 필요한 최소 비용을 저장
dp = [0 for _ in range(N+1)]

for i in range(1, N+1):                     # 1부터 N까지 각 카드 개수 반복
    for k in range(1, i+1):                 # 현재 카드 개수 i에 대해 1부터 i까지의 각 카드 팩 반복
        if dp[i] == 0:
            dp[i] = dp[i-k] + number[k]     # i-k개의 카드를 구매한 비용  + k개의 카드가 포함된 카드 팩의 가격
        else:
            dp[i] = min(dp[i], dp[i-k] + number[k])         # 작은 값 찾기


print(dp[N])
