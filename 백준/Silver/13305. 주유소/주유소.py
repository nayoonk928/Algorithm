import sys
input = sys.stdin.readline

n = int(input())
distance = list(map(int, input().split()))
oil = list(map(int, input().split()))

result = 0
curr_oil = float('inf')  
min_oil_price = oil[0]  

for idx, val in enumerate(distance):
    min_oil_price = min(min_oil_price, oil[idx])  

    if curr_oil > min_oil_price:  
        result += min_oil_price * val
        curr_oil = min_oil_price
    else:
        result += curr_oil * val

print(result)