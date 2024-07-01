'''
프로그래머스 징검다리 건너기

징검다리는 일렬, 징검다리 디딤돌에는 숫자
디딤돌 숫자는 한 번 밟을 때 -1
0이 되면 더이상 밟을 수 없고 그 다음 디딤돌로 한번에 여러칸
다음으로 밟을 디딤돌 중 가장 가까운 디딤돌
stones 배열과 한 번에 건너뛸 수 있는 디딤돌의 최대 칸수 k
'''

# 정확성 통과, 효율성 폭망
'''
# 그냥 전체 값들을 -1씩 해주고
# 연속으로 0인 값이 k를 넘어가면 될 것 같은데
def solution(stones, k):
    answer = 0
    length = len(stones)
    while True:
        # 연속으로 0인 값이 k보다 크면 break
        cnt = 0
        for i in range(length):
            if stones[i] == 0:
                cnt += 1
                if cnt >= k:
                    # 이 부분에서 처음 break 문을 했었는데 그렇게 하니까 맨 위의 while 문이 break가 안되고 for문만 break
                    # => 무한 루프 굴레
                    return answer
            else:
                cnt = 0
            # 전체 값들을 -1씩 해줌
            if stones[i]:
                stones[i] -= 1
        # 다음 반복으로 넘어갈 때 answer 1 증가
        answer += 1
'''

# 정확성 1번 문제 runtime error, 효율성 모두 불통
'''
# 배열 크기가 200,000, 값의 크기가 200,000,000, 각오하고 있었던 결과
# 최소값들만큼만 빼주고 연속성을 검사해본다면?
def solution(stones, k):
    answer = 0
    length = len(stones)
    while True:
        # 리스트 컴프리헨션으로 0보다 큰 값 중 최소값을 구함
        # 원래 그냥 min 함수에 넣으니까 나중에 min 값이 0으로만 잡혀서 무한 루프
        min_v = min([stone for stone in stones if stone > 0])
        cnt = 0
        # 연속으로 0인 값이 k보다 크면 break
        for i in range(length):
            if stones[i] == 0:
                cnt += 1
                if cnt >= k:
                    # 이 부분에서 처음 break 문을 했었는데 그렇게 하니까 맨 위의 while 문이 break가 안되고 for문만 break
                    # => 무한 루프 굴레
                    return answer
            else:
                cnt = 0
            # 전체 값들을 - min_v 씩 해줌
            if stones[i] > min_v:
                stones[i] -= min_v
            else:
                stones[i] = 0
        # 다음 반복으로 넘어갈 때 answer를 min_v 만큼 증가
        answer += min_v
'''

# 테케 첫번째 정확성 틀리는거 아마 한 마리도 못 건너는 경우인 것 같은데??
'''
# 배열 크기가 200,000, 값의 크기가 200,000,000, 각오하고 있었던 결과
# 최소값들만큼만 빼주고 연속성을 검사해본다면?
def solution(stones, k):
    length = len(stones)
    # 이전 최소값을 해당 변수에 저장
    min_v_prev = 0
    while True:
        # 리스트 컴프리헨션으로 0보다 큰 값 중 최소값을 구함
        # 원래 그냥 min 함수에 넣으니까 나중에 min 값이 0으로만 잡혀서 무한 루프
        min_v = min([stone for stone in stones if stone > 0])
        cnt = 0
        # 연속으로 0인 값이 k보다 크면 break
        for i in range(length):
            if stones[i] == 0:
                cnt += 1
                if cnt >= k:
                    # 이 부분에서 처음 break 문을 했었는데 그렇게 하니까 맨 위의 while 문이 break가 안되고 for문만 break
                    # => 무한 루프 굴레
                    # 그래서 return 으로 해주되, 만약 개구리가 빠진거면 이전 단계에서 지난 개구리가 마지막이 되므로 min_v_prev를 반환
                    return min_v_prev
            else:
                cnt = 0
            # min_v보다 적은 값들을 0으로 바꿔주고
            if stones[i] <= min_v:
                stones[i] = 0
        # 위 반복이 종료되면 min_v_prev에 min_v를 저장
        min_v_prev = min_v
'''


# 아예 풀이 방법을 달리해야되나?
# 와 나 진짜 모르겠다,,,