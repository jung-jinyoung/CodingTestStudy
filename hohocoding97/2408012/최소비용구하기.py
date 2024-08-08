import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

N = int(input())            #도시 개수 -> 노드의 수
M = int(input())            #버스 개수 -> 간선의 수
graph = {i: {} for i in range(1, N+1)}    #그래프를 인접리스트로 표현(딕셔너리 of 딕셔너리)
INF = float("inf")          #무한대 값
prices = defaultdict(INF)   #가격 나타내줄 딕셔너리  key:(s,e), val:price
for _ in range(M):
    start, end, cost = map(int, input().split()) # 출발 도시, 도착 도시, 가격
        # 같은 경로의 버스가 여러 개 있을 수 있으므로, 최소 비용만 저장
    if end in graph[start]:
        graph[start][end] = min(graph[start][end], cost)
    else:
        graph[start][end] = cost

# 출발지와 도착지 입력
start, end = map(int, input().split())

def dijkstra(graph, start, end):
    distances = {node: INF for node in graph}
    distances[start] = 0 #시작점에서 시작점으로 가는데 드는 비용

    # 우선순위 큐 초기화
    queue = [(0, start)]