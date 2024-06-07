delta = ((1, 0), (-1, 0), (0, 1), (0, -1))          # 상하좌우
answer = 100                                        # 촤대 16이지만 넉넉하게

def solution(maze):
    global answer
    N, M = len(maze), len(maze[0])                  # maze배열의 크기 N X M
    for i in range(N):
        for j in range(M):
            if maze[i][j] == 1:
                red_start1, red_start2 = i, j       # red 시작점
            elif maze[i][j] == 2:
                blue_start1, blue_start2 = i, j     # blue 시작점

    move(red_start1, red_start2, blue_start1, blue_start2, maze, [(red_start1, red_start2)],
[(blue_start1, blue_start2)])
    if answer == 100:                               # 두 수레 모두 도착 못하는 경우 => 0 출력
        answer = 1
    return answer - 1                               # 시작 점을 visited에 넣고 시작했으니 뺴준다


def move(ri, rj, bi, bj, maze, visited1, visited2):             #  dfs로 완전탐색
    global answer
    N, M = len(maze), len(maze[0])
    if maze[ri][rj] == 3 and maze[bi][bj] == 4:                 # 수레 모두 운행 종료
        answer = min(answer, max(len(visited1), len(visited2)))
        return
    elif maze[ri][rj] == 3:                                     # red 도착 케이스
        for bdi, bdj in delta:
            bni, bnj = bi + bdi, bj + bdj
            if 0 <= bni < N and 0 <= bnj < M and maze[bni][bnj] != 5 and not (ri == bni and rj == bnj) and (
            bni, bnj) not in visited2:
                visited2.append((bni, bnj))
                move(ri, rj, bni, bnj, maze, visited1, visited2)
                visited2.pop()
    elif maze[bi][bj] == 4:                                     # blue 도착 케이스
        for rdi, rdj in delta:
            rni, rnj = ri + rdi, rj + rdj
            if 0 <= rni < N and 0 <= rnj < M and maze[rni][rnj] != 5 and not (rni == bi and rnj == bj) and (
            rni, rnj) not in visited1:
                visited1.append((rni, rnj))
                move(rni, rnj, bi, bj, maze, visited1, visited2)
                visited1.pop()
    else:                                                       # red,blue 모두 도착 전
        for rdi, rdj in delta:
            rni, rnj = ri + rdi, rj + rdj
            if 0 <= rni < N and 0 <= rnj < M and maze[rni][rnj] != 5 and (rni, rnj) not in visited1:
                for bdi, bdj in delta:
                    bni, bnj = bi + bdi, bj + bdj
                    if 0 <= bni < N and 0 <= bnj < M and maze[bni][bnj] != 5 and (bni, bnj) not in visited2:
                        if rni == bi and rnj == bj and bni == ri and bnj == rj:
                            continue
                        elif rni == bni and rnj == bnj:
                            continue
                        else:
                            visited1.append((rni, rnj))
                            visited2.append((bni, bnj))
                            move(rni, rnj, bni, bnj, maze, visited1, visited2)
                            visited1.pop()
                            visited2.pop()