# 프로그래머스 - 가장 많이 받은 선물

# 스장님이 주사위 전에 풀면 좋은 문제라고 올려두신 거 보고 . . 일단 풀었습니다
# 자료 입력받은 후 조건식 얼마나 더 간단하게 만드는지 방법 차이인 것 같아요
# 저는 문제에서 제시한 표 따라가면서 풀었습니당

def solution(friends, gifts):
    n = len(friends)
    info_arr = [[0] * n for _ in range(n)]
    
    # 정보 입력
    for gift in gifts:
        sender, receiver = gift.split(' ')
        for i in range(n):
            for j in range(n):
                # 선물 보낸 사람 & 받은 사람 인덱스에 각각 맞춰 저장
                if friends[i] == sender and friends[j] == receiver:
                    info_arr[i][j] += 1
    
    point_arr = [[0] * 3 for _ in range(n)]  # [준 선물, 받은 선물, 선물 지수]
    
    for x in range(n):
        point_arr[x][0] += sum(info_arr[x])  # 준 선물
        
        for y in range(n):
            point_arr[x][1] += info_arr[y][x]   # 받은 선물
        
        point_arr[x][2] = point_arr[x][0] - point_arr[x][1]
    
    result_arr = [0] * n   # 다음 달에 받게 될 선물
    visited = [[0] * n for _ in range(n)]
    
    for a in range(n):
        for b in range(n):
            if visited[a][b] == 0 and visited[b][a] == 0:
                a2b = info_arr[a][b]
                b2a = info_arr[b][a]

                if a2b == b2a or (a2b == 0 and b2a == 0):
                    # 선물지수 비교
                    if point_arr[a][2] == point_arr[b][2]:
                        pass
                    else: 
                        if point_arr[a][2] > point_arr[b][2]:
                            result_arr[a] += 1
                        # else:
                        elif point_arr[a][2] < point_arr[b][2]:
                            result_arr[b] += 1
                    
                elif a2b != 0 or b2a != 0:   # 이거 and로 해서 값이 하나씩 안나왔음
                    # 더 많이 준 사람 count += 1 
                    if a2b > b2a:
                        result_arr[a] += 1
                    else:
                        result_arr[b] += 1

                # 방문 표시(a<->b 했는데 b<->a 또하면 중복)
                visited[a][b] = 1
                visited[b][a] = 1
            
    answer = max(result_arr)
    return answer