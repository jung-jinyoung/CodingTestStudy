def solution(money):
    n = len(money)# 집의 수
    
    # 첫 번째 집을 터는 경우
    dp1 = [0] * n
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1]) #첫번째 집과 두번째 집 중 더 많은 돈을 가지는 경우
    
    for i in range(2, n - 1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])
    
    # 첫 번째 집을 털지 않는 경우
    dp2 = [0] * n
    dp2[1] = money[1]
    
    for i in range(2, n):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
    
    return max(dp1[n-2], dp2[n-1])

# 예제 테스트
print(solution([1, 2, 3, 1]))  # 4
print(solution([91, 90, 5, 7, 5, 7]))  # 104