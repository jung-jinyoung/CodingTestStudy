from itertools import product

def solution(users, emoticons):
    # 가능한 모든 할인율 조합 생성
    discounts = [40, 30, 20, 10]
    discount_combinations = list(product(discounts, repeat=len(emoticons)))
    
    best_result = [0, 0]  # 최대 이모티콘 플러스 서비스 가입자 수, 최대 이모티콘 매출
    
    for discount_combo in discount_combinations:
        plus_subscriptions = 0  # 이모티콘 플러스 서비스 가입자 수
        total_revenue = 0  # 총 매출
        
        # 유저 리스트 조회 (할인율 최솟값 , 최대 결제 가능 금액)
        for user in users:
            min_discount, max_payment = user
            user_spent = 0
            
            # 사용자가 요구하는 최소 할인율을 만족하는 이모티콘을 할인된 가격으로 구매
            for i in range(len(emoticons)):
                if discount_combo[i] >= min_discount:
                    user_spent += emoticons[i] * (1 - discount_combo[i] / 100)
            
            # 사용자가 최대 지불 금액 이상을 지출하면 이모티콘 플러스 서비스에 가입        
            if user_spent >= max_payment:
                plus_subscriptions += 1
            else: # 아닐 경우 총 결제된 금액에 추가 
                total_revenue += user_spent

        # 최대 구독 수가 더 많거나 구독 수는 같은데 결제 금액이 더 많은 경우  
        # 최적의 결과로 업데이트 한다.      

        if (plus_subscriptions > best_result[0]) or (plus_subscriptions == best_result[0] and total_revenue > best_result[1]):
            best_result = [plus_subscriptions, total_revenue]
    
    return best_result

