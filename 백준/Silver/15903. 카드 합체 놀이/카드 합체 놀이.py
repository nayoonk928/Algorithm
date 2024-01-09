# 백준 15903번 카드 합체 놀이
# 자연수 카드 n장, m번
# 1. x번 카드와 y번 카드를 골라 더하기
# 2. 1번에서 계산한 값을 x번 카드와 y번 카드에 덮어쓰기
# 3. m번 반복
# 4. 답 : n장의 카드 모두 더한 값 -> 가장 작게 만들기
# 우선순위 큐 -> 최소 힙 사용
# 최소 힙에 카드 값 저장 -> 제일 위의 2개 더한 결과 카드에 저장(최소 힙 정렬) -> 반복
import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))

cards = []

for card in a:
    heapq.heappush(cards, card)

for _ in range(m):
    first_card = heapq.heappop(cards)
    second_card = heapq.heappop(cards)
    add = first_card + second_card
    heapq.heappush(cards, add)
    heapq.heappush(cards, add)

print(sum(cards))