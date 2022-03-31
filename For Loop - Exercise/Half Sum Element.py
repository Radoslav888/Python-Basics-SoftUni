import sys
numbers = int(input())
total = 0
max_num = -sys.maxsize

for n in range(numbers):
    number = int(input())
    if number > max_num:
        max_num = number
    total += number

if max_num == total - max_num:
    print("Yes")
    print((f"Sum = {total - max_num}"))
else:
    print("No")
    sum_others = total - max_num
    print(f"Diff = {abs(max_num - sum_others)}")