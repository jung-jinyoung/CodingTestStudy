## 성공코드 

<br/>
---
    발상: 완탐.. 

    구현: 할인율과 이모티콘 개수의 가능한 수가 각각 4, 7 로 정해져있으므로
        dfs 를 통해 모든 경우의 수 돌리기 
-
    문제: 2000ms 나온 tc가 하나 있어서 약간 놀램..
    근데 이렇게 푸는거(b-f알고리즘,dfs)맞더라,,

```python
def find(user_lst, rate, cons):
    global maxcnt, maxcost
    user_cnt = 0
    user_cost = 0
    for user in user_lst:
        percentage = user[0] 
        my_maxcost = user[1]  
        
        con_sum = 0 # 구매가능한 이모티콘 합
        for i in range(n): # 이모티콘 개수 
            if percentage <= rate[i]:
                con_sum += cons[i] * (100-rate[i]) // 100
        if con_sum >= my_maxcost:
            user_cnt += 1 # 할인값 이모티콘이 더 크면 플러스 서비스 가입 
        else:
            user_cost += con_sum # 작으면 x 
    # 모든 user 검사한 뒤에 
    if user_cnt >= maxcnt:
        if user_cnt == maxcnt:
            maxcost = max(maxcost, user_cost)
        else:
            maxcost = user_cost
        maxcnt = user_cnt
        
def solution(users, emoticons):
    global maxcnt, maxcost, n
    n = len(emoticons) 
    maxcnt = 0
    maxcost = 0
    answer = [0 for _ in range(n)]
    rate = [10, 20, 30, 40] 
    
    def dfs(lst, i, num, answer): # 반복할 리스트, 시작수, 총 개수     
        if i == num: 
            find(users, answer, emoticons)
            return

        for j in lst: # 10, 20, 30, 40
            answer[i] = j
            dfs(lst, i + 1, num, answer) 
    
    dfs(rate, 0, n, answer)
    return [maxcnt, maxcost]

```



 ### 약간 더 코드 예쁘게 만들어보자면?
<br/>
---
    1. 전역변수 사용 최소화를 위해 find 의 매 값을 return
    2. dfs 내부에서 find의 return 값을 받아 max 값인지 여부 처리하기. 


```python
def find(users, rate, emoticons):
    user_cnt = 0
    user_cost = 0
    for user in users:
        percentage, max_cost = user
        total_cost = 0
        for i in range(len(emoticons)):
            if percentage <= rate[i]:
                total_cost += emoticons[i] * (100 - rate[i]) // 100
        if total_cost >= max_cost:
            user_cnt += 1
        else:
            user_cost += total_cost
    return user_cnt, user_cost

def solution(users, emoticons):
    global maxcnt, maxcost
    n = len(emoticons)
    maxcnt = 0
    maxcost = 0
    answer = [0] * n
    rate = [10, 20, 30, 40]

    def dfs(idx):
        global maxcnt, maxcost
        if idx == n:
            user_cnt, user_cost = find(users, answer, emoticons)
            if user_cnt > maxcnt or (user_cnt == maxcnt and user_cost > maxcost):
                maxcnt = user_cnt
                maxcost = user_cost
            return

        for r in rate:
            answer[idx] = r
            dfs(idx + 1)

    dfs(0)
    return [maxcnt, maxcost]
```
