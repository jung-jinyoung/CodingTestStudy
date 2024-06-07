'''
댕어려워.. 하지만 시도는 해야하기 때문에 유튜브 강의 참고했어요.. 
'''

''' 
승객이 탑승 중일 때 쾌적한 실내온도 유지
현재(0분) 실내온도는 실외온도와 동일

희망온도 설정 (전원이 켜져 있는 동안 변경 가능)
희망온도 미달성 시 같아지는 방향으로 1도 상승 또는 하강
희망온도 달성 시 실내온도 변화 없음

에어컨 전원 off
실내온도가 실외온도와 같아지는 방향으로 1도 상승 또는 하강
실내온도와 실외온도가 같다면 유지

에어컨 소비 전력
희망온도 != 실내온도 : a 만큼 소비
희망온도 = 실내온도 : b 만큼 소비

에어컨 소비전력 최소화
'''

def solution(temperature, t1, t2, a, b, onboard):
    # 배열에서 -10을 표현하기 어렵기 때문에 +10을 해줌
    # 인덱스 오류 방지 위해서 추가로 +1 을 해줌
    temperature += 11
    t1 += 11
    t2 += 11

    # dp에 최대 전력을 넣어 두고 최소 전력으로 갱신하기 위해
    # float('inf') 사용 -> 항상 float('inf')보다 작다고 결과를 뱉음
    dp = [[float('inf')] * 53 for _ in range(len(onboard))]

    dp[0][temperature] = 0 

    # 0분일 경우 : 실내온도 = 실외온도 이므로 1부터 시작
    for minute in range(1, len(onboard)):
        # 사람이 탑승한다면
        if onboard[minute] == 1:
            l,r = t1, t2 + 1
        else:
            l,r = 1, 52
        # 1도부터 50도까지 
        for temp in range(l, r):
            # 에어컨을 켜지 않는 경우
            # 온도가 같으면
            if temp == temperature:
                dp[minute][temp] = min(dp[minute - 1][temp], dp[minute - 1][temp + 1], dp[minute - 1][temp - 1])
            # 온도가 높을 경우
            elif temp > temperature:
                dp[minute][temp] = dp[minute - 1][temp + 1]
            # 온도가 낮을 경우
            elif temp < temperature:
                dp[minute][temp] = dp[minute - 1][temp - 1]

            # 에어컨을 켜는 경우
            # 에어컨을 켜서 유지시키는 경우, 온도를 올리는 경우, 내리는 경우 중 가장 작은 값
            dp[minute][temp] = min(dp[minute][temp], dp[minute - 1][temp] + b, dp[minute - 1][temp - 1] + a, dp[minute - 1][temp + 1] + a)
        
    return min(dp[-1])
