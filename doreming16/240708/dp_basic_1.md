# DP 공부

저는 .. DP 잘 모르기 때문에 ... 기초부터 하나하나 .... 풀어볼게요 .....

## 1463. 1로 만들기

```python
# GPT한테 DP 기본 개념 좀 알려달라고 하고,
# 해설 보고 다시 풀어보고,
# 이건 그냥 풀이 외움

import sys
input = sys.stdin.readline

n = int(input())

# dp 배열 생성
dp = [0] * (n+1)

# dp[i] = i를 만들기 위해 필요한 최소 연산 횟수

for i in range(2, n+1):
# 2부터 n까지 연산 횟수 최솟값 입력

    # 1을 뺄 때
    dp[i] = dp[i-1] + 1

    # 2로 나눌 때
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
        # 경우 1. 앞의 경우에서 1을 뺀 횟수
        # 경우 2. 2로 나누기 전 숫자의 횟수에 1 더하기
        # -> 그 둘을 비교, 더 작은 값 입력

    # 3으로 나눌 때
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[n])
```

## 11726. 2\*n 타일링

```python
import sys
input = sys.stdin.readline

n = int(input())
# 세로 길이 2, 가로 길이 n 직사각형 채우기

# dp 배열 생성
dp = [0] * 1001
# dp[i] = 가로길이 i인 직사각형 채울 수 있는 방법의 수

# 초기 세팅(점화식 계산할 초기값)
# 그림 그려서 풀어봄
dp[1] = 1
dp[2] = 2
# dp[3] = 3
# dp[4] = 5
# dp[5] = dp[4] + dp[3] --> 규칙

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007
print(dp[n])
```

## 9095. 1+2+3 더하기

```python
import sys
input = sys.stdin.readline


t = int(input())

dp = [0] * 11   # 제시된 n 범위 (0 < n <= 11)
# dp[i] = 각 수를 만들기 위한 최소 방법 수

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(t):
    n = int(input())

    print(dp[n])
```

(런타임에러난버전)

```python
t = int(input())
for _ in range(t):
    n = int(input())

    dp = [0] * (n+1)
    # dp[i] = 각 수를 만들기 위한 최소 방법 수

    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[n])
```

입력 잘받자 범위 잘보자
