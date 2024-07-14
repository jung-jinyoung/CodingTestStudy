~ 240714

백준 그룹 [DP 기초] 문제집 풀기
https://www.acmicpc.net/group/workbook/view/20735/70521

<br>

## 1699. 제곱수의 합

https://www.acmicpc.net/problem/1699

### 통과코드

```python
import sys
input = sys.stdin.readline
n = int(input())

dp = [num for num in range(n+1)]

for i in range(1, n+1):

    # sqrt 처리하는 부분
    if int(i ** 0.5) == i ** 0.5:
        dp[i] = 1

    else:
        for j in range(1, int(i**0.5)+1):
            dp[i] = min(dp[i - j ** 2], dp[i])
        dp[i] += 1

print(dp[n])
```

```python
# sqrt 써도 통과되나 싶어서 다른 풀이 찾아봄
import math
import sys
input = sys.stdin.readline

n = int(sys.stdin.readline())

dp = [num for num in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, int(math.sqrt(i) + 1)):
        if dp[i] > (dp[i - j * j] + 1):
            dp[i] = dp[i - j * j] + 1

print(dp[n])
```

### 시간초과

테케는 맞는데 시간초과 뜸

```python
import sys
input = sys.stdin.readline
n = int(input())

dp = [num for num in range(n+1)]
# 어떤 제곱수를 더해올 수 있는지 저장
# 1+1+1+1+1... 인 max 상태에서 줄여나가기

# dp[4] 부터 어떻게 저장할지?
# sqrt ?

# 더해지는 범위
# n = 1 ~ 3 : 1 ,1+1, 1+1+1
# n = 4 ~ 8 : 2*2, +1, +2, .. +4
# n = 9 ~ 12 : 3*3, .. +3
# n = 13 ~ 15 : 2*2 + 3*3, ..
# n = 16 : 4*4
# -> 거꾸로 생각해서 찾아가기 [10 = 3*3 + 1] -> [1 = 10 - 3*3]

for i in range(1, n+1):
    for j in range(1, i+1):

        if j ** 2 > i:
            break

        else:
            dp[i] = min(dp[i - j ** 2], dp[i])
            dp[i] += 1

print(dp[n])

```

조건 이것저것 다 바꿔보고, 범위 조정도 해보고, 이것저것 고쳐가면서 풀어봤다 -!

<br>
<br>
<br>
