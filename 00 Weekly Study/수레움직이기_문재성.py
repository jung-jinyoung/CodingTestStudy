from collections import deque
from copy import deepcopy

def solution(maze):
    N = len(maze)  # 미로의 행 개수
    M = len(maze[0])  # 미로의 열 개수
    
    # 방문 상태를 추적하기 위한 배열 초기화
    visited_red = [[0]*M for _ in range(N)]
    visited_blue = [[0]*M for _ in range(N)]
    q = deque()
    
    # 미로를 순회하며 초기 상태와 목표 지점 설정
    for i in range(N):
        for j in range(M):
            if maze[i][j] == 5:
                visited_red[i][j] = 1  # 벽은 두 색 모두 방문한 것으로 표시
                visited_blue[i][j] = 1
            elif maze[i][j] == 1:
                red_now = (i, j)  # 빨간색의 초기 위치
                visited_red[i][j] = 1
            elif maze[i][j] == 2:
                blue_now = (i, j)  # 파란색의 초기 위치
                visited_blue[i][j] = 1
            elif maze[i][j] == 3:
                red_goal = (i, j)  # 빨간색의 목표 지점
            elif maze[i][j] == 4:
                blue_goal = (i, j)  # 파란색의 목표 지점

    # 초기 상태를 큐에 추가
    q.append((red_now, blue_now, visited_red, visited_blue, 0))
    # 이동 방향 설정 (오른쪽, 왼쪽, 아래, 위)
    delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while q:
        (red_i, red_j), (blue_i, blue_j), v_r, v_b, cnt = q.popleft()
        red_finished, blue_finished = False, False
        
        if (red_i, red_j) == red_goal:
            red_finished = True  # 빨간색이 목표 지점에 도달
        if (blue_i, blue_j) == blue_goal:
            blue_finished = True  # 파란색이 목표 지점에 도달
        
        if red_finished and blue_finished:
            return cnt  # 둘 다 목표 지점에 도달했을 때 이동 횟수 반환
        elif red_finished and not blue_finished:
            # 빨간색이 목표 지점에 도달했지만 파란색은 도달하지 못했을 때
            for ai, aj in delta:
                blue_ni, blue_nj = blue_i + ai, blue_j + aj
                if 0 <= blue_ni < N and 0 <= blue_nj < M:
                    if not v_b[blue_ni][blue_nj] and (blue_ni, blue_nj) != (red_i, red_j):  # 파란색이 빨간색 위치로 이동하지 않도록
                        new_v_b = deepcopy(v_b)
                        new_v_b[blue_ni][blue_nj] = 1
                        q.append(((red_i, red_j), (blue_ni, blue_nj), deepcopy(v_r), new_v_b, cnt+1))
        elif blue_finished and not red_finished:
            # 파란색이 목표 지점에 도달했지만 빨간색은 도달하지 못했을 때
            for bi, bj in delta:
                red_ni, red_nj = red_i + bi, red_j + bj
                if 0 <= red_ni < N and 0 <= red_nj < M:
                    if not v_r[red_ni][red_nj] and (red_ni, red_nj) != (blue_i, blue_j):  # 빨간색이 파란색 위치로 이동하지 않도록
                        new_v_r = deepcopy(v_r)
                        new_v_r[red_ni][red_nj] = 1
                        q.append(((red_ni, red_nj), (blue_i, blue_j), new_v_r, deepcopy(v_b), cnt+1))
        elif not blue_finished and not red_finished:
            # 둘 다 목표 지점에 도달하지 못했을 때
            for ci, cj in delta:
                red_ni, red_nj = red_i + ci, red_j + cj
                if 0 <= red_ni < N and 0 <= red_nj < M:
                    if not v_r[red_ni][red_nj]:
                        for di, dj in delta:
                            blue_ni, blue_nj = blue_i + di, blue_j + dj
                            if 0 <= blue_ni < N and 0 <= blue_nj < M:
                                if not v_b[blue_ni][blue_nj]:
                                    if (blue_ni, blue_nj) != (red_ni, red_nj):  # 두 수레가 같은 칸에 있지 않도록
                                        if not ((blue_ni, blue_nj) == (red_i, red_j) and (red_ni, red_nj) == (blue_i, blue_j)):  # 두 수레가 자리를 바꾸지 않도록
                                            new_v_r = deepcopy(v_r)
                                            new_v_r[red_ni][red_nj] = 1
                                            new_v_b = deepcopy(v_b)
                                            new_v_b[blue_ni][blue_nj] = 1
                                            q.append(((red_ni, red_nj), (blue_ni, blue_nj), new_v_r, new_v_b, cnt+1))
    return 0  # 두 색 모두 목표 지점에 도달할 수 없을 때
