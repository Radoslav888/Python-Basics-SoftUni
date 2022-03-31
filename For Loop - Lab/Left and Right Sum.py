numbers = int(input())
first = 0
second = 0
for _ in range(numbers):
    current_num1 = int(input())
    first += current_num1
for a in range(numbers):
    current_num2 = int(input())
    second += current_num2

diff = abs(first - second)

if first == second:
    print(f"Yes, sum = {first}")
else:
    print(f"No, diff = {diff}")