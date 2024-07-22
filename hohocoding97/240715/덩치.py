N = int(input())

data = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    cnt = 1
    for j in range(N):
        a, b = data[i]
        c, d = data[j]
        if a < c and b < d:
            cnt += 1
    print(cnt, end=' ')