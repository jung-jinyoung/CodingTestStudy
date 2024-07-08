'''
덧셈 뒤에 나오는 수가 가장 커야하고 뺄셈 뒤에 나오는 수는 가장 작아야함

maxDP 와 minDP 를 둘 다 구해야함
minDP를 구하는 이유
식 X = 식 A - 식 B
식 X 의 최댓값 = 식 A 의 최댓값 - 식 B 의 최솟값
'''

# arr = ["5", "-", "3", "+", "1", "+", "2", "-", "4"]

def solution(arr):
    # 숫자도 문자열로 주어지기 때문에 숫자로 바꿔준다.
    for i, element in enumerate(arr):
        if i % 2 == 0:
            arr[i] = int(element)

    n = len(arr)
    max_dp = [[0 for i in range(n)] for j in range(n)]
    min_dp = [[0 for i in range(n)] for j in range(n)]
    # dp[i][j] = 인덱스 i~j 식의 최댓값 또는 최솟값

    for i in range(0, n, 2):
        # max_dp, min_dp 갱신
        max_dp[i][i] = arr[i]
        min_dp[i][i] = arr[i]
    
    for x in range(3, n+1, 2):
        # 시작점
        for left in range(0, n, 2):
            # 끝점
            right = x + left - 1
            # 범위 제한
            if right >= n:
                break
            candidates_max, candidates_min = [], []
            for operator in range(left+1, right, 2):
                if arr[operator] == "+":
                    candidates_max.append(max_dp[left][operator-1] + max_dp[operator+1][right])
                    candidates_min.append(min_dp[left][operator-1] + min_dp[operator+1][right])
                elif arr[operator] == '-':
                    candidates_max.append(max_dp[left][operator-1] - min_dp[operator+1][right])
                    candidates_min.append(min_dp[left][operator-1] - max_dp[operator+1][right])
            max_dp[left][right] = max(candidates_max)
            min_dp[left][right] = min(candidates_min)

    return max_dp[0][-1]



