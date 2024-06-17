'''
2024 KAKAO WINTER INTERNSHIP
주사위 고르기

A와 B가 주사위게임
주사위의 수 구성은 모두 다름
A가 n/2개의 주사위를 가져가면
B가 나머지 n/2개의 주사위를 가져간다.

각각 가져간 주사위를 모두 굴려 점수의 합산이 더 높으면 승리
같으면 무승부
A는 자신이 승리할 확률이 가장 높도록 주사위를 가져감
'''

# 완전 탐색으로 다 돌려본다.
# 조합으로 뽑아주고
# 하나의 승무패를 계산하자면
# 그것과 짝인 나머지의 승무패가 계산된다.


'''
1차시도: 18/26 성공
시간 초과
재귀에서 시간을 많이 빼았겼으려나
일단 다른 문제들도 봐야되니까?
'''
# 조합을 이용해볼거다!
from itertools import combinations


# 여기는 주사위를 던지는 경우의 수를 재귀로 몽땅 구하는 함수
# 여기서 시간이 많이 빼앗겼을 듯?
def get_result(lst, index, sum_v, goal, result_lst):
    if index == goal:
        result_lst.append(sum_v)
        return
    for value in lst[index]:
        get_result(lst, index+1, sum_v+value, goal, result_lst)


def solution(dice):
    N = len(dice)
    # 주사위를 고르는 모든 경우의 수의 조합
    play = list(combinations(dice, N//2))
    # 각각의 주사위를 골랐을 때의 승무패를 저장해줄 result
    result = [[0, 0, 0, l] for l in range(len(play))]
    # 이제 주사위 경기를 할거야
    for i in range(len(play)):
        # s, e에 각각에 주사위를 뽑은 배열을 저장해주고
        s = play[i]
        e = play[-(i+1)]
        # 아래의 두 빈 배열에다가, 주사위를 던지는 모든 경우의 수를 저장해줄거임
        s_list = []
        e_list = []
        get_result(s, 0, 0, N/2, s_list)
        get_result(e, 0, 0, N/2, e_list)

        # 위에서 저장한 주사위 값들을 모두 순회하며 승무패를 위에서 정의한 result 배열에 저장
        for j in range(len(s_list)):
            for k in range(len(e_list)):
                if s_list[j] > e_list[k]:
                    result[i][0] += 1
                    result[-(i+1)][2] += 1
                elif s_list[j] == e_list[k]:
                    result[i][1] += 1
                    result[-(i+1)][1] += 1
                else:
                    result[i][2] += 1
                    result[-(i+1)][0] += 1

    # 승을 기준으로 정렬해주고
    result.sort(key=lambda x: x[0])
    # 최고 높은 경우의 수를 idx로 저장
    idx = result[-1][-1]
    answer = []
    # idx에 담긴 주사위의 선택 경우의 수를 주사위 번호로 바꿔서 answer 배열에 저장
    for v in play[idx]:
        answer.append(dice.index(v)+1)
    return answer