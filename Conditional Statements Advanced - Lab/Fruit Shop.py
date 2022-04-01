fruit = input()
day = input()
quantity = float(input())
price = 0

if day in 'Monday Tuesday Wednesday Thursday Friday':
    if fruit == 'banana':
        price = 2.5
        print(f'{price * quantity:.2f}')
    elif fruit == 'apple':
        price = 1.2
        print(f'{price * quantity:.2f}')
    elif fruit == 'orange':
        price = 0.85
        print(f'{price * quantity:.2f}')
    elif fruit == 'grapefruit':
        price = 1.45
        print(f'{price * quantity:.2f}')
    elif fruit == 'kiwi':
        price = 2.70
        print(f'{price * quantity:.2f}')
    elif fruit == 'pineapple':
        price = 5.50
        print(f'{price * quantity:.2f}')
    elif fruit == 'grapes':
        price = 3.85
        print(f'{price * quantity:.2f}')
    else:
        print('error')


if day in 'Saturday Sunday':
    if fruit == 'banana':
        price = 2.7
        print(f'{price * quantity:.2f}')
    elif fruit == 'apple':
        price = 1.25
        print(f'{price * quantity:.2f}')
    elif fruit == 'orange':
        price = 0.9
        print(f'{price * quantity:.2f}')
    elif fruit == 'grapefruit':
        price = 1.60
        print(f'{price * quantity:.2f}')
    elif fruit == 'kiwi':
        price = 3
        print(f'{price * quantity:.2f}')
    elif fruit == 'pineapple':
        price = 5.6
        print(f'{price * quantity:.2f}')
    elif fruit == 'grapes':
        price = 4.20
        print(f'{price * quantity:.2f}')
    else:
        print('error')
elif day not in 'Monday Tuesday Wednesday Thursday Friday Saturday Sunday':
    print('error')


