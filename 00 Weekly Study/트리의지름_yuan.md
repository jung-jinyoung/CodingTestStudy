(시간 없어서 코드 공부만)

<br/>

---

    구현: 다익스트라인줄 알았는데 dfs 로도 구현가능! 


```python
import sys

input = sys.stdin.readline

def dfs(now, dist):
    # 다음에 방문 가능한 노드와 해당 노드의 가중치
    for next, next_d in graph[now]:
        if visited[next] == -1: # 아직 방문안했을때
            visited[next] = dist + next_d # 이전까지의 가중치합 + 현재 가중치
            dfs(next, visited[next])# 노드 바꿔서 재방문

n= int(input()) #노드개수
graph = [[] for _ in range(n+1)]

# 가중치 포함한 트리 만들기
for _ in range(n-1):
    # 부모, 자식, 가중치
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

# 방문시 가중치 넣을 배열
visited = [-1] * (n+1)
visited[1] = 0 # 시작노드 1
# 1에서 가장 가중치가 큰 노드 구하기
dfs(1,0)

far_node = visited.index(max(visited))
far_visited = [-1] * (n+1)
far_visited[far_node] = 0
# 1에서 가장 먼 거리 구하기
dfs(far_node,0)

print(max(visited))# 가중치 출력

```
