city = input()
sales = float(input())
commmission = 0

if city == 'Sofia':
    if 0 <= sales <= 500:
        commmission = 0.05
        print(f'{sales * commmission:.2f}')
    elif 500 < sales <= 1000:
        commmission = 0.07
        print(f'{sales * commmission:.2f}')
    elif 1000 < sales <= 10000:
        commmission = 0.08
        print(f'{sales * commmission:.2f}')
    elif sales > 10000:
        commmission = 0.12
        print(f'{sales * commmission:.2f}')
    else:
        print(error)

if city == 'Varna':
    if 0 <= sales <= 500:
        commmission = 0.045
        print(f'{sales * commmission:.2f}')
    elif 500 < sales <= 1000:
        commmission = 0.075
        print(f'{sales * commmission:.2f}')
    elif 1000 < sales <= 10000:
        commmission = 0.10
        print(f'{sales * commmission:.2f}')
    elif sales > 10000:
        commmission = 0.13
        print(f'{sales * commmission:.2f}')
    else:
        print('error')

if city == 'Plovdiv':
    if 0 <= sales <= 500:
        commmission = 0.055
        print(f'{sales * commmission:.2f}')
    elif 500 < sales <= 1000:
        commmission = 0.08
        print(f'{sales * commmission:.2f}')
    elif 1000 < sales <= 10000:
        commmission = 0.12
        print(f'{sales * commmission:.2f}')
    elif sales > 10000:
        commmission = 0.145
        print(f'{sales * commmission:.2f}')
    else:
        print('error')
elif city not in "Sofia Plovdiv Varna":
    print('error')