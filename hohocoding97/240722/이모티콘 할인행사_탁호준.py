from itertools import product

def solution(users, emoticons):
    def user_cost(want_discount, min_cost, i, cost, case): 
        if cost >= min_cost or i==len(case): #만원이상이거나 끝까지 갔으면 return
            return cost
        
        if case[i] >= want_discount: #현재 할인율이 유저가 원하는 할인율 보다 높으면
            return user_cost(want_discount,min_cost, i+1, cost+emoticons[i]*(100-case[i]), case)
        else:
            return user_cost(want_discount,min_cost, i+1, cost, case)
    N = len(users) #유저 수
    M = len(emoticons) #이모티콘 수s
    
    # combinations로 이모티콘 세일하는 경우의 수 만들기
    cases = product([10,20,30,40], repeat=M)
    
    result = [0,0] 
    for case in cases: #case = (10, 10, 40) 같은 형태 
        temp = [0, 0]
        for want_discount, min_cost in users: 
            cost = user_cost(want_discount, min_cost, 0, 0, case)
            # print(cost, min_cost)
            if cost >= min_cost:
                temp[0] += 1
            else:
                temp[1] += cost
        if temp[0] > result[0]:
            result = [temp[0], temp[1]]
        elif temp[0] == result[0] and temp[1] > result[1]:
            result[1] = temp[1]
    #want_discount:유저가원하는할인율, i:이모티콘 인덱스
    #cost: 여태까지 사용한 돈, case:각 이모티콘의 할인율
    
    return result


users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emoticons = [1300, 1500, 1600, 4900]
solution(users, emoticons)