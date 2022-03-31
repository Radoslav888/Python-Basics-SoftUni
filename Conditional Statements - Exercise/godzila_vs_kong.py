budget = float(input())
statists = int(input())
one_cloth_price = float(input())
decor = budget * 0.1
clothes_price = statists * one_cloth_price

if statists > 150:
    clothes_price *= 0.9

needed_money = decor + clothes_price

difference = abs(needed_money - budget)

if needed_money > budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print('Action!')
    print(f"Wingard starts filming with {difference:.2f} leva left.")
