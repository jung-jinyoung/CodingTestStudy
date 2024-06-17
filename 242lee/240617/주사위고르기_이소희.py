'''
프로그래머스 주사위고르기
'''
from itertools import combinations, product

def solution(dice):
    n = len(dice)
    A, result = [], []
    cases = list(combinations(range(n), n // 2))  # 뽑을 수 있는 경우의 수 (인덱스)

    for case in cases:
        dices = [dice[c] for c in case]  # 인덱스에 해당하는 실제 주사위
        nums = sorted([sum(i) for i in product(*dices)])  # 뽑은 주사위의 합의 경우의 수
        A.append(nums)

    a, p = 0, len(A)
    for i in range(p):
        B = A[p - i - 1]  # B와 A는 대칭의 구조를 가지므로 B = A[p-i-1]

        # 각 조합이 이기는 횟수 이분탐색
        temp = 0
        for t in A[i]:
            left, right = 0, len(B) - 1
            while left <= right:
                mid = (left + right) // 2
                if B[mid] < t:
                    left = mid + 1
                else:
                    right = mid - 1
            temp += left

        # 가장 승리 확률이 높은 경우의 수 반환
        if a < temp:
            a = temp
            result = [x + 1 for x in cases[i]]

    return result
