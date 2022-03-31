numbers = int(input())
total = 0
total2 = 0
total3 = 0
total4 = 0
total5 = 0
number1 = 0
number2 = 0
number3 = 0
number4 = 0
number5 = 0

for n in range(numbers):

    number = int(input())

    if number < 200:
        total += 1
        number1 = total / numbers * 100
    elif 200 <= number <= 399:
        total2 += 1
        number2 = total2 / numbers * 100
    elif 400 <= number <= 599:
        total3 += 1
        number3 = total3 / numbers * 100
    elif 600 <= number <= 799:
        total4 += 1
        number4 = total4 / numbers * 100
    elif number >= 800:
        total5 += 1
        number5 = total5 / numbers * 100


print(f"{number1:.2f}%")
print(f"{number2:.2f}%")
print(f"{number3:.2f}%")
print(f"{number4:.2f}%")
print(f"{number5:.2f}%")
