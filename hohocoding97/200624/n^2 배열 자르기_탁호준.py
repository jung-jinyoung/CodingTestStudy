def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        share = i//n #몫
        remainder = i%n #나머지
        answer.append(max(share, remainder)+1)
    return answer