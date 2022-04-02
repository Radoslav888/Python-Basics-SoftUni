number_of_orders = int(input())
total_sum = 0

for i in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())

    total = price_per_capsule * days * capsules_count
    total_sum += total
    print(f"The price for the coffee is: ${total:.2f}")


print(f"Total: ${total_sum:.2f}")