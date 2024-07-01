# 24/07/01 스터디 문제

## 프로그래머스 - 징검다리 건너기

### 1회차 실패
- 정확성 테스트는 다 통과
- 효율성 테스트는 다 실패(시간초과)
- 채점 결과
  - 정확성: 64.1
  - 효율성: 0.0
  - 합계: 64.1 / 100.0

#### 코드

```python
def solution(stones, k):
    # 최대 몇명까지 건널 수 있는가
    # 한 번에 건너뛸 수 있는 디딤돌의 최대 칸 수  = k
    # 징검다리를 1씩 다 감소시키고, 인원수 +1, 0 >=을 발견하면 그 이후의
    # 0의 연속을 확인하여, k와 같거나 크면 중단.
    
    answer = 1  # 건널 수 있는 최대 인원수를 저장할 변수
    # 한명이 건너고 나서 돌을 감소한다고 생각
    while True:
        # 돌 하나씩 감소
        for i in range(len(stones)):
            if stones[i] > 0:
                stones[i] -= 1

        # 연속된 0의 개수 검사
        cnt = 0
        for stone in stones:
            if stone == 0:
                cnt += 1
                if cnt >= k:
                    return answer  # 더 이상 건널 수 없으면 종료
            else:
                cnt = 0  # 연속하지 않으면 초기화

        # 건너간 인원수 증가
        answer += 1
    return answer
```

### 2회차 - 이진탐색(gpt)
- 채점 결과
  - 정확성: 64.1
  - 효율성: 35.9
  - 합계: 100.0 / 100.0

- 주요 아이디어
  - 이진 탐색을 사용해서 가능한 최대 인원을 찾는다.
  - can_cross 함수로 특정 인원이 건널 수 있는지를 확인

#### 예시
돌의 상태가 [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]이고 k가 3인 경우를 예로 들어보겠습니다.

1. 초기 설정: left는 1, right는 5 (돌의 최대 값).

2. 이진 탐색 반복:
    - mid를 3으로 설정하고 can_cross 함수로 확인합니다.
    - 3명은 건널 수 있으므로 answer를 3으로 갱신하고 left를 4로 설정합니다.
    - 다시 mid를 4로 설정하고 확인합니다.
    - 4명은 건널 수 없으므로 right를 3으로 설정합니다.

3. 반복 종료 후, 가능한 최대 인원수인 3을 반환합니다.

이와 같은 방법으로 효율적으로 최대 몇 명이 징검다리를 건널 수 있는지를 계산할 수 있습니다.

#### 코드
```python
def can_cross(stones, k, mid):
    # 주어진 'mid' 인원수가 징검다리를 건널 수 있는지를 판단하는 함수
    count = 0
    for stone in stones:
        if stone < mid:
            # 돌의 값이 'mid'보다 작으면 건널 수 없으므로 count 증가
            count += 1
            if count >= k:
                # 연속된 돌의 값이 'mid'보다 작은 경우가 'k'개 이상이면 건널 수 없음
                return False
        else:
            # 돌의 값이 'mid'보다 크거나 같으면 건널 수 있으므로 count 초기화
            count = 0
    return True  # 모든 돌을 확인했을 때 건널 수 있으면 True 반환

def solution(stones, k):
    # 이진 탐색을 위한 초기 변수 설정
    left, right = 1, max(stones)  # left는 최소 인원, right는 돌의 최대 값
    answer = 0
    
    while left <= right:
        mid = (left + right) // 2  # 현재 중간 값 설정 (건널 수 있는 인원의 후보)
        if can_cross(stones, k, mid):
            # 'mid' 인원수가 건널 수 있으면 answer 갱신
            answer = mid
            left = mid + 1  # 더 큰 인원수를 확인하기 위해 left 이동
        else:
            right = mid - 1  # 건널 수 없으면 더 작은 인원수를 확인하기 위해 right 이동
    
    return answer  # 가능한 최대 인원수 반환
```

#### can_cross 함수
1. 돌 하나하나를 확인합니다.

2. 돌의 값이 mid보다 작으면 건널 수 없다고 판단하고 count를 증가시킵니다.

3. count가 k 이상이면 연속으로 건널 수 없는 돌이 k개 이상이므로 False를 반환합니다.

4. 모든 돌을 확인한 후, 건널 수 있으면 True를 반환합니다.


#### solution 함수
1. left와 right 설정: 가능한 최소 인원수는 1이고, 최대 인원수는 돌의 최대 값으로 설정합니다.

