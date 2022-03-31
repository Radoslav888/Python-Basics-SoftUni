type = str(input())
number = int(input())
budget = int(input())
price = 0
if type == "Roses":
    if number > 80:
        price = number * 5 * 0.9
    elif number < 80:
        price = number * 5
elif type == "Dahlias":
    if number > 90:
        price = number * 3.8 * 0.85
    elif number < 90:
        price = number * 3.8
elif type == "Tulips":
    if number > 80:
        price = number * 2.8 * 0.85
    elif number < 80:
        price = number * 2.8

elif type == "Narcissus":
    if number < 120:
        price = number * 3 * 1.15
    elif number > 120:
        price = number * 3

elif type == "Gladiolus":
    if number < 80:
        price = number * 2.5 * 1.2
    elif number > 80:
        price = number * 2.5

money_left = abs(budget - price)

if budget >= price:
    print(f"Hey, you have a great garden with {number} {type} and {money_left:.2f} leva left.")
elif budget < price:
    print(f"Not enough money, you need {money_left:.2f} leva more.")