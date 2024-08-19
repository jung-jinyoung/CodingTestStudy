di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def turn_dir(dir, c): # 회전시키는 함수
    # L 왼쪽 또는 D 오른쪽으로 90도 방향을 회전
    if c == 'L':
        return (dir + 3) % 4 
    else: 
        return (dir + 1) % 4

def solution():
    global i, j, sec, turn, dir
    while True:
        # 머리를 여기서 이동시킴
        i += di[dir]
        j += dj[dir]
        if 1 <= i <= N and 1 <= j <= N and board[i][j] != 1: # 벽이나 몸에 부딪히지 않은 상황
            if board[i][j] == 0: # 사과가 없으면
                ni, nj = snake.pop(0) # 뱀의 위치에서 꼬리 삭제
                board[ni][nj] = 0
            board[i][j] = 1
            snake.append([i, j]) # 머리 위치 추가
        else: # 부딪히면
            sec += 1
            break # 종료
        sec += 1

        # 회전합시다
        if turn < L and moves[turn][0] == sec:
            dir = turn_dir(dir, moves[turn][1])
            turn += 1
    return sec

N = int(input()) # 보드 칸 수
board = [[0] * (N+1) for _ in range(N+1)]

K = int(input())
for _ in range(K):
    # 사과 위치 board 위에 표시
    i, j = map(int, input().split())
    board[i][j] = -1

moves = []
L = int(input())
for _ in range(L):
    x, c = input().split()  # 게임 시작 시간으로부터 x초가 끝난 뒤 L 왼쪽 또는 D 오른쪽으로 90도 방향을 회전
    moves.append((int(x), c))

i, j = 1, 1 # 뱀의 처음 위치
board[i][j] = 1

dir = 0
sec = 0
turn = 0

snake = [[1, 1]] # 뱀의 위치

print(solution())
