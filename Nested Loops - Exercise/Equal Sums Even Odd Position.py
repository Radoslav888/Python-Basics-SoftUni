n1 = int(input())
n2 = int(input())

for current_n in range(n1, n2 + 1):
    odd = 0
    even = 0
    current_n_as_str = str(current_n)
    for index, digit in enumerate(current_n_as_str):

        if index % 2 == 0:
            even += int(digit)

        else:
            odd += int(digit)

    if even == odd:
        print(f"{current_n_as_str}", end = " ")

