prices = [2,4,5,6,10,1]
min_price = 100000
max_profit = 0
for price in prices:
    if price < min_price:
        min_price = price
    else:
        profit = price - min_price
        max_profit = max(profit, max_profit)

print(max_profit)