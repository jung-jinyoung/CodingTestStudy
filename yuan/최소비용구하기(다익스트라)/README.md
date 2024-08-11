실패코드
<br/>

---

    발상: 각 도시마다 최단거리 업데이트 하기

    구현: 다익스트라(아마도)

- 문제: 시간초과!

```python
from collections import deque
import sys
input = sys.stdin.readline
cityNum = int(input())
busNum = int(input())

# 도시간 최소 비용 저장할 배열
citycost_arr = [[0]*(cityNum+1) for _ in range(cityNum+1)]

for _ in range(busNum):
    #출발, 도착, 비용
    s, e, c = map(int, input().split())
    citycost_arr[s][e] = c

s_city, e_city = map(int, input().split())

# 전체 도시 의 최소 비용배열 만들기( 출발도시부터의 최소비용 갱신 목적)
mincost_arr = [1e9]* (cityNum+1)
# bfs로 모든 도시 순회하면서 최소비용 업데이트
mincost_arr[s_city] = 0 # 시작도시는0
q = deque()
q.append((s_city))
while q:
    now = q.popleft()
# 현재도시에서 갈수있는 모든 도시의 경로의 비용확인
    for go in range(cityNum+1): # go 는 모든 도시
        if citycost_arr[now][go] >0: # 0보다 크면 갈수있는 도시
            # 더 작은 값으로 갱신하기
            mincost_arr[go] = min(mincost_arr[go], mincost_arr[now]+ citycost_arr[now][go] )
            q.append(go)# 갈수 있는도시 q에 추가

print(mincost_arr[e_city]) # 최종 가야할 도시 출력



```

성공 코드
<br/>

---

1. 같은 경로에도 다른 비용 있을수 있으므로
   `citycost_arr[s][e] = min(citycost_arr[s][e], c)`
2. 최소비용 찾는 식이니 문제 없도록 무한한수 1e9로 초기 배열설정

```python
import heapq
import sys
input = sys.stdin.readline
cityNum = int(input())
busNum = int(input())

# 도시간 최소 비용 저장할 배열
citycost_arr = [[1e9]*(cityNum+1) for _ in range(cityNum+1)]

for _ in range(busNum):
    #출발, 도착, 비용
    s, e, c = map(int, input().split())
    citycost_arr[s][e] = min(citycost_arr[s][e], c)

s_city, e_city = map(int, input().split())

# 전체 도시 의 최소 비용배열 만들기( 출발도시부터의 최소비용 갱신 목적)
mincost = [1e9]* (cityNum+1)
# bfs로 모든 도시 순회하면서 최소비용 업데이트
mincost[s_city] = 0 # 시작도시는0
pq = [] # 비용 최소화 위한 힙큐 활용

# 빈배열, (시작)도시까지의 비용, 시작도시 heqppush
heapq.heappush(pq,(0,s_city))

while pq:
    cost, now = heapq.heappop(pq)#pq배열pop// 비용, 도시
    if cost > mincost[now]:
        continue # 배열에서 꺼낸 비용, 도시가 현재 최소보다 크면 패스
    for go in range(cityNum+1):
        # 가려는 도시로 길있음, now까지의 최소인 cost + citycost를 더한 값과 mincost 값 확인하기
        if citycost_arr[now][go]<1e9 and (cost + citycost_arr[now][go]) < mincost[go]:
            mincost[go] = mincost[now] + citycost_arr[now][go]
            heapq.heappush(pq,(mincost[go],go))

print(mincost[e_city])

```
