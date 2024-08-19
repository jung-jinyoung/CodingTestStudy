import sys
sys.setrecursionlimit(1010)


def dijkstra(boarding, previous):
    global arrival

    if checked[boarding]:
        return

    for bus in routes[boarding]:
        if the_way[bus[0]] == bus[1]+previous:
            return
        elif the_way[bus[0]] > bus[1]+previous:
            the_way[bus[0]] = bus[1]+previous
        if bus[0] == arrival:
            continue
        dijkstra(bus[0], the_way[bus[0]])

    checked[boarding] = True


N = int(input())
M = int(input())
routes = [[] for _ in range(N+1)]
for _ in range(M):
    sp, ep, cost = map(int, input().split())
    routes[sp].append((ep, cost))
the_way = [100000]*(N+1)
the_way[0] = 0
checked = [False]*(N+1)
departure, arrival = map(int, input().split())
dijkstra(departure, 0)
print(the_way[arrival])