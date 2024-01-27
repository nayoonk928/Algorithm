import sys
from collections import deque
input = sys.stdin.readline

def card_game(n):
    cards = deque(range(1, n + 1))
    discarded_cards = []

    while len(cards) > 1:
        # 제일 위에 있는 카드를 버리고
        discarded_cards.append(cards.popleft())
        # 그 다음 제일 위에 있는 카드를 제일 아래로 옮김
        cards.append(cards.popleft())

    # 남은 카드를 출력
    remaining_card = cards.pop()
    return discarded_cards, remaining_card

if __name__ == '__main__':
    n = int(input())  # 카드의 개수
    discarded_cards, remaining_card = card_game(n)

    # 버린 카드와 남은 카드를 출력
    print(*discarded_cards, remaining_card)