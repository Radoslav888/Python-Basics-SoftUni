trip_price = float(input())
puzzles = int(input())
doll = int(input())
teddy_bear = int(input())
minions = int(input())
truck = int(input())

total = puzzles * 2.60 + doll * 3 \
        + teddy_bear * 4.10 + minions * 8.2 + truck * 2

number = puzzles + doll + teddy_bear + minions + truck

if number > 50:
    total = 0.75 * total


rent = 0.1 * total

profit = total - rent

final = abs(profit - trip_price)

if profit > trip_price:
    print(f"Yes! {final:.2f} lv left.")

elif profit < trip_price:
    print(f"Not enough money! {final:.2f} lv needed.")


