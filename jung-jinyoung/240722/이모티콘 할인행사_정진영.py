
from itertools import product

def solution(users, emoticons):
    
    discounts = [40,30,20,10]
    

    for check in product(discounts, repeat = len(users)):
        
        print(check)
    
    
    answer = []
    return answer
