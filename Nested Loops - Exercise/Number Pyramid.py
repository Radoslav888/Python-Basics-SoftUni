n = int(input())
number = 1
all_is_printed = False

for row in range(1, n + 1):
    for col in range(1, row + 1):
       print(f"{number}", end = " ")
       number += 1
       if number > n:
           all_is_printed = True
           break
    if all_is_printed:
        break
    print()