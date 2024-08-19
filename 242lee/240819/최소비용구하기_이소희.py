import heapq
import sys

input = sys.stdin.readline

n = int(input())    # 도시 수
m = int(input())    # 버스 수
INF = int(1e9)
graph = [[] for _ in range(n+1)]
visit = [INF] * (n+1)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

def calc_minCost(start):
    # 우선순위 큐 (최소 힙) 초기화
    q = []
    heapq.heappush(q, (start, 0))  # 시작 노드와 시작 비용을 큐에 추가 (노드, 비용)
    visit[start] = 0               # 시작 노드의 최단 거리는 0
    
    while q:
        now, cost = heapq.heappop(q)  # 현재 노드와 그 노드까지의 비용을 큐에서 꺼내기
        
        # 현재 노드까지의 비용이 이미 저장된 비용보다 크다면 무시
        if visit[now] < cost:
            continue
        
        # 현재 노드와 연결된 다른 노드들을 확인
        for next, next_cost in graph[now]:
            nc = cost + next_cost  # 현재 노드를 거쳐 다른 노드로 가는 비용 계산
            
            # 계산된 비용이 현재 저장된 비용보다 작으면 업데이트
            if visit[next] > nc:
                visit[next] = nc  # 더 작은 비용으로 업데이트
                heapq.heappush(q, (next, nc))  # 다음에 처리할 노드를 큐에 추가 (노드, 비용)

calc_minCost(start)
print(visit[end])