2. 이진 탐색 반복:
    - mid를 현재 중간 값으로 설정합니다.
    - can_cross 함수를 사용해서 mid 인원수가 건널 수 있는지를 확인합니다.
    - 건널 수 있으면, answer를 mid로 갱신하고 더 많은 인원수를 확인하기 위해 left를 증가시킵니다.
    - 건널 수 없으면, 더 적은 인원수를 확인하기 위해 right를 감소시킵니다.

3. 반복 종료 후: 가능한 최대 인원수를 answer에 저장하고 반환합니다.

---

<br>

## 프로그래머스 - 기둥과 보 설치

### gpt로 정답 확인 후 이해

#### 접근법 및 느낀점
- 하나의 코드에서 반복문과 조건문을 통해 해결하려고 함
- 함수를 나누어서 해결하는게 더 쉽다는걸 느낌
  - 함수로 나누는 과정이 어려움
  - 각 함수별로 단계적으로 조건 수행 후 결론 도출 하는 로직을 구현하는게 아직 미숙함

#### 코드
```python
# 기둥과 보의 설치 조건 확인 함수
def can_build_pillar(x, y, pillars, beams):
    # 기둥 설치 조건
    # 1. 바닥 위에 있거나
    # 2. 다른 기둥 위에 있거나
    # 3. 보의 한쪽 끝 부분 위에 있거나
    return y == 0 or (x, y - 1) in pillars or (x, y) in beams or (x - 1, y) in beams

def can_build_beam(x, y, pillars, beams):
    # 보 설치 조건
    # 1. 한쪽 끝 부분이 기둥 위에 있거나
    # 2. 양쪽 끝 부분이 다른 보와 동시에 연결되어 있거나
    return (x, y - 1) in pillars or (x + 1, y - 1) in pillars or ((x - 1, y) in beams and (x + 1, y) in beams)


# 현재 구조물이 유효한지 확인하는 함수
def is_valid_structure(pillars, beams):
    # 모든 기둥과 보가 유효한지 확인하는 함수
    for x, y in pillars:
        if not can_build_pillar(x, y, pillars, beams):
            return False
    for x, y in beams:
        if not can_build_beam(x, y, pillars, beams):
            return False
    return True


# 명령어 처리 및 최종 구조물 반환 함수
def solution(n, build_frame):
    pillars = set()  # 기둥을 저장할 집합
    beams = set()    # 보를 저장할 집합
    
    for x, y, a, b in build_frame:
        if b == 1:  # 설치
            if a == 0:  # 기둥 설치
                if can_build_pillar(x, y, pillars, beams):
                    pillars.add((x, y))
            else:  # 보 설치
                if can_build_beam(x, y, pillars, beams):
                    beams.add((x, y))
        else:  # 삭제
            if a == 0:  # 기둥 삭제
                pillars.remove((x, y))
                if not is_valid_structure(pillars, beams):
                    pillars.add((x, y))  # 삭제가 불가능하면 다시 추가
            else:  # 보 삭제
                beams.remove((x, y))
                if not is_valid_structure(pillars, beams):
                    beams.add((x, y))  # 삭제가 불가능하면 다시 추가
    
    # 최종 구조물을 정렬하여 리스트로 반환
    answer = []
    for x, y in sorted(pillars):
        answer.append([x, y, 0])
    for x, y in sorted(beams):
        answer.append([x, y, 1])
    # 정렬 기준: x 좌표 -> y 좌표 -> 구조물 종류 (기둥 먼저, 보 나중)
    answer.sort()
    return answer

```

---

<br>

## 프로그래머스 - 파괴되지 않은 건물
- 느낀점: 효율성에 대한 문제를 더 생각하고 효과적인 알고리즘에 대한 방법에 대한 경험이 더 필요하다고 느낌.


### 처음 코드
- 체점 결과
  - 정확성: 53.8 (테케 다 맞음)
  - 효율성: 0.0 (다 시간초과)
  - 합계: 53.8 / 100.0
  - 
```python
def solution(board, skill):
    i = len(board)  # 세로 길이
    j = len(board[0])   # 가로 길이
    # 누적합을 저장할 change 배열
    change = [[0]*(j+1) for _ in range(i+1)]
 
    for type, x1, y1, x2, y2, degree in skill:
        if type == 1:  # 공격
            degree = -degree
        for k in range(x1, x2+1):
            for l in range(y1, y2+1):
                board[k][l] += degree

    # 파괴되지 않은 건물 수 세기
    answer = 0
    for p in range(i):
        for q in range(j):
            if board[p][q] > 0:
                answer += 1
    return answer
```



