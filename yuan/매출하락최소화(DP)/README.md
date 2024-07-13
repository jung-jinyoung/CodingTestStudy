# 성공코드(못품)

1. 발상: ??? 너무 어려운데? 팀단위로 잘라야한다고 생각하고 고민했는데 아예 틀린 발상이었다. 선수단위로 부분합 계산해야함 
2. 구현
    1. 팀원 한명당 [참여했을때 최소비용, 참여안했을때 최소비용] 의 dp 배열 생성,
    2. dfs 활용하여 거듭 계산

```python
def solution(sales, links):
    sales = [0] + sales
    n = len(sales)
    tree = [[] for _ in range(n+1)]

    for a,b in links:
        tree[a].append(b)
    
    d = [[0,0] for _ in range(n+1)]
    
    dfs(1,d,tree,sales) # 시작번호, dp배열, 트리(사번), 돈 
        
    return min(d[1])

def dfs(node,d,tree,sales):

    if not tree[node]: # 팀원없을때 [워크숍갈때 손해, 안갈때 손해 ]
        d[node][0] = sales[node]
        d[node][1] = 0
        return

    d[node][0] = sales[node] 
    min_gap = float('inf')

    for i in tree[node]:
        dfs(i, d, tree, sales)
        d[node][0] += min(d[i])
        min_gap = min(min_gap,d[i][0]-d[i][1])
        if min_gap < 0:
            min_gap = 0

    d[node][1] = d[node][0] + min_gap - sales[node]
    ```