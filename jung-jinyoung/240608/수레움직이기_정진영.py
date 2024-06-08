"""

N x M 크기의 격자 모양의 퍼즈팔
빨간색 수레와 파란색 수레가 하나씩 존재 -> 자신의 도착 칸까지 이동

각 턴마다 모든 수레는 상하좌우 이동
-> 벽이나 격자판 밖으로 이동 X
-> 방문했던 칸 이동 X
-> 같은 칸에 두 수레 위치 X
-> 두 수레가 자리를 바꾸며 움직일 수 없다.

maze 정보
0 빈칸
1 빨간 수레 시작 2 파란 수레 시작
3 빨간 수레 도착 4 파란 수레 도착
5 벽

Q. 퍼즐을 푸는데 필요한 최소 리턴 값을 구하시오. (풀 수 없을 경우 0)
접근 : BFS

2번 테스트 케이스 막힘  / 전체 65% 정답
[[1, 0, 2], [0, 0, 0], [5, 0 ,5], [4, 0, 3]]
"""

from collections import deque
def solution(maze):

    # maza의 길이 구하기
    m, n = len(maze), len(maze[0])

    # 시작/도착 위치 구하기
    start_R, start_B = None, None
    goal_R, goal_B = None, None
    for i in range(m):
        for j in range(n):
            if maze[i][j] == 1:
                start_R = (i,j)
            elif maze[i][j] == 2:
                start_B = (i,j)
            elif maze[i][j] == 3 :
                goal_R = (i,j)
            elif maze[i][j] == 4 :
                goal_B = (i,j)

    # 방향 벡터 (상, 하, 좌, 우)
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    # BFS 초기화
    path = deque()
    visited = set()

    # 방문 표시
    path.append((start_R, start_B,0)) # 각각의 시작점, 현재 turn 횟수
    visited.add((start_R, start_B))

    while path :
        (r_x, r_y), (b_x, b_y), turns = path.popleft()

        # 목표 지점에 도달했는지 확인
        if (r_x, r_y) == goal_R and (b_x, b_y) == goal_B:
            return turns

        # 빨간 수레 이동
        for dx, dy in directions:
            nr_x, nr_y = r_x + dx, r_y + dy

            # 빨간 수레의 이동이 유효한지 확인
            if 0 <= nr_x < m and 0 <= nr_y < n and maze[nr_x][nr_y] != 5 and (nr_x, nr_y) != (b_x, b_y):
                # 파란 수레 이동
                for dx2, dy2 in directions:
                    nb_x, nb_y = b_x + dx2, b_y + dy2

                    # 파란 수레의 이동이 유효한지 확인
                    if 0 <= nb_x < m and 0 <= nb_y < n and maze[nb_x][nb_y] != 5 and (nb_x, nb_y) != (nr_x, nr_y):
                        next_state = ((nr_x, nr_y), (nb_x, nb_y))
                        if next_state not in visited:
                            visited.add(next_state)
                            path.append(((nr_x, nr_y), (nb_x, nb_y), turns + 1))

    # 그 외 퍼즐을 못 풀 경우는 0 리턴
    return 0

# 테스트
# maze = [[1, 4], [0, 0], [2, 3]]
# print(solution(maze))