budget = int(input())
season = str(input())
number = int(input())
price = 0
if season == "Spring":
    if number <= 6:
        price = 3000 * 0.9
        if number % 2 == 0:
            price *= 0.95
    if 7 <= number <= 11 :
        price = 3000 * 0.85
        if number % 2 == 0:
            price *= 0.95
    if number >= 12:
        price = 3000 * 0.75
        if number % 2 == 0:
            price *= 0.95


if season == "Summer":
    if number <= 6:
        price = 4200 * 0.9
        if number % 2 == 0:
            price *= 0.95
    if 7 <= number <= 11 :
        price = 4200 * 0.85
        if number % 2 == 0:
            price *= 0.95
    if number >= 12:
        price = 4200 * 0.75
        if number % 2 == 0:
            price *= 0.95

if season == "Winter":
    if number <= 6:
        price = 2600 * 0.9
        if number % 2 == 0:
            price *= 0.95
    if 7 <= number <= 11 :
        price = 2600 * 0.85
        if number % 2 == 0:
            price *= 0.95
    if number >= 12:
        price = 2600 * 0.75
        if number % 2 == 0:
            price = price * 0.95

if season == "Autumn":
    if number <= 6:
        price = 4200 * 0.9

    if 7 <= number <= 11 :
        price = 4200 * 0.85

    if number >= 12:
        price = 4200 * 0.75

money_left = abs(budget - price)
if budget >= price:
     print(f"Yes! You have {money_left:.2f} leva left.")
else:
     print(f"Not enough money! You need {money_left:.2f} leva.")
