month = str(input())
nights = int(input())
studio = 0
apartment = 0
if month in ' May October':
    studio = 50
    apartment = 65
    price_studio = studio * nights
    price_apartment = apartment * nights
    if 14 > nights >= 7 and month in ' May October':
        studio *= 0.95
    elif 14 < nights and month in ' May October':
        price_studio *= 0.7
    if 14 < nights:
        price_apartment *= 0.9


if month in ' July August':
    studio = 76
    apartment = 77
    price_studio = studio * nights
    price_apartment = apartment * nights
    if 14 < nights:
        price_apartment *= 0.9


if month in ' September June':
    studio = 75.20
    apartment = 68.70
    price_studio = studio * nights
    price_apartment = apartment * nights
    if 14 < nights and month in 'September June':
        price_studio *= 0.8
    if 14 < nights:
        price_apartment *= 0.9




print(f'Apartment: {price_apartment:.2f} lv.')
print(f'Studio: {price_studio:.2f} lv.')