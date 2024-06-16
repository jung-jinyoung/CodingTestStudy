dir = ((0,1),(0,-1),(1,0),(-1,0))
min_move = 16 #최소 이동횟수

def solution(maze):
    row, col = len(maze), len(maze[0])
    rs, bs = find_start(row, col, maze) #수레시작점 찾기
    dfs(maze, rs, bs, [],[])

    if min_move == 16: #수레들 도착시키지 못하면 0반환
        return 0
    return min_move #정상 도착하면 최소 이동수 반환
def dfs(maze, r_pos, b_pos, r_visited, b_visited): # (미로，빨강위치, 파랑위치, 빨강방문기록，파랑방문기록)
    global min_move
    ri, rj = r_pos
    bi, bj = b_pos
    if maze[ri][rj]==3 and maze[bi][bj]==4: #두 수레 모두 도착한 경우
        move = max(len(r_visited), len(b_visited)) #이동횟수
        min_move = min(min_move, move) #최소 이동횟수 초기화
        return

    if maze[ri][rj] == 3: #빨간수레만 도착한 경우
        for b_di, b_dj in dir:
            b_ni, b_nj = bi+b_di, bj+b_dj
            if 0<=b_ni<len(maze) and 0<=b_nj<len(maze[0]) and maze[b_ni][b_nj] != 5: #정상범위 and 벽아님
                if (b_ni,b_nj) not in b_visited and (b_ni,b_nj) != r_pos: # 방문 한적 없고 같은 구역에 위치하지 않는 경우
                    dfs(maze, r_pos, (b_ni,b_nj), r_visited, b_visited + [(bi,bj)]) #파랑수레 위치 변경하고 이전 위치 방문기록
    elif maze[bi][bj] == 4: #파란수레만 도착한 경우
        for r_di, r_dj in dir:
            r_ni, r_nj = ri+r_di, rj+r_dj
            if 0<=r_ni<len(maze) and 0<=r_nj<len(maze[0]) and maze[r_ni][r_nj] != 5:
                if (r_ni,r_nj) not in r_visited and (r_ni,r_nj) != b_pos:
                    dfs(maze, (r_ni,r_nj), b_pos, r_visited+[(ri,rj)], b_visited)
    else: # 두 수레 모두 도착하지 못한 경우
        for r_di, r_dj in dir:
            for b_di, b_dj in dir:
                r_ni, r_nj = ri + r_di, rj + r_dj
                b_ni, b_nj = bi + b_di, bj + b_dj
                if 0 <= r_ni < len(maze) and 0 <= r_nj < len(maze[0]) and 0<=b_ni<len(maze) and 0<=b_nj<len(maze[0])and maze[r_ni][r_nj] != 5 and maze[b_ni][b_nj] != 5:
                    if (r_ni,r_nj) not in r_visited and (b_ni,b_nj) not in b_visited :
                        if (r_ni,r_nj) != (b_ni,b_nj) and not((r_ni,r_nj)==(bi,bj) and (b_ni,b_nj)==(ri,rj)):
                            dfs(maze,(r_ni, r_nj), (b_ni, b_nj), r_visited+[(ri,rj)], b_visited+[(bi,bj)])

def find_start(row, col, maze):
    for i in range(row):
        for j in range(col):
            if maze[i][j] == 1:
                r_start = (i, j)
            elif maze[i][j] == 2:
                b_start = (i, j)
    return (r_start, b_start)
