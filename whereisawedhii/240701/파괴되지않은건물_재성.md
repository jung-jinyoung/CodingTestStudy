# 파괴되지 않은 건물 

## 일단 해본 코드 (정확성 통과, 효율성 시간초과)
```python
def solution(board, skill):
    li = len(board)
    lj = len(board[0])
    dict = {}
    for a in range(li):
        for b in range(lj):
            dict[(a, b)] = board[a][b]
    
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            for r in range(r1, r2+1):
                for c in range(c1, c2+1):
                    dict[(r, c)] -= degree
        else:
            for r in range(r1, r2+1):
                for c in range(c1, c2+1):
                    dict[(r, c)] += degree
    
    answer = 0
    print(dict.values())
    for each in dict.values():
        if each > 0:
            answer += 1
    
    return answer
```
- 공이동 시뮬레이션에서 시작과 끝을 기준으로 삼은 것을 적용해야 겠다는 생각은 함
- 정확히 구현하기 힘들어서 도움을 좀 받음

## 누적합 적용 
```python
def solution(board, skill):
    n = len(board)
    m = len(board[0])
    
    # 누적합 배열 초기화
    prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]
    
    # 스킬 적용
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:  # 공격
            degree = -degree
        prefix_sum[r1][c1] += degree
        prefix_sum[r1][c2 + 1] -= degree
        prefix_sum[r2 + 1][c1] -= degree
        prefix_sum[r2 + 1][c2 + 1] += degree
    
    # 행 방향으로 누적합 계산
    for i in range(n):
        for j in range(1, m):
            prefix_sum[i][j] += prefix_sum[i][j - 1]
    
    # 열 방향으로 누적합 계산
    for j in range(m):
        for i in range(1, n):
            prefix_sum[i][j] += prefix_sum[i - 1][j]
    
    # 최종 내구도 계산 및 파괴되지 않은 건물의 개수 계산
    answer = 0
    for i in range(n):
        for j in range(m):
            board[i][j] += prefix_sum[i][j]
            if board[i][j] > 0:
                answer += 1
    
    return answer

```