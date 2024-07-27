import sys
from collections import deque

N = int(input())

for _ in range(N):
    VPS = deque(sys.stdin.readline().strip())

    stack = []
    result = ""
    while VPS:
        temp = VPS.popleft()
        if temp == "(":
            stack.append(temp)
        else:
            try:
                stack.pop()
            except IndexError:
                result = "NO"
                print(result)
                break

    if result == "NO":
       continue

    if stack :
        print("NO")
    else :
        print("YES")




