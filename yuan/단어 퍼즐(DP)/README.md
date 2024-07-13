실패코드
<br/>
---
    발상: 주어진 문자열의 뒷부분을 모든 낱말과 비교, 
        dp 배열에 주어진 낱말 만큼을 뺀 문자열을 다시 넣기

    구현: 주어진 문자열의 뒷부분을 체크해서 
        낱말과 동일한 부분을 슬라이싱 하고
        다음 dp배열에 append 하기 
-
    문제: ```if &% not in dp[idx]: dp[idx].append(&%) ```
        이렇게 풀면 가능한 모든 문자열을 append 하게되면서
        시간이 너무 많이 걸림, 
        not in 정도로는 중복체크가 충분하지 않음 

```python
def solution(strs, t):
    answer = 0
    n = len(t) # 찾을 단어 길이
    dp = [ [] for _ in range(n+1)] 
    # dp[0]에는 t 넣기
    dp[0].append(t)

    # dp[i]에는 dp[i-1] 중에 -strs가 가능한거 넣기
    idx = 1
    while idx < n+1:
        for word in dp[idx-1]:
            for wd in strs:
                len_wd = len(wd) # len_Wd개
                # word랑 같을때 바로 리턴
                if word == wd:
                    return idx
                # word - wd 가 가능한거 넣기
                if word[len(word)-len_wd:] == wd:
                    newword = word[:len(word)-len_wd]
                    if newword not in dp[idx]:
                        dp[idx].append(newword)
                        
            # dp에 추가되는 배열 없으면 리턴 
            if len(dp[idx])<1:
                return -1 
        idx +=1

```
성공 코드
<br/>
---
    1. dp에는 **숫자(횟수) 넣기** 
       특히 dp개념인 **부분합의 합이 최적합** 살리기 


```python
def solution(strs, t):
    n = len(t)
    # 낱말 조합가능 개수 최대 n
    dp = [ (n+1) for _ in range(n+1)]
    dp[0] = 0
    
    # strs 의 낱말을 돌면서 strs의 낱말 길이만큼의 이전 dp[]에 저장된 숫자 +1
    idx = 1 
    while idx < n+1:
        for wd in strs:
            len_wd = len(wd)
            if idx>= len_wd and t[idx-len_wd:idx] == wd:
                dp[idx] = min(dp[idx], dp[idx-len_wd]+1)
        idx+=1
    print(dp)
    #낱말 조합의 최대개수는 n, 더 크면 생성 불가 
    if dp[n] >n:
        dp[n] = -1
    return dp[n]
```

 ### 효율성 극대화 코드


```python
코드 복사
def solution(strs, t):
    n = len(t)
    # dp 배열 초기화, 초기값은 n+1로 설정 (최대 길이 초과 값)
    dp = [n + 1] * (n + 1)
    dp[0] = 0  # 빈 문자열을 만들기 위한 조각 수는 0

    # 각 위치 i에 대해 반복
    for i in range(1, n + 1):
        # 단어 조각의 길이는 최대 5이므로, 시작 위치 j 설정
        start = max(0, i - 5)
        # j부터 i까지 부분 문자열이 strs에 있는지 확인
        # 0~5만큼 i-j 랑 동일 함  
        for j in range(start, i):
            if dp[j] + 1 < dp[i] and t[j:i] in strs:
                dp[i] = dp[j] + 1

    # 목표 문자열 t를 만들 수 있는 최소 조각 수 반환
    return dp[n] if dp[n] != n + 1 else -1
```