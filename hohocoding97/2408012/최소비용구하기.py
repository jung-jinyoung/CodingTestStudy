import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())

INF = float('inf')
# i도시에서 다른 도시로 가는 데 드는 비용, 최댓값으로 초기화
costs = {i:{j : INF for j in range(1, N+1)} for i in range(1,N+1)} 

# s->e 로 가는 최소 비용 찾기
for _ in range(N):
    for s, e, c in map(int, input().split()):
        costs[s][e] = min(costs[s][e], c) #중복될 수 있으니 최솟값 찾기

def dijkstra(s:int, e:int):
    hq = [(0,s)] #시작점 넣어주기
    while hq:
        cost, start = heapq.heappop(hq)