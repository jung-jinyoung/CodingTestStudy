# 원래는 순서대로 잘 '닫히면' tmp 에 값을 곱하고 다시 1로 초기화 하려고 했는데
# 실패함 그래서 소히거대로 열릴때부터 곱하고 다시 나눠주는 방식으로 바꿈

arr = list(input())
stack = []

ans = 0
tmp = 1

for i in range(len(arr)):
    if arr[i] == '(':
        tmp *= 2
        stack.append('(')
    elif arr[i] == '[':
        tmp *= 3
        stack.append('[')
    elif arr [i] == ')':
        if stack and stack[-1] == '(':
            if arr[i -1] == '(':
                ans += tmp
            stack.pop()
            tmp //= 2
        else:
            ans = 0
            break
    elif arr[i] == ']':
        if stack and stack[-1] == '[':
            if arr[i -1] == '[':
                ans += tmp
            stack.pop()
            tmp //= 3
        else:
            ans = 0
            break
if stack: 
    print(0)
else:
    print(ans)



