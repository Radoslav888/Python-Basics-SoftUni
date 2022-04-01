n1 = int(input())
n2 = int(input())
magic_n = int(input())
combination = 0
condition = False
for num1 in range(n1, n2 + 1):

    for num2 in range(n1, n2 + 1):
        combination += 1
        if num1 + num2 == magic_n:
            condition = True
            print(f"Combination N:{combination} ({num1} + {num2} = {magic_n})")
            break

    if condition:
        break

if not condition:
    print(f"{combination} combinations - neither equals {magic_n}")


