"""
쾌적한 실내 온도 : t1~t2
에어컨 on :
    - 희망 온도 설정 -> 1분 마다 ^,v (현재 온도와 동일하다면 변하지 않음)
    - 희망 온도와 실내 온도가 다르면 a 만큼 소비
    - 희망 온도와 같으면 b만큼 소비

에어컨 off : 실외 온도와 같아지는 방향으로 1분 마다 ^,v, 전력 소비 X

Q. t1~t2 로 유지하면서 소비 전력을 최소화 해라.
- temperature : 실외 온도
- 쾌적한 실내 온도 범위 : t1~t2
- 소비 전력 :a, b
- 승객이 탑승 중인 시간 : onboard

접근 : DP
해당 시간에 탑승자가 있을 경우 : 이전 시간의 해당 온도 +=1 확인
없을 경우 : 이전 시간 확인

해결 X ..
비용 부분 확인 필요..

"""


def solution(temperature, t1, t2, a, b, onboard):

    # 탑승 확인
    # t1~t2 온도 범위 확인
    dp = [[1e9] * 51 for _ in range (1000)]

    # 초기화
    dp[0][temperature] =0


    offset = 10 # 인덱스 설정을 위함
    N = len(onboard)
    for i in range(1,N):
        for temp in range(-10, 41):
            temp_index = temp + offset
            if dp[i-1][temp_index] == 1e9:
                continue

            # 현대 온도에서의 비용
            current_cost = dp[i-1][temp_index]

            # 온보드 확인
            if onboard[i]:
                for new_temp in range(t1, t2+1):
                    new_temp_index = new_temp + offset
                    if temp == new_temp:
                        dp[i][new_temp_index] = min(dp[i][new_temp_index], current_cost + b)
                    else:
                        dp[i][new_temp_index] = min(dp[i][new_temp_index], current_cost + a)
            else :
                # 실외 온도 확인
                if temp > -10:
                    dp[i][temp_index - 1] = min(dp[i][temp_index - 1], current_cost)
                if temp < 40:
                    dp[i][temp_index + 1] = min(dp[i][temp_index + 1], current_cost)
                dp[i][temp_index] = min(dp[i][temp_index], current_cost)


        # 마지막 시간에서 t1~t2 범위 내의 최소값 계산
        answer = min(dp[N - 1][t + offset] for t in range(t1, t2 + 1))
        return answer if answer != 1e9 else 0




