import sys
sys.stdin=open('input.txt','r')
'''
17135_캐슬 디펜스
파이썬 :31252KB / 372ms
pypy  :111384KB/ 208ms

'''

def game_start(archers, monsters):
    kill = 0
    line = N
    while line:
        dead = set()
        for archer in archers:
            min_distance = D+1
            tmp = 0
            for i, (x, y) in enumerate(monsters):
                if x < line:
                    distance = abs(line - x) + abs(archer - y)
                    if distance <= D:
                        if distance < min_distance or (distance == min_distance and y < tmp[0]):
                            min_distance = distance
                            tmp = (y, i)
            if tmp:
                dead.add(tmp[1])


        new_monsters = []
        for i, (x, y) in enumerate(monsters):
            if i not in dead:
                new_monsters.append((x, y))
        monsters = new_monsters

        kill += len(dead)
        line -= 1
    return kill

N,M,D = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

monsters=[]
for i in range(N):
    for j in range(M):
        if arr[i][j]:
            monsters.append((i,j))

res = 0
case = []
for i in range(1 << M):     # 비트연산으로 조합을 짜고
    temp = []
    for j in range(M):
        if i & (1 << j):
            temp.append(j)
    if len(temp)==3:        # 궁수는 3명으로 고정이므로!!
        case.append(temp)
for i in range(len(case)):
    res = max(res,game_start(case[i],monsters))

print(res)
