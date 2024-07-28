'''
4개의 기호 ‘(’, ‘)’, ‘[’, ‘]’를 이용해서 만들어지는 괄호열
1. 한 쌍의 괄호로만 이루어진 ‘()’와 ‘[]’는 올바른 괄호열이다.
2. 만일 X가 올바른 괄호열이면 ‘(X)’이나 ‘[X]’도 모두 올바른 괄호열이 된다.
3. X와 Y 모두 올바른 괄호열이라면 이들을 결합한 XY도 올바른 괄호열이 된다.

() 2, [] 3
'''

# ( 다음 ) 오면 2, [ 다음 ] 오면 3
# ( 숫자 ) 면 2 * 숫자
# [ 숫자 ] 면 3 * 숫자

# inputStr을 앞에서부터 순회하면서 열린 괄호면 stack에 추가
# stack의 마지막 요소가 열린 괄호 && inputStr의 현재 요소가 맞는 쌍이면
# stack에서 마지막 요소 pop 하고 값을 더해
inputStr = list(input())
stack = []

ans = 0
tmp = 1
for i in range(len(inputStr)):
    # 열린 괄호이면
    if inputStr[i] == '(':
        tmp *= 2
        stack.append('(')
    elif inputStr[i] == '[':
        tmp *= 3
        stack.append('[')
    # 닫힌 괄호이면
    elif inputStr[i] == ')':
        if stack and stack[-1] == '(':      # 스택이 비어있지 않고 마지막이 열린 소괄호일 경우
            if inputStr[i - 1] == '(':      # 직전 문자가 열린 소괄호일 경우
                ans += tmp                  # tmp 값을 ans에 더함
            stack.pop()                     # 스택에서 열린 소괄호 제거
            tmp //= 2                       # 값을 다시 2로 나눔
        else:
            ans = 0                         # 올바르지 않은 경우 0으로 설정
            break                           # 반복문 종료
    else:  # inputStr[i] == ']'
        if stack and stack[-1] == '[':      # 스택이 비어있지 않고 마지막이 열린 대괄호일 경우
            if inputStr[i - 1] == '[':      # 직전 문자가 열린 대괄호일 경우
                ans += tmp                  # tmp 값을 ans에 더함
            stack.pop()                     # 스택에서 열린 대괄호 제거
            tmp //= 3                       # 값을 다시 3으로 나눔
        else:
            ans = 0                         # 올바르지 않은 경우 0으로 설정
            break                           # 반복문 종료

if stack:
    print(0)
else:
    print(ans)