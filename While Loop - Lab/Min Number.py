import sys

min = sys.maxsize

while True:
    number = input()
    if number == "Stop":
        break
    if int(number) < min:
        min = int(number)

print(min)