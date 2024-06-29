# 아침 코테 후 . . .

AI 리포트에 있는 Lv.1 문제 하나씩 풀어봤습니다 ,, 기초부족

## 1. 과일 장수

https://school.programmers.co.kr/learn/courses/30/lessons/135808

```python
def solution(k, m, score):
    # m개의 사과 담기

    score.sort(reverse=True)

    profit = 0
    for i in range(0, len(score), m):
        if len(score[i: i+m]) == m:
            profit += min(score[i: i+m]) * m

    return profit
```

## 2. 오픈채팅방

https://school.programmers.co.kr/learn/courses/30/lessons/42888

```python
def solution(record):
    # nickname 바꿔주기
    user_nickname = {}

    for rec in record:
        temp = rec.split()
        if len(temp) == 3:
            user_nickname[temp[1]] = temp[2]

    answer =[]
    for rec in record:
        temp = rec.split()
        if temp[0] == 'Enter':
            answer.append(f"{user_nickname[temp[1]]}님이 들어왔습니다.")
        if temp[0] == 'Leave':
            answer.append(f"{user_nickname[temp[1]]}님이 나갔습니다.")

    return answer
```

## 3. 3 x n 타일링

https://school.programmers.co.kr/learn/courses/30/lessons/12902

규칙은 찾는 법이나 점화식이나 다 가물가물해서 참고함 ^\_ㅠ
https://velog.io/@bjo6300/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-3xn-%ED%83%80%EC%9D%BC%EB%A7%81

```python
def solution(n):
    # DP
    dp = [0] * (n+1)
    dp[2] = 3
    dp[4] = 11

    # dp[n] = dp[n-2] * 3 + (dp[n-4] + dp[n-6] ... + dp[2]) * 2 + 2
    for i in range(6, n+1, 2):
        dp[i] = dp[i-2] * 3
        for j in range(i-4, -1, -2):
            dp[i] += dp[j] * 2

        dp[i] = (dp[i] + 2) % 1000000007
        # // 1,000,000,007

    return dp[n]
```

for문 돌리기 전에

```python
    # 홀수면 못채움
    if n // 2 != 0:
        break
```

이거 했더니 테케 전부 runtime error. 아주 큰 수 2로 나누는 작업 해야돼서 그런듯

## 디스크 컨트롤러 (푸는중)

https://school.programmers.co.kr/learn/courses/30/lessons/42627

```python
def solution(jobs):
    end_time = 0
    stack = []
    min_avg = 1000

    def dfs():



    answer = 0
    return answer
```
