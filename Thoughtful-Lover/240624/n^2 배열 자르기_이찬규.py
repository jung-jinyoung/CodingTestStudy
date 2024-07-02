'''
프로그래머스_n^2 배열 자르기

그림 덕분에 쉽게 이해했다.
n이 주어졌을 때, 예컨대 n = 3,
아래와 같은 사각형의 모양을 가진다.

1 2 3
2 2 3
3 3 3

이때, 위의 사각형을 1차원 배열 형태로 모두 이어붙였을 때
left 인덱스부터 right 인덱스까지의 값을 1차원 배열로 잘라서 출력한다.
'''


# 전체 테스트케이 6/20 통과
# 시간초과가 난다면 해당 부분을 고쳐주면 되겠지?
def solution(n, left, right):
    # 단순하게 생각하면
    # 1. 2차원 배열을 만든다.
    square = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if j < i:
                square[i][j] = i+1
            else:
                square[i][j] = j+1

    # 2. 1차원 배열로 붙여 버린다.
    array = []
    for rectangle in square:
        array += rectangle

    # 3. 주어진 인덱스만큼 슬라이싱한다.
    answer = array[left:right+1]
    return answer


'''
저 1번과 2번 과정이 오래 걸리는 것 같다.
저 두 개를 통합하되 쌈뽕하게 일일이 다 돌 필요 없도록
n이 무려 최대 10^7 !!??
'''