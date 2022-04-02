number = int(input())
for current_num in range (1111, 10000):
    number_is_special = True
    current_num_str = str(current_num)
    for current_digit in current_num_str:
        if int(current_digit) == 0 or number % int(current_digit) != 0:
            number_is_special = False
            break

    if number_is_special:
        print(current_num, end = ' ')
    