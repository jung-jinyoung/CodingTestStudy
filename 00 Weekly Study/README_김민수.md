## 수레 문제

>n x m 크기 격자 모양의 퍼즐판  
빨간색 수레와 파란색 수레를 각 자신의 도착칸에 도착해야함  
각 턴마다 반드시 모든 수레를 상하좌우로 인접한 칸 중 한 칸으로 움직여야함  
벽이나 격자 판 밖 x  
방문했던 칸 x  
도착 칸에 위치한 수레는 움직일 수 없음. 해당 칸에 고정  
동시에 두 수레를 같은 칸으로 움직일 수 없음  
>수레끼리 자리 바꾸기 못함  

```python
# 20개중 5개 정답

from collections import deque

def solution(maze):
    n = len(maze)
    m = len(maze[0])
    
    # 방향 벡터 정의 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 시작 지점과 도착 지점 찾기
    red_start = blue_start = red_goal = blue_goal = None
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                red_start = (i, j)
            elif maze[i][j] == 2:
                blue_start = (i, j)
            elif maze[i][j] == 3:
                red_goal = (i, j)
            elif maze[i][j] == 4:
                blue_goal = (i, j)
    
    # BFS 초기화
    queue = deque([(red_start, blue_start, 0)])
    visited = set()
    visited.add((red_start, blue_start))
    
    while queue:
        red_pos, blue_pos, turns = queue.popleft()
        
        # 두 수레가 모두 도착 지점에 도착했는지 확인
        if red_pos == red_goal and blue_pos == blue_goal:
            return turns
        
        for dr, dc in directions:
            new_red_pos = (red_pos[0] + dr, red_pos[1] + dc)
            new_blue_pos = (blue_pos[0] + dr, blue_pos[1] + dc)
            
            # 빨간 수레 이동 가능 여부 체크
            if not (0 <= new_red_pos[0] < n and 0 <= new_red_pos[1] < m and maze[new_red_pos[0]][new_red_pos[1]] != 5):
                new_red_pos = red_pos
            
            # 파란 수레 이동 가능 여부 체크
            if not (0 <= new_blue_pos[0] < n and 0 <= new_blue_pos[1] < m and maze[new_blue_pos[0]][new_blue_pos[1]] != 5):
                new_blue_pos = blue_pos
            
            # 두 수레가 같은 칸에 도달하는 경우를 방지
            if new_red_pos != new_blue_pos and (new_red_pos, new_blue_pos) not in visited:
                visited.add((new_red_pos, new_blue_pos))
                queue.append((new_red_pos, new_blue_pos, turns + 1))
    
    return 0

```


<br>


## 에어컨 문제

>실내공조 제어 시스템은 승객이 탑승 중일 때 항상
t1 ~ t2 실내 온도를 유지할 수 있도록 함.  
현재(0분) 실내온도는 실외온도와 같다.  
실내공조 제어 시스템은 실내온도를 조절하기 위해 에어컨의 전원을 켜 희망온도를 설정
>희망온도는 에어컨의 전원이 켜져 있는 동안 원하는 값으로 변경할 수 있음

```python
# 20개중 3개 맞음

def solution(temperature, t1, t2, a, b, onboard):
    # 현재 온도를 나타내는 변수
    current_temp = temperature
    # 현재 시점에서 최소 소비전력을 나타내는 변수
    total_power = 0
    # 에어컨의 상태를 나타내는 변수 (True: 켜짐, False: 꺼짐)
    ac_on = False
    # 희망 온도를 나타내는 변수
    target_temp = None

    for i in range(len(onboard)):
        if onboard[i] == 1:  # 승객이 탑승 중인 시간
            if not ac_on:  # 에어컨이 꺼져 있으면 켬
                ac_on = True
                # 희망온도를 쾌적한 범위의 중앙값으로 설정
                target_temp = (t1 + t2) // 2
            
            # 현재 온도가 쾌적한 범위 안에 있지 않으면 에어컨을 이용하여 맞춤
            if current_temp < t1:
                total_power += a
                current_temp += 1
            elif current_temp > t2:
                total_power += a
                current_temp -= 1
            else:
                total_power += b
        else:  # 승객이 탑승 중이 아닌 시간
            if ac_on:  # 에어컨이 켜져 있으면 끔
                ac_on = False
            
            # 현재 온도가 실외온도로 1도 변화
            if current_temp < temperature:
                current_temp += 1
            elif current_temp > temperature:
                current_temp -= 1

    return total_power
```