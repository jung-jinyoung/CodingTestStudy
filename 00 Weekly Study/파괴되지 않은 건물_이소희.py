#파괴되지 않은 건물

def solution(board, skill):
    def attack(a, b, c, d, degree):
        for i in range(a, c + 1):
            for j in range(b, d + 1):
                board[i][j] -= degree

    def save(a, b, c, d, degree):
        for i in range(a, c + 1):
            for j in range(b, d + 1):
                board[i][j] += degree

    n = len(board)
    m = len(board[0])

    for turn in skill:
        if turn[0] == 1:  # type1 적의 공격
            attack(turn[1], turn[2], turn[3], turn[4], turn[5])
        else:  # type2 아군의 회복
            save(turn[1], turn[2], turn[3], turn[4], turn[5])

    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] >= 1:
                answer += 1
    return answer