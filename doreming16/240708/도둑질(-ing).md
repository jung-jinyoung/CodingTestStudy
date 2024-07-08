# 도둑질

## 1차 시도

[현재 도착한 집 idx - 2] 지점과 한 값과 직전 값([idx-1])비교해서 더 큰 값 구하기

```python
# tc 10개 중 4개 통과
# 3 5 8 9 통과

def solution(money):
    n = len(money)
    dp = [0] * (n)

    for i in range(n):
        dp[i] = max(dp[i-2] + money[i], dp[i-1])
    answer = max(dp)
    return answer
```

## 2차 시도

```python
# 1 2 4 5 7 10 통과
# ????

# 첫번째 집, 마지막 집이 접하는 경우 제외 시도

def solution(money):
    n = len(money)
    dp = [0] * (n)

    for i in range(n):
        dp[i] = max(dp[i-2] + money[i], dp[i-1])
    answer = max(dp[n-2], dp[n-1]-(min(money[0], money[n-1])))
    return answer
```

ㅠㅠ