### gpt 코드 - 누적합 사용

```python
def solution(board, skill):
    n = len(board)
    m = len(board[0])
    change = [[0] * (m + 1) for _ in range(n + 1)]
    
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree = -degree
        change[r1][c1] += degree
        change[r1][c2 + 1] -= degree
        change[r2 + 1][c1] -= degree
        change[r2 + 1][c2 + 1] += degree

    # 가로 누적합 계산
    for i in range(n):
        for j in range(1, m):
            change[i][j] += change[i][j - 1]
    
    # 세로 누적합 계산
    for j in range(m):
        for i in range(1, n):
            change[i][j] += change[i - 1][j]
    
    for i in range(n):
        for j in range(m):
            board[i][j] += change[i][j]
    
    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] > 0:
                answer += 1
    
    return answer
```


### 누적합에 대한 예시

예를 들어, `board`가 다음과 같다고 가정합시다.

```python
board = [
    [5, 5, 5, 5],
    [5, 5, 5, 5],
    [5, 5, 5, 5],
    [5, 5, 5, 5]
]
```

그리고 주어진 `skill`이 다음과 같다고 합시다.

```python
skill = [
    [1, 0, 0, 2, 2, 2]  # (0,0)부터 (2,2)까지의 영역을 공격하여 각 칸의 값을 2씩 감소시킴
]
```

### 변화량 배열 초기화

변화량을 기록할 `change` 배열을 `(n+1) x (m+1)` 크기로 초기화합니다.

```python
change = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
```

### 스킬 적용

`skill`에 주어진 공격을 `change` 배열에 반영합니다. 공격(`type == 1`)이므로 `degree`를 음수로 바꿔서 `-2`를 적용합니다.

```python
# 공격을 적용하여 변화량 배열에 값 추가
change[0][0] += -2      # 시작 지점에 -2를 더합니다.
change[0][2 + 1] -= -2  # (0, 3)에 2를 뺍니다.
change[2 + 1][0] -= -2  # (3, 0)에 2를 뺍니다.
change[2 + 1][2 + 1] += -2  # (3, 3)에 -2를 더합니다.
```

변화량 배열은 다음과 같습니다.

```python
change = [
    [-2, 0, 0, 2, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [2, 0, 0, -2, 0],
    [0, 0, 0, 0, 0]
]
```

### 누적 합 계산

이제 변화량 배열의 누적 합을 계산하여 실제 변화량을 반영합니다.

1. 가로 방향 누적 합 계산

```python
for i in range(n):
    for j in range(1, m):
        change[i][j] += change[i][j - 1]

# 가로 누적 합 결과
change = [
    [-2, -2, -2, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [2, 2, 2, 0, 0],
    [0, 0, 0, 0, 0]
]
```

2. 세로 방향 누적 합 계산

```python
for j in range(m):
    for i in range(1, n):
        change[i][j] += change[i - 1][j]

# 세로 누적 합 결과
change = [
    [-2, -2, -2, 0, 0],
    [-2, -2, -2, 0, 0],
    [-2, -2, -2, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
```

### 변화량을 실제 `board`에 반영

최종적으로 변화량 배열을 이용하여 `board` 배열을 갱신합니다.

```python
for i in range(n):
    for j in range(m):
        board[i][j] += change[i][j]

# 최종 결과
board = [
    [3, 3, 3, 5],
    [3, 3, 3, 5],
    [3, 3, 3, 5],
    [5, 5, 5, 5]
]
```

### 설명 요약

1. **변화량 배열에 값 추가**:
   - `change[r1][c1] += degree`: 시작 지점에 `degree`를 더합니다.
   - `change[r1][c2 + 1] -= degree`: 행의 끝 다음 지점에 `degree`를 뺍니다.
   - `change[r2 + 1][c1] -= degree`: 열의 끝 다음 지점에 `degree`를 뺍니다.
   - `change[r2 + 1][c2 + 1] += degree`: 대각선 방향으로 끝 다음 지점에 `degree`를 더합니다.

2. **누적 합 계산**:
   - 가로 방향과 세로 방향으로 누적 합을 계산하여 변화량을 반영합니다.

3. **변화량을 실제 `board`에 반영**:
   - 최종적으로 변화량을 `board`에 반영하여 최종 상태를 계산합니다.

이와 같이, 변화량 배열을 이용하여 특정 구간에 대한 변화를 효율적으로 적용할 수 있습니다.