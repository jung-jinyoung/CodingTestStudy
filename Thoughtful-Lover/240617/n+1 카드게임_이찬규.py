'''
2024 KAKAO WINTER INTERNSHIP
n+1 카드게임

카드와 coin
처음에 카드 뭉치에서 n/3장을 뽑아 모두 가진다.
당신은 카드와 교환 가능한 동전 coin 개를 가지고 있습니다.

각 라운드가 시작될 때 카드를 두 장 뽑습니다.
남은 카드가 없으면 게임 종료
뽑은 카드는 동전 하나를 소모해 가지거나 동전을 소모하지 않고 버릴 수 있음
카드에 적힌 수의 합이 n_1이 되도록 카드 두 장을 내고 다음 라운드로 진행할 수 있음
만약 카드 두 장을 낼 수 없다면 게임을 종료
'''


# 할 수 있는 행동은 3가지, 카드를 제출하거나, 카드를 버리거나, 코인을 주고 카드를 받아오거나
# 휴 근데 내 머리의 한계,, 결국 제일 먼저 떠오르는 방법은 재귀

max_stage = 0


def card_game(deck, coin_cnt, cards_array, stage):
    global max_stage


def solution(coin, cards):
    global max_stage
    my_card = []
    for i in range(len(cards)//3):
        my_card.append(cards[i])
    card_game(my_card, coin, cards, 1)
    answer = 0
    return answer