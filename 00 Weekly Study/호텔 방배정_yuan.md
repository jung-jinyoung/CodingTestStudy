## 성공(비효율)코드

<br/>
---
    발상: 모든 고객에게 차례대로 방 배정해주고 
        방배정이 불가능할 경우 배정가능한 방 찾기

    구현: 방배정 불가시 while문으로 배정가능한 방 찾기
        고객의 방배정 확정되면 처음 배열에 값 바꿔주기
-
    문제: 완탐으로 풀면 반복이 너무 많아서 시간 많이걸림
        

```python
def solution(k, room_number): # 전체 방개수, 고객원하는 방번호 배열
    answer = []
    check_room = [0]* k
    n = len(room_number)
    
    for idx in range(n): # 1번 고객부터 배정
        num = room_number[idx] # 고객이 원하는 방번호 
        if not check_room[num-1]: # 해당 방이 비어있을경우 
            check_room[num-1] = 1
        else: # 현재 방번호인 num 보다 큰 번호중 비어있는 방 찾기
            while check_room[num-1] != 0:
                num+=1
            room_number[idx] = num # 빈방 찾으면 고객 방배정 정정해주기 
            check_room[num-1] = 1 # 해당 방 채워주기
    
    return room_number

```

 ### 효율성 극대화 코드

원하는 방이 이미 이전에 배정된 방인경우,
**동일한 방을 원했던 사람에게 배정된 방을 참고**하면 시간 단축 가능

 ### 실패코드 2 (while문도 시간 초과)
'''
            while num in answer:
                num = answer[num] # 이미 배정된 방은 계속 value로 바꿔주기
                answer[num]=num+1 
'''
1) new_num = answer[num], answer[new_num] = num+1같이 중간 갱신해줘야함
2) 처음 넣었던 수(room_number[idx]) 도 num으로 딕셔너리에서 갱신해줘야함 
3) 여기서 answer[num]을 넣고 다시 num찾으면 있음-> while문 무한 반복

```python
import sys
sys.setrecursionlimit(100000000)

def solution(k, room_number): # 전체 방개수, 고객원하는 방번호 배열
    answer = {} # {key는 방배정결과, value는 찾기시작할 수} 넣을 딕셔너리 
    n = len(room_number)
    
    for idx in range(n): # 1번 고객부터 배정
        num = room_number[idx] # 고객이 원하는 방번호 
        if num not in answer: # num 차지한 사람 없을 경우  
            answer[num] = num+1 # 고객에게 num 배정, 다음은 num+1부터찾음
            
        else: # 현재 방번호인 num 보다 큰 번호중 비어있는 방 찾기
            while num in answer:
                num = answer[num] # 이미 배정된 방은 계속 value로 바꿔주기
                answer[num]=num+1 
    
    res = list(answer)
    
    return res
```


 ### 성공코드
 **딕셔너리안의 모든 수를 최신값으로 갱신해줄수 있어야함**

```python
import sys
sys.setrecursionlimit(100000000)

def find_room(n, answer):
    if n not in answer:
        answer[n] = n+1
        return n  
    
    room = find_room(answer[n],answer) # 최종 room 찾기 
    answer[n] = room+1 # 최신값이 갱신될때마다 주어진 n의 value값을 갱신해줘야함 
    return room 


def solution(k, room_number): # 전체 방개수, 고객원하는 방번호 배열
    answer = {} # {key는 방배정결과, value는 찾기시작할 수} 넣을 딕셔너리 
    res = []
    
    for room_num in room_number:
        n = find_room(room_num, answer) # 원하는 방, 찾을 딕셔너리
        res.append(n)

    return res
```


### 실패코드 2 고치다가 알아낸 문제점 

     대강 고치는데는 성공했으나 효율성에서 4문제 시간초과남
     차이는 while문으로 인해 반복 과정에서 갱신할수는 없음
     -> 중간과정의 딕셔너리 값이 업데이트가 안됨.

     
    예를들어 134131 의 마지막 1 은
     {1:3}, {3:6} 을 거쳐 6로 고정되고 {6:7} 이 새로 딕셔너리에 등록됨
     ![alt text](image.png)
     여기에서 {1:7}, {3:7} 로 모두 업데이트 해주는 과정이 필요
    그러나 **거치는 수가 3개 이상**이 될경우에 가운데 수는 while문에 의해 거쳐가기만 하고 업데이트가 안되는 문제가 생김, 이경우에 효율성이 빵꾸남


```python
import sys
sys.setrecursionlimit(100000000)

def solution(k, room_number): # 전체 방개수, 고객원하는 방번호 배열
    answer = {} # {key는 방배정결과, value는 찾기시작할 수} 넣을 딕셔너리 
    res = []
    n = len(room_number)
        
    for idx in range(n): # 1번 고객부터 배정
        num = room_number[idx] # 고객이 원하는 방번호 
        if num not in answer: # num 차지한 사람 없을 경우  
            answer[num] = num+1 # 고객에게 num 배정, 다음은 num+1부터찾음
            res.append(num)
            
        else: # 현재 방번호인 num 보다 큰 번호중 비어있는 방 찾기
            while num in answer:
                num = answer[num] # 이미 배정된 방은 계속 value로 바꿔주기
            res.append(num)
            answer[num] = num+1 # 갱신값 넣어주기
            answer[room_number[idx]]=num+1 #초기값도 갱신해주기
    
    
    return res
```
