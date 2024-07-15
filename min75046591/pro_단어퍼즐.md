# 단어 퍼즐
## 생각한 풀이
- dfs로 조합을 만들어서 최솟값 도출
- 아니면 dp
- gpt의 도움을 받음. dp값 갱신 부분을 생각하지 못함
- float('inf') : 무한대


```python
def solution(strs, t):
    # 목표 단어 길이 + 1 만큼 dp 배열 생성 (무한대로 초기화)
    dp = [float('inf')] * (len(t) + 1)
    dp[0] = 0  # 빈 문자열을 완성하는 데 필요한 조각 수는 0

    # 목표 단어의 각 위치에 대해
    for i in range(1, len(t) + 1):
        # 모든 부분 문자열 검사
        for j in range(i):
            # 부분 문자열이 strs에 포함되어 있는지 확인
            if t[j:i] in strs:
                # dp 값을 갱신
                dp[i] = min(dp[i], dp[j] + 1)
    
    # 목표 단어를 완성할 수 없는 경우 -1 반환
    return dp[-1] if dp[-1] != float('inf') else -1

```

### dfs로 푸는법 

```python
def solution(strs, t):
    memo = {}  # 메모이제이션을 위한 딕셔너리

    def dfs(index):
        if index == len(t):  # 목표 단어의 끝에 도달한 경우
            return 0
        if index in memo:  # 이미 계산된 경우 메모이제이션 값 반환
            return memo[index]

        min_pieces = float('inf')  # 최소 조각 수 초기화. 무한대를 나타냄
        for end in range(index + 1, len(t) + 1):
            if t[index:end] in strs:
                result = dfs(end)
                if result != float('inf'):
                    min_pieces = min(min_pieces, result + 1)

        memo[index] = min_pieces  # 메모이제이션에 저장
        return memo[index]

    result = dfs(0)
    return result if result != float('inf') else -1
```