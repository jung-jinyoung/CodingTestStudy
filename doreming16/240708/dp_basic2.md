240704

# 백준 그룹 [DP 기초] 문제집 풀기
https://www.acmicpc.net/group/workbook/view/20735/70521

## 11052. 카드 구매하기
https://www.acmicpc.net/problem/11052

### 처음에 냅다 쓴 코드
```python
import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

dp = [0] * (n+1)
# dp[i] = 카드 n개 구매할 때 금액 최댓값

# 이전 단계에서 1개만 더 더할 때~ 랑 비교해서 MAX

dp[1] = cards[0]   # 1개 구매 입력

for i in range(2, n+1):
    dp[i] = dp[i-1] + cards[0]  # 그 전 max값에서 1개값만 더 더할 때
    dp[i] = max(dp[i], cards[i-1])

print(dp[n])


# cards[0] * i 개가 제일 비쌀 수도 있잖
### dp에 이미 포함되어있나 ?

```

> 뭔가 이렇게 푸는건가 싶었지만 ,, 아직 감이 완전히 오지 않아서 해설 보고 공부함

> dp를 구하는 한 카드에 대해서, 내가 현재 (마지막으로) 골라져있는 카드까지 가격 최대값 구해나가는 게 핵심

### 통과 코드
```python
import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))

dp = [0] * (n+1)

# i번째 카드에 대해 구함
for i in range(1, n+1):
    # 카드팩 j ( 해당 카드팩 꺼내서 이전 dp 값과 더함! )
    for j in range(1, i+1):
            # 값 비교
                # j 돌면서 만들어진 dp[i] 자신 &
                # 마지막으로 뽑은 카드팩의 가격 cards[j-1]과
                # 마지막으로 뽑은 카드팩 직전의 dp값인 dp[i-j]을 더한 값
                # 을 비교해서 max값 추출
        dp[i] = max(dp[i], cards[j-1] + dp[i-j])

print(dp[n])
```

## 리뷰

- 내가 생각하는 DP 핵심? : <code>현재 위치 파악 / 내 직전까지 더해온 값</code> 파악하고 비교해서 현재 값 구하는 루프를 돌기

- DP랑 친해지고 싶은데 그동안 너무 소홀했다 ,,

- 어렵다고 생각하면 문제가 안풀림. 일단 들이받자