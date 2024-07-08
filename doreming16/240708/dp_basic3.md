# 백준 그룹 [DP 기초] 문제집 풀기
240705 ~ 240708

https://www.acmicpc.net/group/workbook/view/20735/70521

<br>

## 16194. 카드 구매하기2

https://www.acmicpc.net/problem/16194

### 통과코드

```python
# 최소로 구매

import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

# dp = [0] * (n+1)
# dp[0] = cards[0]

# 결과로 0만 나옴; min값 -> 이미 입력된 cards 값으로부터 시작해야함
dp = [0] + cards[:]

for i in range(1, n+1):
    for j in range(1, i+1):
        # dp[i] = cards[i-1]
        dp[i] = min(dp[i], cards[j-1] + dp[i-j])
                                    # dp[i-j-1] 이렇게 해서 자꾸 이상한 값 나왔음

print(dp[n])
```

dp 초기 입력 상태, for문 돌 때 값 이상해지는 거 잘 고쳤다 ~~

<br>
<br>
<br>

## 10844. 쉬운 계단 수

https://www.acmicpc.net/problem/10844

### 도전중

```python
# 계단수 : 인접한 모든 자리의 차이가 1 (45656)

# n = 1 -> answer = 9
# 1 2 3 4 5 6 7 8 9

# n = 2 -> answer = 17
# 12 23 34 45 56 67 78 89
# 10 21 32 43 54 65 76 87 98

# n = 3 ->
# 121 232 343 454 565 676 787 898     // 9일 때 하나 빠짐
# 123 234 345 456 567 678 789
# 212 323 434 545 656 767 878 989     // 1일 때 하나 빠짐
# 210 321 432 543 654 765 876 987

# 이걸 어떻게 dp로..??????????
# 방법 고민
# 1. 저 숫자들을 다 돌려야하나? -> cnt 말도 안될듯
# 2. 1~9까지 각각 경우의 수를 구했고, 그 경우에 더해감?
# >> 어떤 기준으로?
```

진짜 한참 고민했는데 구현하는 법을 모르겠어서 검색해봤다.
<br>
<br>
2차원 배열로도 DP를 쓸 수 있다는 힌트만 얻고 다시 풀어봄..! 애초에 어떤 종류의 배열을 만들지, 그런 것에 집중하는 것보다 어떤 알고리즘을 어떻게 왜 쓰는건지 먼저 생각해봐야겠음^\_ ㅠ

### 통과코드

```python
import sys
input = sys.stdin.readline

n = int(input())

# 2차원 배열 생성
dp = [[0] * 10 for _ in range(n+1)]

# n=1일 때 경우의 수 1 초기값으로 입력
for num in range(1, 10):
    dp[1][num] += 1

for i in range(2, n+1):  # 인덱스 조심
    for j in range(10):  # 0~9 각각 조건 탐색
        # 1~8일 때 : 앞뒤로 각각 +1, -1 가능
        if 1 <= j <= 8:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        # 0일 때 - 앞에 1만 가능
        elif j == 0:
            dp[i][j] = dp[i-1][1]
        # 9일 때 - 앞에 8만 가능
        elif j == 9:
            dp[i][j] = dp[i-1][8]

print(sum(dp[n]) % 1000000000)
```

## 15990. 1, 2, 3 더하기 5

https://www.acmicpc.net/problem/15990

### 도전중

```python
import sys
input = sys.stdin.readline

t = int(input())
for tc in range(t):
    n = int(input())

    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 2

'''
연속 사용 안됨
n = 1
1

n = 2
2

n = 3
1 2    -> n = 2 경우 * 1
2 1
3      -> 그냥.. 혼자 경우 -- n = 0 경우 + ?

n = 4
1 2 1  -> n = 1 경우 * 1
1 3    -> n = 3 경우 * 2(자리바꾸기)
3 1

n = 5
2 1 2  ->
1 3 1  -> n = 4 경우 * 1
2 3
3 2

n = 6
1 2 1 2
1 2 3
1 3 2
2 1 3
2 1 2 1
2 3 1
3 1 2
3 2 1
'''
```

### 통과코드
- 또 2차원배열 !
- 규칙 공부
```python
import sys
input = sys.stdin.readline

# 2차원 배열 생성
# dp[i] = 각 자릿수 i마다, 마지막 더하는 수가 각각 (1, 2, 3)인 경우의 수
dp = [[0] * 3 for _ in range(100001)]

dp[1] = [1, 0, 0]   # 1
dp[2] = [0, 1, 0]   # 2
dp[3] = [1, 1, 1]   # 1 2 / 3 / 2 1

for i in range(4, 100001):

    # 마지막 더해지는 수가
    # 1일 때
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % 1000000009
    # 2일 때
    dp[i][1] = (dp[i-2][0] + dp[i-2][2]) % 1000000009
    # 3일 때
    dp[i][2] = (dp[i-3][0] + dp[i-3][1]) % 1000000009

t = int(input())
for tc in range(t):
    n = int(input())
    print(sum(dp[n]) % 1000000009)


# ------------------------------------------ #

#           내가 이해한 내용 추가 설명         #

# i마다, 추가할 수 있는 마지막 자리 수는 해당 수(i)가 아니어야함
# ex) 그 전 수가 (1+2) 였으면
# 다음 단계에서 연결될 수 있는 경우로 (1+2+2)는 안됨. 1, 3만 뒤에 붙을 수 있음
# 1이 붙을 수 있는 건 [i-1] : (1+2)+1
# 3이 붙을 수 있는 건 [i-3] : (1+2)+3
# 이걸 거꾸로 생각해서 계산하고 dp에 입력해보기

# ------------------------------------------ #

```

## 1912. 연속합

https://www.acmicpc.net/problem/1912


### 도전중

```python

```
